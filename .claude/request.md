# ModelDescription第五批文档翻译审查请求（最后一批）

- 时间: 2026-02-04
- 审查对象: 任务#14、#16、#17共7个翻译文件
- 源文件对照: old-doc/ModelDescription/对应HTML文件
- 术语标准参考: .claude/terminology-dictionary.md（v1.4）
- 格式参考: .claude/rules/translation-standards.md（v1.3）

---

## 一、项目基本信息

### 项目概况
- **项目名称**: ModelE2.1.2_Lazenca - NASA GISS地球系统模型中文翻译
- **项目类型**: 大气环流模型(GCM)/地球系统模型技术文档翻译
- **翻译范围**: 620+文件（HTML文档、Fortran代码、脚本、配置文件）
- **当前版本**: 0.2.2
- **翻译阶段**: 2.1（ModelDescription技术文档翻译）- **最后阶段**

### 项目进度
- **已完成任务**: 14/14（100%）🎉
- **本次审查**: 最后一批，完成后所有28个ModelDescription文件翻译完毕

---

## 二、本次工作内容与交付物

### 翻译文件清单（7个文件）

| 序号 | 翻译文件 | 源文件 | 大小 | 内容概述 |
|------|----------|--------|------|----------|
| 1 | doc/ModelDescription/GISS_Dynamic_ocean_model.md | old-doc/ModelDescription/GISS_Dynamic_ocean_model.html | ~180行 | GISS动力学海洋模型完整技术文档（非Boussinesq、C-grid、KPP、状态方程、压力梯度力） |
| 2 | doc/ModelDescription/Ocean_Tracers.md | old-doc/ModelDescription/Ocean_Tracers.html | ~7行 | Russell海洋示踪物启用说明 |
| 3 | doc/ModelDescription/Tracers.md | old-doc/ModelDescription/Tracers.html | ~34行 | 示踪物系统概述（五类示踪物、预处理器指令、TRACER_COM.f） |
| 4 | doc/ModelDescription/Aerosol_Tracers.md | old-doc/ModelDescription/Aerosol_Tracers.html | ~114行 | TOMAS气溶胶微物理模型（二矩分档、物种性质表、TOMAS系列配置） |
| 5 | doc/ModelDescription/Gas_Tracers.md | old-doc/ModelDescription/Gas_Tracers.html | ~35行 | Shindell化学机制（51物种、156反应、Fast-J2光解、对流输送） |
| 6 | doc/ModelDescription/Special_Tracers.md | old-doc/ModelDescription/Special_Tracers.html | ~13行 | 特殊示踪物类型（水同位素O18、平流层/对流层交换Lerner） |
| 7 | doc/ModelDescription/Air_mass_Tracers.md | old-doc/ModelDescription/Air_mass_Tracers.html | ~13行 | 气质量输送示踪物（不溶性气体、理想示踪物、'Air'示踪物特殊处理） |

### 交付物
- 7个Markdown翻译文件，采用中英对照叠放格式
- 位置：doc/ModelDescription/
- 格式：UTF-8编码，Markdown语法
- **总计**: 28个ModelDescription文件全部完成

---

## 三、关键术语对照表（约70个新术语）

### 海洋动力学术语（16个）
| 英文 | 中文 | 说明 |
|------|------|------|
| non-Boussinesq | 非Boussinesq（保留英文） | 跨领域术语，避免误译 |
| free surface | 自由表面 | 海洋表面类型 |
| C-grid / D-grid | C网格 / D网格 | Arakawa交错网格 |
| upstream scheme | 迎风格式 | 数值平流方案 |
| KPP (K-Profile Parameterization) | K-剖面参数化 | 垂直混合方案 |
| mesoscale eddy | 中尺度涡 | 海洋中尺度现象 |
| isopycnal diffusion | 等位密度扩散 | 沿等密度面扩散 |
| subgrid scale straits | 次网格尺度海峡 | 海峡参数化 |
| prognostic variables | 预报变量 | 模型预测变量 |
| potential enthalpy | 位焓 | 热力学函数 |
| specific enthalpy | 比焓 | 单位质量的焓 |
| potential specific enthalpy | 位比焓 | 位温下比焓 |
| specific volume | 比容 | 单位质量体积 |
| potential specific volume | 位比容 | 位温下比容 |
| adiabatic lapse rate | 绝热递减率 | 温度随高度变化 |
| equation of state | 状态方程 | 海水状态方程 |
| pressure gradient force | 压力梯度力 | 海洋动力学基本力 |
| geopotential | 位势 | 重力位势 |
| quadratic precision | 二次精度 | 数值积分精度 |
| least square fit | 最小二乘拟合 | 数学拟合方法 |

### 示踪物基础术语（13个）
| 英文 | 中文 | 说明 |
|------|------|------|
| tracer | 示踪物 | 追踪物质 |
| mass transport | 质量输送 | 质量传输 |
| pre-processor directives | 预处理器指令 | 编译指令 |
| rundeck | 运行配置 | 模型运行配置文件 |
| radioactive decay | 放射性衰变 | 核衰变过程 |
| air mass tracers | 气质量示踪物 | 跟踪气团 |
| insoluble gases | 不溶性气体 | 不溶于水 |
| ideal tracers | 理想示踪物 | 理想化示踪物 |
| air mass age | 气质量龄 | 空气停留时间 |
| source | 来源 | 示踪物来源 |
| air | 空气 | 空气示踪物 |
| concentration | 浓度 | 浓度守恒 |
| water isotopes | 水同位素 | 氧同位素等 |
| stratospheric/tropospheric exchange | 平流层/对流层交换 | 大气层交换 |

### 气溶胶专业术语（25个）
| 英文 | 中文 | 说明 |
|------|------|------|
| TOMAS (TwO-Moment Aerosol Sectional) | 二矩气溶胶分档模型 | 保留英文缩写 |
| sectional approach | 分档方法 | 按尺寸分段 |
| bins | 档/分段 | 尺寸分段 |
| aerosol size distribution | 气溶胶尺寸分布 | 粒径分布 |
| two moments | 二矩 | 总数和质量 |
| size-resolved | 尺寸分辨的 | 按尺寸解析 |
| externally/internally mixed | 外混/内混 | 混合状态 |
| hydrophobic/hydrophilic | 疏水/亲水 | 水亲和性 |
| elemental carbon (EC/BC) | 元素碳/黑碳 | EC=Elemental Carbon |
| organic matter (OM) | 有机物 | 有机物质 |
| organic aerosol (OA) | 有机气溶胶 | OA |
| POA (Primary Organic Aerosol) | 一次有机气溶胶 | 直接排放 |
| SOA (Secondary Organic Aerosol) | 二次有机气溶胶 | 化学生成 |
| coagulation | 碰并 | 颗粒聚并 |
| condensation | 凝结 | 气体凝结 |
| nucleation | 成核 | 颗粒形成 |
| scavenging | 清除 | 湿清除 |
| in-cloud scavenging | 云内清除 | 云中清除 |
| dry deposition | 干沉降 | 地表沉降 |
| series resistance approach | 串联阻力方法 | 阻力模型 |
| gravitational settling | 重力沉降 | 重力作用 |
| quasilaminar sublayer | 准层流子层 | 近地层 |
| supersaturation | 过饱和度 | 饱和度 |
| Köhler theory | Köhler理论 | 云滴形成 |
| pseudo-steady state | 伪稳态 | 近似稳态 |

### 气溶胶物种术语（15个）
| 英文 | 中文 | 说明 |
|------|------|------|
| sulfate | 硫酸盐 | SO4²⁻ |
| sea salt | 海盐 | 海洋气溶胶 |
| mineral dust | 矿物尘埃 | 沙尘 |
| ammonium | 铵 | NH4⁺ |
| aerosol-water | 气溶胶水 | 气溶胶中水 |
| precursor | 前体物 | 前驱体 |
| gas-phase/aqueous-phase | 气相/液相 | 相态 |
| methanesulfonic acid (MSA) | 甲烷磺酸 | MSA |
| dimethylsulfide (DMS) | 二甲基硫醚 | DMS |
| e-folding time | e-fold时间 | 特征时间 |
| OM/OC ratio | 有机物/有机碳比 | 1.4 |
| molecular weight | 分子量 | g/mol |
| density | 密度 | kg/m³ |
| aerosol number | 气溶胶数 | 颗粒数 |
| aerosol optical depth | 气溶胶光学厚度 | AOD |

### 大气化学术语（22个）
| 英文 | 中文 | 说明 |
|------|------|------|
| chemical mechanism | 化学机制 | 反应机制 |
| tropospheric/stratospheric chemistry | 对流层/平流层化学 | 分层化学 |
| NOx-HOx-Ox-CO-CH4 chemistry | NOx-HOx-Ox-CO-CH4化学 | 主要循环 |
| PANs | PAN（过氧羧基硝酸酐） | 保留缩写 |
| hydrocarbons | 烃类 | 碳氢化合物 |
| isoprene | 异戊二烯 | BVOC |
| alkyl nitrates | 烷基硝酸酯 | 有机硝酸酯 |
| aldehydes | 醛类 | 醛化合物 |
| alkenes | 烯烃 | 不饱和烃 |
| paraffins | 烷烃 | 饱和烃 |
| lumped hydrocarbon family scheme | 集总烃族方案 | 碳键机制 |
| Carbon Bond Mechanism-4 (CBM-4) | 碳键机制-4 | 保留缩写 |
| Regional Atmospheric Chemistry Model (RACM) | 大气区域化学模型 | 保留缩写 |
| chlorine- and bromine-containing | 含氯和含溴 | 卤素化合物 |
| CFC | 氟氯碳化物/氟利昂 | 保留缩写 |
| gas-phase chemistry | 气相化学 | 气相反应 |
| photolysis rates | 光解速率 | 光解反应 |
| Fast-J2 scheme | Fast-J2方案 | 光解计算 |
| convective plumes | 对流羽流 | 对流上升气流 |
| updrafts | 上升气流 | 向上气流 |
| rainout | 雨洗 | 云中清除 |
| washout | 冲刷 | 云下清除 |
| detrainment | 夹出 | 离开云体 |
| precipitation | 降水 | 雨雪等 |
| acetone | 丙酮 | CH3COCH3 |
| branching ratio | 分支比 | 反应分支 |
| polar stratospheric cloud (PSC) | 极地平流层云 | 保留缩写 |
| heterogeneous hydrolysis | 非均相水解 | 多相水解 |
| terpene | 萜烯 | 萜类化合物 |
| oxidized organic vapors | 氧化有机蒸气 | 氧化VOC |
| convective transport | 对流输送 | 垂直输送 |
| phase transformation | 相变 | 相态变化 |

### 光学性质术语（5个）
| 英文 | 中文 | 说明 |
|------|------|------|
| light attenuation | 光衰减 | 光强减弱 |
| extinction efficiency | 消光效率 | 消光系数 |
| single scattering albedo | 单次散射反照率 | SSA |
| scattering phase function | 散射相函数 | 角度分布 |
| tabulated optical properties | 列表光学性质 | 预制光学参数 |

---

## 四、审查要点与检查清单

### 1. 技术维度（权重50%）

#### 1.1 术语一致性（25%）
检查项：
- [ ] 所有专业术语是否与词典v1.4一致
- [ ] 新术语（约70个）译名是否准确、规范
- [ ] 同一术语在7个文件中是否保持一致
- [ ] 跨领域术语处理是否得当（如non-Boussinesq保留英文）
- [ ] 缩略词处理是否统一（TOMAS、CFC、PSC、PAN、CBM-4、RACM等）

重点审查：
- TOMAS系列术语翻译是否准确（分档、矩、档等）
- 化学物种术语是否规范（硫酸盐、海盐、黑碳、有机物等）
- 大气化学术语专业性（烃类、醛类、烯烃、烷烃等）
- 海洋热力学术语准确性（位焓、比焓、位温、状态方程等）
- 示踪物分类术语一致性（气质量、理想示踪物等）

#### 1.2 翻译准确性（25%）
检查项：
- [ ] 技术内容是否准确传达原文含义
- [ ] 数学公式和物理方程说明是否清晰
- [ ] 化学物种和反应描述是否准确
- [ ] 数值方法术语是否标准
- [ ] 语句是否通顺流畅，避免欧化句式
- [ ] 是否存在内容遗漏或误译

重点审查：
- GISS_Dynamic_ocean_model.md中压力梯度力推导和状态方程
- Aerosol_Tracers.md中TOMAS模型配置和气溶胶物种性质表
- Gas_Tracers.md中Shindell化学机制（51物种、156反应）
- Tracers.md中五类示踪物分类逻辑
- 物理单位换算是否正确（nm、μm、Torr、Pa等）

### 2. 格式维度（权重30%）

#### 2.1 Markdown格式（15%）
检查项：
- [ ] 标题格式是否正确（`# English / 中文`）
- [ ] 段落分隔是否清晰（中英文之间空一行）
- [ ] 表格格式是否正确（Aerosol_Tracers.md性质表）
- [ ] 代码块和化学式处理是否正确
- [ ] 文件编码是否为UTF-8

#### 2.2 中英对照格式（15%）
检查项：
- [ ] 是否采用"英文在上、中文在下"的叠放形式
- [ ] 标题、段落是否保持原文结构
- [ ] 中英文段落对应是否清晰
- [ ] 列表项翻译是否完整

### 3. 完整性维度（权重20%）

#### 3.1 内容完整性（10%）
检查项：
- [ ] 是否存在内容遗漏
- [ ] 参考文献是否完整保留（Gas_Tracers.md）
- [ ] 例程名是否完整保留（TRACER_COM.f等）

#### 3.2 拼写处理（10%）
检查项：
- [ ] 原文拼写错误是否正确处理
- [ ] 是否在中文译文后标注"（原文拼写：xxx）"
- [ ] 是否保持了与原文的可追溯性

---

## 五、原文拼写错误处理

### 本次发现的拼写错误

#### GISS_Dynamic_ocean_model.html
| 位置 | 原文 | 正确 | 处理方式 |
|------|------|------|----------|
| 第33行 | enthapy | enthalpy | 已在译文中标注 |
| 第47行 | enthapy | enthalpy | 已在译文中标注 |
| 第24行 | contect | connect | 已更正 |

#### Aerosol_Tracers.html
| 位置 | 原文 | 正确 | 处理方式 |
|------|------|------|----------|
| 第74行 | assummed | assumed | 已在译文中标注 |
| 第19行 | Availble | Available | 已在译文中标注 |
| 第12行 | coagualtion | coagulation | 已更正 |

### 处理策略检查
- [ ] 所有拼写错误已在译文中更正
- [ ] 误拼在中文译文后已标注"（原文拼写：xxx）"
- [ ] 保持了与原文的可追溯性

---

## 六、评分标准

### 综合评分计算（0-100分）

- **技术维度**（50分）= 术语一致性（25分）+ 翻译准确性（25分）
- **格式维度**（30分）= Markdown格式（15分）+ 中英对照格式（15分）
- **完整性维度**（20分）= 内容完整性（10分）+ 拼写处理（10分）

### 通过标准
- **综合评分 ≥ 90分**：通过，可提交
- **综合评分 85-89分**：小幅修改后可通过
- **综合评分 < 85分**：退回修改

### 历史评分参考
- 第四批（任务#13、#15、#19）：89/100 → 修改后≥95
- 第三批（任务#10、#12、#18、#20）：83/100 → 修改后≥90
- 第二批（任务#11、#9、#8）：84/100 → 修改后≥90

---

## 七、审查特别关注点

### 1. 新术语数量庞大
本次翻译涉及约70个新术语，是所有批次中最多的，重点检查：
- TOMAS气溶胶微物理术语（25个）
- 大气化学术语（22个）
- 海洋热力学术语（16个）
- 确保术语翻译的专业性和准确性

### 2. 多个科学领域交叉
涉及海洋动力学、示踪物、气溶胶微物理、大气化学等多个领域，需检查：
- 各领域术语的专业性
- 跨领域术语的一致性
- 物理概念的准确性

### 3. 表格和公式处理
- GISS_Dynamic_ocean_model.md中的压力梯度力公式
- Aerosol_Tracers.md中的气溶胶物种性质表
- Gas_Tracers.md中的化学反应式
- 检查格式是否正确、清晰

### 4. 与前批术语的一致性
确保与前14个任务（28个文件）的术语保持一致，特别是：
- 示踪物相关术语与之前一致
- 化学物种术语与UserGuide一致
- 海洋术语与#13一致

### 5. 翻译规范v1.3的遵守情况
检查是否遵守translation-standards.md v1.3中的最新规范：
- 跨领域术语保留英文原则（第十四章）
- 标题与词典一致性（第十四章）
- 海洋与海冰术语特点（第十四章）

---

## 八、输出要求

请Codex提供以下输出：

1. **技术维度评分**（0-50分）
   - 术语一致性（0-25）评分与问题列表
   - 翻译准确性（0-25）评分与问题列表

2. **格式维度评分**（0-30分）
   - Markdown格式（0-15）评分与问题列表
   - 中英对照格式（0-15）评分与问题列表

3. **完整性维度评分**（0-20分）
   - 内容完整性（0-10）评分与问题列表
   - 拼写处理（0-10）评分与问题列表

4. **综合评分**（0-100分，按权重折算）

5. **明确建议**
   - 通过 / 退回修改
   - 支持论据和关键发现

6. **修改记录**（如适用）
   - 按优先级排序的问题清单（P0/P1/P2）
   - 具体修改建议

7. **新术语补录建议**
   - 列出需要补录到术语词典v1.4的所有新术语（约70个）

---

## 九、审查参考文件

### 术语词典
- 文件位置：.claude/terminology-dictionary.md
- 版本：v1.4
- 覆盖领域：气候科学、数值方法、Fortran编程、模型组件等12个类别

### 翻译规范
- 文件位置：.claude/rules/translation-standards.md
- 版本：v1.3
- 更新内容：新增第十四、十五、十六章，总结第四批文档审查经验

### 历史审查报告
- 文件位置：.claude/review-report.md
- 包含4批次的审查记录和改进建议

---

## 十、特别说明

1. **这是最后一批ModelDescription文档**，完成后所有28个文件将进行最终整合和词典补录
2. **新术语数量最多**（约70个），请重点审查术语翻译的准确性和专业性
3. **涉及多个科学领域**（海洋动力学、示踪物、气溶胶微物理、大气化学），请检查各领域术语的专业性
4. **表格和公式较多**，请检查格式是否正确、清晰
5. **参考文献较多**（Gas_Tracers.md），请检查引用格式是否一致

---

**审查请求创建时间**: 2026-02-04
**预期审查完成时间**: 待定
**审查者**: Codex AI
**会话类型**: ModelDescription第五批（最后一批）文档质量审查
**文件数量**: 7个文件
**完成任务**: 14/14（100%）

---

[CONVERSATION_ID]: 019c233e-c228-7771-981b-4e97776aa6af
