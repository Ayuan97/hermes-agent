# AI 早报 · 2026-06-03（周三）

## 📌 一句话总览

微软连发两个自研模型（推理+编码）正面叫板 Anthropic；OpenAI 模型正式登陆 AWS；Anthropic 把 Mythos 级能力扩到 150 家关键基础设施组织；特朗普签了缩减版 AI 行政令。

---

## 🔥 重点新闻（5 条）

### 1. 微软发布 MAI-Thinking-1 和 MAI-Code-1-Flash 双模型

- **链接**：[MAI-Thinking-1](https://microsoft.ai/news/introducing-mai-thinking-1/) · [MAI-Code-1-Flash](https://microsoft.ai/news/introducingmai-code-1-flash/)
- **要点**：
  - MAI-Thinking-1：35B 活跃参数、约 1T 总参数的稀疏 MoE 模型，在 SWE-Bench Pro 上与 Claude Opus 4.6 打平，盲评中优于 Sonnet 4.6
  - MAI-Code-1-Flash：轻量编码模型，在编码基准上性价比超过 Claude Haiku 4.5，已集成进 GitHub Copilot 和 VS Code
- **为什么重要**：微软不再只依赖 OpenAI，自研模型直接对标 Anthropic 产品线，从推理到编码全覆盖
- **主子关注**：可以对比 MAI-Thinking-1 和 Claude Opus 在实际编码任务上的差异，看 MoE 架构在推理模型上的性价比优势

### 2. OpenAI 前沿模型和 Codex 正式上线 AWS

- **链接**：[openai.com](https://openai.com/index/openai-frontier-models-and-codex-are-now-available-on-aws/)
- **要点**：OpenAI 模型（包括 Codex）现在可通过 AWS Bedrock 调用，这是 OpenAI 首次大规模进入竞争对手的云平台
- **为什么重要**：打破了 OpenAI 只能通过 Azure 使用的限制，企业用户选择更多了。也说明 OpenAI 在分发策略上更务实
- **主子关注**：如果主力用 AWS，现在可以直接走 Bedrock 调 GPT 系列，不用再单独接 OpenAI API

### 3. Anthropic 扩展 Project Glasswing 至 150+ 组织

- **链接**：[anthropic.com](https://www.anthropic.com/news/expanding-project-glasswing)
- **要点**：从最初的 50 家扩展到约 150 家，覆盖 15+ 国家，涉及关键基础设施、开源软件维护者和美国政府。Claude Mythos Preview 用于网络防御任务
- **为什么重要**：Anthropic 正在成为政府/国防级 AI 供应商，Mythos 级别能力（可能是最强模型）仅限安全合作伙伴使用
- **主子关注**：关注 Mythos 模型何时公开，以及 Glasswing 模式对 AI 安全治理的影响

### 4. 特朗普签署缩减版 AI 行政令

- **链接**：[Politico](https://www.politico.com/news/2026/06/02/trump-signs-downsized-ai-order-00946389)
- **要点**：经过数周的政策反复，特朗普签署了范围缩减的 AI 行政命令（具体细节待进一步确认）
- **为什么重要**：美国 AI 监管方向的风向标，影响中美 AI 合作、出口管制、企业合规
- **主子关注**：待具体条文出来后重点关注出口管制和开源模型相关条款

### 5. Perplexity 发布「搜索即代码生成」新架构

- **链接**：[research.perplexity.ai](https://research.perplexity.ai/articles/rethinking-search-as-code-generation)
- **要点**：将搜索从单体服务重构为可编程原语（Search as Code, SaC），让 Agent 能像写代码一样组合搜索流程
- **为什么重要**：AI Agent 时代的搜索不再是"发查询、收结果"的黑盒，而是可拆解、可编程的基础设施
- **主子关注**：如果在做 Agent 类产品，这个架构思路值得借鉴

---

## 📈 GitHub 趋势（5 个）

### 1. chopratejas/headroom ⭐ 6.4k (+1,265/天)

- **链接**：[github.com/chopratejas/headroom](https://github.com/chopratejas/headroom)
- **用途**：压缩工具输出、日志、文件、RAG 内容再喂给 LLM，减少 60-95% token 用量，保持答案质量
- **热度原因**：Agent 开发者痛点——上下文窗口不够用，这个工具直接解决
- **上手价值**：⭐⭐⭐⭐⭐ 支持 Python/TypeScript，有 MCP Server 模式，可直接接入 Claude Code/Cursor

### 2. OpenBMB/VoxCPM ⭐ 25.1k (+783/天)

- **链接**：[github.com/OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM)
- **用途**：VoxCPM2——无 Tokenizer 的多语言 TTS，支持语音克隆、创意声音设计
- **热度原因**：清华系出品，Tokenizer-Free 架构是 TTS 新方向，多语言+克隆效果好
- **上手价值**：⭐⭐⭐⭐ 做中文语音合成、数字人、播客工具的话值得关注

### 3. nesquena/hermes-webui ⭐ 12.5k (+1,722/天)

- **链接**：[github.com/nesquena/hermes-webui](https://github.com/nesquena/hermes-webui)
- **用途**：Hermes Agent 的 Web UI，支持浏览器和手机访问
- **热度原因**：让 Hermes Agent 有了图形界面，降低了使用门槛
- **上手价值**：⭐⭐⭐⭐ 已经在用 Hermes Agent 的话直接装上，手机端体验不错

### 4. affaan-m/ECC ⭐ 204k (+1,533/天)

- **链接**：[github.com/affaan-m/ECC](https://github.com/affaan-m/ECC)
- **用途**：Agent Harness 性能优化系统——技能、本能、记忆、安全模块，适配 Claude Code/Codex/Opencode/Cursor
- **热度原因**：20 万 star 的超级项目，编码 Agent 生态的基础设施级工具
- **上手价值**：⭐⭐⭐⭐⭐ 用编码 Agent 必装，能显著提升 Agent 的任务完成率

### 5. D4Vinci/Scrapling (+1,182/天)

- **链接**：[github.com/D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)
- **用途**：自适应网页爬虫框架，从单请求到全规模爬取一站式搞定
- **热度原因**：AI 数据工程刚需，反爬能力强，API 设计友好
- **上手价值**：⭐⭐⭐⭐ 做数据采集、RAG 数据源构建很实用

---

## 🤖 模型/框架更新（5 条）

### 1. MAI-Thinking-1（微软）

- **链接**：[microsoft.ai](https://microsoft.ai/news/introducing-mai-thinking-1/)
- **更新点**：35B-active/~1T-total MoE 推理模型，SWE-Bench Pro 与 Opus 4.6 持平，数学推理强
- **影响**：微软自研推理模型正式上线，中等推理成本即可获得顶级编码能力

### 2. MAI-Code-1-Flash（微软）

- **链接**：[microsoft.ai](https://microsoft.ai/news/introducingmai-code-1-flash/)
- **更新点**：轻量编码模型，已集成到 GitHub Copilot，性价比超 Claude Haiku 4.5
- **影响**：Copilot 用户可能已经在用但不知道，实际编码体验提升

### 3. Anthropic Claude Mythos Preview（via Project Glasswing）

- **链接**：[anthropic.com](https://www.anthropic.com/news/expanding-project-glasswing)
- **更新点**：Mythos 级能力扩展到 150 家组织，用于网络安全防御
- **影响**：目前仅限安全合作伙伴，但暗示 Anthropic 最强模型即将公开

### 4. DeepSeek-V4-Flash × AMD MI300X 兼容性报告

- **链接**：[fergusfinn.com](https://fergusfinn.com/blog/deepseek-v4-flash-mi300x/)
- **更新点**：详细记录了在 AMD MI300X 上用 vLLM 跑 DeepSeek-V4-Flash 的各种坑（FP8 方言、段错误等）
- **影响**：AMD GPU 用户的实战参考，目前 vLLM + MI300X + DeepSeek-V4 还不能直接用

### 5. OpenAI 模型上线 AWS Bedrock

- **链接**：[openai.com](https://openai.com/index/openai-frontier-models-and-codex-are-now-available-on-aws/)
- **更新点**：GPT 系列 + Codex 可通过 AWS Bedrock API 调用
- **影响**：多云策略落地，企业不再被 Azure 绑定

---

## 🏆 今日最值得深挖 Top 3

1. **微软 MAI-Thinking-1**：MoE 架构在推理模型上的性价比验证。值得深挖 35B 活跃参数如何做到与 Opus 4.6 打平，以及 MoE 稀疏激活对推理速度的实际影响。
2. **Perplexity SaC 架构**：搜索即代码生成的范式转换。对做 Agent 产品的人来说，这是搜索基础设施的未来形态，值得通读全文。
3. **headroom token 压缩**：60-95% 的 token 压缩率在实际 Agent 工作流中的效果验证。如果真能保持答案质量，对所有 Agent 开发者都是省钱利器。

---

## ✍️ 可转成视频/文章的选题

1. **微软 vs Anthropic：自研模型正面交锋** — MAI-Thinking-1 对标 Opus 4.6、MAI-Code-1-Flash 对标 Haiku 4.5，微软为什么不再只靠 OpenAI？对比测试 + 行业分析
2. **省 95% token！headroom 压缩工具实测** — 实测在 Claude Code / Cursor 等 Agent 中接入 headroom 后的 token 消耗变化和答案质量，实操教程
3. **AI Agent 时代的搜索长什么样？Perplexity 的新答案** — 解读 SaC 架构，为什么 Agent 需要可编程搜索，以及对开发者意味着什么

---

*数据来源：HackerNews、GitHub Trending、项目官网、HuggingFace · 生成时间：2026-06-03 09:00*
