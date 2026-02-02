# ModelDescription翻译质量审查请求（第二批文档）

- 时间: 2026-02-02
- 审查对象: 任务#12、#18、#20共6个翻译文件
- 源文件对照: old-doc/ModelDescription/对应HTML文件
- 术语标准参考: .claude/terminology-dictionary.md（v1.4）
- 格式参考: .claude/rules/translation-standards.md

---

## 一、项目基本信息

### 项目概况
- **项目名称**: ModelE2.1.2_Lazenca - NASA GISS地球系统模型中文翻译
- **项目类型**: 大气环流模型(GCM)/地球系统模型技术文档翻译
- **翻译范围**: 620+文件（HTML文档、Fortran代码、脚本、配置文件）
- **当前版本**: 0.2.2
- **翻译阶段**: 2.1（ModelDescription技术文档翻译）

### 项目结构
```
modelE2.1.2_Lazenca/
├── old-doc/ModelDescription/    # 原始HTML文档
├── doc/ModelDescription/        # 翻译后Markdown文档
├── .claude/
│   ├── terminology-dictionary.md   # 术语词典v1.4
│   └── rules/
│       └── translation-standards.md  # 翻译规范
```

---

## 二、项目状态与当前任务

### 项目进度
- **已完成任务**: 5/14（35.7%）
  - ✅ #7 大气基础模型文档（3个文件）
  - ✅ #10 陆面基础模型文档（3个文件）
  - ✅ #20 输入输出系统文档（1个文件）
  - ✅ #12 湖泊和河流文档（2个文件）
  - ✅ #18 模型结构和代码文档（3个文件）

- **本次审查范围**: 任务#12、#18、#20的6个翻译文件

### 本次工作内容

**任务#20 - 输入输出系统文档**（1个文件，733B）
- Input_Output.md - 描述模型I/O系统架构（IORSF驱动程序、预报变量）

**任务#12 - 湖泊和河流文档**（2个文件，1.4KB）
- Lake_model.md - 二层湖泊模式、降水蒸发、河流入流出流、对流翻转
- Rivers.md - 河流径流收集、下游方向、门槛深度、海洋沉积

**任务#18 - 模型结构和代码文档**（3个文件，1.1KB）
- Overall_model_structure.md - 整体模型结构
- Source_code_and_directory_structure.md - 源代码和目录结构（空文档）
- Initialisation.md - 初始化流程（INPUT子程序、init_XYZ例程）

### 交付物
- 6个Markdown翻译文件，采用中英对照叠放格式
- 位置：doc/ModelDescription/
- 格式：UTF-8编码，Markdown语法

---

## 三、审查目标文件与范围

### 需要审查的文件

| 序号 | 翻译文件 | 源文件 | 大小 | 内容概述 |
|------|----------|--------|------|----------|
| 1 | doc/ModelDescription/Input_Output.md | old-doc/ModelDescription/Input_Output.html | 733B | I/O系统架构、IORSF驱动程序、预报变量 |
| 2 | doc/ModelDescription/Lake_model.md | old-doc/ModelDescription/Lake_model.html | - | 二层湖泊模式、热扩散、对流翻转 |
| 3 | doc/ModelDescription/Rivers.md | old-doc/ModelDescription/Rivers.html | - | 河流径流、下游方向、门槛深度 |
| 4 | doc/ModelDescription/Overall_model_structure.md | old-doc/ModelDescription/Overall_model_structure.html | - | 整体模型结构（极简） |
| 5 | doc/ModelDescription/Source_code_and_directory_structure.md | old-doc/ModelDescription/Source_code_and_directory_structure.html | - | 源代码和目录结构（空文档） |
| 6 | doc/ModelDescription/Initialisation.md | old-doc/ModelDescription/Initialisation.html | - | 初始化流程、INPUT子程序 |

### 关键术语对照表（本次涉及）

| 英文术语 | 标准译法 | 出现位置 |
|---------|----------|----------|
| boundary condition files | 边界条件文件 | Input_Output.md |
| restart file | 重启动文件 | Input_Output.md |
| I/O | 输入输出 | Input_Output.md |
| driver routine | 驱动例程 | Input_Output.md, Initialisation.md |
| prognostic variables | 预报变量 | Input_Output.md, Initialisation.md |
| tracers | 示踪物 | Input_Output.md |
| diagnostics | 诊断输出 | Input_Output.md |
| two layer code | 二层模式 | Lake_model.md |
| precipitation | 降水 | Lake_model.md |
| evaporation | 蒸发 | Lake_model.md |
| river inflow/outflow | 河流入流/出流 | Lake_model.md |
| heat diffusion | 热扩散 | Lake_model.md |
| convective overturning | 对流翻转 | Lake_model.md |
| temperature stratification | 温度层结 | Lake_model.md |
| runoff | 径流 | Rivers.md |
| land grid boxes | 陆地网格 | Rivers.md |
| downstream direction | 下游方向 | Rivers.md |
| sill depth | 门槛深度 | Rivers.md |
| subroutine | 子程序 | Initialisation.md |
| ocean box | 海洋网格 | Rivers.md |

---

## 四、审查要点与检查清单

### 1. 技术维度（权重50%）

#### 1.1 术语一致性（30%）
检查项：
- [ ] 所有专业术语是否与术语词典v1.4一致
- [ ] 本次翻译的新术语是否使用了标准、规范的译法
- [ ] 同一术语在不同文件中是否保持一致
- [ ] 是否存在口语化或过于简略的表达
- [ ] 专有名词（IORSF、INPUT、ISTART等）是否正确保留

重点审查：
- "prognostic variables"是否统一译为"预报变量"
- "runoff"是否译为"径流"（与任务#10保持一致）
- "convective overturning"是否译为"对流翻转"
- "temperature stratification"是否译为"温度层结"

#### 1.2 翻译准确性（30%）
检查项：
- [ ] 技术内容是否准确传达原文含义
- [ ] 数值、代码、文件名是否100%保真
- [ ] 语句是否通顺流畅，避免生硬直译
- [ ] 关键句是否避免了"直译+括号解释"模式
- [ ] 是否存在内容遗漏或误译

重点审查：
- Lake_model.md中"two layer code"译为"二层模式"是否准确
- Rivers.md中"predefined sill depth"译为"预定义的门槛深度"是否清晰
- Input_Output.md中"driver routine"译为"驱动例程"是否规范
- Initialisation.md中init_XYZ例程的处理是否正确

### 2. 格式维度（权重30%）

#### 2.1 Markdown格式（15%）
检查项：
- [ ] 标题格式是否正确（`# English / 中文`）
- [ ] 段落分隔是否清晰（中英文之间空一行）
- [ ] 代码标签<TT>是否正确使用
- [ ] 文件编码是否为UTF-8

#### 2.2 中英对照格式（15%）
检查项：
- [ ] 是否采用"英文在上、中文在下"的叠放形式
- [ ] 标题、段落是否保持原文结构
- [ ] 空文档（Source_code_and_directory_structure.md）的处理是否合理

### 3. 完整性维度（权重20%）

#### 3.1 内容完整性（10%）
检查项：
- [ ] 是否存在内容遗漏
- [ ] 文献引用、文件名是否保持不变
- [ ] 原文拼写错误（如Rivers.html中的"intereaction"、"Tranpsort"）是否正确处理

#### 3.2 结构保真性（10%）
检查项：
- [ ] 是否保持原有段落结构
- [ ] 文件命名是否符合规范（.html → .md）
- [ ] 目录位置是否正确（doc/ModelDescription/）

---

## 五、评分标准

### 综合评分计算（0-100分）

- **技术维度**（50分）= 术语一致性（25分）+ 翻译准确性（25分）
- **格式维度**（30分）= Markdown格式（15分）+ 中英对照格式（15分）
- **完整性维度**（20分）= 内容完整性（10分）+ 结构保真性（10分）

### 通过标准
- **综合评分 ≥ 90分**：通过，可提交
- **综合评分 85-89分**：小幅修改后可通过
- **综合评分 < 85分**：退回修改

---

## 六、审查特别关注点

### 1. 新术语处理
本次翻译涉及多个新术语，需要特别关注：
- "prognostic variables" → "预报变量"（气象学标准术语）
- "convective overturning" → "对流翻转"（流体力学术语）
- "temperature stratification" → "温度层结"（大气/海洋学术语）
- "sill depth" → "门槛深度"（水文学术语）

### 2. 空文档处理
Source_code_and_directory_structure.md源文件为空，当前处理为仅保留标题，请确认这是否符合项目规范。

### 3. 原文拼写错误处理
Rivers.html中存在拼写错误：
- "intereaction" → 应为 "interaction"
- "Tranpsort" → 应为 "Transport"

当前翻译保留了原文拼写，请在审查中确认处理策略是否正确。

### 4. 与任务#10的一致性
本次翻译的"runoff"（径流）术语需要与任务#10的Ground_Hydrology.md保持一致。

---

## 七、输出要求

请Codex提供以下输出：

1. **技术维度评分**（0-100分）
   - 术语一致性评分与问题列表
   - 翻译准确性评分与问题列表

2. **格式维度评分**（0-60分）
   - Markdown格式评分与问题列表
   - 中英对照格式评分与问题列表

3. **完整性维度评分**（0-20分）
   - 内容完整性评分与问题列表
   - 结构保真性评分与问题列表

4. **综合评分**（0-100分，按权重折算）

5. **明确建议**
   - 通过 / 退回修改
   - 支持论据和关键发现

6. **修改记录**（如适用）
   - 按优先级排序的问题清单（P0/P1/P2）
   - 具体修改建议

---

## 八、审查参考文件

### 术语词典
- 文件位置：.claude/terminology-dictionary.md
- 版本：v1.4
- 覆盖领域：气候科学、数值方法、Fortran编程、模型组件等12个类别

### 翻译规范
- 文件位置：.claude/rules/translation-standards.md
- 创建日期：2026-02-02
- 基于任务#10 Codex审查报告的经验教训

### 历史审查报告
- 文件位置：.claude/review-report.md
- 上次评分：85/100（任务#10陆面模块翻译）
- 主要问题：术语口语化、句式生硬、表述不清晰

---

## 九、用户原始需求

用户原文："创建审查请求"

需求背景：
- 已完成3个翻译任务（#12、#18、#20），共6个文件
- 需要对新翻译文件进行质量审查
- 确保翻译质量符合项目标准
- 为后续翻译工作建立质量基准

---

**审查请求创建时间**: 2026-02-02
**预期审查完成时间**: 待定
**审查者**: Codex AI
**会话ID**: [待生成]
