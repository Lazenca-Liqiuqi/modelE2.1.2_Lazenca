# ModelDescription翻译质量审查请求（第四批文档）

- 时间: 2026-02-03
- 审查对象: 任务#13、#15、#19共6个翻译文件
- 源文件对照: old-doc/ModelDescription/对应HTML文件
- 术语标准参考: .claude/terminology-dictionary.md（v1.4）
- 格式参考: .claude/rules/translation-standards.md（v1.2）

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
│       └── translation-standards.md  # 翻译规范v1.2
```

---

## 二、项目状态与当前任务

### 项目进度
- **已完成任务**: 11/14（78.6%）
  - ✅ #7 大气基础模型文档（3个文件）
  - ✅ #10 陆面基础模型文档（3个文件）
  - ✅ #20 输入输出系统文档（1个文件）
  - ✅ #12 湖泊和河流文档（2个文件）
  - ✅ #18 模型结构和代码文档（3个文件）
  - ✅ #11 植被模型文档（1个文件）
  - ✅ #9 地表通量文档（1个文件）
  - ✅ #8 云和湍流过程文档（2个文件）
  - ✅ #13 海洋基础模型文档（2个文件）
  - ✅ #15 海冰模块文档（2个文件）
  - ✅ #19 时间步进和诊断文档（2个文件）

- **本次审查范围**: 任务#13、#15、#19的6个翻译文件

### 本次工作内容

**任务#13 - 海洋基础模型文档**（2个文件，~20行）
- Ocean_models.md - 海洋模型概述
- Q-flux_mixed_layer_model.md - Q-flux混合层模型详细说明

**任务#15 - 海冰模块文档**（2个文件，~53行）
- Sea_ice_model.md - 海冰模型配置概述
- Basic_thermodynamics.md - 海冰热力学过程详解

**任务#19 - 时间步进和诊断文档**（2个文件，~32行）
- Main_time_stepping_loop.md - 主时间步进循环，16个例程调用顺序
- Diagnostics.md - 诊断系统概述

### 交付物
- 6个Markdown翻译文件，采用中英对照叠放格式
- 位置：doc/ModelDescription/
- 格式：UTF-8编码，Markdown语法

---

## 三、审查目标文件与范围

### 需要审查的文件

| 序号 | 翻译文件 | 源文件 | 大小 | 内容概述 |
|------|----------|--------|------|----------|
| 1 | doc/ModelDescription/Ocean_models.md | old-doc/ModelDescription/Ocean_models.html | ~3行 | 海洋模型标题 |
| 2 | doc/ModelDescription/Q-flux_mixed_layer_model.md | old-doc/ModelDescription/Q-flux_mixed_layer_model.html | ~17行 | Q-flux混合层模型、旋合运行、海洋热辐合、深海扩散 |
| 3 | doc/ModelDescription/Sea_ice_model.md | old-doc/ModelDescription/Sea_ice_model.html | ~6行 | 海冰模型配置概述 |
| 4 | doc/ModelDescription/Basic_thermodynamics.md | old-doc/ModelDescription/Basic_thermodynamics.html | ~47行 | 海冰热力学过程：质量层结构、热力层、通量计算、冰花形成、融池 |
| 5 | doc/ModelDescription/Main_time_stepping_loop.md | old-doc/ModelDescription/Main_time_stepping_loop.html | ~24行 | 主时间步进循环，16个例程的调用顺序详解 |
| 6 | doc/ModelDescription/Diagnostics.md | old-doc/ModelDescription/Diagnostics.html | ~8行 | 诊断系统概述 |

### 关键术语对照表（本批次暂定译法）

| 英文术语 | 暂定译法（待确认/待补录） | 出现位置 |
|---------|----------|----------|
| **海洋模块术语** | | |
| Ocean models | 海洋模型 | Ocean_models.md |
| Q-flux | Q-flux（保持英文） | Q-flux_mixed_layer_model.md |
| mixed layer | 混合层 | Q-flux_mixed_layer_model.md |
| SST | 海表温度 | Q-flux_mixed_layer_model.md |
| spin up run | 旋合运行 | Q-flux_mixed_layer_model.md |
| ocean heat convergence | 海洋热辐合 | Q-flux_mixed_layer_model.md |
| freshwater mass | 淡水质量 | Q-flux_mixed_layer_model.md |
| climatology | 气候态值 | Q-flux_mixed_layer_model.md |
| thermal equilibrium | 热平衡 | Q-flux_mixed_layer_model.md |
| forcing | 强迫 | Q-flux_mixed_layer_model.md |
| **海冰模块术语** | | |
| sea ice model | 海冰模型 | Sea_ice_model.md |
| sea ice concentration | 海冰密集度 | Sea_ice_model.md |
| prognostic | 预报 | Sea_ice_model.md |
| ice advection | 海冰平流 | Sea_ice_model.md |
| frazil ice | 冰花 | Basic_thermodynamics.md |
| basal fluxes | 底部通量 | Basic_thermodynamics.md |
| lateral fluxes | 侧向通量 | Basic_thermodynamics.md |
| lead fraction | 冰缝比例 | Basic_thermodynamics.md |
| melt pond | 融池 | Basic_thermodynamics.md |
| albedo | 反照率 | Basic_thermodynamics.md |
| snow-ice formation | 雪冰形成 | Basic_thermodynamics.md |
| sigma-coordinate | σ坐标 | Basic_thermodynamics.md |
| **系统架构术语** | | |
| time stepping loop | 时间步进循环 | Main_time_stepping_loop.md |
| diagnostics | 诊断 | Diagnostics.md |
| atmospheric dynamics | 大气动力学 | Main_time_stepping_loop.md |
| moist convection | 湿润对流 | Main_time_stepping_loop.md |
| large scale condensation | 大尺度凝结 | Main_time_stepping_loop.md |
| radiative transfer | 辐射传输 | Main_time_stepping_loop.md |
| advective tendencies | 平流趋势 | Main_time_stepping_loop.md |
| atmospheric dissipation | 大气耗散 | Main_time_stepping_loop.md |
| pressure filter | 压力滤波器 | Main_time_stepping_loop.md |
| post-processing | 后处理 | Diagnostics.md |
| budget page diagnostics | 预算页诊断 | Diagnostics.md |
| lat-lon diags | 纬度-经度诊断 | Diagnostics.md |
| lat-height diagnostics | 纬度-高度诊断 | Diagnostics.md |

---

## 四、审查要点与检查清单

### 1. 技术维度（权重50%）

#### 1.1 术语一致性（25%）
检查项：
- [ ] 所有专业术语是否与术语词典v1.4一致
- [ ] 本次翻译的新术语是否使用了标准、规范的译法
- [ ] 同一术语在不同文件中是否保持一致
- [ ] 是否存在口语化或过于简略的表达
- [ ] 例程名是否保持英文不变（SURFCE, UNDERICE, FORM_SI, MELT_SI, DIAGA等）

重点审查：
- "spin up run"译为"旋合运行"是否为标准译法
- "ocean heat convergence"译为"海洋热辐合"是否准确
- "sigma-coordinate"译为"σ坐标"是否准确
- "lead fraction"译为"冰缝比例"是否准确
- "prognostic"译为"预报"是否准确
- "frazil ice"译为"冰花"是否准确
- 例程名是否正确保持英文

#### 1.2 翻译准确性（25%）
检查项：
- [ ] 技术内容是否准确传达原文含义
- [ ] 复杂技术描述是否准确易懂
- [ ] 例程和模块说明是否准确
- [ ] 语句是否通顺流畅，避免生硬直译
- [ ] 是否存在内容遗漏或误译

重点审查：
- Q-flux_mixed_layer_model.md中海洋热辐合和深海扩散的概念描述
- Basic_thermodynamics.md中质量层结构和σ坐标的复杂描述
- Main_time_stepping_loop.md中16个例程调用顺序的清晰度
- Basic_thermodynamics.md第三段冰花形成过程的描述

### 2. 格式维度（权重30%）

#### 2.1 Markdown格式（15%）
检查项：
- [ ] 标题格式是否正确（`# English / 中文`）
- [ ] 段落分隔是否清晰（中英文之间空一行）
- [ ] 文件编码是否为UTF-8

#### 2.2 中英对照格式（15%）
检查项：
- [ ] 是否采用"英文在上、中文在下"的叠放形式
- [ ] 标题、段落是否保持原文结构
- [ ] 中英文段落对应清晰

### 3. 完整性维度（权重20%）

#### 3.1 内容完整性（10%）
检查项：
- [ ] 是否存在内容遗漏
- [ ] 例程名是否完整保留

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

### 历史评分参考
- 任务#10：85/100（修改后预计≥90）
- 任务#12/#18/#20：83/100（修改后预计≥90）
- 任务#11/#9/#8：84/100（修改后预计≥90）

---

## 六、审查特别关注点

### 1. 新术语的准确性
本次翻译涉及多个新领域术语，特别是：
- 海洋科学术语：spin up run、ocean heat convergence、Q-flux等
- 海冰科学术语：frazil ice、lead fraction、melt pond、sigma-coordinate等
- 系统架构术语：time stepping loop、advective tendencies、budget page diagnostics等

### 2. 复杂技术描述的准确性
- Q-flux_mixed_layer_model.md中海洋热辐合计算和深海扩散的概念
- Basic_thermodynamics.md中质量层结构和σ坐标的详细描述
- Main_time_stepping_loop.md中16个例程的调用顺序和功能说明

### 3. 与前批术语的一致性
确保与前几批翻译（#7、#8、#9、#10、#11、#12、#15、#18、#20）的术语保持一致，特别是：
- 云过程相关术语与#8（Cloud_processes）一致
- 大气过程术语与#7、#8（Atmospheric_model、Dynamics、Cloud_processes）一致
- 陆面过程术语与#10、#12（Ground_Hydrology、Lake_model）一致

### 4. 翻译规范v1.2的遵守情况
检查是否遵守translation-standards.md v1.2中的新规范：
- 同根术语一致性（第十一章）
- 术语辨识度（第十一章）
- 位置概念准确性（第十一章）
- 口语化表达需避免（第十一章）
- 原文拼写错误处理策略（第十一章）

---

## 七、输出要求

请Codex提供以下输出：

1. **技术维度评分**（0-50分）
   - 术语一致性（0-25）评分与问题列表
   - 翻译准确性（0-25）评分与问题列表

2. **格式维度评分**（0-30分）
   - Markdown格式（0-15）评分与问题列表
   - 中英对照格式（0-15）评分与问题列表

3. **完整性维度评分**（0-20分）
   - 内容完整性（0-10）评分与问题列表
   - 结构保真性（0-10）评分与问题列表

4. **综合评分**（0-100分，按权重折算）

5. **明确建议**
   - 通过 / 退回修改
   - 支持论据和关键发现

6. **修改记录**（如适用）
   - 按优先级排序的问题清单（P0/P1/P2）
   - 具体修改建议

7. **新术语补录建议**
   - 列出需要补录到术语词典v1.4的新术语

---

## 八、审查参考文件

### 术语词典
- 文件位置：.claude/terminology-dictionary.md
- 版本：v1.4
- 覆盖领域：气候科学、数值方法、Fortran编程、模型组件等12个类别

### 翻译规范
- 文件位置：.claude/rules/translation-standards.md
- 版本：v1.2
- 更新内容：新增第十一、十二、十三章，总结第三批文档审查经验

### 历史审查报告
- 文件位置：.claude/review-report.md
- 包含4批次的审查记录：
  - 任务#10：85/100
  - 任务#12/#18/#20：83/100
  - 任务#11/#9/#8：84/100
  - 主要问题总结和改进建议

---

## 九、用户原始需求

用户原文："创建审查请求"

需求背景：
- 已完成3个新翻译任务（#13、#15、#19），共6个文件
- 涉及海洋科学、海冰科学、系统架构三个领域
- 需要对新翻译文件进行质量审查
- 确保翻译质量符合项目标准
- 为后续翻译工作建立质量基准

---

**审查请求创建时间**: 2026-02-03
**预期审查完成时间**: 待定
**审查者**: Codex AI
**会话类型**: ModelDescription第四批文档质量审查
**文件数量**: 6个文件（Ocean_models.md、Q-flux_mixed_layer_model.md、Sea_ice_model.md、Basic_thermodynamics.md、Main_time_stepping_loop.md、Diagnostics.md）

---

[CONVERSATION_ID]: 019c233e-c228-7771-981b-4e97776aa6af
