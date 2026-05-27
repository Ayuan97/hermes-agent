# 公司 GitLab 日报 —— 2026-05-27

**生成时间**: 2026-05-27 10:08:30 UTC
**GitLab**: https://gitlab.e-idear.com

---

## 一、一句话结论

今日共 7 个活跃项目，16 人参与开发，提交 131 次，MR 14 个，Issue 0 个。最大风险：35 条 Pipeline 失败。

---

## 二、项目看板（Top 活跃项目）

### 1. justus-content-core

- **路径**: `enginer/justus-content-core`
- **活跃分支** (7): hd_dev, dev, fix/dev-hank, dev-qh, feat/video-agent +2
- **统计**: 40 commits | 8 MR | 0 Issues | 59 Pipelines
- **今日内容**:
  - note_collection): excerpt 支持 profile b…
  - note_collection): 手动添加采集的视频笔记补 raw.vid…
  - Merge branch 'hd_dev' into 'dev'
  - note_collection): 摘选 move 后源采集项标记移除 + …
  - Merge branch 'feat/video-agent' into '…
  - [MR] refactor(video_generator): 多参考图全 refer…
  - [MR] fix(note_collection): 摘选 move 后源采集项标记移…
  - [MR] refactor(image_billing): 图片生成统一通用桶 + m…
- **管理判断**: ⚠ Pipeline 失败 18 次; MR 较多，需关注 Code Review 进度

### 2. lnct-web

- **路径**: `zhaowenlong/lnct-web`
- **活跃分支** (10): dev, dev-hd, dev-duouo, dev-wj-workflow, feat/seeding-note-workflow +5
- **统计**: 40 commits | 1 MR | 0 Issues | 66 Pipelines
- **今日内容**:
  - dashboard): 暂时隐藏图片来源下拉中的"引用采集"入口
  - Merge branch 'dev' of gitlab.e-idear.c…
  - Merge branch 'dev-duouo' into dev
  - dashboard): 切换模式时热门模型滚动回最左
  - dashboard): 修复热门模型滚动箭头在模型异步加载后始终不显示
  - [MR] feat(video-agent): 新增视频智能体菜单与 9 个子功能占位页
- **管理判断**: ⚠ Pipeline 失败 14 次; 🔄 Pipeline 运行中 3 次

### 3. JustusCut

- **路径**: `enginer/justuscut`
- **活跃分支** (6): v3/dev, v3/hd, v3/fix/dev-hank, feat/video-agent, v3/dev-qh +1
- **统计**: 10 commits | 4 MR | 0 Issues | 17 Pipelines
- **今日内容**:
  - Merge branch 'feat/video-agent' into '…
  - Merge branch 'v3/fix/dev-hank' into 'v…
  - billing): calculateCostWithSource 支持按 …
  - reorder video model config import stat…
  - Merge branch 'v3/dev' into feat/video-…
  - [MR] refactor(billing): calculateCostWithSo…
  - [MR] Feat/video agent
  - [MR] feat(homepage-models): 对话模型新增「是否支持多模态」字段
- **管理判断**: ⚠ Pipeline 失败 3 次; MR 较多，需关注 Code Review 进度

### 4. whale-flow

- **路径**: `root/whale-flow`
- **活跃分支** (1): main
- **统计**: 29 commits | 0 MR | 0 Issues | 0 Pipelines
- **今日内容**:
  - engine): 批 246 修 studio 265 · daemon 多…
  - engine): 批 245 修 studio 263 回归 · 冷启动 a…
  - engine): 批 244 修 studio 261 · opencli …
  - engine): 批 243 反 loop 推进纪律强化 · 最小可用交付物…
  - engine): 批 242 修 studio 257 · 强推进纪律(别囤…
- **管理判断**: 正常推进

### 5. justUs-web

- **路径**: `enginer/justus-web`
- **活跃分支** (2): web-admin-v2, feat/video-agent
- **统计**: 8 commits | 1 MR | 0 Issues | 0 Pipelines
- **今日内容**:
  - Merge remote-tracking branch 'origin/w…
  - tenant-create-modal): 移除未使用的租户类型选择按钮
  - Merge branch 'feat/video-agent' into '…
  - Merge branch 'web-admin-v2' into feat/…
  - homepage-models): 保存按钮按分块独立判 dirty,只点亮…
  - [MR] Feat/video agent
- **管理判断**: 正常推进

### 6. xhs_helper

- **路径**: `Kakarrot/xhs_helper`
- **活跃分支** (1): dev-zzz
- **统计**: 3 commits | 0 MR | 0 Issues | 0 Pipelines
- **今日内容**:
  - v3): 统一视频链接提取，修复博主页含详情视频笔记 video 为空
  - v3): 导出子评论数取 subCommentCount，修复显示 unde…
  - v3): 导出笔记/博主时在每条主评论后显示子评论数
- **管理判断**: 正常推进

### 7. ln-agents

- **路径**: `enginer/ln-agents`
- **活跃分支** (2): v2/dev, v2/dev-hank
- **统计**: 0 commits | 0 MR | 0 Issues | 0 Pipelines
- **今日内容**: 无代码提交，可能以 Issue 讨论或 Pipeline 运行为主。
- **管理判断**: 正常推进

### 8. livephoto-app

- **路径**: `zhaowenlong/livephoto-app`
- **活跃分支** (1): dev-duoduo-v3
- **统计**: 1 commits | 0 MR | 0 Issues | 0 Pipelines
- **今日内容**:
  - update App Store submission flow
- **管理判断**: 正常推进

### 9. duoyan-ai

- **路径**: `customers/duoyan-ai`
- **活跃分支** (1): master
- **统计**: 0 commits | 0 MR | 0 Issues | 0 Pipelines
- **今日内容**: 无代码提交，可能以 Issue 讨论或 Pipeline 运行为主。
- **管理判断**: 正常推进

### 10. engine-Image-generation

- **路径**: `enginer/engine-image-generation`
- **活跃分支** (1): main
- **统计**: 0 commits | 0 MR | 0 Issues | 0 Pipelines
- **今日内容**: 无代码提交，可能以 Issue 讨论或 Pipeline 运行为主。
- **管理判断**: 正常推进

---

## 三、人员看板（Top 活跃人员）

### 1. zhaowenlong

- **项目**: whale-flow
- **分支**: main
- **动作**: 29 commits | 0 MR | 0 Issues
- **今日内容**:
  - commit: fix(engine): 批 246 修 studio 265 · daemon 多 tool-ca
  - commit: fix(engine): 批 245 修 studio 263 回归 · 冷启动 agent 别预先
  - commit: fix(engine): 批 244 修 studio 261 · opencli 调用契约跨 ru
  - commit: feat(engine): 批 243 反 loop 推进纪律强化 · 最小可用交付物 + 跳过-继
- **管理判断**: 高强度提交，注意代码质量

### 2. hd

- **项目**: lnct-web, justus-content-core
- **分支**: hd_dev, dev-hd, dev
- **动作**: 22 commits | 0 MR | 0 Issues
- **今日内容**:
  - commit: fix(note_collection): excerpt 支持 profile block，非媒体
  - commit: fix(note_collection): 手动添加采集的视频笔记补 raw.videoUrl/me
  - commit: fix(note_collection): 摘选 move 后源采集项标记移除 + 删除级联（新增 
  - commit: feat(material_center_v2): 普通文件夹采集类型筛选下推 collect_fi
- **管理判断**: 高强度提交，注意代码质量

### 3. lichengduo

- **项目**: lnct-web, livephoto-app
- **分支**: dev-duoduo-v3, dev
- **动作**: 14 commits | 0 MR | 0 Issues
- **今日内容**:
  - commit: chore: update App Store submission flow
  - commit: chore(dashboard): 暂时隐藏图片来源下拉中的"引用采集"入口
  - commit: Merge branch 'dev' of gitlab.e-idear.com:zhaowenlo
  - commit: Merge branch 'dev-duouo' into dev
- **管理判断**: 高强度提交，注意代码质量

### 4. hank hank

- **项目**: JustusCut, justus-content-core
- **分支**: hd_dev, v3/dev, dev
- **动作**: 4 commits | 4 MR | 0 Issues
- **今日内容**:
  - commit: Merge branch 'v3/fix/dev-hank' into 'v3/dev'
  - commit: Merge branch 'v3/fix/dev-hank' into 'v3/dev'
  - commit: Merge branch 'fix/dev-hank' into 'dev'
  - commit: Merge branch 'fix/dev-hank' into 'dev'
- **管理判断**: MR 较多，Review 压力大

### 5. yuqiao.xu

- **项目**: lnct-web, justUs-web, JustusCut, justus-content-core
- **分支**: hd_dev, v3/dev, dev, web-admin-v2
- **动作**: 12 commits | 0 MR | 0 Issues
- **今日内容**:
  - commit: Merge branch 'web-admin-v2' into feat/video-agent
  - commit: feat: 视频模型支持为视频复刻智能体指定模型
  - commit: fix: reorder video model config import statements 
  - commit: Merge branch 'v3/dev' into feat/video-agent
- **管理判断**: 高强度提交，注意代码质量

### 6. 许裕桥

- **项目**: lnct-web, justUs-web, JustusCut, justus-content-core
- **分支**: hd_dev, v3/dev, web-admin-v2
- **动作**: 3 commits | 4 MR | 0 Issues
- **今日内容**:
  - commit: Merge branch 'feat/video-agent' into 'web-admin-v2
  - commit: Merge branch 'feat/video-agent' into 'v3/dev'
  - commit: Merge branch 'feat/video-agent' into 'dev'
  - MR[merged]: Feat/video agent
- **管理判断**: MR 较多，Review 压力大

### 7. huang huangd

- **项目**: justus-content-core
- **分支**: 
- **动作**: 0 commits | 4 MR | 0 Issues
- **今日内容**:
  - MR[merged]: fix(note_collection): 摘选 move 后源采集项标记移除 + 删除级联（新增 
  - MR[merged]: feat(material_center_v2): 普通文件夹采集类型筛选下推 collect_fi
- **管理判断**: MR 较多，Review 压力大

### 8. zhaohua

- **项目**: lnct-web, JustusCut, justus-content-core
- **分支**: hd_dev, v3/dev, dev, feature/agent-billing-precheck
- **动作**: 8 commits | 0 MR | 0 Issues
- **今日内容**:
  - commit: feat(billing): InsufficientComputeError 结构化 + calc
  - commit: refactor(billing): PageConfigs 用 slug 替代 numeric a
  - commit: feat(billing): agent 调用前置算力校验 + 页面级预估展示
  - commit: feat(billing): page 算力预估改为数据驱动 + Redis 缓存
- **管理判断**: 正常推进

### 9. hank

- **项目**: lnct-web, justUs-web, JustusCut, justus-content-core
- **分支**: hd_dev, v3/dev, dev, web-admin-v2
- **动作**: 8 commits | 0 MR | 0 Issues
- **今日内容**:
  - commit: fix(homepage-models): 保存按钮按分块独立判 dirty,只点亮真正改过的那一块
  - commit: feat(homepage-models): 改为手动保存,Agent 区 + 三类模型面板各加保存
  - commit: feat(homepage-models): 对话模型编辑弹窗新增"支持多模态"开关
  - commit: refactor(billing): calculateCostWithSource 支持按 mod
- **管理判断**: 正常推进

### 10. qh

- **项目**: justUs-web, JustusCut, justus-content-core
- **分支**: v3/dev-qh, dev-qh, web-admin-v2
- **动作**: 7 commits | 0 MR | 0 Issues
- **今日内容**:
  - commit: Merge remote-tracking branch 'origin/web-admin-v2'
  - commit: refactor(tenant-create-modal): 移除未使用的租户类型选择按钮
  - commit: Merge branch 'v3/dev' into v3/dev-qh
  - commit: Merge branch 'dev' into dev-qh
- **管理判断**: 正常推进

### 11. wj

- **项目**: lnct-web
- **分支**: dev-wj-workflow
- **动作**: 7 commits | 0 MR | 0 Issues
- **今日内容**:
  - commit: Merge branch 'dev' into dev-wj-workflow
  - commit: refactor(topic-workflow): TopicDataColumn 数据处理 pro
  - commit: feat(topic-workflow): 选题工作流接入「选择我的素材」导入下拉词/笔记评论
  - commit: Merge branch 'dev' into dev-wj-workflow
- **管理判断**: 正常推进

### 12. zhangzz

- **项目**: lnct-web, xhs_helper
- **分支**: dev-zzz2, dev-zzz
- **动作**: 6 commits | 0 MR | 0 Issues
- **今日内容**:
  - commit: fix(v3): 统一视频链接提取，修复博主页含详情视频笔记 video 为空
  - commit: fix(v3): 导出子评论数取 subCommentCount，修复显示 undefined
  - commit: feat(v3): 导出笔记/博主时在每条主评论后显示子评论数
  - commit: refactor(materials): 拆分我的采集工具栏 props 为配置对象
- **管理判断**: 正常推进

---

## 四、风险与阻塞

1. ❌ **JustusCut**: Pipeline 失败 (分支 `refs/merge-requests/142/head`) — https://gitlab.e-idear.com/enginer/justuscut/-/pipelines/7755
2. ❌ **JustusCut**: Pipeline 失败 (分支 `feat/video-agent`) — https://gitlab.e-idear.com/enginer/justuscut/-/pipelines/7754
3. ❌ **JustusCut**: Pipeline 失败 (分支 `feat/video-agent`) — https://gitlab.e-idear.com/enginer/justuscut/-/pipelines/7682
4. ❌ **justus-content-core**: Pipeline 失败 (分支 `refs/merge-requests/291/head`) — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/7760
5. ❌ **justus-content-core**: Pipeline 失败 (分支 `refs/merge-requests/291/head`) — https://gitlab.e-idear.com/enginer/justus-content-core/-/pipelines/7750

---

## 五、明日跟进建议

1. 🔄 **lnct-web**: 3 条 Pipeline 运行中，需关注结果

---

## 六、附录：活跃项目判断依据

以下项目在最近 72 小时内有活动（last_activity_at >= 2026-05-24T10:08:30Z）：

- **engine-Image-generation** (`enginer/engine-image-generation`) — 最后活动: 2026-05-26T07:54:51.278Z
- **duoyan-ai** (`customers/duoyan-ai`) — 最后活动: 2026-05-26T02:29:57.905Z
- **ln-agents** (`enginer/ln-agents`) — 最后活动: 2026-05-25T05:50:57.363Z
- **lnct-web** (`zhaowenlong/lnct-web`) — 最后活动: 2026-05-27T09:41:09.378Z
- **justUs-web** (`enginer/justus-web`) — 最后活动: 2026-05-27T09:34:01.952Z
- **xhs_helper** (`Kakarrot/xhs_helper`) — 最后活动: 2026-05-27T09:24:26.445Z
- **justus-content-core** (`enginer/justus-content-core`) — 最后活动: 2026-05-27T08:56:28.138Z
- **JustusCut** (`enginer/justuscut`) — 最后活动: 2026-05-27T08:55:46.120Z
- **whale-flow** (`root/whale-flow`) — 最后活动: 2026-05-27T08:12:24.102Z
- **livephoto-app** (`zhaowenlong/livephoto-app`) — 最后活动: 2026-05-27T07:50:11.736Z