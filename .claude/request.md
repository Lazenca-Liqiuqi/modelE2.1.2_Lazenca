# ModelDescription翻译质量审查请求（第三批文档）

- 时间: 2026-02-03
- 审查对象: 任务#8、#9、#11共4个翻译文件
- 源文件对照: old-doc/ModelDescription/对应HTML文件
- 术语标准参考: .claude/terminology-dictionary.md（v1.4）
- 格式参考: .claude/rules/translation-standards.md（v1.1）

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
│       └── translation-standards.md  # 翻译规范v1.1
```

---

## 二、项目状态与当前任务

### 项目进度
- **已完成任务**: 8/14（57.1%）
  - ✅ #7 大气基础模型文档（3个文件）
  - ✅ #10 陆面基础模型文档（3个文件）
  - ✅ #20 输入输出系统文档（1个文件）
  - ✅ #12 湖泊和河流文档（2个文件）
  - ✅ #18 模型结构和代码文档（3个文件）
  - ✅ #11 植被模型文档（1个文件）
  - ✅ #9 地表通量文档（1个文件）
  - ✅ #8 云和湍流过程文档（2个文件）

- **本次审查范围**: 任务#11、#9、#8的4个翻译文件

### 本次工作内容

**任务#11 - 植被模型文档**（1个文件，~320行）
- Vegetation_model.md - Ent动态陆地生物圈模型（DGVM）、植物功能型（PFT）、生物物理、季节性、土壤生物地球化学

**任务#9 - 地表通量文档**（1个文件，~449行）
- Surface_fluxes.md - 行星边界层（PBL）计算、表面通量参数化、PBL_DRV.f和PBL.f模块详细说明

**任务#8 - 云和湍流过程文档**（2个文件，~378行）
- Cloud_processes.md - 湿润对流、积云参数化、层状云、微物理过程
- Turbulence_and_Dry_convection.md - 湍流闭合方案、干对流、ATURB.f和ATURB_E1.f

### 交付物
- 4个Markdown翻译文件，采用中英对照叠放格式
- 位置：doc/ModelDescription/
- 格式：UTF-8编码，Markdown语法

---

## 三、审查目标文件与范围

### 需要审查的文件

| 序号 | 翻译文件 | 源文件 | 大小 | 内容概述 |
|------|----------|--------|------|----------|
| 1 | doc/ModelDescription/Vegetation_model.md | old-doc/ModelDescription/Vegetation_model.html | ~320行 | Ent动态陆地生物圈模型、PFT、生物物理、季节性、土壤生物地球化学、气象驱动表 |
| 2 | doc/ModelDescription/Surface_fluxes.md | old-doc/ModelDescription/Surface_fluxes.html | ~449行 | PBL计算、表面通量、PBL_DRV.f和PBL.f模块、30+子程序详细说明 |
| 3 | doc/ModelDescription/Cloud_processes.md | old-doc/ModelDescription/Cloud_processes.html | ~116行 | 湿润对流、积云参数化（MSTCNV）、层状云（LSCOND）、微物理、7+3个物理循环 |
| 4 | doc/ModelDescription/Turbulence_and_Dry_convection.md | old-doc/ModelDescription/Turbulence_and_Dry_convection.html | ~262行 | 湍流闭合、干对流、ATURB.f和ATURB_E1.f对比、二阶闭合方案 |

### 关键术语对照表（本次涉及，以下译法为本批次暂定；审查后择优补录到术语词典v1.4）

| 英文术语 | 暂定译法（待确认/待补录） | 出现位置 |
|---------|----------|----------|
| **植被模型术语** | | |
| Dynamic Global Vegetation Model (DGVM) | 动态全球植被模型 | Vegetation_model.md |
| Ent Terrestrial Biosphere Model (Ent TBM) | Ent陆地生物圈模型 | Vegetation_model.md |
| plant functional types (PFTs) | 植物功能型 | Vegetation_model.md |
| canopy | 冠层 | Vegetation_model.md |
| biogeochemistry | 生物地球化学 | Vegetation_model.md |
| photosynthesis | 光合作用 | Vegetation_model.md |
| leaf area index (LAI) | 叶面积指数 | Vegetation_model.md |
| stomatal conductance | 气孔导度 | Vegetation_model.md |
| phenology | 物候 | Vegetation_model.md |
| **表面通量术语** | | |
| Planetary Boundary Layer (PBL) | 行星边界层 | Surface_fluxes.md |
| turbulence closure scheme | 湍流闭合方案 | Surface_fluxes.md |
| virtual potential temperature | 虚拟位温 | Surface_fluxes.md |
| specific humidity | 比湿 | Surface_fluxes.md |
| roughness length | 粗糙长度 | Surface_fluxes.md |
| drag coefficient | 曳力系数 | Surface_fluxes.md |
| Monin-Obukhov length | Monin-Obukhov长度 | Surface_fluxes.md |
| friction velocity | 摩擦速度 | Surface_fluxes.md |
| tridiagonal method | 三对角方法 | Surface_fluxes.md |
| **云过程术语** | | |
| moist convection | 湿润对流 | Cloud_processes.md |
| cumulus parameterization | 积云参数化 | Cloud_processes.md |
| mass flux closure | 质量通量闭合 | Cloud_processes.md |
| entrainment | 卷入 | Cloud_processes.md |
| detrainment | 夹卷 | Cloud_processes.md |
| stratiform clouds | 层状云 | Cloud_processes.md |
| large scale condensation | 大尺度凝结 | Cloud_processes.md |
| autoconversion | 自动转化 | Cloud_processes.md |
| accretion | 碰并 | Cloud_processes.md |
| glaciation | 冰川化 | Cloud_processes.md |
| Bergeron-Findeisen process | Bergeron-Findeisen过程 | Cloud_processes.md |
| **湍流术语** | | |
| dry convection | 干对流 | Turbulence_and_Dry_convection.md |
| Turbulent Kinetic Energy (TKE) | 湍流动能 | Turbulence_and_Dry_convection.md |
| second-order closure (SOC) | 二阶闭合 | Turbulence_and_Dry_convection.md |
| nonlocal vertical transport | 非局地垂直输送 | Turbulence_and_Dry_convection.md |
| bulk Richardson number | 总体理查森数 | Turbulence_and_Dry_convection.md |
| adiabatic warming | 绝热增温 | Turbulence_and_Dry_convection.md |

---

## 四、审查要点与检查清单

### 1. 技术维度（权重50%）

#### 1.1 术语一致性（25%）
检查项：
- [ ] 所有专业术语是否与术语词典v1.4一致
- [ ] 本次翻译的大量新术语是否使用了标准、规范的译法
- [ ] 同一术语在不同文件中是否保持一致
- [ ] 是否存在口语化或过于简略的表达
- [ ] 专有名词（Ent、PFT、PBL、MSTCNV、LSCOND等）是否正确保留

重点审查：
- "canopy"是否统一译为"冠层"（而非"树冠层"等）
- "biogeochemistry"是否译为"生物地球化学"
- "entrainment/detrainment"是否准确译为"卷入/夹卷"
- "glaciation"在云微物理中是否译为"冰川化"
- PBL相关术语（roughness length、drag coefficient等）是否与词典一致
- 湍流闭合方案术语（second-order closure、nonlocal transport等）是否规范

#### 1.2 翻译准确性（25%）
检查项：
- [ ] 技术内容是否准确传达原文含义
- [ ] 复杂技术描述是否准确易懂
- [ ] 子程序和模块说明是否准确
- [ ] 语句是否通顺流畅，避免生硬直译
- [ ] 是否存在内容遗漏或误译

重点审查：
- Vegetation_model.md中Ent模型的复杂描述是否准确
- Surface_fluxes.md中30+子程序的功能说明是否准确
- Cloud_processes.md中7个主要物理循环的描述是否清晰
- Turbulence_and_Dry_convection.md中ATURB.f和ATURB_E1.f的区别是否准确传达
- 表格（Vegetation_model.md中的PFT列表、气象驱动表）是否正确翻译

### 2. 格式维度（权重30%）

#### 2.1 Markdown格式（15%）
检查项：
- [ ] 标题格式是否正确（`# English / 中文`）
- [ ] 段落分隔是否清晰（中英文之间空一行）
- [ ] 代码块和表格格式是否正确
- [ ] 文件编码是否为UTF-8

#### 2.2 中英对照格式（15%）
检查项：
- [ ] 是否采用"英文在上、中文在下"的叠放形式
- [ ] 标题、段落是否保持原文结构
- [ ] 表格翻译是否保持格式一致

### 3. 完整性维度（权重20%）

#### 3.1 内容完整性（10%）
检查项：
- [ ] 是否存在内容遗漏
- [ ] 文献引用是否保持不变
- [ ] 参考文献列表是否完整

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

---

## 六、审查特别关注点

### 1. 大量新术语的一致性
本次翻译涉及大量新术语，特别是：
- 植被模型术语：DGVM、PFT、canopy、biogeochemistry等
- PBL术语：roughness length、drag coefficient、Monin-Obukhov length等
- 云微物理术语：entrainment、detrainment、autoconversion、accretion、glaciation等
- 湍流闭合术语：second-order closure、nonlocal transport等

### 2. 复杂技术描述的准确性
- Vegetation_model.md中Ent模型的详细介绍（ Cohorts、Patch communities、Ent cells等概念）
- Surface_fluxes.md中30+子程序的功能说明
- Cloud_processes.md中7个湿润对流循环和3个层状云循环的描述
- Turbulence_and_Dry_convection.md中ATURB.f和ATURB_E1.f的区别

### 3. 表格翻译
- Vegetation_model.md中有两个表格（PFT列表、气象驱动变量表、输出变量表）
- 表格翻译需要保持格式一致性和术语准确性

### 4. 与前批术语的一致性
确保与前两批翻译（#7、#10、#12、#18、#20）的术语保持一致，特别是：
- PBL相关术语与#7（Atmospheric_model、Dynamics）一致
- 陆面水文相关术语与#10（Ground_Hydrology）一致
- 陆面过程术语与#12（Lake_model、Rivers）一致

### 5. 翻译规范v1.1的遵守情况
检查是否遵守translation-standards.md v1.1中的新规范：
- 段落拆分规则（4.1节）
- 原文拼写错误处理策略（6.2节）
- 术语词典一致性要求（8.1节）
- 语义误导风险避免（8.2节）
- 重复结构优化（8.3节）

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
- 版本：v1.1
- 更新内容：新增第八、九章节，总结第二批文档审查经验

### 历史审查报告
- 文件位置：.claude/review-report.md
- 包含3批次的审查记录：
  - 任务#10：85/100
  - 任务#12/#18/#20：83/100
  - 主要问题总结和改进建议

---

## 九、用户原始需求

用户原文："创建审查请求"

需求背景：
- 已完成3个新翻译任务（#11、#9、#8），共4个文件
- 文档内容较前两批更复杂，涉及大量新术语
- 需要对新翻译文件进行质量审查
- 确保翻译质量符合项目标准
- 为后续翻译工作建立质量基准

---

**审查请求创建时间**: 2026-02-03
**预期审查完成时间**: 待定
**审查者**: Codex AI
**会话类型**: ModelDescription第三批文档质量审查
**文件数量**: 4个文件（Vegetation_model.md、Surface_fluxes.md、Cloud_processes.md、Turbulence_and_Dry_convection.md）
**会话ID**: 019c1ec0-f93f-7f72-94a9-1f11e741bb2a
