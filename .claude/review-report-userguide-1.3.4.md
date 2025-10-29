# ModelE 用户指南阶段1.3.4 翻译质量审查报告

审查时间：2025-10-29 19:41
审查对象：
- doc/UserGuide/Adding_info_for_automatic_documentation.md（91行）
- doc/UserGuide/Vegetation_Guide.md（84行）
- doc/UserGuide/Choosing_proper_ISTART.md（70行）

审查范围：术语一致性、格式规范性、技术准确性、内容完整性、可读性、代码保持
参考标准：.claude/terminology-dictionary.md、.claude/translation-format-standard.md、.claude/html-markdown-conversion-rules.md（UserGuide适用）

---

## 1. 总体结论
- 综合评分：82/100
- 建议：需修改
- 结论说明：技术术语与中文表达总体准确，但两份文档（Vegetation_Guide、Choosing_proper_ISTART）未严格采用“英/中对照叠放”格式；一份文档（Adding_info_for_automatic_documentation）在代码块内混入中文译文，影响代码保真。建议按下述项点修正后再合入。

## 2. 各维度评分
- 技术维度（40%）：82/100
  - 术语准确性：85
  - 概念理解：86
  - 代码完整性：76（Adding_info 在代码块混入译文、ISTART 列表未按 `<tt>`→反引号处理）
- 语言维度（30%）：90/100
  - 中文表达自然，专业性与可读性良好；少量措辞可微调以提升精确性（如下）。
- 格式维度（20%）：65/100
  - 未统一采用“英文（加粗）+中文紧随”的段落级对照；大段内容缺失英文原文对应；行内代码未统一使用反引号。
- 完整性（10%）：92/100
  - 与旧版HTML源（old-doc/UserGuide/*.html）核对，内容基本覆盖；未发现信息缺失，但存在中英对照缺失（属格式问题）。

> 加权总分：82 = 0.4×82 + 0.3×90 + 0.2×65 + 0.1×92

---

## 3. 主要发现与证据（基于文件行号）

### 3.1 添加文档标签指南（Adding_info_for_automatic_documentation.md）
- 代码块内混入中文译文（违反“代码保真”与转换规则）
  - 标签列表示例：doc/UserGuide/Adding_info_for_automatic_documentation.md:10-27
    - 问题：在代码围栏内加入中文行（如 L12、L14、L16、L18、L20、L22、L24、L26），不利于复制使用与自动化提取。
    - 规则：translation-format-standard.md 要求“代码内容保持英文”；html-markdown-conversion-rules.md 要求“代码保真”。
  - Fortran示例：doc/UserGuide/Adding_info_for_automatic_documentation.md:41-66
    - 问题1：重复作者行（L47、L48）
    - 问题2：将中文译文插入代码（L45-46、L51、L54、L60、L62、L64、L66）
    - 影响：示例不再是可编译/可复用的Fortran片段；破坏读者复制验证与工具解析。
- 细微术语与格式
  - “namelist”应统一为“Namelist”（专名首字母大写）：L36

建议修复：
- 将标签列表与Fortran示例代码块还原为纯英文原文；中文译文移出代码块，按“英文（可加粗）+中文紧随”的段落对照形式呈现。
- 去除重复“!@auth John Smith”（保留一次）。
- “Namelist”大小写统一。

---

### 3.2 植被模型用户指南（Vegetation_Guide.md）
- 中英对照不完整（大段中文缺少英文原文对应）
  - 组件选项说明中文化但无英文原文：L28-32
  - INPUT_FILES 列表中文化但无英文原文逐项对照：L36-41
  - Ent附加输入文件列表中文化但无英文原文：L45-49
  - 参数段中文化但无英文原文：L53-57
  - 诊断指标中文化但无英文原文：L61-72
  - 依据：html版原文存在对应英文（见 old-doc/UserGuide/Vegetation_Guide.html:24-59、63-104）
- 代码/参数呈现方式可提升
  - “OPTS_Ent = ONLINE=YES PS_MODEL=FBB PFT_MODEL=ENT”（L24）建议使用行内反引号或文本代码块，便于视觉区分与复制。
  - “E1M20iEnt.R / E4F40iEnt.R”（L15-16）可改为无序列表项，提升可读性。
- 术语与表达
  - “Farquhar/Ball-Berry 生物物理”译法准确；“预报物候学（prognostic phenology）”准确。
  - “force_VEG … 是否从文件强制LAI”建议改为“是否从文件强制使用LAI值”更清晰。

建议修复：
- 逐段补回英文原文，并按“英文（可加粗）→中文”叠放；确保段落等量对应。
- 对参数/文件名采用反引号或列表，保持与项目既有文档一致性。

---

### 3.3 ISTART 初始化选择指南（Choosing_proper_ISTART.md）
- 枚举条目缺少英文原文、行内代码未保留
  - L7-20：仅中文条目；根据HTML源（old-doc/UserGuide/Choosing_proper_ISTART.html:14-40），应为“英文条目（`ISTART=#` 用反引号）+ 中文条目”一一对应。
  - 当前使用粗体“**ISTART=#**”，应改为反引号行内代码：`ISTART=#`（依据 html-markdown-conversion-rules.md 的`<tt>`→反引号规则）。
- 术语一致性
  - “rsf file / AIC / GIC / OIC / rundeck”等均已正确保留并解释到位。
  - “pbl 值”建议在首次出现处补注“行星边界层（PBL）”以消除歧义。
- 其他段落
  - L22-23、L25-26：已按中英对照呈现，风格正确。

建议修复：
- 为每一条 ISTART 选项补回英文原文，并将“ISTART=#”置于反引号中；中文译文紧随其后。
- 首次出现“pbl”补充中文注解“行星边界层（PBL）”。

---

## 4. 术语一致性核查
- 与词典一致：
  - Rundeck → 运行配置（多处一致）
  - Tracer → 示踪物（Choosing_proper_ISTART.md:26）
  - Checkpoint/Restart（未在本批文档中出现显式术语对译，但关联文档一致）
  - Namelist：建议统一专名大小写（Namelist），中文可作“参数名录”注释。
- 建议新增/完善词条（词典补充）：
  - PBL → 行星边界层
  - Ent（模块名，保留英文专名并注释）
  - PFT → 植物功能型
  - LAI → 叶面积指数
  - Farquhar/Ball-Berry（生理模型名，保留专名）
  - phenology → 物候学 / 预报物候学（prognostic phenology）

---

## 5. 建议的统一格式基线（与现有UserGuide保持一致）
- 标题：`# 英文 / 中文` 或 “英文一行、中文一行”二选一，但同一文档内需统一。
- 段落：英文原文使用粗体（**...**），下一行中文译文；段落间空一行；中英段落数量必须一一对应。
- 行内代码：使用反引号（`...`）保留大小写与占位符；将 HTML `<tt>` 统一转换为反引号。
- 代码块：仅保留英文原文；中文说明置于代码块外；Fortran/命令行等按规则标注语言（fortran、bash、text）。
- 列表与表格：中英项目等量对应；文件名和参数名使用反引号。

---

## 6. 可读性微调建议
- “是否从文件强制LAI” → “是否从文件强制使用LAI值”。
- “预报季节性”可在首次处标注“（prognostic seasonality）”。
- 首次出现“pbl”补注“行星边界层（PBL）”。

---

## 7. 修复清单（可按文件分批提交）
1) doc/UserGuide/Adding_info_for_automatic_documentation.md（高优先级）
- 将 L10-27、L41-66 的中文译文移出代码块；保留代码块为英文原文；中文译文在代码块外按段落对照呈现。
- 删除重复行 L48；统一“Namelist”大小写（如 L36）。

2) doc/UserGuide/Vegetation_Guide.md（高优先级）
- 为 L28-32、L36-41、L45-49、L53-57、L61-72 补回英文原文段落（可参考 old-doc/UserGuide/Vegetation_Guide.html）。
- 将 L24 用反引号包裹；L15-16 改为列表项。

3) doc/UserGuide/Choosing_proper_ISTART.md（高优先级）
- 为 L7-20 每条 ISTART 选项补回英文原文；将“ISTART=#”改为反引号格式。
- 首次出现“pbl”处补充中文注释。

4) 术语词典补充（建议）
- 在 .claude/terminology-dictionary.md 增加 PBL、Ent、PFT、LAI、Farquhar/Ball-Berry、phenology 相关条目，统一大小写与注释风格。

---

## 8. 验收建议
- 建议结论：需修改
- 通过条件：
  - 三个文件均补齐英文原文与中文对照，代码块恢复为纯英文；
  - 行内代码与专名格式对齐转换规则；
  - 术语大小写与词典一致；
  - 以上修复完成后可判定为“通过”。

---

（本报告基于仓库文件与 old-doc HTML 源逐项比对，包含行号定位以便快速修复。）

