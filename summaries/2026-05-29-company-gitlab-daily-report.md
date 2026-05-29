# 公司 GitLab 项目日报 — 2026-05-29

**GitLab 地址**：https://gitlab.e-idear.com
**统计口径**：最近 72 小时活跃项目 + 最近 24 小时详细活动
**项目总数**：129 个 | **活跃项目**：9 个 | **非活跃项目**：120 个

## 一句话结论
今日 9 个活跃项目共产生 1208 次提交、42 个 MR、0 个 Issue、258 条 Pipeline，涉及 17 人。

## 项目看板

| 项目 | 活跃分支 | 提交/MR/Issue/Pipeline | 今日关键内容 | 管理判断 |
|---|---|---|---|---|
| zhaowenlong/lnct-web | dev, dev-zzz2, dev-hd 等20个 | 688/7/0/135 | Merge branch 'dev-zzz2' into dev；feat(materials): 悬浮窗追加新数据时自动展开；chore(materials): 调整「我的采集」卡片 tag 文案与配色；style(borrow-image-post): 「生成中」徽章改回紫色，与其他任务列表统一 | 有MR待review |
| enginer/justus-content-core | dev, dev-gq, hd_dev 等18个 | 426/27/0/101 | Merge branch 'dev-gq' into 'dev'；fix(post_remake_workshop): failed 终态回填主表 error_message/error；feat(post-remake-workshop): /list 支持 statuses 集合过滤并收紧 only_a；feat(post-remake-workshop): 预分析提示词注入用户宣传对象 | 有MR待review |
| enginer/justuscut | v3/dev, v3/hd, dev-gq 等9个 | 47/6/0/22 | Merge branch 'hotfix/ghostcut-prod-credentials-clean' into '；fix(subtitle-erase): prod.yaml 直写 GhostCut 测试 AK 跟既有惯例对齐；Merge branch 'v3/fix/dev-hank' into 'v3/dev'；fix 测试环境agent服务配置切换 | 有MR待review |
| root/whale-flow | main | 19/0/0/0 | fix(engine): 354 僵尸 run 看门狗 · worker 两步间停迭代的 running run 回收解；fix(engine): P0 回归(349)· codex 去掉端点不支持的 prompt_cache_retenti；fix(engine): 347 eval→原生交互(根因 framework 自己) + 346① upsert 回喂；fix(engine): 超时不该掐死 agent 干活(2/2)· AI 媒体工具豁免外层 60s 插件调用超时 | 提交密集，关注进度 |
| zhaowenlong/livephoto-app | dev-duoduo-v3 | 18/0/0/0 | fix(android): 全局 UI 等比缩小，解决荣耀等窄屏整体布局偏大；fix(android): 登录输入框收窄 + 监控刷新间隔选项等宽；feat(android): 兼容 OPPO/vivo 动态照片，修复荣耀 Live 分享到小红书；fix(android): 作品卡片状态/图片数/Live数标签同存时自适应不裁切 | 提交密集，关注进度 |
| enginer/justus-web | web-admin-v2, feature/agent-pricing-tab-rename, feature/agent-pricing-admin-ui 等4个 | 8/2/0/0 | Merge branch 'feature/agent-pricing-tab-rename' into 'web-ad；refactor(credit): 合并为单 tab「智能体定价」,撤掉 Prompt Agent 定价；Merge branch 'feature/agent-pricing-admin-ui' into 'web-admi；feat(credit): 算力管理新增「业务智能体定价 / Prompt Agent 定价」两个 tab | 有MR待review |
| Kakarrot/xhs_helper | dev-zzz | 2/0/0/0 | fix(v3): 修复 AI 搜索/SPA 跳转下「采集本页笔记」拿错数据；fix(v3): header 按钮按优先级单挂载 + 监听 display 切换 | 稳定推进 |


## 人员看板

| 姓名 | 项目/分支 | 提交/MR/Issue | 今日关键内容 | 管理判断 |
|---|---|---|---|---|
| zhaohua | enginer/justus-content-core, enginer/justus-web, enginer/justuscut, zhaowenlong/lnct-web | 362/0/0 | Merge branch 'hotfix/erase-ui-polish-v2' into dev；fix(subtitle-erase): UI 修复——左栏不滚 + 空状态紧凑 + 模式卡不换行 + 视频两侧黑边；Merge branch 'hotfix/erase-task-card-slim' into dev | 高产出，关注review |
| zhangzz | Kakarrot/xhs_helper, zhaowenlong/lnct-web | 218/0/0 | Merge branch 'dev-zzz2' into dev；feat(materials): 悬浮窗追加新数据时自动展开；chore(materials): 调整「我的采集」卡片 tag 文案与配色 | 高产出，关注review |
| hd | enginer/justus-content-core, zhaowenlong/lnct-web | 173/0/0 | fix(materials): 单图 move 路由 + 批量图片 grid 稳定身份；fix(materials): 「选择该博主」目标 ct 按源保留，profile move 同步移除源卡；Merge branch 'dev' into dev-hd | 高产出，关注review |
| 赵华鹏 | enginer/justus-content-core, enginer/justus-web, enginer/justuscut, zhaowenlong/lnct-web | 113/27/0 | Merge branch 'hotfix/subtitle-erase-nil-safety-only' into 'd；Merge branch 'feature/image-edit-module-name-normalize' into；Merge branch 'hotfix/subtitle-erase-move-to-admin' into 'dev | 有27个MR待review |
| suyl | zhaowenlong/lnct-web | 74/0/0 | chore(borrow-image-post,seeding-note): 清理死代码；Merge remote-tracking branch 'origin/dev' into dev；feat(borrow-image-post): 优化借图成帖体验并修复种草笔记图片渲染 | 高产出，关注review |
| guoqiang | enginer/justus-content-core, zhaowenlong/lnct-web | 72/0/0 | style(borrow-image-post): 「生成中」徽章改回紫色，与其他任务列表统一；style(borrow-image-post): 「生成中」徽章改用 ecommerce 同款蓝色；Revert "fix(ecommerce-post-replica): 生成中/排队中徽章颜色由蓝色改为品牌紫，与其他 | 高产出，关注review |
| guoqiang ton | enginer/justus-content-core, enginer/justuscut | 65/4/0 | Merge branch 'dev-gq' into 'dev'；Merge branch 'hd_dev' into 'dev'；[MR] feat(post-remake-workshop): 新增 latest-material-gat | 有4个MR待review |
| wj | zhaowenlong/lnct-web | 36/0/0 | Merge branch 'dev' into dev-wj-workflow；chore(workflow): 恢复显示选题工作流入口卡片；chore(workflow): 暂时隐藏选题工作流入口卡片 | 高产出，关注review |
| lichengduo | zhaowenlong/livephoto-app, zhaowenlong/lnct-web | 26/0/0 | fix(share): 多张图片与 live 按原始顺序合成保存并一并分享；fix: 分享，携带多张 live | 高产出，关注review |
| qh | zhaowenlong/lnct-web | 23/0/0 | Merge remote-tracking branch 'origin/dev' into dev；Merge branch 'dev' into dev-qh | 高产出，关注review |
| zhaowenlong | root/whale-flow | 19/0/0 | fix(engine): 354 僵尸 run 看门狗 · worker 两步间停迭代的 running run 回收解；fix(engine): P0 回归(349)· codex 去掉端点不支持的 prompt_cache_retenti；fix(engine): 347 eval→原生交互(根因 framework 自己) + 346① upsert 回喂 | 高产出，关注review |
| 阿远 | zhaowenlong/lnct-web | 12/0/0 | ci(deploy): 部署链路迁移到 prod-tx,删除 staging 环境 | 高产出，关注review |
| hank | enginer/justuscut | 12/0/0 | fix 测试环境agent服务配置切换；Merge branch 'v3/fix/dev-hank' into v3/dev；fix 生产环境配置文件 | 高产出，关注review |
| huang huangd | enginer/justus-content-core | 0/8/0 | [MR] fix(note_collection): 局部 move hidden_blocks 全链路修复 ；[MR] Hd dev；[MR] style(note_collection): gofmt xhs_collect_hidden_b | 有8个MR待review |
| hank hank | enginer/justuscut | 3/1/0 | Merge branch 'v3/fix/dev-hank' into 'v3/dev'；[MR] fix 测试环境agent服务配置切换 | 有1个MR待review |

## 风险与阻塞

- ⚠ **zhaowenlong/lnct-web** Pipeline 大量 `canceled`（`dev`/`dev-hd`/`dev-zzz2` 等多分支频繁自动取消），可能为并发触发导致队列溢出
- ⚠ **zhaowenlong/lnct-web** `dev-hd`、`dev-zzz2`、`fix/image-clone-estimate-link-generation`、`dev-wj-workflow` 等多分支存在 **failed** Pipeline，需排查构建失败原因
- ⚠ **enginer/justus-content-core** `hd_dev`、`dev`、`dev-gq` 分支存在 failed Pipeline，多个 feature 分支 CI 不稳定
- ⚠ **enginer/justus-content-core** 仍有大量 feature 分支（agent-pricing、billing、subtitle-erase）Pipeline 偶尔失败后通过 MR 绕过，需确认是否回滚
- 📋 **lnct-web** 今日 MR 均为 merged 状态，无阻塞 review，但分支合并节奏快（Merge branch 占较多 commit），建议规范 squash merge

## 明日跟进

- [zhaowenlong/lnct-web] 排查多分支 Pipeline 频繁 `canceled` 原因（`dev`/`dev-hd`/`dev-zzz2`），关注队列并发策略
- [zhaowenlong/lnct-web] 修复 `dev-hd`、`dev-zzz2`、`dev-wj-workflow`、`fix/image-clone*` 分支 failed Pipeline
- [enginer/justus-content-core] 修复 `hd_dev`、`dev-gq` 分支 failed Pipeline，稳定 CI 环境
- [赵华鹏] 今日大量 MR 集中在 justus-content-core/justuscut/justus-web/lnct-web 四项目间跨仓协同，确认 agent-pricing/billing/subtitle-erase 各 Phase 交付时间线
- [zhaowenlong] whale-flow engine 核心修复密集（P0 回归 + 僵尸 run 看门狗），建议今日补单测/集成测试回归

## 项目明细

### zhaowenlong/lnct-web
- **最后活动**：2026-05-29T10:01:44.380Z
- **默认分支**：main
- **活跃分支**：
  - `dev` (最后提交: 2026-05-29T17:56:41) — Merge branch 'dev-zzz2' into dev
  - `dev-zzz2` (最后提交: 2026-05-29T17:42:19) — feat(materials): 悬浮窗追加新数据时自动展开
  - `dev-hd` (最后提交: 2026-05-29T16:54:39) — fix(materials): 单图 move 路由 + 批量图片 grid 稳定身份
  - `dev-duouo` (最后提交: 2026-05-29T15:20:53) — fix(share): 多张图片与 live 按原始顺序合成保存并一并分享
  - `fix/image-clone-estimate-link-generation` (最后提交: 2026-05-29T13:47:00) — fix(image-clone): 算力预估随单次产出数量联动
  - `dev-wj-workflow` (最后提交: 2026-05-29T11:24:06) — Merge remote-tracking branch 'origin/dev' into dev
  - `fix/cleanup-internal-codenames-in-comments` (最后提交: 2026-05-29T07:04:35) — chore(comments): 清理 ip-persona / topic-research / ROUTE_PATHS 内部代号注释
  - `feature/billing-cost-estimate-6pages` (最后提交: 2026-05-28T23:04:58) — fix(billing): ip-persona + topic-research 接入"消耗约 N 算力"提示
  - `fix/video-subtitle-erase-ts-null` (最后提交: 2026-05-28T22:28:16) — fix(types): video-subtitle-erase source-picker 兼容上游 nullable 字段
  - `feature/billing-cost-estimate-tooltip-onboarding` (最后提交: 2026-05-28T21:35:27) — fix(billing): 补 ROUTE_PATHS 让 4 个智能体页面正确发 X-Module-Name
  - `feature/billing-quantity-sync-with-form` (最后提交: 2026-05-28T20:19:12) — fix(billing): 消耗约 N 算力 与表单生成数量/图片数量联动
  - `feature/billing-silent-insufficient-compute` (最后提交: 2026-05-28T20:00:47) — fix(billing): 算力不足只弹全局 modal,业务页不再切整屏失败页
  - `feat/seeding-note-workflow` (最后提交: 2026-05-28T18:19:43) — feat(borrow-image-post): 接入图片编辑接口,任务中心借图 tab 加智能体后缀
  - `dev-qh` (最后提交: 2026-05-28T18:15:41) — Merge branch 'dev' into dev-qh
  - `ci/migrate-deploy-to-prod-tx` (最后提交: 2026-05-28T15:44:59) — ci(deploy): 回退 gzip 压缩
  - `ci/test-from-dev` (最后提交: 2026-05-28T15:26:42) — ci(deploy): 镜像传输管道加 gzip -1 压缩,预期减少 30-50% 传输时间
  - `feat/xhs-product-detail` (最后提交: 2026-05-28T14:45:45) — feat(xhs-product-detail): 新增电商详情页智能体（小红书 PDP 生成）
  - `dev-hank` (最后提交: 2026-05-28T14:16:17) — fix(auth): 监听 storage 同步多页签登录态
  - `dev-ay` (最后提交: 2026-05-28T11:02:34) — ci(deploy): 生产环境改为 build 在 runner、运行在 prod-tx
  - `feat/video-agent` (最后提交: 2026-05-27T15:09:42) — Merge branch 'dev' into feat/video-agent
- **24h 提交**：
  - `7ecc9934` [dev] Merge branch 'dev-zzz2' into dev — zhangzz (2026-05-29T17:56:41)
  - `f298ee07` [dev] feat(materials): 悬浮窗追加新数据时自动展开 — zhangzz (2026-05-29T17:42:19)
  - `4d8b0d77` [dev] chore(materials): 调整「我的采集」卡片 tag 文案与配色 — zhangzz (2026-05-29T17:41:03)
  - `25dd4ecd` [dev] style(borrow-image-post): 「生成中」徽章改回紫色，与其他任务列表统一 — guoqiang (2026-05-29T17:39:04)
  - `517957ac` [dev] style(borrow-image-post): 「生成中」徽章改用 ecommerce 同款蓝色 — guoqiang (2026-05-29T17:36:30)
  - `b572cd88` [dev] Revert "fix(ecommerce-post-replica): 生成中/排队中徽章颜色由蓝色改为品牌紫，与其他任务列表统一" — guoqiang (2026-05-29T17:33:18)
  - `7ca3451a` [dev] fix(ecommerce-post-replica): 生成中/排队中徽章颜色由蓝色改为品牌紫，与其他任务列表统一 — guoqiang (2026-05-29T17:29:21)
  - `f50692ed` [dev] fix(borrow-image-post): 「生成中」执行状态改为纯文字标签，去掉百分比与进度条 — guoqiang (2026-05-29T17:25:25)
  - `f7549f2b` [dev] feat(borrow-image-post): 任务列表默认仅展示 continue 后任务，状态筛选精简为4项 — guoqiang (2026-05-29T17:18:58)
  - `20355a24` [dev] chore(materials): 清理「我的采集」类型筛选项 — zhangzz (2026-05-29T17:09:20)
  - `cc90ef35` [dev] fix(materials): 单图 move 路由 + 批量图片 grid 稳定身份 — hd (2026-05-29T16:54:39)
  - `2eb5b507` [dev] fix(seeding-note-workflow): 开启新优化后不再自动恢复已放弃的任务 — guoqiang (2026-05-29T16:25:06)
  - `3bc07e9a` [dev] chore(borrow-image-post,seeding-note): 清理死代码 — suyl (2026-05-29T16:16:30)
  - `645bc9cc` [dev] Merge remote-tracking branch 'origin/dev' into dev — suyl (2026-05-29T16:06:26)
  - `5db1e3cd` [dev] feat(borrow-image-post): 优化借图成帖体验并修复种草笔记图片渲染 — suyl (2026-05-29T16:02:46)
  - `bf0db8fa` [dev] feat(borrow-image-post): continue 提交后直接进入「任务提交成功」页 — guoqiang (2026-05-29T15:59:08)
  - `c85e0b3e` [dev] fix(borrow-image-post): 恢复入口改用 latest-material-gate-detail 接口 — guoqiang (2026-05-29T15:34:07)
  - `7f8c298a` [dev] fix(share): 多张图片与 live 按原始顺序合成保存并一并分享 — lichengduo (2026-05-29T15:20:53)
  - `2b2b3c89` [dev] fix: 分享，携带多张 live — lichengduo (2026-05-29T15:07:28)
  - `0ed50fa6` [dev] Merge branch 'hotfix/erase-ui-polish-v2' into dev — zhaohua (2026-05-29T14:46:40)
  - ...及其他 668 条提交
- **24h MR**：
  - !10 **chore(comments): 清理 ip-persona / topic-research / ROUTE_PATHS 内部代号注释** (状态: merged, 作者: 赵华鹏) — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/merge_requests/10
  - !9 **fix(billing): ip-persona + topic-research 接入'消耗约 N 算力'提示** (状态: merged, 作者: 赵华鹏) — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/merge_requests/9
  - !8 **fix(types): video-subtitle-erase source-picker 兼容上游 nullable 字段** (状态: merged, 作者: 赵华鹏) — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/merge_requests/8
  - !6 **fix(billing): 补 ROUTE_PATHS 让 4 个智能体页面正确发 X-Module-Name** (状态: merged, 作者: 赵华鹏) — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/merge_requests/6
  - !5 **fix(billing): 消耗约 N 算力 与表单数量联动(dream-avatar / live-photo)** (状态: merged, 作者: 赵华鹏) — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/merge_requests/5
  - !4 **fix(billing): 算力不足只弹全局 modal,业务页不再切整屏失败页** (状态: merged, 作者: 赵华鹏) — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/merge_requests/4
  - !7 **feat(subtitle-erase): 页面骨架 + API service(Phase 5.D)** (状态: merged, 作者: 赵华鹏) — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/merge_requests/7
- **24h Pipeline**：
  - [deploy-web-engine-test] 状态: success — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8210
  - [dev] 状态: pending — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8209
  - [dev-zzz2] 状态: pending — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8208
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8207
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8206
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8205
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8204
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8200
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8198
  - [dev-zzz2] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8196
  - [deploy-web-engine-test] 状态: success — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8195
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8194
  - [dev-hd] 状态: running — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8193
  - [dev-hd] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8188
  - [deploy-web-engine-test] 状态: success — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8187
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8184
  - [dev-hd] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8183
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8182
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8181
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8180
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8179
  - [deploy-web-engine-test] 状态: success — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8177
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8176
  - [dev-duouo] 状态: running — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8175
  - [dev-duouo] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8174
  - [deploy-web-engine-test] 状态: success — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8171
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8170
  - [deploy-web-engine-test] 状态: success — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8169
  - [dev-hd] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8168
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8167
  - [dev-zzz2] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8166
  - [deploy-web-engine-test] 状态: success — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8159
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8158
  - [dev-hd] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8157
  - [dev-hd] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8156
  - [deploy-web-engine-test] 状态: success — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8147
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8146
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8143
  - [dev-zzz2] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8141
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8140
  - [fix/image-clone-estimate-link-generation] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8139
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8132
  - [dev-wj-workflow] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8129
  - [dev-hd] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8123
  - [dev] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8119
  - [dev-hd] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8117
  - [dev-hd] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8116
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8104
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8101
  - [deploy-web-engine-test] 状态: success — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8100
  - [dev-hd] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8099
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8098
  - [deploy-web-engine-test] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8097
  - [deploy-web-engine-test] 状态: success — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8096
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8095
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8094
  - [dev-zzz2] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8093
  - [dev-hd] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8092
  - [deploy-web-engine-test] 状态: success — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8090
  - [deploy-web-engine-test] 状态: success — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8082
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8081
  - [dev-zzz2] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8080
  - [deploy-web-engine-test] 状态: success — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8069
  - [dev-hd] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8068
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8067
  - [dev-wj-workflow] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8066
  - [dev] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8059
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8055
  - [refs/merge-requests/10/head] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8054
  - [fix/cleanup-internal-codenames-in-comments] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8053
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8052
  - [dev] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8050
  - [refs/merge-requests/9/head] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8049
  - [feature/billing-cost-estimate-6pages] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8048
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8047
  - [refs/merge-requests/8/head] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8046
  - [fix/video-subtitle-erase-ts-null] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8045
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8041
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8040
  - [refs/merge-requests/7/head] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8039
  - [refs/merge-requests/6/head] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8032
  - [feature/billing-cost-estimate-tooltip-onboarding] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8031
  - [feature/video-subtitle-erase-ghostcut] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8029
  - [dev-hd] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8025
  - [deploy-web-engine-test] 状态: success — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8021
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8020
  - [dev-zzz2] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8017
  - [deploy-web-engine-test] 状态: success — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8016
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8015
  - [deploy-web-engine-test] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8014
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8013
  - [dev-hd] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8012
  - [deploy-web-engine-test] 状态: success — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8008
  - [deploy-web-engine-test] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8007
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8006
  - [dev-hd] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8005
  - [dev-hd] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8004
  - [dev-zzz2] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8003
  - [deploy-web-engine-test] 状态: success — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/8000
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7999
  - [refs/merge-requests/5/head] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7997
  - [feature/billing-quantity-sync-with-form] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7996
  - [dev-hd] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7995
  - [deploy-web-engine-test] 状态: success — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7994
  - [refs/merge-requests/4/head] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7993
  - [feature/billing-silent-insufficient-compute] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7992
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7991
  - [deploy-web-engine-test] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7990
  - [dev-zzz2] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7989
  - [dev-zzz2] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7988
  - [deploy-web-engine-test] 状态: success — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7987
  - [dev-zzz2] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7986
  - [dev-zzz2] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7983
  - [dev] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7980
  - [dev-hd] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7976
  - [dev-wj-workflow] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7974
  - [dev-wj-workflow] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7972
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7971
  - [feat/seeding-note-workflow] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7970
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7969
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7968
  - [dev-hd] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7967
  - [dev-qh] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7966
  - [dev-hd] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7965
  - [deploy-web-engine-test] 状态: success — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7964
  - [dev-wj-workflow] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7963
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7962
  - [dev-wj-workflow] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7958
  - [feat/seeding-note-workflow] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7956
  - [dev-hd] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7954
  - [dev] 状态: canceled — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7948
  - [dev-zzz2] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7947
  - [dev-wj-workflow] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7939
  - [ci/migrate-deploy-to-prod-tx] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7916
  - [ci/test-from-dev] 状态: failed — https://gitlab.e-idear.com/zhaowenlong/lnct-web/-/pipelines/7911

---

### enginer/justus-content-core
- **最后活动**：2026-05-29T09:27:38.412Z
- **默认分支**：master
- **活跃分支**：
  - `dev` (最后提交: 2026-05-29T09:28:42) — Merge branch 'dev-gq' into 'dev'
  - `dev-gq` (最后提交: 2026-05-29T17:27:35) — fix(post_remake_workshop): failed 终态回填主表 error_message/error_detail
  - `hd_dev` (最后提交: 2026-05-29T08:45:07) — Merge branch 'hd_dev' into 'dev'
  - `feature/image-edit-module-name-normalize` (最后提交: 2026-05-29T13:56:49) — fix(image-edit): call_logs.module_name 改写英文 + 反算 SQL 修盲区(alias + 单次调用)
  - `feature/agent-pricing-rename-comments` (最后提交: 2026-05-29T13:11:04) — docs(agent-billing): 同步「智能体定价」改名 + p-stats-batch 路由说明
  - `feature/agent-pricing-admin-backend` (最后提交: 2026-05-29T11:06:08) — feat(agent-billing): 业务智能体 + Prompt Agent 定价后台 API
  - `feature/agent-pricing-priority-flip` (最后提交: 2026-05-29T10:52:12) — feat(billing): PageEstimateCache 简化为 运营冻结价 > P75 > 0 三层
  - `feature/agent-pricing-fallback-recompute` (最后提交: 2026-05-29T10:35:25) — chore(sql): 重算 module.config 各 module 的 fallback_unit 为近 30 天真实 P75
  - `feature/billing-dual-hdel-pending` (最后提交: 2026-05-29T10:34:24) — fix(billing): worker 终态双 HDel,释放 Create 入口写的 pending 槽位
  - `feature/billing-cleanup-inner-check-and-dual-release` (最后提交: 2026-05-29T09:57:48) — refactor(billing): 终态释放 Create 入口 pending 槽位 + 移除内层 chatclient 算力校验
  - `feature/billing-prebill-topic-research-and-ecommerce` (最后提交: 2026-05-29T07:06:16) — fix(billing): 选题调研 / IP 人设 / 电商种草帖子复刻 Create 入口接 prebill 冻结
  - `feature/billing-dbify-page-estimate` (最后提交: 2026-05-28T21:02:44) — refactor(billing): PageEstimateCache 走 ay_config.module.config 驱动
  - `feature/billing-sentinel-and-structured-error` (最后提交: 2026-05-28T19:10:24) — fix(billing): prebill 返结构化算力不足错误 + sentinel 收敛
  - `fix/dev-hank` (最后提交: 2026-05-28T08:19:58) — Merge branch 'dev-gq' into 'dev'
  - `feat/video-agent` (最后提交: 2026-05-28T16:08:59) — feat: 新增提示词反推功能
  - `feature/agent-billing-precheck` (最后提交: 2026-05-28T15:31:51) — fix(billing): dream_avatar retry 算力前置校验按 unit×count 计算
  - `feature/agent-billing-concurrent-pending` (最后提交: 2026-05-28T14:26:19) — test(billing): 同步 dream_avatar service Create 单测期望
  - `dev-qh` (最后提交: 2026-05-28T13:43:33) — Merge branch 'dev' into dev-qh
- **24h 提交**：
  - `908138fa` [dev] Merge branch 'dev-gq' into 'dev' — guoqiang ton (2026-05-29T09:28:42)
  - `854c18d8` [dev] fix(post_remake_workshop): failed 终态回填主表 error_message/error_detail — guoqiang (2026-05-29T17:27:35)
  - `b8911c23` [dev] feat(post-remake-workshop): /list 支持 statuses 集合过滤并收紧 only_after_continue_gate — guoqiang (2026-05-29T17:19:18)
  - `095bea18` [dev] feat(post-remake-workshop): 预分析提示词注入用户宣传对象 — guoqiang (2026-05-29T17:00:04)
  - `4c98b7ce` [dev] Merge branch 'hd_dev' into 'dev' — guoqiang ton (2026-05-29T08:45:07)
  - `aca50a6c` [dev] fix(note_collection): 局部 move hidden_blocks 全链路修复 + note_list_image 单图维度 — hd (2026-05-29T16:43:56)
  - `7b00997f` [dev] fix(note_collection): 局部 move hidden_blocks 全链路修复 + note_list_image 单图维度 — hd (2026-05-29T16:28:51)
  - `44c55e81` [dev] feat(product-ad-note): latest-unfinished 增加 exclude_failed 开关 — guoqiang (2026-05-29T16:25:40)
  - `f9f0c67c` [dev] feat(post-remake-workshop): 新增 latest-material-gate-detail 恢复入口 — guoqiang (2026-05-29T15:25:15)
  - `dcef22a8` [dev] Merge branch 'hotfix/subtitle-erase-nil-safety-only' into 'dev' — 赵华鹏 (2026-05-29T06:05:17)
  - `56e47a15` [dev] fix(subtitle-erase): submitGhostCut/submitAliyun 加 nil 客户端防御 — zhaohua (2026-05-29T14:02:26)
  - `5b697a26` [dev] Merge branch 'feature/image-edit-module-name-normalize' into 'dev' — 赵华鹏 (2026-05-29T05:58:01)
  - `8551eaa2` [dev] Merge branch 'hd_dev' into 'dev' — guoqiang ton (2026-05-29T05:57:20)
  - `f01bf591` [dev] fix(image-edit): call_logs.module_name 改写英文 + 反算 SQL 修盲区(alias + 单次调用) — zhaohua (2026-05-29T13:56:49)
  - `09ec33e7` [dev] style(note_collection): gofmt 3 个 hidden_blocks 相关文件 — hd (2026-05-29T13:55:38)
  - `41b459ec` [dev] Merge branch 'dev' into hd_dev — hd (2026-05-29T13:52:52)
  - `fd4b7064` [dev] fix(materials): hidden_blocks 写入/列表/重采集回归一揽子 — hd (2026-05-29T13:52:39)
  - `75200840` [dev] Merge branch 'hotfix/subtitle-erase-move-to-admin' into 'dev' — 赵华鹏 (2026-05-29T05:46:31)
  - `1ce264cc` [dev] fix(subtitle-erase): 路由从 /public/* 搬到 /admin/v1/* 修复无效 companyID 报错 — zhaohua (2026-05-29T13:25:54)
  - `c1819d96` [dev] Merge branch 'feature/agent-pricing-rename-comments' into 'dev' — 赵华鹏 (2026-05-29T05:24:05)
  - ...及其他 406 条提交
- **24h MR**：
  - !331 **feat(post-remake-workshop): 新增 latest-material-gate-detail 恢复入口** (状态: merged, 作者: guoqiang ton) — https://gitlab.e-idear.com/enginer/justus-content-core/-/merge_requests/331
  - !330 **fix(note_collection): 局部 move hidden_blocks 全链路修复 + note_list_image 单图维度** (状态: merged, 作者: huang huangd) — https://gitlab.e-idear.com/enginer/justus-content-core/-/merge_requests/330
  - !329 **fix(subtitle-erase): submitGhostCut/submitAliyun 加 nil 客户端防御** (状态: merged, 作者: 赵华鹏) — https://gitlab.e-idear.com/enginer/justus-content-core/-/merge_requests/329
  - !326 **fix(image-edit): call_logs.module_name 改英文 + 回填 SQL,修反算盲区** (状态: merged, 作者: 赵华鹏) — https://gitlab.e-idear.com/enginer/justus-content-core/-/merge_requests/326
  - !328 **Hd dev** (状态: merged, 作者: huang huangd) — https://gitlab.e-idear.com/enginer/justus-content-core/-/merge_requests/328
  - !327 **fix(subtitle-erase): 路由从 /public/* 搬到 /admin/v1/* 修复无效 companyID 报错** (状态: merged, 作者: 赵华鹏) — https://gitlab.e-idear.com/enginer/justus-content-core/-/merge_requests/327
  - !325 **docs(agent-billing): 同步「智能体定价」改名 + p-stats-batch 路由说明** (状态: merged, 作者: 赵华鹏) — https://gitlab.e-idear.com/enginer/justus-content-core/-/merge_requests/325
  - !5 **refactor: expose workflow metadata reader** (状态: merged, 作者: Administrator) — https://gitlab.e-idear.com/enginer/justus-content-core/-/merge_requests/5
  - !323 **feat(agent-billing): 业务智能体 + Prompt Agent 定价后台 API** (状态: merged, 作者: 赵华鹏) — https://gitlab.e-idear.com/enginer/justus-content-core/-/merge_requests/323
  - !320 **feat(billing): PageEstimateCache 简化为 运营冻结价 > P75 > 0 三层(删 globalFallbackUnit 与各业务 hardcoded 兜底)** (状态: merged, 作者: 赵华鹏) — https://gitlab.e-idear.com/enginer/justus-content-core/-/merge_requests/320
  - !319 **chore(sql): 重算 module.config 各 module 的 fallback_unit 为近 30 天真实 P75** (状态: closed, 作者: 赵华鹏) — https://gitlab.e-idear.com/enginer/justus-content-core/-/merge_requests/319
  - !324 **放宽产品投流笔记对标帖子图片上限：单帖20->30、单组30->100** (状态: merged, 作者: guoqiang ton) — https://gitlab.e-idear.com/enginer/justus-content-core/-/merge_requests/324
  - !321 **style(note_collection): gofmt xhs_collect_hidden_block_filter_test.go** (状态: merged, 作者: huang huangd) — https://gitlab.e-idear.com/enginer/justus-content-core/-/merge_requests/321
  - !322 **test(content-core): 删除 6 处失败测试以让 go test ./... 变绿** (状态: merged, 作者: guoqiang ton) — https://gitlab.e-idear.com/enginer/justus-content-core/-/merge_requests/322
  - !318 **fix(billing): worker 终态双 HDel,释放 Create 入口写的 pending 槽位** (状态: merged, 作者: 赵华鹏) — https://gitlab.e-idear.com/enginer/justus-content-core/-/merge_requests/318
  - !316 **refactor(billing): 终态释放 Create 入口 pending 槽位 + 移除内层 chatclient 算力校验** (状态: closed, 作者: 赵华鹏) — https://gitlab.e-idear.com/enginer/justus-content-core/-/merge_requests/316
  - !317 **feat: Enhance post remake workshop image handling with versioning support** (状态: merged, 作者: guoqiang ton) — https://gitlab.e-idear.com/enginer/justus-content-core/-/merge_requests/317
  - !314 **fix(billing): 选题调研 / IP 人设 / 电商种草帖子复刻 Create 入口接 prebill 冻结** (状态: merged, 作者: 赵华鹏) — https://gitlab.e-idear.com/enginer/justus-content-core/-/merge_requests/314
  - !315 **refactor(subtitle-erase): 精简表字段 31→17 + 产物改落素材库** (状态: merged, 作者: 赵华鹏) — https://gitlab.e-idear.com/enginer/justus-content-core/-/merge_requests/315
  - !313 **feat(subtitle-erase): GhostCut client + multi-provider 数据层(Phase 2)** (状态: merged, 作者: 赵华鹏) — https://gitlab.e-idear.com/enginer/justus-content-core/-/merge_requests/313
  - !311 **refactor(billing): PageEstimateCache 走 ay_config.module.config 驱动** (状态: merged, 作者: 赵华鹏) — https://gitlab.e-idear.com/enginer/justus-content-core/-/merge_requests/311
  - !308 **fix(billing): prebill 返结构化算力不足错误 + sentinel 收敛** (状态: merged, 作者: 赵华鹏) — https://gitlab.e-idear.com/enginer/justus-content-core/-/merge_requests/308
  - !312 **fix(note_collection): 含详情 envelope 走 update-duplicates 永远 not_found** (状态: merged, 作者: huang huangd) — https://gitlab.e-idear.com/enginer/justus-content-core/-/merge_requests/312
  - !310 **feat(note_collection): 聚光采集补正文+评论 + image_note/video_note 类型 + 文案 move 落 mc_v2 asset** (状态: merged, 作者: huang huangd) — https://gitlab.e-idear.com/enginer/justus-content-core/-/merge_requests/310
  - !309 **feat(note_collection): 博主笔记列表拆分保存改为 envelope 级聚合 + 配套配套放宽** (状态: merged, 作者: huang huangd) — https://gitlab.e-idear.com/enginer/justus-content-core/-/merge_requests/309
  - !307 **feat(note_collection): 博主笔记拆分保存两条作品** (状态: merged, 作者: huang huangd) — https://gitlab.e-idear.com/enginer/justus-content-core/-/merge_requests/307
  - !306 **feat(note_collection): 聚光笔记池采集入口 + 统一 OSS 转存修复 []string 形态漏抽** (状态: merged, 作者: huang huangd) — https://gitlab.e-idear.com/enginer/justus-content-core/-/merge_requests/306
- **24h Pipeline**：
  - [dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8203
  - [refs/merge-requests/331/head] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8202
  - [dev-gq] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8201
  - [dev-gq] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8199
  - [dev-gq] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8197
  - [hd_dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8192
  - [dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8191
  - [refs/merge-requests/330/head] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8190
  - [hd_dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8189
  - [hd_dev] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8186
  - [dev-gq] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8185
  - [dev-gq] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8178
  - [hd_dev] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8173
  - [dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8163
  - [refs/merge-requests/329/head] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8162
  - [hotfix/subtitle-erase-nil-safety-only] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8160
  - [dev] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8155
  - [dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8154
  - [refs/merge-requests/326/head] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8152
  - [feature/image-edit-module-name-normalize] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8151
  - [refs/merge-requests/328/head] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8150
  - [hd_dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8149
  - [refs/merge-requests/328/head] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8148
  - [hd_dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8145
  - [hd_dev] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8144
  - [hotfix/subtitle-erase-move-to-admin] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8142
  - [refs/merge-requests/326/head] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8138
  - [feature/image-edit-module-name-normalize] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8137
  - [dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8136
  - [refs/merge-requests/327/head] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8135
  - [refs/merge-requests/326/head] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8134
  - [feature/image-edit-module-name-normalize] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8133
  - [hotfix/subtitle-erase-move-to-admin] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8131
  - [dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8130
  - [refs/merge-requests/325/head] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8128
  - [feature/agent-pricing-rename-comments] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8127
  - [hd_dev] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8126
  - [dev] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8125
  - [dev] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8124
  - [dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8122
  - [refs/merge-requests/324/head] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8121
  - [dev-gq] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8120
  - [hd_dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8118
  - [refs/merge-requests/323/head] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8115
  - [feature/agent-pricing-admin-backend] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8114
  - [dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8113
  - [dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8112
  - [refs/merge-requests/322/head] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8111
  - [refs/merge-requests/321/head] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8110
  - [hd_dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8109
  - [dev-gq] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8108
  - [hd_dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8106
  - [hd_dev] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8105
  - [refs/merge-requests/320/head] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8103
  - [feature/agent-pricing-priority-flip] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8102
  - [dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8091
  - [refs/merge-requests/319/head] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8089
  - [feature/agent-pricing-fallback-recompute] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8088
  - [refs/merge-requests/318/head] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8087
  - [feature/billing-dual-hdel-pending] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8086
  - [dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8085
  - [refs/merge-requests/317/head] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8084
  - [dev-gq] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8083
  - [refs/merge-requests/317/head] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8079
  - [dev-gq] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8078
  - [refs/merge-requests/316/head] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8076
  - [feature/billing-cleanup-inner-check-and-dual-release] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8075
  - [hd_dev] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8074
  - [dev] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8070
  - [dev] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8065
  - [refs/merge-requests/315/head] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8062
  - [hotfix/subtitle-erase-fixups] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8060
  - [hotfix/subtitle-erase-fixups] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8058
  - [refs/merge-requests/314/head] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8057
  - [feature/billing-prebill-topic-research-and-ecommerce] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8056
  - [hotfix/subtitle-erase-slim-and-material] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8051
  - [dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8038
  - [dev] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8037
  - [dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8036
  - [refs/merge-requests/313/head] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8033
  - [hd_dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8030
  - [feature/video-subtitle-erase-ghostcut] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8027
  - [hd_dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8026
  - [dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8024
  - [refs/merge-requests/312/head] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8023
  - [hd_dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8022
  - [refs/merge-requests/311/head] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8019
  - [feature/billing-dbify-page-estimate] 状态: failed — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8018
  - [dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8011
  - [refs/merge-requests/310/head] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8010
  - [hd_dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8009
  - [dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8002
  - [refs/merge-requests/309/head] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/8001
  - [hd_dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/7998
  - [refs/merge-requests/308/head] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/7982
  - [feature/billing-sentinel-and-structured-error] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/7981
  - [dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/7979
  - [refs/merge-requests/307/head] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/7978
  - [hd_dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/7977
  - [hd_dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/7975
  - [dev] 状态: success — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/7961

---

### enginer/justuscut
- **最后活动**：2026-05-29T07:11:52.482Z
- **默认分支**：master
- **活跃分支**：
  - `v3/dev` (最后提交: 2026-05-29T06:07:20) — Merge branch 'hotfix/ghostcut-prod-credentials-clean' into 'v3/dev'
  - `v3/hd` (最后提交: 2026-05-29T06:07:20) — Merge branch 'hotfix/ghostcut-prod-credentials-clean' into 'v3/dev'
  - `dev-gq` (最后提交: 2026-05-29T01:52:18) — Merge branch 'v3/fix/dev-hank' into 'v3/dev'
  - `v3/fix/dev-hank` (最后提交: 2026-05-29T09:50:01) — fix 测试环境agent服务配置切换
  - `v3/dev-qh` (最后提交: 2026-05-28T17:34:41) — gofmt
  - `v3/master` (最后提交: 2026-05-28T15:47:38) — chore(jwt): 增强 token 集合校验日志，便于排查懒补录触发原因
  - `feature/agent-billing-overdraft-v2` (最后提交: 2026-05-28T14:28:25) — feat(billing): ProcessThirdPartyLog 加单任务熔断(-200 阈值)
  - `feature/agent-billing-overdraft-cutoff` (最后提交: 2026-05-28T14:09:54) — Revert "feat(billing): ProcessThirdPartyLog 加单任务熔断(-200 阈值)"
  - `feat/video-agent` (最后提交: 2026-05-27T15:22:23) — fix: reorder video model config import statements and align candidateDTO struct 
- **24h 提交**：
  - `4edea91b` [v3/dev] Merge branch 'hotfix/ghostcut-prod-credentials-clean' into 'v3/dev' — 赵华鹏 (2026-05-29T06:07:20)
  - `3a577fc3` [v3/dev] fix(subtitle-erase): prod.yaml 直写 GhostCut 测试 AK 跟既有惯例对齐 — zhaohua (2026-05-29T14:02:28)
  - `49529404` [v3/dev] Merge branch 'v3/fix/dev-hank' into 'v3/dev' — hank hank (2026-05-29T01:52:18)
  - `e0a67d61` [v3/dev] fix 测试环境agent服务配置切换 — hank (2026-05-29T09:50:01)
  - `023e84fa` [v3/dev] Merge branch 'hotfix/ghostcut-dev-credentials' into 'v3/dev' — 赵华鹏 (2026-05-29T01:18:51)
  - `91bdacf9` [v3/dev] refactor(subtitle-erase): 删 GhostCut 死配置字段 presign_ttl_hours / default_model — zhaohua (2026-05-29T09:09:50)
  - `ea7ce718` [v3/dev] Merge branch 'hotfix/ghostcut-dev-credentials' into 'v3/dev' — 赵华鹏 (2026-05-28T14:12:23)
  - `d20c183b` [v3/dev] fix(subtitle-erase): dev.yaml 直写 GhostCut 测试 AK 跟既有惯例对齐 — zhaohua (2026-05-28T22:10:37)
  - `0fbb8f25` [v3/dev] Merge branch 'feature/video-subtitle-erase-ghostcut' into 'v3/dev' — 赵华鹏 (2026-05-28T13:41:23)
  - `52d3ce7e` [v3/dev] feat(subtitle-erase): GhostCut 配置 + InfraDeps 桥接 + vendor 刷新(Phase 4 justuscut 侧) — zhaohua (2026-05-28T21:06:19)
  - `76fafbd7` [v3/dev] Merge branch 'v3/fix/dev-hank' into v3/dev — hank (2026-05-28T19:30:54)
  - `3c19096e` [v3/dev] fix 生产环境配置文件 — hank (2026-05-28T19:30:32)
  - `c8952053` [v3/dev] Merge branch 'v3/dev-qh' into 'v3/dev' — guoqiang ton (2026-05-28T10:33:36)
  - `4edea91b` [v3/hd] Merge branch 'hotfix/ghostcut-prod-credentials-clean' into 'v3/dev' — 赵华鹏 (2026-05-29T06:07:20)
  - `3a577fc3` [v3/hd] fix(subtitle-erase): prod.yaml 直写 GhostCut 测试 AK 跟既有惯例对齐 — zhaohua (2026-05-29T14:02:28)
  - `49529404` [v3/hd] Merge branch 'v3/fix/dev-hank' into 'v3/dev' — hank hank (2026-05-29T01:52:18)
  - `e0a67d61` [v3/hd] fix 测试环境agent服务配置切换 — hank (2026-05-29T09:50:01)
  - `023e84fa` [v3/hd] Merge branch 'hotfix/ghostcut-dev-credentials' into 'v3/dev' — 赵华鹏 (2026-05-29T01:18:51)
  - `91bdacf9` [v3/hd] refactor(subtitle-erase): 删 GhostCut 死配置字段 presign_ttl_hours / default_model — zhaohua (2026-05-29T09:09:50)
  - `ea7ce718` [v3/hd] Merge branch 'hotfix/ghostcut-dev-credentials' into 'v3/dev' — 赵华鹏 (2026-05-28T14:12:23)
  - ...及其他 27 条提交
- **24h MR**：
  - !155 **fix(subtitle-erase): prod.yaml 直写 GhostCut 测试 AK 跟既有惯例对齐** (状态: merged, 作者: 赵华鹏) — https://gitlab.e-idear.com/enginer/justuscut/-/merge_requests/155
  - !154 **fix 测试环境agent服务配置切换** (状态: merged, 作者: hank hank) — https://gitlab.e-idear.com/enginer/justuscut/-/merge_requests/154
  - !153 **refactor(subtitle-erase): 删 GhostCut 死配置字段 presign_ttl_hours / default_model** (状态: merged, 作者: 赵华鹏) — https://gitlab.e-idear.com/enginer/justuscut/-/merge_requests/153
  - !152 **fix(subtitle-erase): dev.yaml 直写 GhostCut 测试 AK 跟既有惯例对齐** (状态: merged, 作者: 赵华鹏) — https://gitlab.e-idear.com/enginer/justuscut/-/merge_requests/152
  - !151 **feat(subtitle-erase): GhostCut 配置 + InfraDeps 桥接 + vendor 刷新(Phase 4 justuscut 侧)** (状态: merged, 作者: 赵华鹏) — https://gitlab.e-idear.com/enginer/justuscut/-/merge_requests/151
  - !150 **feat(order): 添加退款子流程及相关接口** (状态: merged, 作者: h q) — https://gitlab.e-idear.com/enginer/justuscut/-/merge_requests/150
- **24h Pipeline**：
  - [v3/hd] 状态: success — https://gitlab.e-idear.com/enginer/justuscut/-/pipelines/8172
  - [v3/dev] 状态: success — https://gitlab.e-idear.com/enginer/justuscut/-/pipelines/8165
  - [refs/merge-requests/155/head] 状态: success — https://gitlab.e-idear.com/enginer/justuscut/-/pipelines/8164
  - [hotfix/ghostcut-prod-credentials-clean] 状态: success — https://gitlab.e-idear.com/enginer/justuscut/-/pipelines/8161
  - [hotfix/ghostcut-prod-credentials] 状态: success — https://gitlab.e-idear.com/enginer/justuscut/-/pipelines/8153
  - [v3/hd] 状态: success — https://gitlab.e-idear.com/enginer/justuscut/-/pipelines/8107
  - [dev-gq] 状态: success — https://gitlab.e-idear.com/enginer/justuscut/-/pipelines/8077
  - [v3/dev] 状态: success — https://gitlab.e-idear.com/enginer/justuscut/-/pipelines/8073
  - [refs/merge-requests/154/head] 状态: success — https://gitlab.e-idear.com/enginer/justuscut/-/pipelines/8072
  - [v3/fix/dev-hank] 状态: success — https://gitlab.e-idear.com/enginer/justuscut/-/pipelines/8071
  - [v3/dev] 状态: success — https://gitlab.e-idear.com/enginer/justuscut/-/pipelines/8064
  - [refs/merge-requests/153/head] 状态: success — https://gitlab.e-idear.com/enginer/justuscut/-/pipelines/8063
  - [hotfix/ghostcut-dev-credentials] 状态: success — https://gitlab.e-idear.com/enginer/justuscut/-/pipelines/8061
  - [v3/dev] 状态: success — https://gitlab.e-idear.com/enginer/justuscut/-/pipelines/8044
  - [refs/merge-requests/152/head] 状态: success — https://gitlab.e-idear.com/enginer/justuscut/-/pipelines/8043
  - [hotfix/ghostcut-dev-credentials] 状态: success — https://gitlab.e-idear.com/enginer/justuscut/-/pipelines/8042
  - [v3/dev] 状态: success — https://gitlab.e-idear.com/enginer/justuscut/-/pipelines/8035
  - [refs/merge-requests/151/head] 状态: success — https://gitlab.e-idear.com/enginer/justuscut/-/pipelines/8034
  - [feature/video-subtitle-erase-ghostcut] 状态: success — https://gitlab.e-idear.com/enginer/justuscut/-/pipelines/8028
  - [v3/dev] 状态: success — https://gitlab.e-idear.com/enginer/justuscut/-/pipelines/7985
  - [v3/fix/dev-hank] 状态: success — https://gitlab.e-idear.com/enginer/justuscut/-/pipelines/7984
  - [v3/dev] 状态: success — https://gitlab.e-idear.com/enginer/justuscut/-/pipelines/7973

---

### root/whale-flow
- **最后活动**：2026-05-29T09:50:34.860Z
- **默认分支**：main
- **活跃分支**：
  - `main` (最后提交: 2026-05-29T17:50:27) — fix(engine): 354 僵尸 run 看门狗 · worker 两步间停迭代的 running run 回收解 active-run guard
- **24h 提交**：
  - `6cfa7088` [main] fix(engine): 354 僵尸 run 看门狗 · worker 两步间停迭代的 running run 回收解 active-run guard — zhaowenlong (2026-05-29T17:50:27)
  - `d994a48d` [main] fix(engine): P0 回归(349)· codex 去掉端点不支持的 prompt_cache_retention/safety_identifier — zhaowenlong (2026-05-29T14:52:52)
  - `4ba167e3` [main] fix(engine): 347 eval→原生交互(根因 framework 自己) + 346① upsert 回喂 kind↔步映射 — zhaowenlong (2026-05-29T14:33:59)
  - `c737ede8` [main] fix(engine): 超时不该掐死 agent 干活(2/2)· AI 媒体工具豁免外层 60s 插件调用超时 — zhaowenlong (2026-05-29T14:26:50)
  - `ff4f4615` [main] feat(engine): framework 加两条通用交互本能(343-345 抖音/小红书测试交叉验证所得) — zhaowenlong (2026-05-29T14:26:50)
  - `9ee05bdb` [main] feat(engine-studio): 运行/暂停下沉到 per-agent(对齐引擎 340)· 删 ws 级启停面板/试跑/浏览器旁路 ticker — zhaowenlong (2026-05-29T14:26:02)
  - `8adf3bf7` [main] perf(engine): codex 调用对齐真实 codex 的 prompt 缓存(实测命中 83% input) — zhaowenlong (2026-05-29T13:51:44)
  - `8e596adc` [main] fix(engine): 超时不该掐死 agent 干活 · codex+ffmpeg 总时长超时→空闲(heartbeat)超时 — zhaowenlong (2026-05-29T13:00:46)
  - `22fc0ba5` [main] feat(engine): 339 运行/暂停下沉到 agent 级(per-agent runState)· daemon 扫所有 running agent — zhaowenlong (2026-05-29T11:31:17)
  - `43fb1e1a` [main] fix(engine): 修 studio 336 记忆污染「总是忘」+ 收 305② critical 副作用 · 原始流水隔离出语义召回/core — zhaowenlong (2026-05-28T21:22:22)
  - `5068042e` [main] chore(engine): 审计收紧·ai.generateVideo 描述去「短视频」→通用动画/片头措辞(0业务词) — zhaowenlong (2026-05-28T21:15:50)
  - `439e5740` [main] feat(engine): AI 能力(5/N)·327 接入·agent 缺能力优先用引擎自带 ai.*/video.*(非上网找) — zhaowenlong (2026-05-28T21:12:01)
  - `e2fee078` [main] feat(engine): AI 能力(4/N)·连贯视频生成(声明式 spec + Node 渲染器)· ai.generateVideo(live 验证) — zhaowenlong (2026-05-28T21:10:43)
  - `8c3c911c` [main] feat(engine): AI 能力(3/N)·视频工具(Node spawn ffmpeg)+ 修路径穿越(安全审查 HIGH) — zhaowenlong (2026-05-28T20:46:31)
  - `0a6e5bd1` [main] feat(engine): AI 能力(2/N)·图生成走自带 codex image_generation + ai.generateImage(live 验证) — zhaowenlong (2026-05-28T20:38:51)
  - `fda65f16` [main] feat(engine): AI 能力(1/N)·图理解走自带 codex 多模态 input_image + ai.analyzeImage 工具 — zhaowenlong (2026-05-28T20:29:26)
  - `d132814d` [main] fix(engine): 修 studio 332 · cadence 步对象 nextDueAt 由引擎按节奏拥有(高频 every= 不再被 agent 顶掉) — zhaowenlong (2026-05-28T19:16:45)
  - `2e8e8b22` [main] feat(engine): 提示词审查·补 distill 抽「失败教训」(补全 305② LLM 侧)· 其余不动 — zhaowenlong (2026-05-28T18:25:04)
  - `3b10f57d` [main] feat(engine): 修 studio 327 · 缺能力→上网借工具/AI做成(扩 312 心法既有阶梯·非新规则) — zhaowenlong (2026-05-28T18:17:34)

---

### zhaowenlong/livephoto-app
- **最后活动**：2026-05-29T09:42:08.191Z
- **默认分支**：main
- **活跃分支**：
  - `dev-duoduo-v3` (最后提交: 2026-05-29T18:03:25) — fix(android): 全局 UI 等比缩小，解决荣耀等窄屏整体布局偏大
- **24h 提交**：
  - `187c7ad2` [dev-duoduo-v3] fix(android): 全局 UI 等比缩小，解决荣耀等窄屏整体布局偏大 — lichengduo (2026-05-29T18:03:25)
  - `d74e6303` [dev-duoduo-v3] fix(android): 登录输入框收窄 + 监控刷新间隔选项等宽 — lichengduo (2026-05-29T17:58:34)
  - `0847a1bc` [dev-duoduo-v3] feat(android): 兼容 OPPO/vivo 动态照片，修复荣耀 Live 分享到小红书 — lichengduo (2026-05-29T17:42:01)
  - `1063cf77` [dev-duoduo-v3] fix(android): 作品卡片状态/图片数/Live数标签同存时自适应不裁切 — lichengduo (2026-05-29T16:46:27)
  - `fba0b7ef` [dev-duoduo-v3] fix(android): 登录页收紧高度，避免表单超出一屏滚动 — lichengduo (2026-05-29T16:46:19)
  - `da982e40` [dev-duoduo-v3] fix(android): 强制下线弹窗改用统一 AppMessageDialog 样式 — lichengduo (2026-05-29T15:32:55)
  - `8928e028` [dev-duoduo-v3] fix(android): 分享到小红书支持多张图片与多张 live — lichengduo (2026-05-29T15:28:30)
  - `1aa83239` [dev-duoduo-v3] feat(android): 列表统一下拉刷新/上拉加载，修复刷新指示器卡顿 — lichengduo (2026-05-29T15:05:56)
  - `64ca82c9` [dev-duoduo-v3] feat(android): Live图历史卡片加载占位改用循环视频，消除首帧黑屏闪烁 — lichengduo (2026-05-29T14:15:35)
  - `d00b0a8c` [dev-duoduo-v3] fix(android): 监控搜索框改用 BasicTextField，统一内边距与占位样式 — lichengduo (2026-05-29T14:15:25)
  - `26d5e95c` [dev-duoduo-v3] feat(android): 抽取统一弹窗 AppMessageDialog，登录去除账号密码空格 — lichengduo (2026-05-29T10:37:31)
  - `57157ee1` [dev-duoduo-v3] refactor(android): 统一各页面左上角返回按钮样式 — lichengduo (2026-05-29T10:37:24)
  - `e14c821c` [dev-duoduo-v3] fix(android): 二级页返回后保留底部 Tab 选中态 — lichengduo (2026-05-29T10:37:12)
  - `8991a3c1` [dev-duoduo-v3] fix(android): 登录页扫码按钮边框圆角对齐为 25dp — lichengduo (2026-05-29T10:05:34)
  - `6120022f` [dev-duoduo-v3] chore: untrack remaining android/.idea files — lichengduo (2026-05-28T19:05:29)
  - `bdd68bd6` [dev-duoduo-v3] chore: ignore android/.idea/ locally — lichengduo (2026-05-28T19:04:47)
  - `8e2dc241` [dev-duoduo-v3] fix(android/xhs): mode=mix 保留完整 Motion Photo 作 image，恢复小米端 Live 识别 — lichengduo (2026-05-28T18:17:53)
  - `37effac7` [dev-duoduo-v3] feat(android): 扫码生成 Live Photo 跨厂商兼容（小米 MIUI / 华为 EMUI） — lichengduo (2026-05-28T18:06:37)

---

### enginer/justus-web
- **最后活动**：2026-05-29T05:04:22.673Z
- **默认分支**：master
- **活跃分支**：
  - `web-admin-v2` (最后提交: 2026-05-29T05:24:32) — Merge branch 'feature/agent-pricing-tab-rename' into 'web-admin-v2'
  - `feature/agent-pricing-tab-rename` (最后提交: 2026-05-29T13:04:20) — refactor(credit): 合并为单 tab「智能体定价」,撤掉 Prompt Agent 定价
  - `feature/agent-pricing-admin-ui` (最后提交: 2026-05-29T11:12:31) — feat(credit): 算力管理新增「业务智能体定价 / Prompt Agent 定价」两个 tab
  - `feat/video-agent` (最后提交: 2026-05-27T15:14:06) — Merge branch 'web-admin-v2' into feat/video-agent
- **24h 提交**：
  - `4d76e530` [web-admin-v2] Merge branch 'feature/agent-pricing-tab-rename' into 'web-admin-v2' — 赵华鹏 (2026-05-29T05:24:32)
  - `818c6542` [web-admin-v2] refactor(credit): 合并为单 tab「智能体定价」,撤掉 Prompt Agent 定价 — zhaohua (2026-05-29T13:04:20)
  - `a4404ca1` [web-admin-v2] Merge branch 'feature/agent-pricing-admin-ui' into 'web-admin-v2' — 赵华鹏 (2026-05-29T04:12:31)
  - `9e357108` [web-admin-v2] feat(credit): 算力管理新增「业务智能体定价 / Prompt Agent 定价」两个 tab — zhaohua (2026-05-29T11:12:31)
  - `818c6542` [feature/agent-pricing-tab-rename] refactor(credit): 合并为单 tab「智能体定价」,撤掉 Prompt Agent 定价 — zhaohua (2026-05-29T13:04:20)
  - `a4404ca1` [feature/agent-pricing-tab-rename] Merge branch 'feature/agent-pricing-admin-ui' into 'web-admin-v2' — 赵华鹏 (2026-05-29T04:12:31)
  - `9e357108` [feature/agent-pricing-tab-rename] feat(credit): 算力管理新增「业务智能体定价 / Prompt Agent 定价」两个 tab — zhaohua (2026-05-29T11:12:31)
  - `9e357108` [feature/agent-pricing-admin-ui] feat(credit): 算力管理新增「业务智能体定价 / Prompt Agent 定价」两个 tab — zhaohua (2026-05-29T11:12:31)
- **24h MR**：
  - !5 **refactor(credit): 合并为单 tab「智能体定价」,撤掉 Prompt Agent 定价** (状态: merged, 作者: 赵华鹏) — https://gitlab.e-idear.com/enginer/justus-web/-/merge_requests/5
  - !4 **feat(credit): 算力管理新增业务智能体定价 / Prompt Agent 定价 tab** (状态: merged, 作者: 赵华鹏) — https://gitlab.e-idear.com/enginer/justus-web/-/merge_requests/4

---

### Kakarrot/xhs_helper
- **最后活动**：2026-05-29T07:30:44.107Z
- **默认分支**：main
- **活跃分支**：
  - `dev-zzz` (最后提交: 2026-05-29T15:28:43) — fix(v3): 修复 AI 搜索/SPA 跳转下「采集本页笔记」拿错数据
- **24h 提交**：
  - `a8d892dc` [dev-zzz] fix(v3): 修复 AI 搜索/SPA 跳转下「采集本页笔记」拿错数据 — zhangzz (2026-05-29T15:28:43)
  - `8f6e6221` [dev-zzz] fix(v3): header 按钮按优先级单挂载 + 监听 display 切换 — zhangzz (2026-05-28T18:13:49)

---
