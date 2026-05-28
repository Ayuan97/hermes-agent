"""Tests for agent/display.py — build_tool_preview() and inline diff previews."""

import json
import pytest
from unittest.mock import MagicMock

from agent.display import (
    build_tool_preview,
    capture_local_edit_snapshot,
    extract_edit_diff,
    format_tool_progress_line,
    get_cute_tool_message,
    get_tool_display_name,
    set_tool_preview_max_len,
    _render_inline_unified_diff,
    _summarize_rendered_diff_sections,
    render_edit_diff_with_delta,
)


@pytest.fixture(autouse=True)
def reset_tool_preview_max_len():
    set_tool_preview_max_len(0)
    yield
    set_tool_preview_max_len(0)


class TestBuildToolPreview:
    """Tests for build_tool_preview defensive handling and normal operation."""

    def test_none_args_returns_none(self):
        """PR #453: None args should not crash, should return None."""
        assert build_tool_preview("terminal", None) is None

    def test_empty_dict_returns_none(self):
        """Empty dict has no keys to preview."""
        assert build_tool_preview("terminal", {}) is None

    def test_known_tool_with_primary_arg(self):
        """Known tool with its primary arg should return a preview string."""
        result = build_tool_preview("terminal", {"command": "ls -la"})
        assert result is not None
        assert "ls -la" in result

    def test_web_search_preview(self):
        result = build_tool_preview("web_search", {"query": "hello world"})
        assert result is not None
        assert "hello world" in result

    def test_read_file_preview(self):
        result = build_tool_preview("read_file", {"path": "/tmp/test.py", "offset": 1})
        assert result is not None
        assert "/tmp/test.py" in result

    def test_unknown_tool_with_fallback_key(self):
        """Unknown tool but with a recognized fallback key should still preview."""
        result = build_tool_preview("custom_tool", {"query": "test query"})
        assert result is not None
        assert "test query" in result

    def test_unknown_tool_no_matching_key(self):
        """Unknown tool with no recognized keys should return None."""
        result = build_tool_preview("custom_tool", {"foo": "bar"})
        assert result is None

    def test_long_value_truncated(self):
        """Preview should truncate long values."""
        long_cmd = "a" * 100
        result = build_tool_preview("terminal", {"command": long_cmd}, max_len=40)
        assert result is not None
        assert len(result) <= 43  # max_len + "..."

    def test_process_tool_with_none_args(self):
        """Process tool special case should also handle None args."""
        assert build_tool_preview("process", None) is None

    def test_process_tool_normal(self):
        result = build_tool_preview("process", {"action": "poll", "session_id": "abc123"})
        assert result is not None
        assert "poll" in result

    def test_todo_tool_read(self):
        result = build_tool_preview("todo", {"merge": False})
        assert result is not None
        assert "reading" in result

    def test_todo_tool_with_todos(self):
        result = build_tool_preview("todo", {"todos": [{"id": "1", "content": "test", "status": "pending"}]})
        assert result is not None
        assert "1 task" in result

    def test_memory_tool_add(self):
        result = build_tool_preview("memory", {"action": "add", "target": "user", "content": "test note"})
        assert result is not None
        assert "user" in result

    def test_memory_replace_missing_old_text_marked(self):
        # Avoid empty quotes "" in the preview when old_text is missing/None.
        result = build_tool_preview("memory", {"action": "replace", "target": "memory"})
        assert result == '~memory: "<missing old_text>"'
        result = build_tool_preview("memory", {"action": "remove", "target": "memory", "old_text": None})
        assert result == '-memory: "<missing old_text>"'

    def test_session_search_preview(self):
        result = build_tool_preview("session_search", {"query": "find something"})
        assert result is not None
        assert "find something" in result

    def test_false_like_args_zero(self):
        """Non-dict falsy values should return None, not crash."""
        assert build_tool_preview("terminal", 0) is None
        assert build_tool_preview("terminal", "") is None
        assert build_tool_preview("terminal", []) is None


class TestBuildToolPreviewLocalization:
    """build_tool_preview(lang=...) localizes dynamic English fragments.

    The English / default behavior must stay byte-identical so legacy callers
    (CLI spinner, API server SSE) keep their current output; the Chinese path
    only kicks in when ``lang="zh"`` is passed explicitly.
    """

    def test_todo_planning_zh(self):
        result = build_tool_preview(
            "todo",
            {"todos": [{"id": "1"}, {"id": "2"}, {"id": "3"}]},
            lang="zh",
        )
        assert result == "规划 3 个任务"

    def test_todo_updating_zh(self):
        result = build_tool_preview(
            "todo",
            {"todos": [{"id": "1"}], "merge": True},
            lang="zh",
        )
        assert result == "更新 1 个任务"

    def test_todo_reading_zh(self):
        result = build_tool_preview("todo", {"merge": False}, lang="zh")
        assert result == "读取任务列表"

    def test_todo_planning_default_unchanged(self):
        """No lang -> existing English phrasing, unchanged for legacy callers."""
        result = build_tool_preview(
            "todo", {"todos": [{"id": "1"}, {"id": "2"}, {"id": "3"}]},
        )
        assert result == "planning 3 task(s)"

    def test_todo_planning_explicit_en(self):
        """Explicit lang='en' must match the no-lang default."""
        result = build_tool_preview(
            "todo", {"todos": [{"id": "1"}]}, lang="en",
        )
        assert result == "planning 1 task(s)"

    def test_session_search_zh_uses_chinese_recall_phrase(self):
        result = build_tool_preview(
            "session_search", {"query": "找点东西"}, lang="zh",
        )
        assert result is not None
        assert "回忆" in result
        assert "找点东西" in result

    def test_memory_replace_missing_old_zh(self):
        result = build_tool_preview(
            "memory", {"action": "replace", "target": "user"}, lang="zh",
        )
        assert result == '~user: "<缺少 old_text>"'

    def test_send_message_zh(self):
        result = build_tool_preview(
            "send_message", {"target": "alice", "message": "hi"}, lang="zh",
        )
        assert result == '发往 alice：「hi」'

    def test_unknown_lang_falls_back_to_english(self):
        """Garbage lang values should not crash, just stay in English."""
        result = build_tool_preview(
            "todo", {"todos": [{"id": "1"}]}, lang="klingon",
        )
        assert result == "planning 1 task(s)"

    def test_skill_view_preview_independent_of_lang(self):
        """Primary-arg passthrough tools don't localize -- the *name* arg is
        a skill identifier and must stay verbatim regardless of locale."""
        en = build_tool_preview("skill_view", {"name": "wiki"})
        zh = build_tool_preview("skill_view", {"name": "wiki"}, lang="zh")
        assert en == "wiki"
        assert zh == "wiki"


class TestGetToolDisplayName:
    def test_default_returns_tool_name(self):
        assert get_tool_display_name("skill_view") == "skill_view"

    def test_english_returns_tool_name(self):
        assert get_tool_display_name("skill_view", lang="en") == "skill_view"

    def test_zh_overrides_known_tools(self):
        assert get_tool_display_name("skill_view", lang="zh") == "技能详情"
        assert get_tool_display_name("todo", lang="zh") == "任务计划"
        assert get_tool_display_name("terminal", lang="zh") == "终端"

    def test_zh_unknown_tool_falls_back(self):
        assert get_tool_display_name("imaginary_tool", lang="zh") == "imaginary_tool"

    def test_unknown_lang_falls_back(self):
        assert get_tool_display_name("skill_view", lang="klingon") == "skill_view"

    def test_empty_tool_name(self):
        assert get_tool_display_name("", lang="zh") == ""


class TestFormatToolProgressLine:
    """The gateway bubble formatter is a pure function so we can pin its
    output exactly without spinning up the messaging runtime."""

    def test_short_mode_english(self):
        line = format_tool_progress_line(
            "skill_view",
            {"name": "wiki"},
            emoji="📚",
            mode="all",
        )
        assert line == '📚 skill_view: "wiki"'

    def test_short_mode_zh_localizes_name_and_preview(self):
        line = format_tool_progress_line(
            "todo",
            {"todos": [{"id": "1"}, {"id": "2"}, {"id": "3"}]},
            emoji="📝",
            mode="all",
            lang="zh",
        )
        assert line == '📝 任务计划：「规划 3 个任务」'

    def test_skill_view_zh_bubble(self):
        """Exact regression scenario from the user complaint: a Chinese user
        seeing "skill_view: ..." should now see "技能详情：..."."""
        line = format_tool_progress_line(
            "skill_view",
            {"name": "wiki"},
            emoji="📚",
            mode="all",
            lang="zh",
        )
        assert line == '📚 技能详情：「wiki」'

    def test_short_mode_falls_back_when_no_preview(self):
        line = format_tool_progress_line(
            "skill_view",
            None,
            emoji="📚",
            preview=None,
            mode="all",
        )
        assert line == "📚 skill_view..."

    def test_short_mode_truncates_to_cap(self):
        line = format_tool_progress_line(
            "terminal",
            {"command": "a" * 100},
            emoji="⚡",
            mode="all",
            preview_cap=20,
        )
        assert line.endswith('..."')
        assert len(line) <= 40  # emoji + name + quotes + 20 chars + ellipsis

    def test_verbose_mode_dumps_args(self):
        line = format_tool_progress_line(
            "skill_view",
            {"name": "wiki"},
            emoji="📚",
            mode="verbose",
            preview_cap=0,
        )
        assert "skill_view(['name'])" in line
        assert '"name": "wiki"' in line

    def test_verbose_mode_zh_uses_localized_name(self):
        line = format_tool_progress_line(
            "skill_view",
            {"name": "wiki"},
            emoji="📚",
            mode="verbose",
            lang="zh",
            preview_cap=0,
        )
        assert "技能详情(['name'])" in line

    def test_explicit_preview_overrides_derivation(self):
        """If the caller pre-computed a preview, the formatter uses it
        instead of recomputing from args -- lets the gateway pass through
        the localized preview the agent core already built."""
        line = format_tool_progress_line(
            "todo",
            {"todos": [{"id": "1"}]},
            emoji="📝",
            preview="custom preview",
            mode="all",
            lang="en",
        )
        assert line == '📝 todo: "custom preview"'


class TestCuteToolMessagePreviewLength:
    def test_terminal_preview_unlimited_when_config_is_zero(self):
        set_tool_preview_max_len(0)
        command = "curl -s http://localhost:9222/json/list | jq -r '.[] | select(.type==\"page\")' | head -5"

        line = get_cute_tool_message("terminal", {"command": command}, 0.1)

        assert command in line
        assert "..." not in line

    def test_terminal_preview_uses_positive_configured_limit(self):
        set_tool_preview_max_len(80)
        command = "curl -s http://localhost:9222/json/list | jq -r '.[] | select(.type==\"page\")' | head -5"

        line = get_cute_tool_message("terminal", {"command": command}, 0.1)

        assert command[:77] in line
        assert "..." in line
        assert "head -5" not in line

    def test_search_files_preview_uses_positive_configured_limit_not_default(self):
        set_tool_preview_max_len(80)
        pattern = "function.formatToolCall.context.preview.compactPreview.maxLength.truncate"

        line = get_cute_tool_message("search_files", {"pattern": pattern}, 0.1)

        assert pattern in line
        assert "..." not in line

    def test_path_preview_uses_positive_configured_limit_not_default(self):
        set_tool_preview_max_len(80)
        path = "/tmp/hermes-test-preview-length/deeply/nested/path/test-output.txt"

        line = get_cute_tool_message("read_file", {"path": path}, 0.1)

        assert path in line
        assert "..." not in line

    def test_write_file_lint_error_result_is_not_marked_failed(self):
        result = json.dumps({
            "bytes_written": 12,
            "lint": {"status": "error", "output": "SyntaxError: invalid syntax"},
        })

        line = get_cute_tool_message("write_file", {"path": "/tmp/a.py"}, 0.1, result=result)

        assert "[error]" not in line

    def test_patch_lsp_diagnostics_result_is_not_marked_failed(self):
        result = json.dumps({
            "success": True,
            "diff": "--- a/tmp.py\n+++ b/tmp.py\n",
            "lsp_diagnostics": "<diagnostics>ERROR [1:1] type mismatch</diagnostics>",
        })

        line = get_cute_tool_message("patch", {"path": "/tmp/a.py"}, 0.1, result=result)

        assert "[error]" not in line


class TestEditDiffPreview:
    def test_extract_edit_diff_for_patch(self):
        diff = extract_edit_diff("patch", '{"success": true, "diff": "--- a/x\\n+++ b/x\\n"}')
        assert diff is not None
        assert "+++ b/x" in diff

    def test_render_inline_unified_diff_colors_added_and_removed_lines(self):
        rendered = _render_inline_unified_diff(
            "--- a/cli.py\n"
            "+++ b/cli.py\n"
            "@@ -1,2 +1,2 @@\n"
            "-old line\n"
            "+new line\n"
            " context\n"
        )

        assert "a/cli.py" in rendered[0]
        assert "b/cli.py" in rendered[0]
        assert any("old line" in line for line in rendered)
        assert any("new line" in line for line in rendered)
        assert any("48;2;" in line for line in rendered)

    def test_extract_edit_diff_ignores_non_edit_tools(self):
        assert extract_edit_diff("web_search", '{"diff": "--- a\\n+++ b\\n"}') is None

    def test_extract_edit_diff_uses_local_snapshot_for_write_file(self, tmp_path):
        target = tmp_path / "note.txt"
        target.write_text("old\n", encoding="utf-8")

        snapshot = capture_local_edit_snapshot("write_file", {"path": str(target)})

        target.write_text("new\n", encoding="utf-8")

        diff = extract_edit_diff(
            "write_file",
            '{"bytes_written": 4}',
            function_args={"path": str(target)},
            snapshot=snapshot,
        )

        assert diff is not None
        assert "--- a/" in diff
        assert "+++ b/" in diff
        assert "-old" in diff
        assert "+new" in diff

    def test_render_edit_diff_with_delta_invokes_printer(self):
        printer = MagicMock()

        rendered = render_edit_diff_with_delta(
            "patch",
            '{"diff": "--- a/x\\n+++ b/x\\n@@ -1 +1 @@\\n-old\\n+new\\n"}',
            print_fn=printer,
        )

        assert rendered is True
        assert printer.call_count >= 2
        calls = [call.args[0] for call in printer.call_args_list]
        assert any("a/x" in line and "b/x" in line for line in calls)
        assert any("old" in line for line in calls)
        assert any("new" in line for line in calls)

    def test_render_edit_diff_with_delta_skips_without_diff(self):
        rendered = render_edit_diff_with_delta(
            "patch",
            '{"success": true}',
        )

        assert rendered is False

    def test_render_edit_diff_with_delta_handles_renderer_errors(self, monkeypatch):
        printer = MagicMock()

        monkeypatch.setattr("agent.display._summarize_rendered_diff_sections", MagicMock(side_effect=RuntimeError("boom")))

        rendered = render_edit_diff_with_delta(
            "patch",
            '{"diff": "--- a/x\\n+++ b/x\\n"}',
            print_fn=printer,
        )

        assert rendered is False
        assert printer.call_count == 0

    def test_summarize_rendered_diff_sections_truncates_large_diff(self):
        diff = "--- a/x.py\n+++ b/x.py\n" + "".join(f"+line{i}\n" for i in range(120))

        rendered = _summarize_rendered_diff_sections(diff, max_lines=20)

        assert len(rendered) == 21
        assert "omitted" in rendered[-1]

    def test_summarize_rendered_diff_sections_limits_file_count(self):
        diff = "".join(
            f"--- a/file{i}.py\n+++ b/file{i}.py\n+line{i}\n"
            for i in range(8)
        )

        rendered = _summarize_rendered_diff_sections(diff, max_files=3, max_lines=50)

        assert any("a/file0.py" in line for line in rendered)
        assert any("a/file1.py" in line for line in rendered)
        assert any("a/file2.py" in line for line in rendered)
        assert not any("a/file7.py" in line for line in rendered)
        assert "additional file" in rendered[-1]
