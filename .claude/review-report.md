# ModelE2.1.2_Lazenca｜HOWTO 翻译质量审查报告（第1-2批次）

- 时间：2026-02-05 22:48
- 审查类型：批次翻译质量审查
- 审查范围：`doc/HOWTO/` 目录 4 个翻译文档
- 参考依据：`.claude/request.md`、`.claude/rules/translation-standards.md (v1.3)`、`.claude/terminology-dictionary.md (v1.5)`、`.claude/translation-format-standard.md (v1.0)`

## 1. 综合评估

- 综合评分：**96/100**
- 建议：**通过**（满足≥95；P0 文档 `newio.md` 满足≥96）
- 关键结论：翻译整体准确、结构保真；发现的 2 个阻断项（P0）已在本次审查中完成修复：
  - `doc/HOWTO/newio.md`：目录（TOC）锚点链接原本在 Markdown 渲染中会失效，已补齐显式锚点。
  - `doc/HOWTO/time_management.md`：原文拼写错误处理未按规范“更正+可追溯标注”，已更正并标注。

## 2. 分维度评分（按权重）

| 维度 | 权重 | 评分 | 主要问题（摘要） |
|---|---:|---:|---|
| 术语一致性 | 30% | 28/30 | Git/NEW_IO/SCM 相关新术语大量未入词典（需补录），但译文内部基本一致 |
| 翻译准确性 | 30% | 29/30 | 个别句子仍有轻微欧化/直译痕迹，但不影响技术含义 |
| 格式规范性 | 20% | 19/20 | `newio.md` 目录锚点已修复；少量标题/段落对照风格在不同规范文件间存在口径差异（建议统一） |
| 完整性 | 10% | 10/10 | 4 个文档均存在，章节结构与源文档匹配，代码/命令/路径保留良好 |
| 特殊处理 | 10% | 10/10 | `time_management` 原文拼写错误已按“更正+标注”策略处理 |

> 说明：术语一致性扣分主要来自“词典缺口”而非译文乱用；建议尽快补录以锁定后续批次一致性。

## 3. 文档级详细审查

### 3.1 `doc/HOWTO/SCM.md`（目标≥95）

- 评分：**96/100**
- 优点：
  - 源文档结构与条目完整保留（输入文件列表、运行时参数、模板 deck 等）。
  - 专有名词/文件名/变量名保留准确（如 `SCM_NML`、`SCM_lon`、`SCM_lat` 等）。
- 主要问题（非阻断）：
  - 个别术语建议固化：`profile` 当前译为“廓线”，建议在词典补录并在全项目保持一致。

### 3.2 `doc/HOWTO/git_howto.md`（目标≥95）

- 评分：**95/100**
- 优点：
  - 技术语义传达准确，命令/代码块保留完整（`git clone/checkout/branch` 等）。
  - 关键概念对译稳定（central repository → 中央仓库，local commits → 本地提交等）。
- 主要问题（非阻断）：
  - Git 术语目前未在 `.claude/terminology-dictionary.md` 中标准化（clone/commit/push/pull/checkout 等），建议补录以避免后续文档漂移。

### 3.3 `doc/HOWTO/time_management.md`（目标≥95）

- 评分：**96/100**
- 关键修复（本次审查已完成）：
  - 原文拼写错误更正并标注可追溯信息：
    - `doc/HOWTO/time_management.md:76-77`：`repsonsibilities` → `responsibilities`，中文行追加“（原文拼写：repsonsibilities）”。
    - `doc/HOWTO/time_management.md:99-100`：`AbsractCalendar` → `AbstractCalendar`，中文标题标注“（原文拼写：AbsractCalendar）”。
    - `doc/HOWTO/time_management.md:135-136`：`currenTime` → `currentTime`，中文行标注“（原文拼写：currenTime）”。
  - 小节标题补齐中英对照（如 `Rational/BaseTime/...`），提升一致性（参见 `doc/HOWTO/time_management.md:81+`）。
- 仍可优化（非阻断）：
  - 个别长句可进一步中文化以提高可读性，但当前不影响理解。

### 3.4 `doc/HOWTO/newio.md`（P0，目标≥96）

- 评分：**97/100**
- 关键修复（本次审查已完成）：
  - 目录（TOC）锚点补齐：源 HTML 依赖 `<a name="...">`，Markdown 若无显式锚点将导致 `(#rundeck/#model_state/...)` 失效。
  - 已在各章节标题前补充 `<a id="..."></a>`，覆盖全文所有被引用的锚点（示例：`doc/HOWTO/newio.md:35,91,112,153,...,739`）。
  - 同步修正章节标题用词以匹配目录与源文档：`doc/HOWTO/newio.md:155` 将 “save ... to the restart file” 改为 “save ... in the restart file”。
- 仍可优化（非阻断）：
  - NEW_IO 相关术语密集，建议优先补录词典（见第 4 节），否则后续批次易出现“同物异译”。

## 4. 术语补录建议（v1.6/v1.7）

### 4.1 Git 术语（建议优先补录）

| English | 建议译法 | 备注 |
|---|---|---|
| clone | 克隆 | `git clone` 语境 |
| commit | 提交 | 名词/动词均常用 |
| push | 推送 | |
| pull | 拉取 | 与“拉取请求”区分可在注释说明 |
| checkout | 检出 | |
| branch | 分支 | |
| repository | 仓库 | |
| remote | 远程 | remote branch/remote repo |
| merge | 合并 | |
| conflict | 冲突 | |
| tracking branch | 跟踪分支 | |

### 4.2 SCM 术语

| English | 建议译法 | 备注 |
|---|---|---|
| single-column model (SCM) | 单列模型（SCM） | |
| forcing (term) | 强迫（项） | 建议统一“强迫/强迫项”口径 |
| nudging | 松弛（nudge）/松弛同化 | 可在首次出现处括注英文 |
| profile | 廓线/剖面 | 当前译文用“廓线”，建议在词典锁定 |
| run deck / rundeck | 运行配置（rundeck） | 建议统一译法与保留英文策略 |

### 4.3 时间管理术语

| English | 建议译法 | 备注 |
|---|---|---|
| encapsulation | 封装 | |
| epoch | 纪元 | |
| pseudo-Julian calendar | 伪儒略历 | |
| exoplanet | 系外行星 | |
| (clock) tick | 时钟 tick/滴答步 | 可保留 tick 并释义 |

### 4.4 NEW_IO / I/O 系统术语

| English | 建议译法 | 备注 |
|---|---|---|
| restart file | 重启文件 | 词典 v1.5 已收录，建议在 HOWTO 里保持一致 |
| cubed-sphere | 立方体球面 | |
| remap | 重映射 | |
| acc-file (accumulation file) | acc 文件/累积文件 | 建议保留 acc 并释义 |
| scaled diagnostics | 缩放诊断输出 | |
| diagnostics table | 诊断表 | |
| parallel-netcdf (PNETCDF) | 并行 NetCDF（PNETCDF） | 建议大小写统一策略 |

## 5. 修改记录（本次审查落地的具体修改）

> 注：以下为“已在工作区内完成”的最小必要修复，目的为满足规范与可用性；不包含风格性重写。

### 5.1 `doc/HOWTO/newio.md`

- `doc/HOWTO/newio.md:35` 等：为 TOC 中引用的锚点补充显式 `<a id="..."></a>`（覆盖 `rundeck/model_state/diffreport/defvar/pdE/.../local_info`）。
  - 原因：TOC 使用 `(#id)`，Markdown 默认锚点生成规则与源 HTML 的 `<a name="id">` 不一致，导致链接不可用。
- `doc/HOWTO/newio.md:155`：章节标题 “save ... to the restart file” → “save ... in the restart file”。
  - 原因：与源 HTML/TOC 文案保持一致。

### 5.2 `doc/HOWTO/time_management.md`

- `doc/HOWTO/time_management.md:76`：`repsonsibilities` → `responsibilities`；`doc/HOWTO/time_management.md:77` 追加“（原文拼写：repsonsibilities）”。
- `doc/HOWTO/time_management.md:99`：`AbsractCalendar` → `AbstractCalendar`；`doc/HOWTO/time_management.md:100` 标注“（原文拼写：AbsractCalendar）”。
- `doc/HOWTO/time_management.md:135`：`currenTime` → `currentTime`；`doc/HOWTO/time_management.md:136` 标注“（原文拼写：currenTime）”。
- `doc/HOWTO/time_management.md`：补齐 `###` 级标题的中英对照（如 `Rational/BaseTime/...`）。

## 6. 结论与后续建议

- 结论：本批次 4 个 HOWTO 文档达到质量门槛，建议通过并进入下一批次。
- 建议后续（按优先级）：
  1. 将第 4 节列出的 Git/SCM/NEW_IO 术语补录到 `.claude/terminology-dictionary.md`（v1.6/v1.7）。
  2. 统一“格式规范”的口径：`.claude/rules/translation-standards.md` 与 `.claude/translation-format-standard.md` 对标题/空行要求存在差异，建议明确 HOWTO 采用哪一套，以减少后续审查争议。

---

[CONVERSATION_ID]: 019c2e26-9b68-71c0-a9a7-26702e928f25
