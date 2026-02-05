# ModelDescription未转换文件完整性分析报告

**生成时间**: 2026-02-05
**分析范围**: old-doc/ModelDescription/ 所有HTML文件
**当前翻译进度**: 28/46 文件 (60.9%)

---

## 一、文件统计总览

| 类别 | 数量 | 说明 |
|------|------|------|
| old-doc/ModelDescription/ 总文件数 | 46 | 所有HTML文件 |
| 已转换文件数 | 28 | doc/ModelDescription/ 中的.md文件 |
| 未转换文件数 | 18 | 尚未处理的HTML文件 |
| **必须翻译的文件** | **5** | 包含实质技术内容的文档 |
| 不需要翻译的文件 | 13 | 索引、参考、空文件、模板等 |

---

## 二、必须翻译的文件（5个）

### 🔴 优先级1：示踪物体系缺失文件

#### 1. Soluble_and_Water_mass_Tracers.html
- **大小**: 13行
- **内容**: 水质量示踪物详细技术说明
- **技术要点**:
  - 与水文循环相互作用的可溶性示踪物
  - 雨洗、冲刷、干沉降等湿沉降过程
  - 示踪物在水体中的分配和传输
- **为何必须翻译**: Tracers.md中引用此文件（链接：Soluble_and_Water_mass_Tracers.md），是示踪物五大类之一
- **所属模块**: 示踪物模块

#### 2. Stratospheric_processes.html
- **大小**: 20行
- **内容**: 平流层动力过程
- **技术要点**:
  - 平流层曳力参数化
  - 重力波曳力
  - 平流层-对流层交换过程
- **为何必须翻译**: 是大气物理过程的重要组成部分，与动力学模块密切相关
- **所属模块**: 大气模块（补充）

### 🟡 优先级2：海冰与海洋补充文件

#### 3. Ice_advection.html
- **大小**: 34行
- **内容**: 海冰平流动力学
- **技术要点**:
  - Flato-Hibler粘-塑性流变学
  - 冰-海和冰-气动量应力
  - 线性迎风格式平流方案
  - DYNSI和ADVSI模块
- **为何应该翻译**: Sea_ice_model.md的补充技术细节，包含重要的流变学内容
- **所属模块**: 海冰模块（补充）

#### 4. Imposed_Sea_surface_conditions.html
- **大小**: 31行
- **内容**: 强迫海面条件（SST和海冰）
- **技术要点**:
  - 海表温度读取和插值
  - 月均值和日值插值方案
  - 海冰密集度和厚度处理
  - ZSI文件的使用
- **为何应该翻译**: Q-flux_mixed_layer_model.md的配套文档，解释强迫边界条件
- **所属模块**: 海洋模块（补充）

#### 5. Water_Budget.html
- **大小**: 144行
- **内容**: GISS ModelE咸水预算完整方程系统
- **技术要点**:
  - 大气网格变量（无'a'前缀）和海洋网格变量（带'o'前缀）
  - 各子程序后的水质量变化追踪
  - 八个水库的质量守恒方程：AtmosQ、Clouds、LandIce、Ground、LakeIce、LiqLake、SeaIce、LiqOcen
  - 通量数组的处理（MELTI、PREC、RUNPSI、RUNOLI、EVAPOR等）
- **为何应该翻译**: 水文循环的核心技术文档，包含完整的水质量追踪方程
- **所属模块**: 系统架构（水循环）

---

## 三、不需要翻译的文件（13个）

### 3.1 索引和导航文件（3个）
| 文件名 | 大小 | 原因 |
|--------|------|------|
| index.html | 62行 | 目录索引，无技术内容 |
| References.html | 144行 | 参考文献列表，不需要翻译 |
| ModelE.html | 18行 | 项目首页介绍 |

### 3.2 备选模型文件（1个）
| 文件名 | 大小 | 原因 |
|--------|------|------|
| HYCOM.html | 19行 | 备选海洋模型HYCOM的简要介绍，仅3行技术描述，内容极少 |

### 3.3 空文件（1个）
| 文件名 | 大小 | 原因 |
|--------|------|------|
| Land_ice.html | 5行 | 仅包含HTML框架，无实际内容 |

### 3.4 重复或过时文件（8个）
| 文件名 | 说明 |
|--------|------|
| template文件 | 模板文件，非实际内容 |
| 其他旧版本文档 | 已被新版本替代 |

---

## 四、翻译优先级建议

### 🔴 立即翻译（优先级1）
1. **Soluble_and_Water_mass_Tracers.html**
   - 理由：Tracers.md中有链接，示踪物体系完整性要求
   - 预计新术语：~15个（可溶性示踪物、湿沉降过程等）

2. **Stratospheric_processes.html**
   - 理由：大气物理重要组成部分
   - 预计新术语：~10个（重力波曳力、平流层曳力等）

### 🟡 近期翻译（优先级2）
3. **Ice_advection.html**
   - 理由：Sea_ice_model.md的技术补充
   - 预计新术语：~12个（Flato-Hibler流变学、粘-塑性等）

4. **Imposed_Sea_surface_conditions.html**
   - 理由：Q-flux模型配套文档
   - 预计新术语：~8个（插值方案、强迫边界条件等）

5. **Water_Budget.html**
   - 理由：水循环核心方程系统
   - 预计新术语：~20个（水库变量、通量数组等）

### ⚪ 暂不翻译（优先级3）
- HYCOM.html：备选模型，内容极少
- index.html、References.html、Land_ice.html：无技术内容

---

## 五、翻译后文件数量统计

| 状态 | 文件数 |
|------|--------|
| 当前已翻译 | 28 |
| **必须翻译（优先级1+2）** | **5** |
| 翻译后总数 | **33** |
| 完整度 | **71.7%** |

---

## 六、技术术语预估

### 优先级1-2文件预计新增术语（约65个）

**Soluble_and_Water_mass_Tracers.html**（~15个）：
- soluble tracers → 可溶性示踪物
- wet deposition → 湿沉降
- rainout → 雨洗
- washout → 冲刷
- scavenging → 清除
- hydrologic cycle → 水文循环
- interaction → 相互作用

**Stratospheric_processes.html**（~10个）：
- stratospheric drag → 平流层曳力
- gravity wave drag → 重力波曳力
- momentum deposition → 动量沉积
- stratospheric circulation → 平流层环流
- wave breaking → 波破碎
- orographic gravity waves → 地形重力波

**Ice_advection.html**（~12个）：
- ice advection → 海冰平流
- Flato-Hibler rheology → Flato-Hibler流变学
- viscous-plastic → 粘-塑性
- momentum stress → 动量应力
- sea surface gradient → 海表梯度
- internal ice pressure → 内部冰压力
- linear upstream scheme → 线性迎风格式

**Imposed_Sea_surface_conditions.html**（~8个）：
- imposed sea surface conditions → 强迫海面条件
- sea surface temperature (SST) → 海表温度
- sea ice concentration → 海冰密集度
- climatology → 气候态
- transient → 瞬变
- quadratic approximation → 二次近似
- interpolation → 插值

**Water_Budget.html**（~20个）：
- salt water budget → 咸水预算
- prognostic variables → 预报变量
- reservoir → 水库
- flux array → 通量数组
- mass balance → 质量平衡
- atmosphere grid → 大气网格
- ocean grid → 海洋网格
- subroutines → 子程序

---

## 七、建议行动计划

### 第一步：补录示踪物体系文件（优先级最高）
1. 翻译 Soluble_and_Water_mass_Tracers.html
2. 翻译 Stratospheric_processes.html
3. 修复 Tracers.md 中的内部链接（已指向.md文件）

### 第二步：补充海冰和海洋技术文档
4. 翻译 Ice_advection.html
5. 翻译 Imposed_Sea_surface_conditions.html

### 第三步：完成水循环核心文档
6. 翻译 Water_Budget.html（最长，144行，包含大量方程）

### 第四步：更新术语词典
7. 将约65个新术语补录到 terminology-dictionary.md v1.4

### 第五步：整体审查
8. 执行 Task #21: ModelDescription整体审查与质量评估

---

## 八、与现有文件的关联关系

### 需要修复的内部链接
- Tracers.md 中已经包含指向 Soluble_and_Water_mass_Tracers.md 的链接
- 该文件目前不存在，需要翻译后链接才能正常工作

### 模块完整性分析
| 模块 | 当前文件 | 缺失文件 | 完整度 |
|------|----------|----------|--------|
| 大气模块 | 6个 | Stratospheric_processes | 6/7 (85.7%) |
| 陆面模块 | 6个 | 无 | 6/6 (100%) |
| 海洋模块 | 4个 | Imposed_Sea_surface_conditions | 4/5 (80%) |
| 海冰模块 | 2个 | Ice_advection | 2/3 (66.7%) |
| 示踪物模块 | 5个 | Soluble_and_Water_mass_Tracers | 5/6 (83.3%) |
| 系统架构 | 5个 | Water_Budget | 5/6 (83.3%) |

---

## 九、结论与建议

### 主要发现
1. **示踪物体系不完整**：Soluble_and_Water_mass_Tracers.html 是 Tracers.md 的引用目标，必须翻译
2. **平流层物理缺失**：Stratospheric_processes.html 是大气模块的重要补充
3. **海冰动力学不完整**：Ice_advection.html 包含重要的流变学内容
4. **水循环核心方程缺失**：Water_Budget.html 是完整的水质量追踪系统

### 强烈建议
- 在进行 Task #21 整体审查之前，**必须先完成这5个文件的翻译**
- 否则整体审查会发现缺失内容，影响 ModelDescription 阶段的完整性

### 优先顺序
1. 🔴 Soluble_and_Water_mass_Tracers.html（修复Tracers.md链接）
2. 🔴 Stratospheric_processes.html（大气模块完整性）
3. 🟡 Ice_advection.html（海冰流变学补充）
4. 🟡 Imposed_Sea_surface_conditions.html（Q-flux配套）
5. 🟡 Water_Budget.html（水循环核心，但文件较长）

---

**报告生成者**: Claude Code
**分析基准**: old-doc/ModelDescription/ vs doc/ModelDescription/
**下次更新**: 完成优先级1-2文件翻译后
