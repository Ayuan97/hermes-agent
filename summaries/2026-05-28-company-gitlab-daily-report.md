# 公司 GitLab 项目日报 — 2026-05-28

> 生成时间：2026-05-28 18:09
> 数据来源：GitLab API
> 总项目数：102，72h 活跃：9

---

## 一句话结论

今日 7/9 个活跃项目，14 人参与，共 428 个提交，19 个 MR。核心推进：justuscut/justus-content-core（视频Agent、账单透支/预检）、lnct-web（工作流节点编辑、CI部署迁移）、whale-flow（工作流引擎迭代）。

---

## 项目看板

| 项目 | 活跃分支 | 提交 | MR | Pipeline | 今日内容 |
|------|---------|------|----|----|---------|
| enginer/justus-content-core | dev, hd_dev, fix/dev-hank, dev-gq +4 | 169 | 12 | 57 | Merge branch 'hd_dev' into 'dev' (×35)；fix(note_collection): 博主含详情重复响应聚合为 user_profile + duplicate_notes，与不含详情同格式 (×18)；Merge branch 'feature/agent-billing-precheck' into 'dev' (×10)；feat(note_collection): split_save_mode 触发条件放宽 + display_name 通用展示名 4 接口透传 (×10) 有MR待审 CI高频运行 |
| zhaowenlong/lnct-web | dev-wj-workflow, feat/seeding-note-workflow, dev, dev-hd +10 | 155 | 0 | 65 | Merge branch 'dev-wj-workflow' into dev (×13)；refactor(billing): "消耗约 X 算力"改成提交按钮 hover Tooltip (×8)；Merge branch 'dev' into dev-wj-workflow (×8)；feat(materials): 选择素材弹窗支持「我的采集」虚拟文件夹 (×8) CI高频运行 |
| enginer/justuscut | v3/dev-qh, v3/dev, dev-gq, v3/master +5 | 68 | 7 | 33 | feat(billing): ProcessThirdPartyLog 加单任务熔断(-200 阈值) (×13)；Merge remote-tracking branch 'refs/remotes/origin/v3/dev' into dev-gq (×9)；fix(jwt): Redis 切换后合法 JWT 走懒补录而非踢下线 (×8)；Revert "feat(billing): ProcessThirdPartyLog 加单任务熔断(-200 阈值)" (×7) 有MR待审 CI高频运行 |
| root/whale-flow | main | 26 | 0 | 0 | revert(engine): 回退 323(账号阻断本能)· 用户:运行时situation对话解决即可,不该焊进引擎；feat(engine): 修 studio 323 · 账号阻断优雅自救=引擎通用本能(322下一层)· 通用 0业务词；feat(engine): 修 studio 321 · agent 凭结果不凭动作判发布成败(假成功修)· 通用本能；feat(engine): 修 studio 315 全链卡D + 317 执行展示中文意图 · 通用 · 0业务词 |
| enginer/ln-agents | v2/master, v2/master-ci, v2/dev-hank | 6 | 0 | 1 | chore: 同步 v2/dev (4a38214) 的代码到 v2/master-ci (×2)；Merge branch 'v2/master-ci' into v2/dev (×2)；ci: 生产部署触发条件改为 v2/master 分支 push + 手动确认 (×2) |
| zhaowenlong/livephoto-app | dev-duoduo-v3 | 3 | 0 | 0 | fix(android/xhs): 修复 H5 → 小红书 live 分享在荣耀/华为上的多个问题；fix: Android UI 细节对齐 iOS；feat: Android 端重写为 Compose 原生应用，对齐 iOS 全功能 |
| enginer/engine-image-generation | main | 1 | 0 | 0 | feat(video): add minimax protocol adapter for MiniMax-Hailuo-2.3 |

---

## 人员看板

| 姓名 | 涉及项目/分支 | 提交 | MR | Issue | 今日内容 |
|------|-------------|------|----|-------|---------|
| zhaohua | enginer/justus-content-core, enginer/justuscut | 99 | 7 | 0 | Merge branch 'feature/agent-billing-overdraft-v2' into 'v3/d；feat(billing): ProcessThirdPartyLog 加单任务熔断(-200 阈值)；Revert "feat(billing): ProcessThirdPartyLog 加单任务熔断(-200 阈值)" |
| zhangzz | zhaowenlong/lnct-web | 77 | 0 | 0 | Merge branch 'dev-zzz2' into dev；feat(materials): SelectionCart 视觉稿对齐 + 全模块统一空态/异常态 EmptyStat；feat(materials): 内页图 per-image 选择 + 缺 asset_id 自动回退 excerpt |
| guoqiang | enginer/engine-image-generation, enginer/justus-content-core | 71 | 2 | 0 | Merge branch 'dev-gq' into 'v3/dev'；Merge remote-tracking branch 'refs/remotes/origin/v3/dev' in；Merge remote-tracking branch 'refs/remotes/origin/v3/dev' in |
| hd | enginer/justus-content-core, zhaowenlong/lnct-web | 64 | 0 | 0 | feat(note_collection): 聚光笔记池采集入口 + 统一 OSS 转存修复 []string 形态漏抽；feat(note_collection): 聚光笔记池采集入口 + 统一 OSS 转存修复 []string 形态漏抽；feat(note_collection): split_save_mode 触发条件放宽 + display_name |
| wj | zhaowenlong/lnct-web | 35 | 0 | 0 | feat(materials): 选择素材弹窗卡片视觉对齐素材中心；Merge branch 'dev-wj-workflow' into dev；refactor(topic-workflow): 抽取 shared 共享模块，整理目录结构 |
| hank | enginer/justuscut, enginer/ln-agents | 28 | 1 | 0 | Merge branch 'v3/fix/dev-hank' into 'v3/dev'；fix(jwt): Redis 切换后合法 JWT 走懒补录而非踢下线；Merge branch 'v3/fix/dev-hank' into 'v3/dev' |
| zhaowenlong | root/whale-flow | 26 | 0 | 0 | revert(engine): 回退 323(账号阻断本能)· 用户:运行时situation对话解决即可,不该焊进引擎；feat(engine): 修 studio 323 · 账号阻断优雅自救=引擎通用本能(322下一层)· 通用 0业务；feat(engine): 修 studio 321 · agent 凭结果不凭动作判发布成败(假成功修)· 通用本能 |
| qh | enginer/justus-content-core, enginer/justuscut | 12 | 0 | 0 | gofmt；Merge branch 'v3/dev' into v3/dev-qh；feat(refund): 添加 GetDetail 端点用于退款状态轮询并增强错误信息 |
| huang huangd | enginer/justus-content-core | 0 | 7 | 0 | [MR] feat(note_collection): 聚光笔记池采集入口 + 统一 OSS 转存修复 []s；[MR] feat(note_collection): split_save_mode 触发条件放宽 + di |
| 阿远 | zhaowenlong/lnct-web | 6 | 0 | 0 | ci(deploy): 回退 gzip 压缩；ci(deploy): 镜像传输管道加 gzip -1 压缩,预期减少 30-50% 传输时间；ci(deploy): 部署链路迁移到 prod-tx,删除 staging 环境 |
| yuqiao.xu | enginer/justus-content-core, zhaowenlong/lnct-web | 5 | 0 | 0 | feat: 新增提示词反推功能；feat: 新增提示词反推功能；feat: 新增提示词反推功能 |
| lichengduo | zhaowenlong/livephoto-app | 3 | 0 | 0 | fix(android/xhs): 修复 H5 → 小红书 live 分享在荣耀/华为上的多个问题；fix: Android UI 细节对齐 iOS；feat: Android 端重写为 Compose 原生应用，对齐 iOS 全功能 |
| suyl | zhaowenlong/lnct-web | 2 | 0 | 0 | feat(borrow-image-post): 对接帖子改造工坊接口并整合到全局任务中心；feat(xhs-product-detail): 新增电商详情页智能体（小红书 PDP 生成） |
| h q | enginer/justus-content-core, enginer/justuscut | 0 | 2 | 0 | [MR] feat(order): 添加退款子流程及相关接口；[MR] feat(smart_creation): 实现选题工作流功能 |

---

## 风险 / 阻塞

1. **enginer/justuscut**：1/33 条 Pipeline 失败/取消。需检查 CI 配置或代码回归。
2. **enginer/justus-content-core**：11/57 条 Pipeline 失败/取消。需检查 CI 配置或代码回归。
3. **zhaowenlong/lnct-web**：49/65 条 Pipeline 失败/取消。需检查 CI 配置或代码回归。
4. **zhaowenlong/lnct-web**：14 个活跃分支持续提交但无 MR，代码可能未及时合并，存在冲突风险。

---

## 明日跟进建议

1. 跟进 **enginer/justus-content-core**：今日提交密集，确认关键分支合并状态和测试覆盖率
2. 跟进 **zhaowenlong/lnct-web**：今日提交密集，确认关键分支合并状态和测试覆盖率
3. 跟进 **enginer/justuscut**：今日提交密集，确认关键分支合并状态和测试覆盖率
4. 关注 **enginer/justuscut** CI 稳定性：今日 33 条 Pipeline，检查失败原因
5. 关注 **enginer/justus-content-core** CI 稳定性：今日 57 条 Pipeline，检查失败原因

---


## 附录：项目提交明细

### enginer/justus-content-core
- 活跃分支数：8
- 24h 提交数：169
  - **dev** (35 commits):
    - `2e115fcb` zhaohua: Merge branch 'hd_dev' into 'dev'
    - `dbb37ada` hd: feat(note_collection): 聚光笔记池采集入口 + 统一 OSS 转存修复 []string 形态漏抽
    - `c00d12d0` hd: feat(note_collection): 聚光笔记池采集入口 + 统一 OSS 转存修复 []string 形态漏抽
    - `b340eccb` guoqiang: Merge branch 'dev-gq' into 'dev'
    - `97210bb0` guoqiang: style(post_remake_workshop): 修正 constants 与 step_pre_analysis 的 gofmt 偏差
    - `e62571d9` guoqiang: Merge remote-tracking branch 'refs/remotes/origin/dev' into dev-gq
    - `4996dab4` guoqiang: fix(post_remake_workshop): 修正生图非2xx错误分类与失败attempt响应留痕
    - `53a5f573` zhaohua: Merge branch 'feature/agent-billing-precheck' into 'dev'
    - ... 还有 27 个提交
  - **fix/dev-hank** (32 commits):
    - `b340eccb` guoqiang: Merge branch 'dev-gq' into 'dev'
    - `97210bb0` guoqiang: style(post_remake_workshop): 修正 constants 与 step_pre_analysis 的 gofmt 偏差
    - `e62571d9` guoqiang: Merge remote-tracking branch 'refs/remotes/origin/dev' into dev-gq
    - `4996dab4` guoqiang: fix(post_remake_workshop): 修正生图非2xx错误分类与失败attempt响应留痕
    - `53a5f573` zhaohua: Merge branch 'feature/agent-billing-precheck' into 'dev'
    - `a371a04c` zhaohua: fix(billing): dream_avatar retry 算力前置校验按 unit×count 计算
    - `898ef289` zhaohua: Merge branch 'hd_dev' into 'dev'
    - `0dd8e194` hd: feat(note_collection): split_save_mode 触发条件放宽 + display_name 通用展示名 4 接口透传
    - ... 还有 24 个提交
  - **dev-gq** (31 commits):
    - `97210bb0` guoqiang: style(post_remake_workshop): 修正 constants 与 step_pre_analysis 的 gofmt 偏差
    - `e62571d9` guoqiang: Merge remote-tracking branch 'refs/remotes/origin/dev' into dev-gq
    - `4996dab4` guoqiang: fix(post_remake_workshop): 修正生图非2xx错误分类与失败attempt响应留痕
    - `53a5f573` zhaohua: Merge branch 'feature/agent-billing-precheck' into 'dev'
    - `a371a04c` zhaohua: fix(billing): dream_avatar retry 算力前置校验按 unit×count 计算
    - `898ef289` zhaohua: Merge branch 'hd_dev' into 'dev'
    - `0dd8e194` hd: feat(note_collection): split_save_mode 触发条件放宽 + display_name 通用展示名 4 接口透传
    - `7f73532a` hd: feat(note_collection): split_save_mode 触发条件放宽 + display_name 通用展示名 4 接口透传
    - ... 还有 23 个提交
  - **feat/video-agent** (24 commits):
    - `6312c772` yuqiao.xu: feat: 新增提示词反推功能
    - `53a5f573` zhaohua: Merge branch 'feature/agent-billing-precheck' into 'dev'
    - `a371a04c` zhaohua: fix(billing): dream_avatar retry 算力前置校验按 unit×count 计算
    - `898ef289` zhaohua: Merge branch 'hd_dev' into 'dev'
    - `0dd8e194` hd: feat(note_collection): split_save_mode 触发条件放宽 + display_name 通用展示名 4 接口透传
    - `7f73532a` hd: feat(note_collection): split_save_mode 触发条件放宽 + display_name 通用展示名 4 接口透传
    - `862885c6` zhaohua: test(billing): 同步 dream_avatar service Create 单测期望
    - `9c9026ae` zhaohua: Merge branch 'feature/agent-billing-concurrent-pending' into 'dev'
    - ... 还有 16 个提交
  - **hd_dev** (21 commits):
    - `dbb37ada` hd: feat(note_collection): 聚光笔记池采集入口 + 统一 OSS 转存修复 []string 形态漏抽
    - `c00d12d0` hd: feat(note_collection): 聚光笔记池采集入口 + 统一 OSS 转存修复 []string 形态漏抽
    - `0dd8e194` hd: feat(note_collection): split_save_mode 触发条件放宽 + display_name 通用展示名 4 接口透传
    - `7f73532a` hd: feat(note_collection): split_save_mode 触发条件放宽 + display_name 通用展示名 4 接口透传
    - `9c9026ae` zhaohua: Merge branch 'feature/agent-billing-concurrent-pending' into 'dev'
    - `866f77dc` zhaohua: refactor(billing): final plan 修订(单一 SoT + bizTaskID 统一 + 单任务熔断)
    - `715b1db6` guoqiang: Merge branch 'hd_dev' into 'dev'
    - `6331076e` hd: feat(note_collection): /save 支持博主笔记列表「文本+图片」拆分保存(split_save_mode)
    - ... 还有 13 个提交
  - **dev-qh** (17 commits):
    - `e954b467` qh: Merge branch 'dev' into dev-qh
    - `715b1db6` guoqiang: Merge branch 'hd_dev' into 'dev'
    - `6331076e` hd: feat(note_collection): /save 支持博主笔记列表「文本+图片」拆分保存(split_save_mode)
    - `b8951f65` guoqiang: Merge branch 'hd_dev' into 'dev'
    - `a64f211c` hd: fix(note_collection): 博主含详情重复响应聚合为 user_profile + duplicate_notes，与不含详情同格式
    - `6a1be62a` qh: Merge branch 'dev' into dev-qh
    - `8a980a84` zhaohua: Merge branch 'hd_dev' into 'dev'
    - `8964b606` hd: Merge branch 'dev' into hd_dev
    - ... 还有 9 个提交
  - **feature/agent-billing-precheck** (5 commits):
    - `a371a04c` zhaohua: fix(billing): dream_avatar retry 算力前置校验按 unit×count 计算
    - `862885c6` zhaohua: test(billing): 同步 dream_avatar service Create 单测期望
    - `866f77dc` zhaohua: refactor(billing): final plan 修订(单一 SoT + bizTaskID 统一 + 单任务熔断)
    - `be5208e7` zhaohua: fix(billing): 并发穿透修复(Redis Hash 按 bizTaskID 分槽)
    - `78206faf` zhaohua: docs(billing): image-clone ModuleName 留空处补 TODO 注释
  - **feature/agent-billing-concurrent-pending** (4 commits):
    - `862885c6` zhaohua: test(billing): 同步 dream_avatar service Create 单测期望
    - `866f77dc` zhaohua: refactor(billing): final plan 修订(单一 SoT + bizTaskID 统一 + 单任务熔断)
    - `be5208e7` zhaohua: fix(billing): 并发穿透修复(Redis Hash 按 bizTaskID 分槽)
    - `78206faf` zhaohua: docs(billing): image-clone ModuleName 留空处补 TODO 注释
- 24h MRs：12
  - !306 [merged] feat(note_collection): 聚光笔记池采集入口 + 统一 OSS 转存修复 []string 形态漏抽 — huang huangd (hd_dev → dev)
  - !305 [merged] feat(smart_creation): 新增产品投流笔记生成子域 product_ad_note;帖子改造工坊 post_remake_workshop — guoqiang ton (dev-gq → dev)
  - !304 [merged] test(billing): 同步 dream_avatar service Create 单测期望 — 赵华鹏 (feature/agent-billing-precheck → dev)
  - !303 [merged] feat(note_collection): split_save_mode 触发条件放宽 + display_name 通用展示名 4 接口透传 — huang huangd (hd_dev → dev)
  - !302 [merged] feat(note_collection): /save 支持博主笔记列表「文本+图片」拆分保存(split_save_mode) — huang huangd (hd_dev → dev)

### zhaowenlong/lnct-web
- 活跃分支数：14
- 24h 提交数：155
  - **dev** (30 commits):
    - `bce4730f` zhangzz: fix(materials): RawComment 接口 subCommentCount 字段去重
    - `ad576ad0` zhangzz: feat(materials): 标题正文 / 文档 占位图标更新
    - `75c0df0a` zhangzz: feat(materials): 类型筛选下线「笔记」「博主资料」入口，「笔记列表+详情」改名「博主笔记详情」
    - `a183198c` zhangzz: Merge branch 'dev-zzz2' into dev
    - `e5e05d2c` zhangzz: feat(materials): SelectionCart 视觉稿对齐 + 全模块统一空态/异常态 EmptyState
    - `ef23ab72` zhangzz: feat(materials): 内页图 per-image 选择 + 缺 asset_id 自动回退 excerpt
    - `1952ebcf` yuqiao.xu: feat: 新增提示词反推功能
    - `16fec01e` zhangzz: feat(materials): 本页笔记极简详情 + 底部按钮设计稿对齐 + 整篇选择走卡片
    - ... 还有 22 个提交
  - **dev-hd** (30 commits):
    - `bce4730f` zhangzz: fix(materials): RawComment 接口 subCommentCount 字段去重
    - `ad576ad0` zhangzz: feat(materials): 标题正文 / 文档 占位图标更新
    - `75c0df0a` zhangzz: feat(materials): 类型筛选下线「笔记」「博主资料」入口，「笔记列表+详情」改名「博主笔记详情」
    - `a183198c` zhangzz: Merge branch 'dev-zzz2' into dev
    - `e5e05d2c` zhangzz: feat(materials): SelectionCart 视觉稿对齐 + 全模块统一空态/异常态 EmptyState
    - `ef23ab72` zhangzz: feat(materials): 内页图 per-image 选择 + 缺 asset_id 自动回退 excerpt
    - `1952ebcf` yuqiao.xu: feat: 新增提示词反推功能
    - `16fec01e` zhangzz: feat(materials): 本页笔记极简详情 + 底部按钮设计稿对齐 + 整篇选择走卡片
    - ... 还有 22 个提交
  - **dev-zzz2** (30 commits):
    - `bce4730f` zhangzz: fix(materials): RawComment 接口 subCommentCount 字段去重
    - `ad576ad0` zhangzz: feat(materials): 标题正文 / 文档 占位图标更新
    - `75c0df0a` zhangzz: feat(materials): 类型筛选下线「笔记」「博主资料」入口，「笔记列表+详情」改名「博主笔记详情」
    - `a183198c` zhangzz: Merge branch 'dev-zzz2' into dev
    - `e5e05d2c` zhangzz: feat(materials): SelectionCart 视觉稿对齐 + 全模块统一空态/异常态 EmptyState
    - `ef23ab72` zhangzz: feat(materials): 内页图 per-image 选择 + 缺 asset_id 自动回退 excerpt
    - `1952ebcf` yuqiao.xu: feat: 新增提示词反推功能
    - `16fec01e` zhangzz: feat(materials): 本页笔记极简详情 + 底部按钮设计稿对齐 + 整篇选择走卡片
    - ... 还有 22 个提交
  - **dev-wj-workflow** (28 commits):
    - `068327c7` wj: feat(materials): 选择素材弹窗卡片视觉对齐素材中心
    - `a183198c` zhangzz: Merge branch 'dev-zzz2' into dev
    - `e5e05d2c` zhangzz: feat(materials): SelectionCart 视觉稿对齐 + 全模块统一空态/异常态 EmptyState
    - `ef23ab72` zhangzz: feat(materials): 内页图 per-image 选择 + 缺 asset_id 自动回退 excerpt
    - `1952ebcf` yuqiao.xu: feat: 新增提示词反推功能
    - `16fec01e` zhangzz: feat(materials): 本页笔记极简详情 + 底部按钮设计稿对齐 + 整篇选择走卡片
    - `35b62516` zhangzz: fix(materials): 统一两边卡片选中边框与复选框样式
    - `9bd576c4` wj: Merge branch 'dev-wj-workflow' into dev
    - ... 还有 20 个提交
  - **ci/test-from-dev** (11 commits):
    - `9ddadb39` 阿远: ci(deploy): 镜像传输管道加 gzip -1 压缩,预期减少 30-50% 传输时间
    - `91796f09` 阿远: ci(deploy): 部署链路迁移到 prod-tx,删除 staging 环境
    - `9bd576c4` wj: Merge branch 'dev-wj-workflow' into dev
    - `baebb280` wj: refactor(topic-workflow): 抽取 shared 共享模块，整理目录结构
    - `4ccf6fb1` hank: fix(auth): 监听 storage 同步多页签登录态
    - `3bafa20e` hd: fix(materials): 移除视频源缺陷限制
    - `1820c550` wj: Merge branch 'dev-wj-workflow' into dev
    - `25357e00` zhaohua: refactor(billing): "消耗约 X 算力"改成提交按钮 hover Tooltip
    - ... 还有 3 个提交
  - **dev-qh** (8 commits):
    - `d0c90739` qh: fix(refund-progress): 修复进度提示文本溢出布局
    - `3f936c54` qh: feat(refund): 添加退款详情获取和轮询机制
    - `e98f8cca` qh: Merge branch 'dev' into dev-qh
    - `1820c550` wj: Merge branch 'dev-wj-workflow' into dev
    - `25357e00` zhaohua: refactor(billing): "消耗约 X 算力"改成提交按钮 hover Tooltip
    - `3b23e9a8` wj: Merge branch 'dev' into dev-wj-workflow
    - `d6266a17` wj: feat(materials): 选择素材弹窗支持「我的采集」虚拟文件夹
    - `2784d070` hd: Merge branch 'dev' into dev-hd
  - **dev-hank** (7 commits):
    - `4ccf6fb1` hank: fix(auth): 监听 storage 同步多页签登录态
    - `3bafa20e` hd: fix(materials): 移除视频源缺陷限制
    - `1820c550` wj: Merge branch 'dev-wj-workflow' into dev
    - `25357e00` zhaohua: refactor(billing): "消耗约 X 算力"改成提交按钮 hover Tooltip
    - `3b23e9a8` wj: Merge branch 'dev' into dev-wj-workflow
    - `d6266a17` wj: feat(materials): 选择素材弹窗支持「我的采集」虚拟文件夹
    - `2784d070` hd: Merge branch 'dev' into dev-hd
  - **feat/xhs-product-detail** (6 commits):
    - `e791afba` suyl: feat(xhs-product-detail): 新增电商详情页智能体（小红书 PDP 生成）
    - `1820c550` wj: Merge branch 'dev-wj-workflow' into dev
    - `25357e00` zhaohua: refactor(billing): "消耗约 X 算力"改成提交按钮 hover Tooltip
    - `3b23e9a8` wj: Merge branch 'dev' into dev-wj-workflow
    - `d6266a17` wj: feat(materials): 选择素材弹窗支持「我的采集」虚拟文件夹
    - `2784d070` hd: Merge branch 'dev' into dev-hd
  - **ci/migrate-deploy-to-prod-tx** (3 commits):
    - `37ceadb8` 阿远: ci(deploy): 回退 gzip 压缩
    - `a96481d2` 阿远: ci(deploy): 镜像传输管道加 gzip -1 压缩,预期减少 30-50% 传输时间
    - `125efcbc` 阿远: ci(deploy): 部署链路迁移到 prod-tx,删除 staging 环境
  - **feat/seeding-note-workflow** (1 commits):
    - `99a8ebfa` suyl: feat(borrow-image-post): 对接帖子改造工坊接口并整合到全局任务中心
  - **dev-ay** (1 commits):
    - `f1b1332d` 阿远: ci(deploy): 生产环境改为 build 在 runner、运行在 prod-tx

### enginer/justuscut
- 活跃分支数：9
- 24h 提交数：68
  - **v3/dev-qh** (18 commits):
    - `34dd20e2` qh: gofmt
    - `fb31ea52` qh: Merge branch 'v3/dev' into v3/dev-qh
    - `17528c7f` guoqiang: Merge branch 'dev-gq' into 'v3/dev'
    - `600ca5c6` guoqiang: Merge remote-tracking branch 'refs/remotes/origin/v3/dev' into dev-gq
    - `cb5c97fa` qh: feat(refund): 添加 GetDetail 端点用于退款状态轮询并增强错误信息
    - `89141f38` zhaohua: Merge branch 'feature/agent-billing-overdraft-v2' into 'v3/dev'
    - `0b487fe0` zhaohua: feat(billing): ProcessThirdPartyLog 加单任务熔断(-200 阈值)
    - `5303e478` zhaohua: Revert "feat(billing): ProcessThirdPartyLog 加单任务熔断(-200 阈值)"
    - ... 还有 10 个提交
  - **v3/dev** (12 commits):
    - `17528c7f` guoqiang: Merge branch 'dev-gq' into 'v3/dev'
    - `600ca5c6` guoqiang: Merge remote-tracking branch 'refs/remotes/origin/v3/dev' into dev-gq
    - `89141f38` zhaohua: Merge branch 'feature/agent-billing-overdraft-v2' into 'v3/dev'
    - `0b487fe0` zhaohua: feat(billing): ProcessThirdPartyLog 加单任务熔断(-200 阈值)
    - `5303e478` zhaohua: Revert "feat(billing): ProcessThirdPartyLog 加单任务熔断(-200 阈值)"
    - `1c520b84` zhaohua: feat(billing): ProcessThirdPartyLog 加单任务熔断(-200 阈值)
    - `2bd92c75` guoqiang: Merge remote-tracking branch 'refs/remotes/origin/v3/dev' into dev-gq
    - `e3ab8d12` hank: Merge branch 'v3/fix/dev-hank' into 'v3/dev'
    - ... 还有 4 个提交
  - **dev-gq** (11 commits):
    - `600ca5c6` guoqiang: Merge remote-tracking branch 'refs/remotes/origin/v3/dev' into dev-gq
    - `89141f38` zhaohua: Merge branch 'feature/agent-billing-overdraft-v2' into 'v3/dev'
    - `0b487fe0` zhaohua: feat(billing): ProcessThirdPartyLog 加单任务熔断(-200 阈值)
    - `5303e478` zhaohua: Revert "feat(billing): ProcessThirdPartyLog 加单任务熔断(-200 阈值)"
    - `1c520b84` zhaohua: feat(billing): ProcessThirdPartyLog 加单任务熔断(-200 阈值)
    - `2bd92c75` guoqiang: Merge remote-tracking branch 'refs/remotes/origin/v3/dev' into dev-gq
    - `e3ab8d12` hank: Merge branch 'v3/fix/dev-hank' into 'v3/dev'
    - `be9ef515` hank: fix(jwt): Redis 切换后合法 JWT 走懒补录而非踢下线
    - ... 还有 3 个提交
  - **v3/fix/dev-hank** (7 commits):
    - `89141f38` zhaohua: Merge branch 'feature/agent-billing-overdraft-v2' into 'v3/dev'
    - `0b487fe0` zhaohua: feat(billing): ProcessThirdPartyLog 加单任务熔断(-200 阈值)
    - `5303e478` zhaohua: Revert "feat(billing): ProcessThirdPartyLog 加单任务熔断(-200 阈值)"
    - `1c520b84` zhaohua: feat(billing): ProcessThirdPartyLog 加单任务熔断(-200 阈值)
    - `e3ab8d12` hank: Merge branch 'v3/fix/dev-hank' into 'v3/dev'
    - `be9ef515` hank: fix(jwt): Redis 切换后合法 JWT 走懒补录而非踢下线
    - `098fe411` zhaohua: feat(billing): 新增 CheckComputeWithCountAndPending 防并发穿透
  - **v3/hd** (7 commits):
    - `89141f38` zhaohua: Merge branch 'feature/agent-billing-overdraft-v2' into 'v3/dev'
    - `0b487fe0` zhaohua: feat(billing): ProcessThirdPartyLog 加单任务熔断(-200 阈值)
    - `5303e478` zhaohua: Revert "feat(billing): ProcessThirdPartyLog 加单任务熔断(-200 阈值)"
    - `1c520b84` zhaohua: feat(billing): ProcessThirdPartyLog 加单任务熔断(-200 阈值)
    - `e3ab8d12` hank: Merge branch 'v3/fix/dev-hank' into 'v3/dev'
    - `be9ef515` hank: fix(jwt): Redis 切换后合法 JWT 走懒补录而非踢下线
    - `098fe411` zhaohua: feat(billing): 新增 CheckComputeWithCountAndPending 防并发穿透
  - **feature/agent-billing-overdraft-v2** (6 commits):
    - `0b487fe0` zhaohua: feat(billing): ProcessThirdPartyLog 加单任务熔断(-200 阈值)
    - `5303e478` zhaohua: Revert "feat(billing): ProcessThirdPartyLog 加单任务熔断(-200 阈值)"
    - `1c520b84` zhaohua: feat(billing): ProcessThirdPartyLog 加单任务熔断(-200 阈值)
    - `e3ab8d12` hank: Merge branch 'v3/fix/dev-hank' into 'v3/dev'
    - `be9ef515` hank: fix(jwt): Redis 切换后合法 JWT 走懒补录而非踢下线
    - `098fe411` zhaohua: feat(billing): 新增 CheckComputeWithCountAndPending 防并发穿透
  - **feature/agent-billing-overdraft-cutoff** (5 commits):
    - `5303e478` zhaohua: Revert "feat(billing): ProcessThirdPartyLog 加单任务熔断(-200 阈值)"
    - `1c520b84` zhaohua: feat(billing): ProcessThirdPartyLog 加单任务熔断(-200 阈值)
    - `e3ab8d12` hank: Merge branch 'v3/fix/dev-hank' into 'v3/dev'
    - `be9ef515` hank: fix(jwt): Redis 切换后合法 JWT 走懒补录而非踢下线
    - `098fe411` zhaohua: feat(billing): 新增 CheckComputeWithCountAndPending 防并发穿透
  - **v3/master** (2 commits):
    - `3e715f7e` hank: chore(jwt): 增强 token 集合校验日志，便于排查懒补录触发原因
    - `3ad3024e` hank: fix(jwt): Redis 切换后合法 JWT 走懒补录而非踢下线
- 24h MRs：7
  - !150 [opened] feat(order): 添加退款子流程及相关接口 — h q (v3/dev-qh → v3/dev)
  - !149 [merged] 帖子改造工坊 post_remake_workshop — guoqiang ton (dev-gq → v3/dev)
  - !148 [merged] feat(billing): ProcessThirdPartyLog 单任务熔断(-200) — 赵华鹏 (feature/agent-billing-overdraft-v2 → v3/dev)
  - !147 [closed] Draft: feat(billing): ProcessThirdPartyLog 单任务熔断(-200) — 赵华鹏 (feature/agent-billing-overdraft-cutoff → v3/dev)
  - !146 [closed] Draft: Feature/agent billing overdraft cutoff — 赵华鹏 (feature/agent-billing-overdraft-cutoff → v3/dev)

### root/whale-flow
- 活跃分支数：1
- 24h 提交数：26
  - **main** (26 commits):
    - `832bc11e` zhaowenlong: revert(engine): 回退 323(账号阻断本能)· 用户:运行时situation对话解决即可,不该焊进引擎
    - `06957f77` zhaowenlong: feat(engine): 修 studio 323 · 账号阻断优雅自救=引擎通用本能(322下一层)· 通用 0业务词
    - `f2797a01` zhaowenlong: feat(engine): 修 studio 321 · agent 凭结果不凭动作判发布成败(假成功修)· 通用本能
    - `16bcdada` zhaowenlong: feat(engine): 修 studio 315 全链卡D + 317 执行展示中文意图 · 通用 · 0业务词
    - `89fb4c31` zhaowenlong: feat(engine): 修 studio 311 · 用户 chat 指令注入自驱 run(说一套做一套修)
    - `da7d894c` zhaowenlong: refactor(engine): agent 执行提示词「少规则多原则」重构 · 特质当脊梁 tactic 降级成例子
    - `f145a8e2` zhaowenlong: feat(engine): 修 studio 309 · 教 agent「find 不穷举·够不着用 eval 挖 DOM」万能兜底本能(纯提示词)
    - `f228fbd8` zhaowenlong: feat(engine): 修 studio 305 agent「没记忆·重复踩坑」4 断点 · 打法召回+失败可见+教训蒸馏+新生避坑
    - ... 还有 18 个提交

### enginer/ln-agents
- 活跃分支数：3
- 24h 提交数：6
  - **v2/master** (3 commits):
    - `b82430a0` hank: chore: 同步 v2/dev (4a38214) 的代码到 v2/master-ci
    - `7120d4cc` hank: Merge branch 'v2/master-ci' into v2/dev
    - `32ad1129` hank: ci: 生产部署触发条件改为 v2/master 分支 push + 手动确认
  - **v2/master-ci** (3 commits):
    - `b82430a0` hank: chore: 同步 v2/dev (4a38214) 的代码到 v2/master-ci
    - `7120d4cc` hank: Merge branch 'v2/master-ci' into v2/dev
    - `32ad1129` hank: ci: 生产部署触发条件改为 v2/master 分支 push + 手动确认

### zhaowenlong/livephoto-app
- 活跃分支数：1
- 24h 提交数：3
  - **dev-duoduo-v3** (3 commits):
    - `b5595806` lichengduo: fix(android/xhs): 修复 H5 → 小红书 live 分享在荣耀/华为上的多个问题
    - `6deaa002` lichengduo: fix: Android UI 细节对齐 iOS
    - `bdf82a55` lichengduo: feat: Android 端重写为 Compose 原生应用，对齐 iOS 全功能

### enginer/engine-image-generation
- 活跃分支数：1
- 24h 提交数：1
  - **main** (1 commits):
    - `d0798f7d` guoqiang: feat(video): add minimax protocol adapter for MiniMax-Hailuo-2.3

## 附录：人员工作明细

### zhaohua（99 commits, 7 MRs, 0 issues）
- **enginer/justus-content-core**:
  - Merge branch 'hd_dev' into 'dev'
  - Merge branch 'feature/agent-billing-precheck' into 'dev'
  - fix(billing): dream_avatar retry 算力前置校验按 unit×count 计算
  - Merge branch 'hd_dev' into 'dev'
  - test(billing): 同步 dream_avatar service Create 单测期望
- **enginer/justuscut**:
  - Merge branch 'feature/agent-billing-overdraft-v2' into 'v3/dev'
  - feat(billing): ProcessThirdPartyLog 加单任务熔断(-200 阈值)
  - Revert "feat(billing): ProcessThirdPartyLog 加单任务熔断(-200 阈值)"
  - feat(billing): ProcessThirdPartyLog 加单任务熔断(-200 阈值)
  - feat(billing): 新增 CheckComputeWithCountAndPending 防并发穿透
- **zhaowenlong/lnct-web**:
  - refactor(billing): "消耗约 X 算力"改成提交按钮 hover Tooltip
  - refactor(billing): "消耗约 X 算力"改成提交按钮 hover Tooltip
  - refactor(billing): "消耗约 X 算力"改成提交按钮 hover Tooltip
  - refactor(billing): "消耗约 X 算力"改成提交按钮 hover Tooltip
  - refactor(billing): "消耗约 X 算力"改成提交按钮 hover Tooltip

### zhangzz（77 commits, 0 MRs, 0 issues）
- **zhaowenlong/lnct-web**:
  - Merge branch 'dev-zzz2' into dev
  - feat(materials): SelectionCart 视觉稿对齐 + 全模块统一空态/异常态 EmptyState
  - feat(materials): 内页图 per-image 选择 + 缺 asset_id 自动回退 excerpt
  - feat(materials): 本页笔记极简详情 + 底部按钮设计稿对齐 + 整篇选择走卡片
  - fix(materials): 统一两边卡片选中边框与复选框样式

### guoqiang（71 commits, 2 MRs, 0 issues）
- **enginer/engine-image-generation**:
  - feat(video): add minimax protocol adapter for MiniMax-Hailuo-2.3
- **enginer/justus-content-core**:
  - Merge branch 'dev-gq' into 'dev'
  - style(post_remake_workshop): 修正 constants 与 step_pre_analysis 的 gofmt 偏差
  - Merge remote-tracking branch 'refs/remotes/origin/dev' into dev-gq
  - fix(post_remake_workshop): 修正生图非2xx错误分类与失败attempt响应留痕
  - fix(post_remake_workshop): 更新删除任务提示信息为“任务处理中,暂不可删除”
- **enginer/justuscut**:
  - Merge branch 'dev-gq' into 'v3/dev'
  - Merge remote-tracking branch 'refs/remotes/origin/v3/dev' into dev-gq
  - Merge remote-tracking branch 'refs/remotes/origin/v3/dev' into dev-gq
  - Merge remote-tracking branch 'refs/remotes/origin/v3/dev' into dev-gq
  - 帖子改造工坊 post_remake_workshop

### hd（64 commits, 0 MRs, 0 issues）
- **enginer/justus-content-core**:
  - feat(note_collection): 聚光笔记池采集入口 + 统一 OSS 转存修复 []string 形态漏抽
  - feat(note_collection): 聚光笔记池采集入口 + 统一 OSS 转存修复 []string 形态漏抽
  - feat(note_collection): split_save_mode 触发条件放宽 + display_name 通用展示名 4 接口透传
  - feat(note_collection): split_save_mode 触发条件放宽 + display_name 通用展示名 4 接口透传
  - feat(note_collection): /save 支持博主笔记列表「文本+图片」拆分保存(split_save_mode)
- **zhaowenlong/lnct-web**:
  - fix(materials): 移除视频源缺陷限制
  - Merge branch 'dev' into dev-hd
  - fix(materials): 移除视频源缺陷限制
  - Merge branch 'dev' into dev-hd
  - fix(materials): 移除视频源缺陷限制

### wj（35 commits, 0 MRs, 0 issues）
- **zhaowenlong/lnct-web**:
  - feat(materials): 选择素材弹窗卡片视觉对齐素材中心
  - Merge branch 'dev-wj-workflow' into dev
  - refactor(topic-workflow): 抽取 shared 共享模块，整理目录结构
  - Merge branch 'dev-wj-workflow' into dev
  - Merge branch 'dev' into dev-wj-workflow

### hank（28 commits, 1 MRs, 0 issues）
- **enginer/justuscut**:
  - Merge branch 'v3/fix/dev-hank' into 'v3/dev'
  - fix(jwt): Redis 切换后合法 JWT 走懒补录而非踢下线
  - Merge branch 'v3/fix/dev-hank' into 'v3/dev'
  - fix(jwt): Redis 切换后合法 JWT 走懒补录而非踢下线
  - Merge branch 'v3/fix/dev-hank' into 'v3/dev'
- **enginer/ln-agents**:
  - chore: 同步 v2/dev (4a38214) 的代码到 v2/master-ci
  - Merge branch 'v2/master-ci' into v2/dev
  - ci: 生产部署触发条件改为 v2/master 分支 push + 手动确认
  - chore: 同步 v2/dev (4a38214) 的代码到 v2/master-ci
  - Merge branch 'v2/master-ci' into v2/dev
- **zhaowenlong/lnct-web**:
  - fix(auth): 监听 storage 同步多页签登录态
  - fix(auth): 监听 storage 同步多页签登录态
  - fix(auth): 监听 storage 同步多页签登录态
  - fix(auth): 监听 storage 同步多页签登录态
  - fix(auth): 监听 storage 同步多页签登录态

### zhaowenlong（26 commits, 0 MRs, 0 issues）
- **root/whale-flow**:
  - revert(engine): 回退 323(账号阻断本能)· 用户:运行时situation对话解决即可,不该焊进引擎
  - feat(engine): 修 studio 323 · 账号阻断优雅自救=引擎通用本能(322下一层)· 通用 0业务词
  - feat(engine): 修 studio 321 · agent 凭结果不凭动作判发布成败(假成功修)· 通用本能
  - feat(engine): 修 studio 315 全链卡D + 317 执行展示中文意图 · 通用 · 0业务词
  - feat(engine): 修 studio 311 · 用户 chat 指令注入自驱 run(说一套做一套修)

### qh（12 commits, 0 MRs, 0 issues）
- **enginer/justus-content-core**:
  - Merge branch 'dev' into dev-qh
  - Merge branch 'dev' into dev-qh
  - Merge branch 'dev' into dev-qh
- **enginer/justuscut**:
  - gofmt
  - Merge branch 'v3/dev' into v3/dev-qh
  - feat(refund): 添加 GetDetail 端点用于退款状态轮询并增强错误信息
  - fix(company): 修复管理员手机号变更时的冗余字段同步
  - Merge branch 'v3/dev' into v3/dev-qh
- **zhaowenlong/lnct-web**:
  - fix(refund-progress): 修复进度提示文本溢出布局
  - feat(refund): 添加退款详情获取和轮询机制
  - Merge branch 'dev' into dev-qh

### huang huangd（0 commits, 7 MRs, 0 issues）
- **enginer/justus-content-core**:
  - [MR] feat(note_collection): 聚光笔记池采集入口 + 统一 OSS 转存修复 []string 形态漏抽
  - [MR] feat(note_collection): split_save_mode 触发条件放宽 + display_name 通用展示名 4 接口透传
  - [MR] feat(note_collection): /save 支持博主笔记列表「文本+图片」拆分保存(split_save_mode)
  - [MR] fix(note_collection): 博主含详情重复响应聚合为 user_profile + duplicate_notes，与不含详情同格式
  - [MR] fix(note_collection): 博主含详情重复响应聚合为 user_profile + duplicate_notes，与不含详情同格式

### 阿远（6 commits, 0 MRs, 0 issues）
- **zhaowenlong/lnct-web**:
  - ci(deploy): 回退 gzip 压缩
  - ci(deploy): 镜像传输管道加 gzip -1 压缩,预期减少 30-50% 传输时间
  - ci(deploy): 部署链路迁移到 prod-tx,删除 staging 环境
  - ci(deploy): 镜像传输管道加 gzip -1 压缩,预期减少 30-50% 传输时间
  - ci(deploy): 部署链路迁移到 prod-tx,删除 staging 环境

### yuqiao.xu（5 commits, 0 MRs, 0 issues）
- **enginer/justus-content-core**:
  - feat: 新增提示词反推功能
- **zhaowenlong/lnct-web**:
  - feat: 新增提示词反推功能
  - feat: 新增提示词反推功能
  - feat: 新增提示词反推功能
  - feat: 新增提示词反推功能

### lichengduo（3 commits, 0 MRs, 0 issues）
- **zhaowenlong/livephoto-app**:
  - fix(android/xhs): 修复 H5 → 小红书 live 分享在荣耀/华为上的多个问题
  - fix: Android UI 细节对齐 iOS
  - feat: Android 端重写为 Compose 原生应用，对齐 iOS 全功能

### suyl（2 commits, 0 MRs, 0 issues）
- **zhaowenlong/lnct-web**:
  - feat(borrow-image-post): 对接帖子改造工坊接口并整合到全局任务中心
  - feat(xhs-product-detail): 新增电商详情页智能体（小红书 PDP 生成）

### h q（0 commits, 2 MRs, 0 issues）
- **enginer/justus-content-core**:
  - [MR] feat(smart_creation): 实现选题工作流功能
- **enginer/justuscut**:
  - [MR] feat(order): 添加退款子流程及相关接口
