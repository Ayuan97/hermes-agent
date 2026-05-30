# 公司 GitLab 日报 — 2026-05-30

**日期：** 2026-05-30（周六）
**数据范围：** 2026-05-28 ~ 2026-05-30（最近 72 小时）
**来源：** GitLab API（gitlab.e-idear.com）

---

## 1. 活跃项目筛选依据

全部 89 个项目中，按 `last_activity_at`、分支最新 commit 时间、MR/Pipeline 活动综合判断，最近 72 小时有实际活动的项目共 **9 个**，其中 Top 7 为重点跟踪项目：

| 项目 | 最后活动时间 | 活跃分支数 | 判定依据 |
|------|-------------|-----------|---------|
| lnct-web | 05-30 17:58 | 7 | dev/dev-hd/dev-duouo/dev-hank/dev-wj-workflow/ci/* 持续推送 50+ commit |
| livephoto-app | 05-30 17:50 | 2 | dev-duoduo-v3 分支 17 commits，Android 端适配密集 |
| justuscut | 05-30 17:25 | 6 | v3/dev/dev-gq/feat/video-agent/feature/* 大批分支活跃，Pipeline 5 次成功 |
| justus-content-core | 05-30 17:29 | 14 | dev/dev-gq/hd_dev/feature/* 共 50+ commits，3 条 MR 合并，Pipeline 持续成功 |
| whale-flow | 05-30 17:28 | 1 | main 分支 zhaowenlong 密集提交 20+ commits |
| engine-image-generation | 05-30 15:34 | 2 | feat/gemini-native-protocol + main 各有更新 |
| xhs_helper | 05-30 13:30 | 1 | dev-zzz 分支持续提交 |
| justus-web | 05-29 13:04 | 3 | web-admin-v2 + feature/agent-pricing-* 分支 |
| ln-agents | 05-28 10:29 | 2 | v2/master 有 Pipeline (#7851 生产环境) |

其他 80 个项目（如 boss-agi、crawler-server、media-agent 等）最近活动均超过 1 个月，无变化。

---

## 2. 项目看板

### 2.1 lnct-web（前端项目，小红书内容创作工具）

| 指标 | 数据 |
|------|------|
| 活跃分支 | dev + dev-hd + dev-duouo + dev-hank + dev-wj-workflow + ci/*（共 7 个） |
| 提交数 | 50+（近 24h 约 30 个） |
| MR | 10 个已合并（05-28），当前无 open MR |
| Pipeline | #8302 pending (dev)、#8301 pending (dev-wj-workflow)、#8299 success (deploy-web-engine-te) |
| Issues | 无 |

**今日内容：**
- **对标帖子（seeding-note）**：网格新增「+」继续添加入口、提交保留原始链接、产品主图上传引入裁剪、恢复任务时回填产品信息
- **借图成帖（borrow-image-post）**：补充素材统一为单图横向卡+裁剪、提交前表单草稿本地持久化、生成中任务可进结果页看实时进度
- **素材采集（materials）**：transfer 后强制刷列表、drawer 自动关闭、hidden_blocks 全链路修复
- **视频生成 & 字幕擦除**：撤回 duration*50 前端预估（回退）、逐标题前端按时长粗估算力拦截
- **素人人设（amateur-persona）**：新增素人人设智能体 + 结果页 + 任务列表视图（wj 开发）
- **分享修复**：多图与 Live 按原始顺序合成保存（lichengduo）

**管理判断：** 项目高度活跃，guoqiang 集中推进 seeding-note 和 borrow-image-post 两条功能线进入收尾冲刺；hd 持续修复采集模块 hidden_blocks；zhaohua 合并视频算力预检。建议明日 review 所有 MR。

### 2.2 livephoto-app（Android 客户端）

| 指标 | 数据 |
|------|------|
| 活跃分支 | dev-duoduo-v3（唯一活跃） |
| 提交数 | 17 个（05-28~05-30） |
| MR | 无 |
| Pipeline | 无 |
| Issues | 无 |

**今日内容：**
- Android 端 vivo/OPPO 动态照片兼容适配
- 全局 UI 等比缩小解决荣耀窄屏适配、登录页表单高度适配
- 弹窗统一为 AppMessageDialog/AppConfirmDialog
- Live 分享多图到小红书、列表下拉刷新/上拉加载

**管理判断：** lichengduo 独自推进 Android 端适配，覆盖范围广（兼容性+UI+分享），但无 MR 提交和无 reviewer。建议安排 code review。

### 2.3 justuscut（后端核心服务）

| 指标 | 数据 |
|------|------|
| 活跃分支 | v3/dev + dev-gq + feat/video-agent + v3/dev-qh + v3/fix/dev-hank + feature/*（6+） |
| 提交数 | 33 个（v3/dev） + 32 个（dev-gq） |
| MR | 8 个已合并（05-28~05-30）：字幕擦除、熔断、退款、JWT 修复等 |
| Pipeline | 5 次成功（05-30）：v3/dev、dev-gq、feat/video-agent 等 |
| Issues | 无 |

**今日内容：**
- **字幕擦除（subtitle-erase）**：GhostCut 配置桥接、YAML 直写 AK、清理死配置字段（zhaohua/hank）
- **计费熔断（billing）**：ProcessThirdPartyLog 单任务熔断（-200阈值）+ revert + 防并发穿透（zhaohua）
- **退款子流程**：GetDetail 端点用于退款状态轮询（qh）
- **JWT 修复**：Redis 切换后合法 JWT 走懒补录而非踢下线（hank）
- **帖子改造工坊（post_remake_workshop）**：v3/dev 接入（guoqiang）
- **公司管理**：管理员手机号变更冗余字段同步修复（qh）

**管理判断：** 多人并行开发，计费熔断经历了「加→revert→再调整」过程，说明该模块风险较高。建议关注 billing 模块稳定性。

### 2.4 justus-content-core（内容核心服务）

| 指标 | 数据 |
|------|------|
| 活跃分支 | dev + dev-gq + hd_dev + feature/*（14 个） |
| 提交数 | 50+（近 24h 约 35 个） |
| MR | 11 个已合并（05-29~05-30）：智能体定价、字幕擦除、采集修复、工坊优化 |
| Pipeline | #8297 success (dev)、#8293 success (dev-gq) 等持续成功 |
| Issues | 无 |

**今日内容：**
- **智能体定价（agent-pricing）**：业务智能体+Prompt Agent 定价后台 API、PageEstimateCache 三层简化、重算 fallback_unit P75（zhaohua）
- **字幕擦除**：接入 llm_models+model_pricing 精细化定价、算力计费冻结/结算/退款（zhaohua）
- **采集修复（xhs-collect）**：局部 move hidden_blocks 全链路修订、视频 cover 不被污染、博主简介/性别字段（hd）
- **帖子工坊（post_remake_workshop）**：补素材改为一项一图、修正编排耗尽误判、预分析提示词注入、latest-material-gate-detail 恢复入口（guoqiang）
- **对标帖子（product-ad-note）**：支持记录原始链接 source_url、latest-unfinished 增加 exclude_failed（guoqiang）
- **图片编辑**：call_logs.module_name 改写英文+反算 SQL 修盲区（zhaohua）

**管理判断：** 内容核心服务是最活跃的后端项目，guoqiang（工坊/对标帖子）和 zhaohua（定价/计费/字幕擦除）两条线并行推进，hd 集中修采集 hidden_blocks。建议关注 MR #338（定价加字幕擦除项）的审核。

### 2.5 whale-flow（AI Agent 引擎）

| 指标 | 数据 |
|------|------|
| 活跃分支 | main（唯一活跃） |
| 提交数 | 22 个（05-30 密集推送） |
| MR | !1 docs: add AI assistant integration design spec（open） |
| Pipeline | 无最新 Pipeline（上次 #3281 failed） |
| Issues | 无 |

**今日内容：**
- **Engine 核心改造**：384/385 批次共 10+ commit，涵盖 perTurnRecall、跨 run 工作态续传、skill dedup、SOP cadence 兜底、stuck detection、framework kind 对照 payload、memory archive swee
- **378 daemon mode 重构**：废止 engine 自启 Chrome，直接 daemon API 操作用户 Chrome，SSE 路由修复，screencast 跟随 active page
- **screencast handoff**：用户浏览器镜像引导接管扫码/登录/授权
- **Framework 心法强化**：401 学习闭环 4 断点全修、400 P1 假成功回归、同一命令反复返空→换路非换词

**管理判断：** zhaowenlong 单人在 main 分支密集提交 22 个 commit，无 MR 审核直接推 main。涉及核心引擎架构重构（daemon mode、framework 心法），风险极高，建议强制 code review。

### 2.6 engine-image-generation（图片生成引擎）

| 指标 | 数据 |
|------|------|
| 活跃分支 | feat/gemini-native-protocol + main（实质同一 commit） |
| 提交数 | 1（05-30） |
| MR | 无 |
| Pipeline | 无最新（上次 04-07 失败） |
| Issues | 无 |

**今日内容：**
- 新增 Gemini native generateContent 协议（gemini_generate）

**管理判断：** hank 添加 Gemini 原生协议适配，单 commit 无 MR。建议补充单元测试和 MR review。

### 2.7 xhs_helper（小红书辅助工具）

| 指标 | 数据 |
|------|------|
| 活跃分支 | dev-zzz（唯一活跃） |
| 提交数 | 6 个（05-28~05-30） |
| MR | 无 |
| Pipeline | 无最新 |
| Issues | 无 |

**今日内容：**
- v3 适配 XHS 新 header DOM + dual-mount
- push 博主纯笔记列表时携带 split_save_mode=text_image
- header 按钮按优先级单挂载 + display 切换
- 修复「采集本页笔记」拿错数据

**管理判断：** zhangzz 持续适配 XHS 前端变更，单人开发无 MR。建议补充 review。

### 2.8 justus-web（后台管理界面）

| 指标 | 数据 |
|------|------|
| 活跃分支 | web-admin-v2（feature/agent-pricing-*） |
| 提交数 | 4（05-29） |
| MR | !5 合并为单 tab「智能体定价」、!4 新增定价 tab |
| Pipeline | 无 |
| Issues | 无 |

**今日内容：**
- 算力管理新增「业务智能体定价 / Prompt Agent 定价」两个 tab → 合并为单 tab「智能体定价」

**管理判断：** zhaohua 推进定价后台 UI，前日拆两个 tab 后日合并为一个，反映产品需求仍在快速迭代。

### 2.9 ln-agents（AI Agent 代理层）

| 指标 | 数据 |
|------|------|
| 活跃分支 | v2/master（生产环境） |
| 提交数 | 0（但 Pipeline 有部署） |
| Pipeline | #7851 success「生产环境-0528」 |
| MR | 无 open |

**管理判断：** 05-28 部署生产环境版本，之后无代码变更。稳定运行中。

---

## 3. 人员看板

### 3.1 赵华鹏（zhaohua）

| 项目 | 分支 | 提交数 | 内容摘要 |
|------|------|--------|---------|
| justus-content-core | dev + feature/* | ~15 | 智能体定价 API、字幕擦除计费接入、PageEstimateCache 三层简化、fallback_unit 重算 |
| justuscut | v3/dev + feature/* | ~8 | GhostCut 配置桥接、计费熔断、字幕擦除清理 |
| lnct-web | dev | ~7 | 视频算力预检、前端时长粗估、字幕擦除 API path 调整、UI 修复 |
| justus-web | web-admin-v2 | ~4 | 定价后台 UI tab |
| whale-flow | MR !1 | — | 提交 AI 助手集成设计规范 MR |

**具体事项：**
1. justus-content-core：智能体定价后台 API + 字幕擦除 llm_models 精细化定价 + 算力计费冻结/结算
2. justuscut：GhostCut 配置桥接 + 计费熔断（单任务 -200 阈值）
3. lnct-web：视频生成/字幕擦除前端按时长粗估算力拦截 + UI 修复
4. justus-web：算力管理后台「智能体定价」tab 合并

**管理判断：** 今日覆盖面极广，横跨 4 个项目、计费/定价/字幕擦除/UI 四条线。建议主子关注计费熔断模块是否需要统一收敛。

### 3.2 guoqiang（国强）

| 项目 | 分支 | 提交数 | 内容摘要 |
|------|------|--------|---------|
| justus-content-core | dev + dev-gq | ~20 | 帖子工坊素材修复/编排修正/恢复入口、对标帖子 source_url、产品投笔记对标图片上限放宽 |
| justuscut | v3/dev + dev-gq | ~8 | 帖子改造工坊后端正向推进 |
| lnct-web | dev | ~15 | seeding-note 入口/主图/提交、borrow-image-post 表单持久化/进度/徽章 |

**具体事项：**
1. content-core：补素材一项一图、编排耗尽误判修正、latest-material-gate-detail 恢复入口、预分析提示词注入、对标帖子 source_url
2. lnct-web：seeding-note 新增继续添加入口+主图裁剪、borrow-image-post 草稿持久化+进度实时+补充素材卡片统一

**管理判断：** 前端+后端双线高产，是今日 commit 数最多的开发人员。帖子工坊和对标帖子两条功能线即将收尾，建议本周安排验收。

### 3.3 hd（黄东）

| 项目 | 分支 | 提交数 | 内容摘要 |
|------|------|--------|---------|
| justus-content-core | dev + hd_dev | ~15 | 素材采集 hidden_blocks 全链路修复、局部 move 口径/展示/视频 cover |
| lnct-web | dev-hd | ~6 | materials transfer 后强制刷列表、drawer 自动关闭、hidden_blocks 跟随派生 |

**具体事项：**
1. content-core：mc_v2 List/Get hidden filter、局部 move A/B/C/D/E/F 6 步全链路、每张 asset 双 URL hidden_block
2. lnct-web：普通文件夹 collect_excerpt drawer 跟随 materials 重派生 + fully-hidden 自动关

**管理判断：** 专注 hidden_blocks 功能模块的端到端修复，后端+前端全链路覆盖。建议关注该模块 05-28~30 间是否已稳定。

### 3.4 lichengduo（李成多）

| 项目 | 分支 | 提交数 | 内容摘要 |
|------|------|--------|---------|
| livephoto-app | dev-duoduo-v3 | 17 | OPPO/vivo 动态照片兼容、全局 UI 缩小适配荣耀、统一弹窗、Live 分享修复 |
| lnct-web | dev-duouo | 2 | 多图 live 按原始顺序合成分享 |

**具体事项：**
1. livephoto-app：Android 端 vivo/OPPO 动态照片兼容、UI 等比缩小适配、统一弹窗样式、Live 图历史卡片首帧黑屏修复
2. lnct-web：分享多张图片与 Live 合成保存

**管理判断：** Android 端全量问题修复，覆盖兼容性/UI/分享/弹窗四大块，但无 Mr 审核。建议安排 code review。

### 3.5 hank

| 项目 | 分支 | 提交数 | 内容摘要 |
|------|------|--------|---------|
| engine-image-generation | feat/gemini-native-protocol | 1 | Gemini native generateContent 协议 |
| justuscut | v3/dev + v3/fix/dev-hank | 4 | JWT 懒补录修复、测试环境 agent 配置切换、生产配置文件修复 |

**具体事项：**
1. engine-image-generation：新增 Gemini 原生协议适配
2. justuscut：Redis 切换后 JWT 走懒补录 + agent 配置切换 + 生产配置文件修复

**管理判断：** Gemini 协议适配是关键基础设施更新，建议补充单元测试。

### 3.6 zhangzz（张ZZ）

| 项目 | 分支 | 提交数 | 内容摘要 |
|------|------|--------|---------|
| lnct-web | dev + dev-zzz2 | ~10 | 素材卡片类型适配、全选生成 group block、悬浮窗展开、评论详情显示 |
| xhs_helper | dev-zzz | 6 | XHS 新 header DOM 适配、split_save_mode、博主推送参数 |

**具体事项：**
1. lnct-web：摘选文本类素材 cards SVG、图片全选生成 group block、摘选评论详情显示源笔记标题
2. xhs_helper：XHS v3 header dual-mount + display 切换 + 采集修复

**管理判断：** 前端物料模块细节打磨 + 小红书插件端适配。单人双线，建议关注 xhs_helper 是否需要合并到主分支。

### 3.7 qh（秦浩）

| 项目 | 分支 | 提交数 | 内容摘要 |
|------|------|--------|---------|
| justuscut | v3/dev-qh | 5 | 退款 GetDetail 端点、管理员手机号同步修复、gofmt |

**具体事项：**
1. justuscut：退款子流程 GetDetail 端点 + 退款状态轮询
2. justuscut：修复管理员手机号变更时冗余字段同步

**管理判断：** 退款功能上线中，建议主子关注退款流程的测试覆盖。

### 3.8 suyl（孙YL）

| 项目 | 分支 | 提交数 | 内容摘要 |
|------|------|--------|---------|
| lnct-web | dev | 4 | 借图成帖体验优化+种草笔记图片渲染、死代码清理、注释清理 |

**具体事项：**
1. lnct-web：优化借图成帖体验 + 修复种草笔记图片渲染
2. lnct-web：清理 borrow-image-post/seeding-note 死代码

**管理判断：** 代码清理是好事，建议持续。

### 3.9 wj（王杰）

| 项目 | 分支 | 提交数 | 内容摘要 |
|------|------|--------|---------|
| lnct-web | dev-wj-workflow | 3 | 素人人设智能体 + 结果页 + 任务列表视图 |

**具体事项：**
1. lnct-web：新增素人人设智能体（amateur-persona）前端功能
2. lnct-web：弹窗扩展 batch_text raw 透传

**管理判断：** 素人人设功能前端基本就绪，建议明日关注后端联调状态。

### 3.10 许裕桥（yuqiao.xu）

| 项目 | 分支 | 提交数 | 内容摘要 |
|------|------|--------|---------|
| justus-content-core | feat/video-agent | 1 | Merge branch 'dev' into feat/video-agent |

**管理判断：** 仅做了分支同步，未见新增开发内容。

---

## 4. 风险/阻塞

| 序号 | 风险描述 | 涉及项目 | 严重程度 |
|------|----------|---------|---------|
| 1 | **whale-flow 引擎核心重构无 MR 审核**：zhaowenlong 在 main 分支直接推送 22 个 commit，涉及 daemon mode 废弃自启 Chrome、framework 心法改造等核心变更，无 Code Review | whale-flow | 🔴 高 |
| 2 | **justus-content-core CI 卡走本地合并**：多个 commit 标记「CI 卡走本地合」，表明 Pipeline CI 可能阻塞了正常的合并流程 | justus-content-core | 🟡 中 |
| 3 | **计费熔断反转**：billing ProcessThirdPartyLog 熔断经历了「加→revert→refine」过程，该模块稳定性需要关注 | justuscut | 🟡 中 |
| 4 | **livephoto-app / xhs_helper 无 MR 无 Pipeline**：两项目大量代码推送但无 CI 验证和审查流程 | livephoto-app / xhs_helper | 🟡 中 |
| 5 | **engine-image-generation Pipeline 长期失败**：自 04-07 以来所有 Pipeline 均失败或取消，Gemini 新协议无 CI 覆盖 | engine-image-generation | 🟡 中 |

---

## 5. 明日跟进（05-31）

| 序号 | 跟进事项 | 责任人 |
|------|---------|--------|
| 1 | whale-flow engine 架构重构（daemon mode + framework 心法）——要求 zhaowenlong 补 MR 并安排 Code Review | zhaowenlong |
| 2 | 帖子工坊（post_remake_workshop）和 seeding-note 功能验收——两条线均在收尾冲刺 | guoqiang / 产品 |
| 3 | 字幕擦除计费全链路（前端粗估→后端冻结→终态结算）——关注是否有遗漏场景 | zhaohua |
| 4 | livephoto-app Android 端适配——安排 code review | lichengduo |
| 5 | justus-content-core Pipeline CI 卡顿问题排查 | infra / guoqiang |

---

## 6. 统计汇总

**全部项目数：** 89
**近期活跃项目（72h）：** 9
**重点活跃项目：** 7
**活跃开发人员：** 10
**总提交数（近 24h 估算）：** ~100+
**已合并 MR：** 18
**Open MR：** 2
**活跃 Pipeline：** ~8

---

*报告由 Hermes Agent 自动生成于 2026-05-30 18:00*
