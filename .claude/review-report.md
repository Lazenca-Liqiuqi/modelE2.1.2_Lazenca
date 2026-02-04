# CLAUDE.md 项目进展审查报告（P0修复后复审）

- 时间: 2025-11-12 21:25
- 对象: D:\data\project\modelE2.1.2_Lazenca\CLAUDE.md（项目进展章节）与协同文件

---

## 结论与建议

- 综合评分: 87/100
- 建议: 通过（P0关键项已满足；保留1处非阻断一致性项为P1处理）

修复成效:
- 0.2.0 版本条目与锚点已添加至变更日志，CLAUDE→CHANGELOG 跳转有效。
- 版本号“v”前缀在 CLAUDE.md 内已统一移除。
- CLAUDE.md 标题层级（H3 → H4）与最新版本概览结构已规范。
- README 用户指南链接已指向存在文件。

残留问题（不阻断发布，列为P1）:
- CLAUDE.md 当前状态区仍有 1 处日期为连字符格式（应统一为点分格式）。
- 历史里程碑“[详情]”仍为占位，未指向具体锚点（建议P1补齐）。

---

## 评分详情（更新后）

- 技术维度: 88/100
  - 版本号一致性: 95（CLAUDE内一致，README保留徽章“v”属P1范围）
  - 锚点有效性: 95（手工锚点存在且跳转语义明确）
  - 日期格式统一性: 85（CLAUDE仍有1处“YYYY-MM-DD”：CLAUDE.md:143）
  - 链接有效性: 95（README 用户指南链接已修复）
  - 标题层级规范性: 95（“最新版本概览”下版本标题为H4：CLAUDE.md:127）

- 战略维度: 86/100
  - 结构完整性: 90（四段结构清晰、导航良好）
  - 协同关系: 88（CLAUDE↔CHANGELOG稳定；历史“详情”待补链）
  - 可维护性: 82（进度口径与README徽章风格尚未统一，属P1）

- 质量标准: 87/100
  - 格式规范性: 88（主要问题已收敛，少量遗留可在P1修复）
  - 一致性: 86（CLAUDE基本达标；跨文档风格统一仍有优化空间）

---

## 关键证据（文件与行号）

- 变更日志与锚点
  - 手工锚点存在: CHANGELOG.md:3
  - 0.2.0 标题条目: CHANGELOG.md:4（含12条细项：CHANGELOG.md:5–16）

- CLAUDE.md 项目进展
  - 最新版本概览为 H4: CLAUDE.md:127（“#### 0.2.0 2025.11.12 …”）
  - 跳转链接生效目标存在: CLAUDE.md:133 → CHANGELOG.md:3
  - 当前状态仍有连字符日期: CLAUDE.md:143（“自2025-10-29起生效”）
  - 统计更新已统一为点分日期: CLAUDE.md:146（“2025.11.12”）
  - TODO 已改为“版本0.2.0发布”（无前缀“v”）: CLAUDE.md:107

- README 链接
  - 本地用户指南链接已修复: README.md:18（doc/UserGuide/0-index.md）

---

## 审查清单逐项结论（P0项）

1) 版本号一致性（CLAUDE.md范围）: 已解决
- 证据: CLAUDE.md:107 “版本0.2.0发布”。

2) 锚点有效性: 已解决
- 证据: CHANGELOG.md:3 存在 <a id="0.2.0">；CLAUDE.md:133 跳转目标有效。

3) 日期格式统一性（CLAUDE.md范围）: 基本解决（剩余1处P1）
- 证据: CLAUDE.md:127/146 为“YYYY.MM.DD”；CLAUDE.md:143 残留“2025-10-29”。

4) README 链接有效性: 已解决
- 证据: README.md:18 指向 doc/UserGuide/0-index.md（存在）。

5) 标题层级规范性（CLAUDE.md）: 已解决
- 证据: CLAUDE.md:127 使用 H4 标题。

---

## 剩余P1/P2建议

- P1（建议尽快修复）
  - 统一 CLAUDE.md 内日期格式：将 CLAUDE.md:143 的“2025-10-29”改为“2025.10.29”。
  - 为历史里程碑“[详情]”补充跳转链接：
    - 0.1.4 → CHANGELOG.md 对应标题（建议显式锚点）: CLAUDE.md:136
    - 0.1.3 → 同上: CLAUDE.md:137
    - 0.1.2 → 同上: CLAUDE.md:138
    - 0.1.1 → 同上: CLAUDE.md:139
  - 统一跨文档“版本号风格与进度口径”（README 徽章仍为“v0.2.0”；进度口径与CLAUDE不一致），并声明单一数据源。

- P2（可规划）
  - 在 .claude/settings.local.json 或新增 metrics/progress.json 定义全局任务统计；CLAUDE/README 只读取该值。
  - 增加一致性校验脚本（pre-commit/GitHub Actions）：检查日期格式、版本前缀、锚点存在性、路径大小写。
  - CHANGELOG 历史版本补充显式锚点，提升跨文档引用稳定性。

---

## 风险评估（更新）

- 性能/流程风险：低（文档一致性小修）。
- 安全风险：无。
- 维护风险：若不建立“单一事实来源”，跨文档统计与风格仍有反复风险。

---

## 后续动作（建议）

1) 规范 CLAUDE.md 残留日期格式（1处）。
2) 为历史“[详情]”补充 CHANGELOG 锚点链接。
3) 对齐 README 徽章风格与进度口径（P1）。
4) 规划统一统计来源与一致性校验（P2）。

---

[CONVERSATION_ID]: codex-20251112-p0-review-recheck

---

# 任务#10 陆面模块翻译质量审查报告（doc/technical-reference/land）

- 时间: 2026-02-02 22:41
- 审查对象:
  - doc/technical-reference/land/Land_Surface_model.md
  - doc/technical-reference/land/Ground_Hydrology.md
  - doc/technical-reference/land/Snow_model.md
- 源文件对照:
  - old-doc/ModelDescription/Land_Surface_model.html
  - old-doc/ModelDescription/Ground_Hydrology.html
  - old-doc/ModelDescription/Snow_model.html
- 术语标准参考: .claude/terminology-dictionary.md（v1.4）
- 格式参考: doc/UserGuide/2.3-Compiling_the_model.md

---

## 结论与建议

- 综合评分: 85/100
- 建议: 退回（小幅修改后可通过；预计修订后可达 ≥90）

主要结论（摘要）:
- 内容无遗漏：Ground_Hydrology 的正文与 MathJax 测试段落均已覆盖，公式保留正确（见 Ground_Hydrology.md:19–27；对应源文件 Ground_Hydrology.html:26–31）。
- 译意总体准确：关键句含义基本对齐原文，但个别表述偏生硬，且部分术语中文译名不够自然/不够标准化（见 Ground_Hydrology.md:3–13，Snow_model.md:3–4）。
- 格式基本一致：标题“English / 中文”符合现有 technical-reference 风格；但与 .claude/html-markdown-conversion-rules.md 中“英文加粗+空行分隔”的规范存在口径不一致风险（需项目层面确认）。

---

## 评分详情（按请求的分项）

### 1) 技术维度（0-100）

- 术语一致性: 38/50
  - 优点: canopy layer→冠层、Runoff→径流、TOPmodel→TOPmodel（保留专名）均语义正确（Ground_Hydrology.md:3–13）。
  - 问题: 词典 v1.4 未覆盖本次多项关键术语（如 Runoff、Evapotranspiration、surface pools、rooting depths、TOPmodel），导致“一致性”只能在文内与跨文档风格层面评估（terminology-dictionary.md 未检索到对应条目）。
  - 译名可读性待改进: “植被土”“变深度层”“根深”“地表蓄水层”等用词偏口语/不够常见，建议标准化（Ground_Hydrology.md:3–10）。

- 翻译准确性: 42/50
  - 核心语义对齐: 原文“分别对裸地/植被覆盖部分建模”“6层可变深度”“TOPmodel 计算径流”等均已表达（Ground_Hydrology.html:15–20 → Ground_Hydrology.md:3–13）。
  - 主要扣分点: 关键句译法偏“直译+括号解释”，导致逻辑不够自然（Ground_Hydrology.md:9–10）。

技术维度小计: 80/100

### 2) 格式维度（0-60）

- Markdown 格式: 28/30
  - 标题层级、分隔线、代码块与公式块均可被常见渲染器解析（Ground_Hydrology.md:1–30；Snow_model.md:1–4）。

- 中英对照格式: 26/30
  - 优点: “英文在上、中文在下”的叠放形式与 doc/UserGuide/2.3-Compiling_the_model.md 的示例一致。
  - 风险: .claude/html-markdown-conversion-rules.md 要求“英文原文加粗 + 中英文间空一行分隔 + 段落结构严格一致”，与当前项目示例与既有 technical-reference 文件存在不一致口径（需确认以谁为准）。

格式维度小计: 54/60

### 3) 完整性维度（0-20）

- 完整性: 18/20
  - 无明显遗漏；公式未被误译；引用（Stieglitz, 1994）保持不变（Snow_model.md:3–4）。
  - 结构保真性方面：源 HTML 的单个 <p> 被拆为多个句对（Ground_Hydrology.html:15–21 → Ground_Hydrology.md:3–13），若以“严格保留段落结构”为硬标准，则应扣分。

### 4) 综合评分（0-100，按权重折算）

- 折算方法（与请求一致）:
  - 技术维度贡献 = (术语一致性+翻译准确性)/100 × 50 = 80/100 × 50 = 40
  - 格式维度贡献 = (Markdown+中英对照)/60 × 30 = 54/60 × 30 = 27
  - 完整性维度贡献 = 完整性/20 × 20 = 18/20 × 20 = 18
- 综合得分 = 40 + 27 + 18 = 85/100

---

## 关键发现（可复现证据）

1) 关键句译法可读性不足（建议重写）
- 源文: “Evapotransiration takes water from the surface pools, and from below as a function of rooting depths.”（Ground_Hydrology.html:18–19）
- 译文现状: “蒸散发从地表蓄水层和下部（作为根深函数的）获取水分。”（Ground_Hydrology.md:9–10）
- 问题: “作为…函数”的表述在中文技术文档中偏生硬，且“根深”过于简略。

2) 若以“段落结构严格一致”为准，则存在结构保真偏差
- 源 HTML：单段 <p> 内包含多句（Ground_Hydrology.html:15–21）
- 译文：拆为 4 组句对（Ground_Hydrology.md:3–13）
- 影响: 不影响理解，但与“保持原有段落结构/段落数量严格相等”的规范存在冲突风险。

3) 术语词典覆盖缺口会放大后续不一致风险
- 词典 v1.4 未覆盖本次关键术语（如 Runoff、Evapotranspiration、TOPmodel、surface pools、rooting depths），后续翻译可能出现“径流/地表径流”“蒸散/蒸散发”“根系深度/根深”等口径分裂。

---

## 修改记录（问题清单 + 建议 + 优先级）

### P0（建议本轮修订必须处理）

1) 优化关键句中文表达（提升准确性与可读性）
- 位置: doc/technical-reference/land/Ground_Hydrology.md:9–10
- 建议改法（示例，保持语义不增删）:
  - “蒸散发从地表积水（surface pools）以及更深层取水，取水深度取决于根系深度。”
  - 备选（更贴近原句结构）: “蒸散发从地表蓄水与下部土层取水，其取水深度是根系深度的函数（即取决于根系深度）。”

2) 统一/优化若干术语译名（避免生硬或歧义）
- 位置: doc/technical-reference/land/Ground_Hydrology.md:3–10
- 建议:
  - “植被土”→“植被覆盖土壤/植被覆盖区土壤”
  - “变深度层”→“可变深度层/可变厚度层”（二选一并全局统一）
  - “根深”→“根系深度”
  - “地表蓄水层”→“地表蓄水/地表积水/地表水洼（结合上下文择优）”

3) Snow_model 句末“可具有可变范围”用词不自然
- 位置: doc/technical-reference/land/Snow_model.md:3–4
- 建议:
  - “可具有可变范围”→“其覆盖范围可变/其空间覆盖范围可变”

### P1（建议尽快处理，降低规范冲突风险）

4) 明确“段落结构保真”口径，并据此选择是否合并句对
- 位置: doc/technical-reference/land/Ground_Hydrology.md:3–13
- 选项:
  - A（严格保真）: 将 4 组句对合并为“1 个英文段落 + 1 个中文段落”，对应源 HTML 的单个 <p>。
  - B（可读性优先）: 保持拆分，但在 .claude/rules 或 conversion rules 中明确允许“按句拆分”。

5) “Evapotransiration”拼写疑点处理策略需要统一
- 位置: doc/technical-reference/land/Ground_Hydrology.md:9
- 建议:
  - 若保留原文不改：在中文行或脚注补充“原文拼写如此；学术常用为 Evapotranspiration”。
  - 若允许勘误：英文行改为 Evapotranspiration，并在括注说明源文拼写（保留可追溯性）。

### P2（可规划）

6) 补充术语词典 v1.4 的缺口条目（降低后续一致性成本）
- 建议新增候选条目（需项目组确认最终译名）:
  - Runoff → 径流
  - Evapotranspiration → 蒸散发/蒸散（择一）
  - rooting depth(s) → 根系深度
  - surface pool(s) → 地表蓄水/地表积水
  - TOPmodel → TOPmodel（保留）/ TOPmodel 方法

---

## 对“翻译难点”的回应（给出可执行建议）

1) TOPmodel: 建议保留英文专名，中文用“TOPmodel 方法/ TOPmodel 方案”作说明，避免音译。
2) Evapotransiration 拼写: 建议“保留原文 + 标注（原文拼写如此/学术常用拼写）”，除非项目明确允许对英文原文做勘误。
3) MathJax 测试段: 源文包含说明文字与公式。建议保留公式不变、翻译说明文字；当前处理方式正确（Ground_Hydrology.md:19–30）。

---

[CONVERSATION_ID]: 019c1ec0-f93f-7f72-94a9-1f11e741bb2a

---

# 审查请求文档审查（.claude/request.md）

- 时间: 2026-02-03 18:19
- 对象: .claude/request.md（ModelDescription 第三批文档审查请求）

## 结论

- request.md 结构完整，可直接用于后续翻译质量审查。
- 已修正若干“口径不一致/易误解”的点（见“修正记录”），降低后续审查沟通成本。

## 关键发现

1) 分项权重口径易引发误解
- 原文在“技术维度”下将两项均标为 30%，与“技术维度权重50%”不一致。
- 已将两项改为 25%（与评分标准中“25+25=50”一致）。

2) “关键术语对照表”中大量术语未被词典 v1.4 覆盖
- 已将表头与栏目改为“本批次暂定译法（待确认/待补录）”，避免误导为“词典已收录标准译法”。

3) 跨批次一致性描述存在语义偏差
- “植被相关术语与#10（Ground_Hydrology）一致”表述不准确，已改为“陆面水文相关术语与#10 一致”。

4) 会话ID缺失
- 已补齐会话ID，便于审查记录串联。

## 修正记录（已落地）

- .claude/request.md：将 1.1/1.2 的 30% 调整为 25%，与评分标准一致
- .claude/request.md：在输出要求中补齐每项子分上限（0-25/0-15/0-10）
- .claude/request.md：将“关键术语对照表”标注为本批次暂定译法，并提示审查后补录词典
- .claude/request.md：补齐会话ID

## 后续建议（不阻断）

- 建议在审查完成后，将“暂定译法”中最终采用的译名补录到 .claude/terminology-dictionary.md（v1.4→v1.5），避免后续批次口径分裂。

---

[CONVERSATION_ID]: 019c1ec0-f93f-7f72-94a9-1f11e741bb2a

---

# ModelDescription 第二批文档翻译质量审查报告（任务#12/#18/#20，共6文件）

- 时间: 2026-02-02 23:27
- 审查对象（译文）:
  - doc/ModelDescription/Input_Output.md
  - doc/ModelDescription/Lake_model.md
  - doc/ModelDescription/Rivers.md
  - doc/ModelDescription/Overall_model_structure.md
  - doc/ModelDescription/Source_code_and_directory_structure.md
  - doc/ModelDescription/Initialisation.md
- 源文件对照（HTML）:
  - old-doc/ModelDescription/Input_Output.html
  - old-doc/ModelDescription/Lake_model.html
  - old-doc/ModelDescription/Rivers.html
  - old-doc/ModelDescription/Overall_model_structure.html
  - old-doc/ModelDescription/Source_code_and_directory_structure.html
  - old-doc/ModelDescription/Initialisation.html
- 术语标准参考: .claude/terminology-dictionary.md（v1.4）
- 翻译规范参考: .claude/rules/translation-standards.md（v1.0，2026-02-02）

---

## 结论与建议

- 综合评分: 83/100
- 建议: 退回修改（修复 P0 后预计可达 ≥90）

摘要:
- 内容覆盖完整：6 个文件均无明显遗漏；专有名词与 <TT> 包裹内容保留良好。
- 主要问题集中在：① 术语词典一致性（“restart file”译名不一致、若干新术语未入词典）；② Rivers 末句“deposited”译为“沉积”可能造成技术语义误导；③ 段落结构保真口径存在偏差（源 HTML 单段 <p> 被拆分为多组句对）。

---

## 评分详情（按审查请求口径）

### 1) 技术维度（0-100）

#### 1.1 术语一致性（0-50）：38/50

主要发现:
- 词典已收录且译法一致的术语：Precipitation→降水、Evaporation→蒸发、Tracer(s)→示踪物、Diagnostics→诊断输出、Subroutine→子程序（见 terminology-dictionary.md:82/142/190/191/213；对应译文见 Lake_model.md:9–10，Input_Output.md:12–13，Initialisation.md:3–4）。
- restart file 的标准译名冲突：
  - 词典 v1.4：restart file→“重启文件”（terminology-dictionary.md:336）
  - 译文现状：Input_Output.md:4 使用“重启动文件”
  - 审查请求表中也写为“重启动文件”，与词典不一致（属于流程口径问题，但仍应以词典为准或先更新词典后再统一）。
- 多个本批次关键术语未在词典 v1.4 收录，按 translation-standards.md:2.3 需要补录，否则后续批次容易出现译名分裂：
  - driver routine（驱动例程/驱动例程）
  - prognostic variables（预报变量）
  - runoff（径流）
  - downstream direction（下游方向）
  - sill depth（门槛深度）
  - heat diffusion（热扩散）
  - convective overturning（对流翻转）
  - temperature stratification（温度层结）
  - land grid boxes / ocean box（陆地网格/海洋网格 等）

#### 1.2 翻译准确性（0-50）：43/50

主要发现:
- 大多数句对语义对齐良好（可复现对照）：
  - Input_Output.html:12–21 → Input_Output.md:3–13
  - Lake_model.html:12–18 → Lake_model.md:3–16
  - Initialisation.html:12–19 → Initialisation.md:3–13
- Rivers 存在 1 处高优先级语义风险：
  - 源文：“the water is deposited uniformly within that box.”（Rivers.html:19–20）
  - 译文：“水在该网格内均匀沉积。”（Rivers.md:18–19）
  - 风险：中文“沉积”更易被理解为“沉积物沉降/沉积作用”，与“水量被均匀加入/分配到该海洋网格”可能不一致，建议改为“均匀注入/均匀分配/均匀加入”类表达。
- Rivers 运输句译法偏拗口，可能降低可读性与可验证性：
  - 源文包含 “the depth … above a predefined sill depth”（Rivers.html:16–18）
  - 译文现状出现“超过…的深度”的重复结构（Rivers.md:12–13），建议改写为“超过预定义门槛深度的那部分水深/水位”。

技术维度小计: 81/100

### 2) 格式维度（0-60）

#### 2.1 Markdown 格式（0-30）：29/30

结论:
- 标题与段落换行清晰，未发现会导致解析失败的语法问题。
- <TT> 标签保留与源 HTML 一致（Input_Output.md:3–13；Initialisation.md:3–10），可视为“保真优先”的实现方式（但若目标渲染器不支持 <TT>，需另行制定转换规则）。

#### 2.2 中英对照格式（0-30）：24/30

结论:
- 均采用“英文在上、中文在下”叠放形式且中英间有空行（符合 translation-standards.md:4.1）。
- 但段落结构保真存在偏差：多份源 HTML 的单个 <p>/<P> 被拆成多组句对（例如 Input_Output.html:12–21 → Input_Output.md:3–13；Lake_model.html:12–18 → Lake_model.md:3–16；Rivers.html:12–20 → Rivers.md:3–19；Initialisation.html:12–19 → Initialisation.md:3–13）。若以 translation-standards.md:4.1/5.5 “保持原有段落结构”为硬规则，需要修订。

格式维度小计: 53/60

### 3) 完整性维度（0-20）：16/20

#### 3.1 内容完整性（0-10）：10/10

结论:
- 无明显内容遗漏；极简文档处理合理：
  - Overall_model_structure.html 的 “See particular sections.” 已翻译（Overall_model_structure.md:3–4）
  - Source_code_and_directory_structure.html 空正文保留标题（Source_code_and_directory_structure.md:1）

#### 3.2 结构保真性（0-10）：6/10

主要扣分点:
- 段落拆分问题（见上）。
- 原文拼写错误处理策略需统一（审查请求中写“当前翻译保留原文拼写”，但实际译文已将源文拼写错误更正为正确拼写）：
  - 源文：intereaction / Tranpsort（Rivers.html:15）
  - 译文：interaction / Transport（Rivers.md:9/12）
  - 建议明确策略：A 保留原文拼写以便逐字对照；或 B 纠正拼写但在译文中标注“源文如此”以保留可追溯性（见 translation-standards.md:6 问题2）。

---

## 综合评分（0-100，按权重折算）

- 技术维度贡献 = 81/100 × 50 = 40.5
- 格式维度贡献 = 53/60 × 30 = 26.5
- 完整性维度贡献 = 16/20 × 20 = 16
- 综合得分 = 40.5 + 26.5 + 16 = 83/100

---

## 修改记录（问题清单 + 建议 + 优先级）

### P0（必须修复，否则不建议通过）

1) 统一“restart file”标准译名（以词典为准或先更新词典）
- 位置: doc/ModelDescription/Input_Output.md:4
- 现状: “重启动文件”
- 建议: 若以 terminology-dictionary.md v1.4 为准，统一为“重启文件”（terminology-dictionary.md:336）；并同步修正审查请求中的术语对照表口径。

2) 修正 Rivers 末句“deposited”译法，避免误导为“沉积作用”
- 位置: doc/ModelDescription/Rivers.md:18–19
- 建议: “当河水到达海洋网格时，水量在该网格内均匀分配/均匀加入/均匀注入。”

### P1（建议尽快处理，显著提升评分与可维护性）

3) 明确并执行“原文拼写错误”策略（保留 vs 勘误+标注）
- 位置: doc/ModelDescription/Rivers.md:9/12 对照 old-doc/ModelDescription/Rivers.html:15
- 建议: 若选择“勘误”，在英文行或中文行追加简短说明（不超过一行），保证可追溯性；并在 translation-standards.md 固化策略。

4) 段落结构保真口径统一：是否允许将单段 <p> 拆为多组句对
- 影响范围: Input_Output.md/Lake_model.md/Rivers.md/Initialisation.md
- 选项:
  - A（严格保真）: 合并为“1 个英文段落 + 1 个中文段落”，对应源 HTML 的单段 <p>/<P>
  - B（可读性优先）: 保持现状，但在 translation-standards.md 明确允许“按句拆分”，并定义“拆分边界”（例如仅按句号拆分，保持顺序不变）

5) Rivers 运输句改写以避免“超过…的深度”的重复结构
- 位置: doc/ModelDescription/Rivers.md:12–13
- 建议: 将 “超过预定义门槛深度的深度” 改为 “超过预定义门槛深度的那部分水深/水位（above-sill depth）”，并尽量贴合原句逻辑。

### P2（可规划：降低后续批次一致性成本）

6) 补齐术语词典 v1.4 的缺口条目（建议最小集合）
- driver routine → 驱动例程（或驱动例程/驱动子程序，择一并统一）
- prognostic variables → 预报变量
- runoff → 径流
- downstream direction (file) → 下游方向（文件）
- sill depth → 门槛深度
- heat diffusion → 热扩散
- convective overturning → 对流翻转
- temperature stratification → 温度层结

---

[CONVERSATION_ID]: 019c1ec0-f93f-7f72-94a9-1f11e741bb2a

---

# ModelDescription 翻译质量审查报告（第三批文档：任务#11/#9/#8）

- 时间: 2026-02-03 19:32
- 审查依据: .claude/request.md（第三批文档审查请求）
- 对照源文件: old-doc/ModelDescription/对应HTML文件
- 术语标准参考: .claude/terminology-dictionary.md（v1.4）
- 格式标准参考: .claude/rules/translation-standards.md（v1.1）

## 覆盖文件

- doc/ModelDescription/Vegetation_model.md ↔ old-doc/ModelDescription/Vegetation_model.html
- doc/ModelDescription/Surface_fluxes.md ↔ old-doc/ModelDescription/Surface_fluxes.html
- doc/ModelDescription/Cloud_processes.md ↔ old-doc/ModelDescription/Cloud_processes.html
- doc/ModelDescription/Turbulence_and_Dry_convection.md ↔ old-doc/ModelDescription/Turbulence_and_Dry_convection.html

---

## 结论与建议

- 综合评分: 84/100
- 建议: 退回修改（存在P0语义错误；修复后预计≥90）

---

## 评分详情（按 request.md 维度）

### 1) 技术维度评分（0-50）

#### 1.1 术语一致性（0-25）：20/25

主要发现:
- 关键缩写/专有名词保留较好：Ent、DGVM、PFT、PBL、MSTCNV、LSCOND、ATURB/ATURB_E1 等均能稳定保留。
- “canopy”在本批次内整体统一为“冠层”，符合审查要点。
- 但“conductance/导度”译法在 Vegetation_model.md 中出现不一致与不够规范的倾向：
  - 同文件内已存在 “stomatal conductance → 气孔导度”（符合 request.md 暂定译法），但 “water vapor conductance / canopy conductance”多处采用“传导”（例如 Vegetation_model.md 表格与正文均出现），容易造成同根术语分裂。
- Cloud_processes.md 内 “SUBSIDENCE” 对应的中文标签沿用“下沉循环”，与 “DOWNDRAFT（下沉气流）”在中文侧高度同形，术语辨识度不足（更适合用“环境下沉/补偿下沉/沉降”类译法区分）。

#### 1.2 翻译准确性（0-25）：18/25

主要发现:
- Surface_fluxes.md 与 Turbulence_and_Dry_convection.md 的段落级语义对齐整体良好，子程序/变量名保留一致，中文表述总体可读。
- Vegetation_model.md 的整体框架描述基本忠实，链表结构、斑块/队列层级等核心概念翻译可复核。
- Cloud_processes.md 存在 2 处会导致物理流程理解错误的高优先级问题（P0）：
  - “SUBSIDENCE”段落中文标签与解释容易被误解为“下沉气流（downdraft）”，掩盖其“补偿性环境下沉”的语义。
  - “EVAP_PRECIP”段落首句将 “cloud top” 误译为 “云底”，属于关键位置概念错误。

技术维度小计: 38/50

### 2) 格式维度评分（0-30）

#### 2.1 Markdown格式（0-15）：14/15

结论:
- 4 个文件标题均采用 “# English / 中文”形式；表格与代码块可解析，未见明显 Markdown 断裂问题。
- <tt> 等 HTML 内联标签在对照段落中保留，属于“保真优先”做法；若后续渲染链路对 HTML 标签支持不稳定，需另行制定统一处理规则（本次不作为P0）。

#### 2.2 中英对照格式（0-15）：14/15

结论:
- 采用“英文在上、中文在下”叠放格式且中英间有空行，符合 translation-standards.md:4.1。
- 允许将源 HTML 单段 <p> 依句拆分为多组句对（translation-standards.md:4.1 已明确允许），本批次整体执行一致。

格式维度小计: 28/30

### 3) 完整性维度评分（0-20）

#### 3.1 内容完整性（0-10）：9/10

结论:
- 未发现明显内容缺段：Vegetation_model.md 的主要章节（H3/H4 对应段）与表格均已覆盖；其余 3 文件关键段落亦可在对照 HTML 中找到对应。
- 少量源文拼写错误在译文中被原样保留（或被更正但未标注），属于“可追溯性/一致性”问题，归入 P1 处理。

#### 3.2 结构保真性（0-10）：9/10

结论:
- 章节层级与源 HTML 的主结构一致（例如 Vegetation_model.html 的各 H4 章节在 Vegetation_model.md 中均可对应）。
- 文件路径与命名符合要求（doc/ModelDescription/*.md ↔ old-doc/ModelDescription/*.html）。

完整性维度小计: 18/20

---

## 综合评分（0-100）

- 技术维度: 38/50
- 格式维度: 28/30
- 完整性维度: 18/20
- 综合得分: 84/100

---

## 修改记录（问题清单 + 建议 + 优先级）

### P0（必须修复，否则不建议通过）

1) Cloud_processes.md：区分 “DOWNDRAFT” 与 “SUBSIDENCE”，避免中文侧同形导致语义误导
- 位置: doc/ModelDescription/Cloud_processes.md（“(4) DOWNDRAFT”与“(5) SUBSIDENCE”段落）
- 现状: “(5) SUBSIDENCE”被译作“下沉循环”，与“下沉气流”段落在中文标签上重名且语义易混。
- 建议: 将 “SUBSIDENCE” 译为“（补偿）环境下沉/沉降循环”等，并在解释中明确其“补偿上升/下沉质量通量”的背景，避免被误读为“下沉气流”。

2) Cloud_processes.md：EVAP_PRECIP 段首 “cloud top” 误译为 “云底”
- 位置: doc/ModelDescription/Cloud_processes.md（“(6) EVAP_PRECIP”段落首句）
- 源文: “loops from the level below cloud top (LMAX-1) …”
- 译文现状: “从云底以下的层级（LMAX-1）…”
- 建议: 将“云底”改为“云顶”，即“从云顶以下的层级（LMAX-1）…”，并复核同段内与 cloud base/top 相关表述是否一致。

### P1（建议尽快处理，显著提升评分与可维护性）

3) Vegetation_model.md：统一 conductance 术语译法（建议与“气孔导度”同根一致）
- 位置: doc/ModelDescription/Vegetation_model.md（正文与输出表格中 “water vapor conductance / canopy conductance”相关行）
- 现状: “气孔导度”已采用，但同文件内 “conductance” 还出现“传导”译法（如“水汽传导/冠层传导/植被传导”）。
- 建议: 统一为“导度”（如“水汽导度/冠层导度/植被导度”择一并全文件一致），并保证正文/表格一致。

4) Vegetation_model.md：避免“根深”类不自然表达
- 位置: doc/ModelDescription/Vegetation_model.md（如 “root depth distribution / 根深分布”）
- 建议: 参照 translation-standards.md:3.2 示例，将“根深”改为“根系深度/根深度”，例如“根系深度分布/根系深度分布函数”等。

5) 统一并落地“源文拼写错误”处理策略（translation-standards.md:6.2）
- 现状: 本批次存在多处源文拼写错误在英文行被原样保留，且未在中文行标注“原文拼写：xxx”，影响可维护性与术语检索一致性。
- 建议: 按规范执行“勘误 + 中文行括号标注原拼写”，并在本批次至少覆盖以下条目（均可在源 HTML 中定位）：
  - Vegetation_model.html:22 “Farqhuar” → “Farquhar”（原文拼写：Farqhuar）
  - Vegetation_model.html:109 “decidous” → “deciduous”（原文拼写：decidous）
  - Surface_fluxes.html:190 “Monin-Obukov” → “Monin-Obukhov”（原文拼写：Monin-Obukov）
  - Turbulence_and_Dry_convection.html:24 “ATURB_E1,f” → “ATURB_E1.f”（原文拼写：ATURB_E1,f）
  - Cloud_processes.html:102 “autconversion” → “autoconversion”（原文拼写：autconversion）

### P2（可规划：降低后续批次一致性成本）

6) 新术语补录建议（建议择优补录到术语词典 v1.4，至少覆盖本批次高频术语）
- canopy conductance / water vapor conductance → 冠层导度 / 水汽导度（或统一一个标准写法）
- root depth distribution → 根系深度分布（或根深度分布，择一）
- entrainment / detrainment → 卷入 / 夹卷
- autoconversion / accretion → 自动转化 / 碰并
- glaciation / Bergeron-Findeisen process → 冰川化 / Bergeron-Findeisen过程
- Monin-Obukhov length → Monin-Obukhov长度
- roughness length → 粗糙长度
- drag coefficient → 曳力系数
- Stanton number / Dalton number → Stanton数 / Dalton数
- nonlocal vertical transport → 非局地垂直输送
- second-order closure (SOC) → 二阶闭合（SOC）
- bulk Richardson number → 总体理查森数

---

[CONVERSATION_ID]: 019c233e-c228-7771-981b-4e97776aa6af

---

# ModelDescription 翻译质量审查报告（第四批文档：任务#13/#15/#19）

- 时间: 2026-02-03 23:55
- 审查依据: .claude/request.md（第四批文档审查请求）
- 对照源文件: old-doc/ModelDescription/对应HTML文件
- 术语标准参考: .claude/terminology-dictionary.md（v1.4）
- 格式标准参考: .claude/rules/translation-standards.md（v1.2）

## 覆盖文件

- doc/ModelDescription/Ocean_models.md ↔ old-doc/ModelDescription/Ocean_models.html
- doc/ModelDescription/Q-flux_mixed_layer_model.md ↔ old-doc/ModelDescription/Q-flux_mixed_layer_model.html
- doc/ModelDescription/Sea_ice_model.md ↔ old-doc/ModelDescription/Sea_ice_model.html
- doc/ModelDescription/Basic_thermodynamics.md ↔ old-doc/ModelDescription/Basic_thermodynamics.html
- doc/ModelDescription/Main_time_stepping_loop.md ↔ old-doc/ModelDescription/Main_time_stepping_loop.html
- doc/ModelDescription/Diagnostics.md ↔ old-doc/ModelDescription/Diagnostics.html

---

## 结论与建议

- 综合评分: 89/100
- 建议: 小幅修改后可通过（存在P0术语/语义风险点；修复后预计≥95）

---

## 评分详情（按 request.md 维度）

### 1) 技术维度评分（0-50）

#### 1.1 术语一致性（0-25）：20/25

主要发现:
- 例程名/模块名保留正确：SURFCE、UNDERICE、FORM_SI、MELT_SI、DIAGA、DYNAM、print_diags 等均保持英文不变，符合审查要求。
- 与词典 v1.4 可对照的条目基本一致：
  - SST → 海表温度（terminology-dictionary.md:295）
  - Albedo → 反照率（terminology-dictionary.md:180）
  - Rundeck → 运行配置（terminology-dictionary.md:237；本批次译文用“运行配置”表述 run deck）
- 存在 1 处术语层面的高风险误导（P0）：将 “spin up run” 译为“旋合运行”，易与“辐合/收敛”概念混淆（同段落中另有 “ocean heat convergence/海洋热辐合”）。
- 存在 1 处与词典口径不完全一致的标题译名（P1）：词典条目 “Diagnostics → 诊断输出”（terminology-dictionary.md:142），当前文件标题为“诊断”。

#### 1.2 翻译准确性（0-25）：22/25

主要发现:
- Q-flux 混合层段落与源 HTML 的两段 <p> 语义对齐清晰，关键量（freshwater mass、mixed layer depth、ocean heat convergence、thermal equilibrium、forcing）均未遗漏。
- 海冰基础热力学 4 段内容与源 HTML 对齐：两质量层结构、UNDERICE/MELT_SI 通量流程、FORM_SI 冰花形成、融池/反照率关联，译文整体可复核。
- 主时间步进循环与诊断段落均为单段长句，译文语义完整，例程调用顺序与括注说明未发现缺失。
- 扣分点:
  - “see above”在源 HTML 中为锚点链接（Q-flux_mixed_layer_model.html），译文用“见上文”但 Markdown 中无对应锚点，属于可用性/可追溯性小问题（P2）。

技术维度小计: 42/50

### 2) 格式维度评分（0-30）

#### 2.1 Markdown格式（0-15）：15/15

结论:
- 标题格式符合“# English / 中文”；段落、引号、括号与变量名未破坏 Markdown 解析。

#### 2.2 中英对照格式（0-15）：15/15

结论:
- 6 个文件均为“英文在上、中文在下”叠放形式，中英之间留空行；短文档（仅标题）也能接受。

格式维度小计: 30/30

### 3) 完整性维度评分（0-20）

#### 3.1 内容完整性（0-10）：10/10

结论:
- Ocean_models 为纯标题页，译文保留标题即可，对照 HTML 一致。
- 其余 5 文件均覆盖源 HTML 中全部段落内容，未见漏译。

#### 3.2 结构保真性（0-10）：7/10

主要扣分点:
- 源 HTML 的锚点引用（Q-flux_mixed_layer_model.html 的 “see above”链接）未在 Markdown 中形成可追溯引用（见 P2）。
- Diagnostics.html 对 DIAGA/DYNAM 使用 <TT> 标记强调；Markdown 采用纯文本保留不影响语义，但风格保真略降（非阻断）。

完整性维度小计: 17/20

---

## 综合评分（0-100）

- 技术维度: 42/50
- 格式维度: 30/30
- 完整性维度: 17/20
- 综合得分: 89/100

---

## 修改记录（问题清单 + 建议 + 优先级）

### P0（必须修复，否则不建议通过）

1) Q-flux_mixed_layer_model.md：“spin up run”译法存在语义误导风险
- 位置: doc/ModelDescription/Q-flux_mixed_layer_model.md（两处 “spin up run”）
- 源文: “spin up run”
- 译文现状: “旋合运行”
- 风险: “旋合”更常指“（气象/流场）收敛/辐合”，与同段落 “ocean heat convergence/海洋热辐合”并列时更易引发误读。
- 建议（择一并全文件统一）:
  - 保留英文: “spin-up 运行”（中文行解释为“自旋预平衡/预平衡运行”等）
  - 或译为“预平衡运行/自旋预热运行”，避免使用“旋合”字样。

### P1（建议尽快处理，显著提升一致性）

2) Diagnostics.md：标题译名与词典条目不一致
- 位置: doc/ModelDescription/Diagnostics.md:1
- 词典: Diagnostics → 诊断输出（terminology-dictionary.md:142）
- 建议: 标题改为 “# Diagnostics / 诊断输出”，并在正文中继续使用“诊断/诊断输出”择一统一。

### P2（可规划：提升可追溯性与后续一致性成本）

3) Q-flux_mixed_layer_model.md：处理 “see above”锚点引用
- 位置: doc/ModelDescription/Q-flux_mixed_layer_model.md（“见上文”）
- 建议: 若无可对应锚点，可改为“见上文（原文锚点：#part4_2）”或直接保留英文链接文本，避免读者误以为本文档内有可跳转位置。

4) 术语补录建议（补录到术语词典 v1.4，至少覆盖本批次新增术语）
- spin-up run → spin-up 运行 / 预平衡运行（建议保留英文并给出中文释义）
- ocean heat convergence → 海洋热辐合（或热收敛，择一并统一）
- sea ice concentration → 海冰密集度（或海冰浓度，择一并统一）
- frazil ice → 冰花
- basal fluxes / lateral fluxes → 底部通量 / 侧向通量
- lead fraction → 冰缝比例（或开阔水域比例，择一并统一）
- melt pond → 融池
- sigma-coordinate → σ坐标
- post-processing → 后处理
- budget page diagnostics → 预算页诊断
- lat-lon diags / lat-height diagnostics → 纬度-经度诊断 / 纬度-高度诊断
- (advective) tendencies → （平流）趋势
- atmospheric dissipation → 大气耗散
- pressure filter → 压力滤波器

---

[CONVERSATION_ID]: 019c233e-c228-7771-981b-4e97776aa6af

---

# 审查请求文档审查（.claude/request.md：第四批文档）

- 时间: 2026-02-03 23:40
- 对象: .claude/request.md（ModelDescription 翻译质量审查请求：第四批文档）

## 结论

- 综合评分: 93/100
- 建议: 通过（已补齐会话ID；并修正1处跨批一致性表述，现可直接用于后续审查）

## 关键发现

1) 信息一致性良好，可作为审查输入
- 文件顶部元信息（第四批、任务#13/#15/#19、6文件）与“需要审查的文件”表格一致。
- 评分维度与权重（50/30/20）及子分上限（25/25/15/15/10/10）清晰，便于按条目输出。
- 翻译规范引用已更新为 `.claude/rules/translation-standards.md` v1.2，并在“审查特别关注点”中引用了第十一章相关条目，口径一致。

2) 已修正跨批一致性描述的语义偏差（避免误导审查者）
- 原表述“海冰相关术语与#8（Cloud_processes）一致”不准确，已改为“云过程相关术语与#8一致”，与本批次文件（Main_time_stepping_loop.md 中涉及 moist convection/large scale condensation）更贴合。

3) 会话ID已补齐，便于后续审查记录串联
- 已在 `.claude/request.md` 末尾追加 `[CONVERSATION_ID]`。

## 修改记录（已落地）

- `.claude/request.md`：修正“与前批术语一致性”中的 1 处表述（海冰→云过程）
- `.claude/request.md`：追加会话ID块（便于追溯）

---

[CONVERSATION_ID]: 019c233e-c228-7771-981b-4e97776aa6af

---

# ModelDescription 翻译质量审查报告（第五批/最后一批：任务#14/#16/#17）

- 时间: 2026-02-04 22:35
- 审查依据: .claude/request.md（第五批文档翻译审查请求/最后一批）
- 对照源文件: old-doc/ModelDescription/对应HTML文件
- 术语标准参考: .claude/terminology-dictionary.md（v1.4）
- 格式标准参考: .claude/rules/translation-standards.md（v1.3）

## 覆盖文件（7个）

- doc/ModelDescription/GISS_Dynamic_ocean_model.md ↔ old-doc/ModelDescription/GISS_Dynamic_ocean_model.html
- doc/ModelDescription/Ocean_Tracers.md ↔ old-doc/ModelDescription/Ocean_Tracers.html
- doc/ModelDescription/Tracers.md ↔ old-doc/ModelDescription/Tracers.html
- doc/ModelDescription/Aerosol_Tracers.md ↔ old-doc/ModelDescription/Aerosol_Tracers.html
- doc/ModelDescription/Gas_Tracers.md ↔ old-doc/ModelDescription/Gas_Tracers.html
- doc/ModelDescription/Special_Tracers.md ↔ old-doc/ModelDescription/Special_Tracers.html
- doc/ModelDescription/Air_mass_Tracers.md ↔ old-doc/ModelDescription/Air_mass_Tracers.html

---

## 结论与建议

- 综合评分: 85/100
- 建议: 小幅修改后可通过（P0主要集中在“拼写错误处理策略”的落地不一致；修复后预计≥93）

---

## 评分详情（按 request.md 维度）

### 1) 技术维度评分（0-50）

#### 1.1 术语一致性（0-25）：22/25

主要发现（证据）:
- 海洋动力学术语整体与请求中的“暂定译法”一致，且跨文件一致性较好：
  - non-Boussinesq → 非Boussinesq（GISS_Dynamic_ocean_model.md:3-4）
  - C-grid/D-grid、upstream scheme、KPP 等译法稳定（GISS_Dynamic_ocean_model.md:5-14）
  - pressure gradient force / equation of state / geopotential 等译法可复核（GISS_Dynamic_ocean_model.md:208-214 等段落）
- 示踪物相关术语与词典条目能对齐的部分保持一致：
  - rundeck → 运行配置（Tracers.md:10；terminology-dictionary.md:237）
- 气溶胶与化学缩略词保留良好：TOMAS、CFC、PSC、CBM-4、RACM 等均稳定保留（Aerosol_Tracers.md、Gas_Tracers.md）。

主要扣分点:
- “elemental carbon / BC / EC”中文侧使用“元素碳/EC/BC”混用但未给出一次性口径说明，容易在后续词典补录时分裂（Aerosol_Tracers.md:17-20、125-134）。
- request.md 的“detrainment → 夹出”口径已在 Gas_Tracers.md 中使用，但与第三批 Cloud_processes.md 的“夹卷”口径不同；建议最终在词典 v1.4 固化并回填前批次（跨批一致性问题，非本批次P0）。

#### 1.2 翻译准确性（0-25）：23/25

主要发现（证据）:
- GISS_Dynamic_ocean_model.md 的状态方程推导与压力梯度力段落语义对齐良好，符号/单位保持一致（例如 α/β/Γ/Θ 定义段：GISS_Dynamic_ocean_model.md:96-133；压力梯度力段：GISS_Dynamic_ocean_model.md:208 起）。
- Aerosol_Tracers.md 的 TOMAS 模型流程描述与源文一致，关键过程（碰并/凝结/成核、云内清除、干沉降）均覆盖（Aerosol_Tracers.md:1-31）。
- Gas_Tracers.md 对 Shindell 机制的关键参数（51物种、156反应、Fast-J2、对流羽流输送等）保留完整（Gas_Tracers.md:19-33）。
- 其余短文档（Ocean_Tracers/Air_mass_Tracers/Special_Tracers）语义对齐稳定，可复核。

主要扣分点:
- 少量中文措辞略拗口但不影响准确性（例如 “平均平均体积”：GISS_Dynamic_ocean_model.md:214）。
- 部分公式排版未使用代码块/LaTeX，可能影响渲染可读性（见格式维度）。

技术维度小计: 45/50

### 2) 格式维度评分（0-30）

#### 2.1 Markdown格式（0-15）：14/15

结论:
- 标题、段落、表格均可被 Markdown 解析；多数段落中英之间空行清晰。
- 扣分点：GISS_Dynamic_ocean_model.md 的多行积分/公式块为“裸文本多行”，建议用代码块或 LaTeX 包裹以避免不同渲染器下错行（GISS_Dynamic_ocean_model.md:262-279 附近）。

#### 2.2 中英对照格式（0-15）：12/15

结论:
- 大部分段落遵循“英文在上、中文在下”的句对/段对格式。
- 扣分点（可定位）：
  - 存在仅中文的小标题，缺少“English / 中文”配对（Tracers.md:27；Aerosol_Tracers.md:86；Special_Tracers.md:9）。
  - Tracers.md 的列表项使用“同一行中英混排”，不符合严格叠放口径（Tracers.md:29-35）；建议改为“英文一行 + 中文一行”的列表句对形式。

格式维度小计: 26/30

### 3) 完整性维度评分（0-20）

#### 3.1 内容完整性（0-10）：10/10

结论:
- 7 个文件均能在对应 HTML 中定位到全部段落/列表内容；未发现漏段。
- Gas_Tracers.md 参考文献段落完整保留（Gas_Tracers.md:35-41）。

#### 3.2 拼写处理（0-10）：4/10

主要发现（与 request.md 第五章“更正+标注”策略不一致）:
- request.md 明确列出并声称“已更正/已标注”的拼写错误，在译文英文行中仍保留误拼，或未标注：
  - contect 未更正且未标注（GISS_Dynamic_ocean_model.md:18）
  - enthapy 未更正，仅在中文行标注（GISS_Dynamic_ocean_model.md:32-33；68-69）
  - coagualtion 未更正且未标注（Aerosol_Tracers.md:24）
  - Availble 未更正，仅在中文行标注（Aerosol_Tracers.md:47-48）
  - assummed 未更正，仅在中文行标注（Aerosol_Tracers.md:99-100）
- 另有未纳入 request.md 拼写清单的明显误拼仍保留（示例）：
  - spatically（应为 spatially）：GISS_Dynamic_ocean_model.md:12
  - conjuction（应为 conjunction）：Gas_Tracers.md:3

完整性维度小计: 14/20

---

## 综合评分（0-100）

- 技术维度: 45/50
- 格式维度: 26/30
- 完整性维度: 14/20
- 综合得分: 85/100

---

## 修改记录（问题清单 + 建议 + 优先级）

### P0（必须修复，否则不建议提交为“最终整合版本”）

1) 落地“原文拼写错误处理策略”（更正 + 中文括注原拼写）
- 影响范围: doc/ModelDescription/GISS_Dynamic_ocean_model.md、doc/ModelDescription/Aerosol_Tracers.md（以及本批次其他文件中的明显误拼）
- 现状证据:
  - GISS_Dynamic_ocean_model.md:18 contect 未更正/未标注
  - GISS_Dynamic_ocean_model.md:32-33、68-69 enthapy 未更正（仅中文标注）
  - Aerosol_Tracers.md:24 coagualtion 未更正/未标注
  - Aerosol_Tracers.md:47-48 Availble 未更正（仅中文标注）
  - Aerosol_Tracers.md:99-100 assummed 未更正（仅中文标注）
- 建议（对每一处误拼统一执行）:
  - 英文行改为正确拼写
  - 中文行末尾追加“（原文拼写：xxx）”

### P1（建议尽快处理，提升一致性与可读性）

2) 统一中英对照标题/小标题格式
- 位置:
  - Tracers.md:27（“## 示踪物类型”）
  - Aerosol_Tracers.md:86（“## 气溶胶物种性质表”）
  - Special_Tracers.md:9（“## 特殊示踪物类型”）
- 建议: 改为 “## English / 中文”形式，保持目录结构一致。

3) Tracers.md 列表改为严格叠放句对
- 位置: doc/ModelDescription/Tracers.md:29-35
- 建议: 每个条目拆为“英文行（含链接）”+“中文行”，避免同一行中英混排。

4) GISS_Dynamic_ocean_model.md 公式块改为代码块或 LaTeX
- 位置: doc/ModelDescription/GISS_Dynamic_ocean_model.md（多行积分/公式段落）
- 建议: 使用代码块包裹多行公式，或用 LaTeX 以保证渲染稳定性与可读性。

### P2（可规划：为最终整合与词典补录降低成本）

5) 内部链接从 `.html` 迁移到 `.md`（如目标是 Markdown 文档站点）
- 位置: doc/ModelDescription/Tracers.md:29-35
- 建议: 将链接指向同目录下的 `.md` 文件（并保留必要的“源文链接”说明）。

6) 术语词典 v1.4 补录建议（最小优先集合）
- 建议优先补录（本批次高频/跨文件术语）:
  - non-Boussinesq、free surface、C-grid/D-grid、upstream scheme、KPP
  - isopycnal diffusion、mesoscale eddy、subgrid scale straits
  - potential enthalpy / specific enthalpy / (potential) specific enthalpy
  - specific volume / potential specific volume、geopotential、pressure gradient force、equation of state
  - TOMAS、sectional approach、bins、(externally/internally mixed)、hydrophobic/hydrophilic
  - coagulation、condensation、nucleation、scavenging（云内/云下）、dry deposition
  - photolysis rates、Fast-J2、PSC、CBM-4、RACM、detrainment（与第三批口径统一后再入库）

---

[CONVERSATION_ID]: 019c2813-f6f6-7322-b30b-f6ff83c96711
