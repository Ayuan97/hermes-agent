# 公司 GitLab 项目日报 — 2026-05-31

> 统计时间窗口：2026-05-30 00:00 UTC ~ 2026-05-31 08:00 UTC（北京时间 08:00 ~ 次日 16:00）
> 数据来源：GitLab API (gitlab.e-idear.com)

---

## 一、活跃项目筛选依据

扫描全部 129 个项目，按 `last_activity_at` 排序，筛选出最近 24-72 小时有实际开发活动的项目共 **9 个**（其余 120 个项目近期无更新）：

| # | 项目 | 命名空间 | 最后活跃时间 | 活跃分支数 |
|---|------|----------|-------------|-----------|
| 1 | **JustusCut** | enginer/justuscut | 05-30 18:33 | 3 个活跃分支 |
| 2 | **lnct-web** | zhaowenlong/lnct-web | 05-30 18:23 | 5 个活跃分支 |
| 3 | **xhs_helper** | Kakarrot/xhs_helper | 05-30 18:39 | 1 个活跃分支 |
| 4 | **whale-flow** | root/whale-flow | 05-30 18:19 | 1 个活跃分支 (main) |
| 5 | **justus-content-core** | enginer/justus-content-core | 05-30 18:17 | 6+ 个活跃分支 |
| 6 | **livephoto-app** | zhaowenlong/livephoto-app | 05-30 17:50 | 1 个活跃分支 |
| 7 | **engine-Image-generation** | enginer/engine-image-generation | 05-30 15:34 | 1 个活跃分支 |
| 8 | **justUs-web** | enginer/justus-web | 05-29 05:04 | 近 24h 无 commit |
| 9 | **ln-agents** | enginer/ln-agents | 05-28 10:51 | 近 24h 无 commit |

> 注：justUs-web、ln-agents 虽然 last_activity_at 在 48h 内，但近 24h 无提交，本期仅统计有实际 commits 的项目。

---

## 二、项目详情

### 1. JustusCut (enginer/justuscut)

**活跃分支：** dev-gq, v3/dev, v3/hd

**提交统计：** 2 commits（含 merge 重复计数，实际 1 个有效提交）

| 提交者 | 时间 | 内容 |
|-------|------|------|
| guoqiang | 05-30 17:25 | Extra 注释 |

**Pipeline：** #8312 ✅ success (v3/hd)

**MR：** 无

**小结：** 今日仅一笔注释提交，无明显功能推进。dev-gq 分支有开发动作但内容少量。

---

### 2. lnct-web (zhaowenlong/lnct-web)

**活跃分支：** dev, dev-hd, dev-wj-workflow

**提交统计：** 24 条 commits（含 merge 重复）

| 提交者 | 提交数 | 主要工作内容 |
|-------|-------|------------|
| guoqiang | 10 | seeding-note（种草笔记）表单功能：产品主图裁剪、对标帖子保留原始链接、草稿本地持久化、"+继续添加"入口；borrow-image-post（借图发帖）功能：生成中任务看实时进度、补充素材 UI 重构、表单草稿持久化；修复 heic 不显示、恢复任务丢产品主图等问题 |
| hd | 4 | materials（素材库）修复：我的采集 transfer 后强制刷新列表、drawer 自动关闭、普通文件夹 collect_excerpt drawer 跟随重置 |
| zhaohua | 2 | 撤回视频生成前端 duration*50 预估 → 改回纯余额兜底 |
| wj | 2 | 素人人设智能体+结果页+任务列表视图（amateur-persona） |

**Pipeline：**
- #8311 ✅ success (deploy-web-engine-test)
- #8309 ❌ failed (dev-hd)
- #8307 ❌ failed (dev)
- #8301 ❌ failed (dev-wj-workflow)
- #8283 ❌ failed (feat/video-agent)

**MR：** 无

**小结：** lnct-web 是今日最活跃的前端项目。**guoqiang** 重点推进「种草笔记」和「借图发帖」两大功能模块，完成了多个表单交互改进。**wj** 新增「素人人设」功能。**zhaohua** 回滚了视频生成时长预估逻辑。Pipeline 有多条失败，dev-wj-workflow 和 feat/video-agent 需要关注。

---

### 3. xhs_helper (Kakarrot/xhs_helper)

**活跃分支：** dev-zzz

| 提交者 | 时间 | 内容 |
|-------|------|------|
| zhangzz | 05-30 18:39 | feat(v3): 搜索结果主动翻页采集核心模块（逆向做法 A，暂未接入） |
| zhangzz | 05-30 13:30 | feat: v2 纯笔记列表博主推送增加 split_save_mode 图文分存参数 |

**MR/Issue/Pipeline：** 无

**小结：** **张卓志** 在推进小红书采集工具 v3 版本——搜索结果主动翻页采集（逆向模式），以及 v2 笔记列表推送增加图文分存参数。

---

### 4. whale-flow (root/whale-flow)

**活跃分支：** main

**提交统计：** 23 条 commits（全部赵文龙）

| 提交者 | 主要工作内容 |
|-------|------------|
| zhaowenlong | **引擎核心改造（384/385 batch 1-9）**：runAgentLoop 加 perTurnRecall、跨 run 工作态续传、skill dedup 阈值 0.4、STAGE_SAFETY_NET 拉大缓解预算死锁、work-queue stuck detection、framework kind 对照 payload、SOP cadence 兜底、runCountMax 减半、memory archive sweep、cached_tokens 真读 |
| | **Screencast/Handoff（378）**：完全重构 daemon mode（废自启 Chrome，走 daemon API 操作用户 Chrome）、SSE 路由修复、screencast 跟随 active page + 防白屏 |
| | **browser.page.open RPC（390）**：CDP /json/new 创持久 page |
| | **基础修复**：403 P0 sop-parser frontmatter 非对象不抛错、framework 核心心法（同一命令反复返空→换路）、373 复发治理（kind 误分类警告 + framework 占位激活两段式） |
| | **Studio 修复**：主对话区只竖滚、378 screencast handoff viewer、askUser webAction marker |

**MR：** !1 — docs: add AI assistant integration design spec (赵华鹏, fix-ignore-docs-scratch→main)

**Pipeline：** 无

**小结：** **赵文龙** 今日主力推进 whale-flow 引擎层，涉及 384/385 batch 多个改造包（引擎核心强化）、378 daemon/screencast/handoff（浏览器操控基础设施）、390 browser.page.open RPC 等。属重大底层重构，建议关注：378 daemon 模式重构后需验证稳定性。

---

### 5. justus-content-core (enginer/justus-content-core)

**活跃分支：** dev, dev-gq, dev-qh, hd_dev, feature/feature-pricing-add-subtitle-erase, feat/video-agent 等

**提交统计：** 30+ 条 commits

| 提交者 | 提交数 | 主要工作内容 |
|-------|-------|------------|
| guoqiang | 8+ | product-ad-note（产品广告笔记）：对标帖子支持 source_url；ay_config.module.config 新模块展示映射；post_remake_workshop（帖子改造工坊）：修正生图编排耗尽误判为违规、补素材改为一项一图 |
| hd | 6+ | xhs-collect（小红书采集）：局部 move 隐藏全链路修订、mc_v2 List/Get 接 hidden filter、视频 cover 不被污染、博主简介/性别字段批量筛选 |
| zhaohua | 3+ | subtitle-erase（字幕擦除）：接入 llm_models + model_pricing 精细定价、算力计费对接（时长粗估冻结+终态结算）、定价管理前台新增字幕擦除价目卡 |
| qh | 2 | expert-persona（专家人设工作流完整实现）、smart-persona（素人人设工作流功能） |
| yuqiao.xu | 1 | Merge dev→feat/video-agent |

**Pipeline：**
- #8310 ✅ success (hd_dev)
- #8306 ❌ failed (dev-qh)

**MR：** ! — chore(sql): 定价管理价目卡新增「字幕擦除」(zhaohua, feature/feature-pricing-add-subtitle-erase→dev)

**小结：** justus-content-core 是今日后端主力。**guoqiang** 推进产品广告笔记和帖子改造工坊模块；**hd** 大修小红书采集隐藏逻辑全链路；**zhaohua** 完成字幕擦除计费全链路（模型定价+算力计费+前台价目）；**qh** 实现专家人设和素人人设工作流。Pipeline 中 dev-qh 失败需关注。

---

### 6. livephoto-app (zhaowenlong/livephoto-app)

**活跃分支：** dev-duoduo-v3

| 提交者 | 时间 | 内容 |
|-------|------|------|
| lichengduo | 05-30 17:50 | fix(android): 选择文件夹弹窗限定最大高度并内部滚动 |
| lichengduo | 05-30 13:49 | refactor(android): 全局警告/确认弹窗统一为 AppMessageDialog/AppConfirmDialog |
| lichengduo | 05-30 10:51 | feat(android): vivo 动态照片适配 + 去小红书走相册选择器 |

**小结：** **李程多** 在 Android 端推进动态照片功能——vivo 适配、相册选择器接入、全局弹窗重构、文件夹选择 UI 优化。

---

### 7. engine-Image-generation (enginer/engine-image-generation)

**活跃分支：** feat/gemini-native-protocol, main

| 提交者 | 时间 | 内容 |
|-------|------|------|
| hank | 05-30 15:34 | feat(image): add Gemini native generateContent protocol (gemini_generate) |

**MR：** !6 — feat: 生图与失败重试的真实成本精确追踪 + 业务/企业归因 (赵华鹏, feat/cost-tracing-p0p2→main)

**小结：** **hank** 为生图引擎新增 Gemini 原生 generateContent 协议支持。**赵华鹏** 提交了 MR（生图成本追踪+企业归因），待合入。

---

## 三、人员开发进度

### 1. 赵文龙 (zhaowenlong)
| 项目 | 分支 | 动作 |
|-----|------|------|
| whale-flow | main | 23 commits |
| **今日内容：** |
| ① whale-flow 引擎层 384/385 batch 批量改造（perTurnRecall、跨 run 续传、skill dedup、safety net、work-queue 防死锁等 9 个 batch） |
| ② 378 daemon/screencast/handoff 完全重构（废自启 Chrome，改 daemon API 操作用户 Chrome） |
| ③ 390 browser.page.open RPC（CDP 持久 page）、373/368 复发治理（framework 心法强化） |
| **管理判断：** 今日产出极大，属架构级推进。378 daemon 模式重构后需验证稳定性，建议明日关注 CI 和测试覆盖。 |

### 2. 郭强 (guoqiang)
| 项目 | 分支 | 动作 |
|-----|------|------|
| lnct-web | dev, dev-hd | 10 commits |
| justus-content-core | dev, dev-gq | 8+ commits |
| JustusCut | dev-gq | 1 commit |
| **今日内容：** |
| ① lnct-web「种草笔记」模块：产品主图裁剪、对标帖子原始链接、表单草稿持久化、heic 不显示修复等 |
| ② lnct-web「借图发帖」模块：生成中任务实时进度、补充素材 UI 重构 |
| ③ justus-content-core：产品广告笔记 source_url、帖子改造工坊编排耗尽误判修正、补素材改为一项一图 |
| **管理判断：** 跨三个项目高强度推进前端功能开发，lnct-web 两个模块同时迭代，质量稳定。 |

### 3. hd
| 项目 | 分支 | 动作 |
|-----|------|------|
| lnct-web | dev, dev-hd | 4 commits |
| justus-content-core | dev, hd_dev | 6+ commits |
| **今日内容：** |
| ① lnct-web 素材库修复：transfer 后强制刷新列表、drawer 自动关闭、隐藏逻辑重置 |
| ② justus-content-core 小红书采集器：局部 move 隐藏全链路大修（A/B/C/D/E/F 六处）、hidden filter 接入、博主简介/性别字段 |
| **管理判断：** 集中在采集器和素材库隐藏逻辑的深度修复，技术复杂度高，今日完成质量较好。 |

### 4. 赵华鹏 (zhaohua)
| 项目 | 分支 | 动作 |
|-----|------|------|
| lnct-web | dev | 2 commits |
| justus-content-core | dev, feature/* | 3+ commits + 1 MR |
| engine-image-generation | feat/cost-tracing-p0p2 | 1 MR |
| whale-flow | fix-ignore-docs-scratch | 1 MR |
| **今日内容：** |
| ① lnct-web：撤回视频生成前端 duration*50 预估，改回纯余额兜底 |
| ② justus-content-core 字幕擦除计费：模型按 model 精细定价 + 算力计费（时长粗估冻结+终态结算）+ 前台价目卡新增 |
| ③ engine-image-generation MR：生图与失败重试的真实成本追踪 + 业务/企业归因 |
| ④ whale-flow MR：AI assistant 集成设计规格文档 |
| **管理判断：** 跨 4 个项目推进，计费侧工作量最大。字幕擦除计费全链路已就绪，需确认部署计划。 |

### 5. wj
| 项目 | 分支 | 动作 |
|-----|------|------|
| lnct-web | dev-wj-workflow | 2 commits |
| **今日内容：** |
| ① lnct-web「素人人设智能体」+ 结果页 + 任务列表视图 |
| ② batch_text raw 透传扩展 |
| **管理判断：** 人设工作流方向的新功能开发，与 qh 的专家人设/素人人设对应前端+后端配套。dev-wj-workflow 分支有 Pipeline 失败。 |

### 6. 张卓志 (zhangzz)
| 项目 | 分支 | 动作 |
|-----|------|------|
| xhs_helper | dev-zzz | 2 commits |
| **今日内容：** |
| ① xhs_helper v3：搜索结果主动翻页采集核心模块（逆向做法，暂未接入） |
| ② xhs_helper v2：笔记列表博主推送增加 split_save_mode 图文分存参数 |
| **管理判断：** 小红书采集工具 v3 逆向方案进入核心模块编码阶段，暂未启用。 |

### 7. 李程多 (lichengduo)
| 项目 | 分支 | 动作 |
|-----|------|------|
| livephoto-app | dev-duoduo-v3 | 3 commits |
| **今日内容：** |
| ① livephoto-app Android：vivo 动态照片适配 + 相册选择器接入 |
| ② 全局警告/确认弹窗统一重构（AppMessageDialog/AppConfirmDialog） |
| ③ 文件夹选择弹窗 UI 优化（最大高度+内部滚动） |
| **管理判断：** Android 端动态照片功能稳步推进，vivo 适配完成后需测试多机型兼容。 |

### 8. qh
| 项目 | 分支 | 动作 |
|-----|------|------|
| justus-content-core | dev-qh | 2 commits |
| **今日内容：** |
| ① justus-content-core「专家人设工作流」完整实现 |
| ② justus-content-core「素人人设工作流」功能 |
| **管理判断：** 人设工作流后端实现完成，dev-qh Pipeline 失败需排查。 |

### 9. hank
| 项目 | 分支 | 动作 |
|-----|------|------|
| engine-Image-generation | feat/gemini-native-protocol, main | 1 commit |
| **今日内容：** |
| ① 生图引擎新增 Gemini 原生 generateContent 协议 |
| **管理判断：** Gemini 协议接入完成，待后续集成测试。 |

### 10. 徐雨桥 (yuqiao.xu)
| 项目 | 分支 | 动作 |
|-----|------|------|
| justus-content-core | feat/video-agent | 1 merge |
| **今日内容：** |
| ① 合并 dev 到 feat/video-agent 分支 |

---

## 四、风险与阻塞

1. **🔴 lnct-web Pipeline 失败**：dev-wj-workflow (#8301 ❌ failed)、dev (#8307 ❌ failed)、dev-hd (#8309 ❌ failed)、feat/video-agent (#8283 ❌ failed) 多条 Pipeline 失败，需确认失败原因并修复。
2. **🔴 justus-content-core dev-qh Pipeline 失败** (#8306 ❌ failed)：qh 的人设工作流提交后 CI 未通过，需排查编译/测试问题。
3. **🟡 justus-web / ln-agents 无活跃提交**：这两个项目已有 2-3 天无明显开发动作，需确认资源分配是否正常。
4. **🟡 whale-flow 378 daemon 模式重构风险**：赵文龙今日完全重构了 daemon 模式（废自启 Chrome → daemon API 操作用户 Chrome），涉及底层架构变更，需验证无回归。
5. **🟡 xhs_helper v3 逆向方案未接入**：翻页采集核心模块已完成但暂未接入，进度可控但需关注落地上线时间。

---

## 五、明日跟进

1. **lnct-web Pipeline 修复**：跟进 guoqiang/hd/wj 修复 dev/dev-hd/dev-wj-workflow 分支 Pipeline 失败。
2. **justus-content-core dev-qh CI**：确认 qh 的 CI 失败原因，确保人设工作流可合入 dev。
3. **whale-flow 378 daemon 测试**：确认赵文龙的 daemon 重构有足够的端到端测试覆盖。
4. **字幕擦除计费部署确认**：赵华鹏的计费全链路（模型定价+算力计费+前台价目）已就绪，确认部署计划。
5. **justus-web / ln-agents 进展**：了解这两个项目当前无活跃提交的原因，确认开发资源安排。

---

## 六、原始数据说明

- 扫描项目总数：129
- 过滤规则：`last_activity_at` 在 2026-05-28 ~ 2026-05-31 范围内，且近 24h 有实际 commits
- API 端点：`/api/v4/projects`、`/repository/branches`、`/repository/commits`、`/merge_requests`、`/issues`、`/pipelines`
- 报告生成时间：2026-05-31 ~16:00 CST
