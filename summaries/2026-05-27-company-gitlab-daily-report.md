# 公司 GitLab 每日进度汇报（2026-05-27）

- 统计时间：2026-05-27 14:20:03（北京时间）
- 统计窗口：最近 24 小时；风险背景参考最近 2-3 天及打开事项
- GitLab：https://gitlab.e-idear.com

## 今日一句话总览
近 24 小时检查 30/102 个项目，5 个项目有活动，共 32 次提交、7 个 MR 更新、0 个 Issue 更新；最活跃人员：zhaowenlong；失败/异常 Pipeline 42 个。

## 项目进展摘要
- **root/whale-flow**：提交 31，MR 更新 0，Issue 更新 0；Pipeline：#3281 failed(main)；风险：Pipeline #3281 failed
  - 主要提交：feat(engine): 批 238 §6.3.3 agent self-edit · memory.add 工具(通用工作集持久化)（zhaowenlong）；fix(engine): 批 237 修 studio 251 · 操作事实/进度独立注入 system prompt(防卡步骤0)（zhaowenlong）；fix(engine): 批 236 修 studio 250 · active-run 检查移出 speedMode 跳过块(防同 agent 并发重叠)（zhaowenlong）；fix(engine): 批 235 修 studio 249 · operationalFacts 去 LLM 噪音 + distill 喂真 args/result（zhaowenlong）；fix(studio): agent 待答卡片移到底部输入框正上方(对标 Claude Code/Codex)（zhaowenlong）
- **zhaowenlong/lnct-web**：提交 0，MR 更新 0，Issue 更新 0；Pipeline：#7738 success(deploy-web-engine-test), #7737 pending(dev), #7732 canceled(dev)；风险：Pipeline #7732 canceled；Pipeline #7734 canceled
- **enginer/justuscut**：提交 0，MR 更新 2，Issue 更新 0；Pipeline：#7726 success(v3/hd), #7713 success(dev-gq), #7685 success(v3/dev)；风险：Pipeline #7682 failed
  - MR：!132 closed docs: 费用追踪设计说明与实施记录；!141 merged feat(homepage-models): 对话模型新增「是否支持多模态」字段
- **enginer/justus-content-core**：提交 0，MR 更新 5，Issue 更新 0；Pipeline：#7729 success(dev), #7728 success(refs/merge-requests/289/head), #7727 success(hd_dev)；风险：Pipeline #7724 failed
  - MR：!289 merged fix(note_collection): 纯文本采集项 excerpt 兜底（下拉词/单条评论）；!288 merged feat(material_center_v2): 文件夹 grouped count 口径 + note_collec；!287 merged feat(billing): agent 调用前置算力校验 + 页面级预估展示；!286 merged feat(smart_creation): 新增「图文自动化生成」6 步 Agent 流水线模块（同步 + SSE）；!285 merged feat(material_center_v2): .txt 文本素材上传 + raw_metadata 透传链路 + 
- **enginer/engine-image-generation**：提交 1，MR 更新 0，Issue 更新 0；Pipeline：#4699 failed(main), #4698 canceled(main), #4697 canceled(main)；风险：Pipeline #4699 failed；Pipeline #4698 canceled；Pipeline #4697 canceled
  - 主要提交：fix(video): enforce seedance duration envelope at model layer（guoqiang）

### 近 24 小时无明显动静的重点项目
- customers/duoyan-ai、enginer/ln-agents、customers/scripts、enginer/engine-auto-test、zhaowenlong/livephoto-app、enginer/team-daily-progress、enginer/gotools、root/oa-new、root/justus-client、enginer/lnct、enginer/app/landingpage、enginer/web/v3、enginer/web/website、enginer/hermes、enginer/ares、enginer/app/cron、justus/feishu-order-plugin、root/xhs-pay-hook、root/ai_ads、enginer/boss-agi 等 24 个

## 人员开发进度
- **zhaowenlong**：提交 31 次，涉及项目：root/whale-flow。主要工作：提交：feat(engine): 批 238 §6.3.3 agent self-edit · memory.add 工具(通用工作集持久化)；fix(engine): 批 237 修 studio 251 · 操作事实/进度独立注入 system prompt(防卡步骤0)；fix(engine): 批 236 修 studio 250 · active-run 检查移出 speedMode 跳过块(防同 agent 并发重叠)；fix(engine): 批 235 修 studio 249 · operationalFacts 去 LLM 噪音 + distill 喂真 args/result；fix(studio): agent 待答卡片移到底部输入框正上方(对标 Claude Code/Codex)
- **guoqiang**：提交 1 次，涉及项目：enginer/engine-image-generation。主要工作：提交：fix(video): enforce seedance duration envelope at model layer
- **huang huangd**：提交 0 次，涉及项目：无提交项目。主要工作：MR：enginer/justus-content-core !289 merged fix(note_collection): 纯文本采集项 excerpt 兜底（；enginer/justus-content-core !288 merged feat(material_center_v2): 文件夹 grouped co；enginer/justus-content-core !285 merged feat(material_center_v2): .txt 文本素材上传 + 
- **赵华鹏**：提交 0 次，涉及项目：无提交项目。主要工作：MR：enginer/justuscut !132 closed docs: 费用追踪设计说明与实施记录；enginer/justus-content-core !287 merged feat(billing): agent 调用前置算力校验 + 页面级预估展示
- **hank hank**：提交 0 次，涉及项目：无提交项目。主要工作：MR：enginer/justuscut !141 merged feat(homepage-models): 对话模型新增「是否支持多模态」字段；enginer/justus-content-core !286 merged feat(smart_creation): 新增「图文自动化生成」6 步 Age

## 风险与阻塞
- Pipeline 异常：**root/whale-flow** #3281 状态 failed，分支/引用 main。
- Pipeline 异常：**zhaowenlong/lnct-web** #7732 状态 canceled，分支/引用 dev。
- Pipeline 异常：**zhaowenlong/lnct-web** #7734 状态 canceled，分支/引用 dev-wj-workflow。
- Pipeline 异常：**enginer/justuscut** #7682 状态 failed，分支/引用 feat/video-agent。
- Pipeline 异常：**enginer/justus-web** #957 状态 failed，分支/引用 master。
- Pipeline 异常：**enginer/justus-web** #956 状态 canceled，分支/引用 master。
- Pipeline 异常：**enginer/justus-web** #955 状态 canceled，分支/引用 master。
- Pipeline 异常：**enginer/justus-content-core** #7724 状态 failed，分支/引用 hd_dev。
- Pipeline 异常：**enginer/engine-image-generation** #4699 状态 failed，分支/引用 main。
- Pipeline 异常：**enginer/engine-image-generation** #4698 状态 canceled，分支/引用 main。
- MR 长期未合并：**root/whale-flow** !1《docs: add AI assistant integration design spec》，已打开 32 天，闲置 32 天。
- MR 长期未合并：**enginer/engine-image-generation** !6《feat: 生图与失败重试的真实成本精确追踪 + 业务/企业归因》，已打开 4 天，闲置 4 天。
- MR 长期未合并：**enginer/web/v3** !1《dev》，已打开 283 天，闲置 210 天。

## 明天建议跟进事项
- 优先处理失败/取消的 Pipeline，避免阻塞合并和发版。
- 梳理长期未合并 MR：确认是否继续推进、补评审还是关闭。
- 对近 24 小时无动静但仍在进行中的项目，明天站会确认是否卡住或只是未提交代码。
