# ModelE2.1.2_Lazenca 专业术语词典 | Professional Terminology Dictionary
# NASA GISS 地球系统模型翻译标准化术语库 | Standardized Terminology for NASA GISS Earth System Model Translation

## 词典使用说明 | Dictionary Usage Guide

本词典为ModelE2.1.2_Lazenca项目翻译工作提供标准化术语，确保整个项目翻译的一致性和专业性。
This dictionary provides standardized terminology for the ModelE2.1.2_Lazenca project translation, ensuring consistency and professionalism throughout the project.

---

## 1. 气候科学基础术语 | Climate Science Fundamentals

### 大气科学 | Atmospheric Science
| English | 中文 | 注释 |
|---------|------|------|
| General Circulation Model (GCM) | 大气环流模型 | General Circulation Model的简称，用于模拟全球大气环流 |
| Earth System Model (ESM) | 地球系统模型 | 包含大气、海洋、陆面、海冰等组件的综合气候模型 |
| Atmospheric Driver | 大气驱动程序 | 协调所有大气物理过程的主程序模块 |
| Planetary Boundary Layer (PBL) | 行星边界层 | 大气底层受地面直接影响的一层 |
| Atmospheric Dynamics | 大气动力学 | 研究大气运动规律的科学 |
| Radiative Transfer | 辐射传输 | 电磁波在介质中传播时的能量传递过程 |
| Cloud Microphysics | 云微物理 | 研究云粒子形成、增长和消失过程的学科 |
| Convection Parameterization | 对流参数化 | 用参数化方法描述积云对流对环境场的作用 |

### 海洋科学 | Ocean Science
| English | 中文 | 注释 |
|---------|------|------|
| Ocean Dynamics | 海洋动力学 | 研究海水运动规律的科学 |
| Ocean Driver | 海洋驱动程序 | 控制海洋模型运行的主程序 |
| K-Profile Parameterization (KPP) | K-剖面参数化 | 海洋垂直混合参数化方案 |
| Quasi-Geostrophic | 准地转 | 接近地转平衡的流动状态 |
| Ocean Tracer | 海洋示踪物 | 用于追踪海水运动的物质或特性 |
| Biogeochemical Cycle | 生物地球化学循环 | 元素在地球各圈层间的循环过程 |

### 陆面过程 | Land Surface Processes
| English | 中文 | 注释 |
|---------|------|------|
| Land Surface Driver | 陆面驱动程序 | 控制陆面过程模拟的主程序 |
| Hydrology | 水文学 | 研究水循环的科学 |
| Vegetation Dynamics | 植被动力学 | 研究植被生长和变化的科学 |
| Land Ice | 陆地冰盖 | 大陆上的冰川和冰盖 |
| Soil Moisture | 土壤湿度 | 土壤中含水的程度 |
| Surface Albedo | 表面反照率 | 地表反射太阳辐射的能力 |

---

## 2. 数值方法和计算技术 | Numerical Methods and Computing

### 数值方法 | Numerical Methods
| English | 中文 | 注释 |
|---------|------|------|
| Time Integration | 时间积分 | 求解时间演化问题的数值方法 |
| Explicit Scheme | 显式格式 | 直接计算当前时间步的数值方法 |
| Implicit Scheme | 隐式格式 | 需要求解方程组的数值方法 |
| Semi-implicit Scheme | 半隐式格式 | 显式和隐式结合的数值方法 |
| Advection | 平流 | 污染物或物理量随流体的输运过程 |
| Finite Difference | 有限差分 | 用差商代替导数的数值方法 |
| Spectral Method | 谱方法 | 基于函数级数展开的数值方法 |
| Multigrid Method | 多重网格法 | 使用不同精度网格的迭代求解方法 |
| Conjugate Gradient Method | 共轭梯度法 | 求解大型线性方程组的迭代方法 |

### 并行计算 | Parallel Computing
| English | 中文 | 注释 |
|---------|------|------|
| Domain Decomposition | 域分解 | 将计算区域分解为多个子区域并行计算 |
| MPI (Message Passing Interface) | 消息传递接口 | 并行计算机间通信的标准接口 |
| OpenMP | 开放多处理 | 共享内存并行编程标准 |
| Hybrid Parallelization | 混合并行 | MPI和OpenMP结合的并行方式 |

---

## 3. Fortran编程术语 | Fortran Programming Terms

### 语言特性 | Language Features
| English | 中文 | 注释 |
|---------|------|------|
| Fortran 90/95 | Fortran 90/95标准 | 现代Fortran语言标准版本 |
| Fixed Format | 固定格式 | 传统Fortran代码格式，列位置有特殊含义 |
| Free Format | 自由格式 | 现代Fortran代码格式，更灵活的排版 |
| Module | 模块 | Fortran中封装数据和过程的程序单元 |
| Derived Type | 派生类型 | 用户自定义的数据结构 |
| Subroutine | 子程序 | 不返回值的Fortran过程 |
| Function | 函数 | 返回值的Fortran过程 |
| Implicit None | 隐式类型禁用 | 禁用变量隐式类型声明的语句 |
| Intent | 意图属性 | 指定参数用途（输入/输出/输入输出）的属性 |
| Private/Private | 私有/公有 | 控制模块实体访问权限的关键字 |

### 编译和链接 | Compilation and Linking
| English | 中文 | 注释 |
|---------|------|------|
| Compiler | 编译器 | 将源代码转换为可执行代码的程序 |
| Module File (.mod) | 模块文件 | 存储Fortran模块接口信息的文件 |
| Object File (.o) | 目标文件 | 编译后的机器代码文件 |
| Linker | 链接器 | 将多个目标文件组合成可执行文件 |
| Build System | 构建系统 | 自动化编译和链接过程的系统 |
| Makefile | Make文件 | 定义编译规则的文件 |
| Dependency | 依赖关系 | 文件或模块间的相互依赖关系 |

---

## 4. 模型组件和模块 | Model Components and Modules

### 核心模块 | Core Modules
| English | 中文 | 注释 |
|---------|------|------|
| ATM_DRV.f | 大气驱动程序 | 61KB，大气过程主驱动程序 |
| RADIATION.f | 辐射传输模块 | 330KB，处理长短波辐射计算 |
| CLOUDS2.F90 | 云微物理模块 | 259KB，云微物理和宏观物理过程 |
| PBL.f | 边界层模块 | 行星边界层过程处理 |
| convec.f | 对流模块 | 对流参数化方案 |
| OCNDYN.f | 海洋动力学模块 | 212KB，海洋环流计算 |
| GHY_DRV.f | 陆面驱动模块 | 159KB，陆面过程主程序 |
| SEAICE.f | 海冰模块 | 海冰热力学和动力学 |
| DIAG.f | 诊断模块 | 238KB，诊断和输出处理 |

### 共享工具 | Shared Utilities
| English | 中文 | 注释 |
|---------|------|------|
| ATM_COM.f | 大气公共模块 | 大气过程共享变量和常量 |
| ATM_UTILS.f | 大气工具模块 | 大气处理通用函数 |
| RAD_DRV.f | 辐射驱动模块 | 辐射计算驱动程序 |
| RAD_UTILS.f | 辐射工具模块 | 辐射计算辅助函数 |
| DIAG_COM.f | 诊断公共模块 | 诊断系统共享变量 |
| DIAG_PRT.f | 诊断输出模块 | 诊断结果打印输出 |

---

## 5. 输入输出和数据处理 | Input/Output and Data Processing

### 文件格式 | File Formats
| English | 中文 | 注释 |
|---------|------|------|
| NetCDF | 网络通用数据格式 | 科学数据常用的二进制文件格式 |
| Binary Sequential Access | 二进制顺序访问 | Fortran传统的文件访问方式 |
| Direct Access | 直接访问 | 随机访问文件记录的方式 |
| Formatted I/O | 格式化输入输出 | 按指定格式读写文本数据 |
| Unformatted I/O | 非格式化输入输出 | 直接读写二进制数据 |

### 数据处理 | Data Processing
| English | 中文 | 注释 |
|---------|------|------|
| Diagnostics | 诊断输出 | 模型运行结果的分析和输出 |
| Initial Conditions | 初始条件 | 模拟开始时的状态数据 |
| Boundary Conditions | 边界条件 | 模拟区域边界上的约束条件 |
| Forcing Data | 强迫数据 | 驱动模型运行的外部数据 |
| Validation | 验证 | 检查模型结果准确性的过程 |

---

## 6. 计算网格和离散化 | Computational Grids and Discretization

### 网格类型 | Grid Types
| English | 中文 | 注释 |
|---------|------|------|
| Latitude-Longitude Grid | 经纬度网格 | 常用的地理坐标网格 |
| Cubed-Sphere Grid | 立方体球面网格 | 减少极地奇异性的一种网格 |
| Gaussian Grid | 高斯网格 | 用于谱模型的特殊经纬度网格 |
| Vertical Levels | 垂直层次 | 大气垂直方向的离散层数 |
| Resolution | 分辨率 | 网格密度，表示模型精度 |

### 空间离散化 | Spatial Discretization
| English | 中文 | 注释 |
|---------|------|------|
| Staggered Grid | 交错网格 | 变量定义在不同网格点上的网格 |
| Arakawa Grids | 荒川网格 | 几种常用的交错网格类型（A-E网格） |
| Finite Volume Method | 有限体积法 | 基于守恒律的数值方法 |
| Spectral Transform | 谱变换 | 在谱空间和物理空间间转换的方法 |

---

## 7. 物理过程和参数化 | Physical Processes and Parameterizations

### 辐射过程 | Radiation Processes
| English | 中文 | 注释 |
|---------|------|------|
| Shortwave Radiation | 短波辐射 | 太阳辐射，波长较短 |
| Longwave Radiation | 长波辐射 | 地球热辐射，波长较长 |
| Radiative Forcing | 辐射强迫 | 影响地球辐射平衡的因素 |
| Greenhouse Effect | 温室效应 | 大气吸收长波辐射的效应 |
| Albedo | 反照率 | 表面反射太阳辐射的比例 |
| Rayleigh Scattering | 瑞利散射 | 小粒子引起的光散射 |
| Cloud Radiative Effect | 云辐射效应 | 云对辐射场的影响 |

### 云和降水过程 | Cloud and Precipitation Processes
| English | 中文 | 注释 |
|---------|------|------|
| Cloud Microphysics | 云微物理 | 云粒子形成和增长的物理过程 |
| Cloud Macrophysics | 云宏观物理 | 云的形成、发展和消散的宏观过程 |
| Condensation | 凝结 | 水汽转变为液态水的过程 |
| Evaporation | 蒸发 | 液态水转变为水汽的过程 |
| Precipitation | 降水 | 从云中降落的水粒子 |
| Cloud Droplet | 云滴 | 悬浮在云中的小水滴 |
| Ice Crystal | 冰晶 | 悬浮在云中的冰粒子 |
| Bergeron Process | 贝吉龙过程 | 冰晶与水滴共同存在的云中增长过程 |

### 边界层和湍流 | Boundary Layer and Turbulence
| English | 中文 | 注释 |
|---------|------|------|
| Turbulence | 湍流 | 不规则的流体运动 |
| Eddy Diffusivity | 涡扩散系数 | 参数化湍流混合的系数 |
| Mixing Length | 混合长度 | 湍流混合的特征长度 |
| Surface Layer | 近地层 | 紧贴地面的边界层底层 |
| Stable Stratification | 稳定层结 | 有利于湍流抑制的温度分布 |
| Unstable Stratification | 不稳定层结 | 有利于湍流发展的温度分布 |

---

## 8. 化学和气溶胶 | Chemistry and Aerosols

### 大气化学 | Atmospheric Chemistry
| English | 中文 | 注释 |
|---------|------|------|
| Tracer | 示踪物 | 用于追踪大气运动的物质 |
| Chemical Reaction | 化学反应 | 物质间的化学转化过程 |
| Photolysis | 光解 | 光引起的化学反应 |
| Catalytic Cycle | 催化循环 | 催化剂参与的化学反应循环 |
| Ozone Depletion | 臭氧损耗 | 臭氧层破坏的过程 |
| Greenhouse Gas | 温室气体 | 吸收长波辐射的气体 |

### 气溶胶 | Aerosols
| English | 中文 | 注释 |
|---------|------|------|
| Aerosol | 气溶胶 | 悬浮在大气中的微小粒子 |
| Nucleation | 成核 | 气相物质形成粒子的过程 |
| Coagulation | 凝并 | 小粒子合并成大粒子的过程 |
| Deposition | 沉降 | 粒子从大气中移除的过程 |
| Direct Effect | 直接效应 | 气溶胶直接散射和吸收辐射 |
| Indirect Effect | 间接效应 | 气溶胶通过影响云产生的效应 |

---

## 9. 模型配置和运行 | Model Configuration and Execution

### 编译系统 | Build System
| English | 中文 | 注释 |
|---------|------|------|
| Rundeck | 运行配置 | 定义模型运行参数的配置文件 |
| Compiler Options | 编译选项 | 控制编译过程的参数 |
| Optimization | 优化 | 提高代码性能的编译选项 |
| Debugging | 调试 | 查找和修复程序错误的过程 |
| Profiling | 性能分析 | 分析程序性能特征的过程 |
| Libraries | 库 | 预编译的代码集合 |
| Dependencies | 依赖关系 | 软件组件间的依赖关系 |

### 运行控制 | Execution Control
| English | 中文 | 注释 |
|---------|------|------|
| Time Step | 时间步长 | 模型积分的时间间隔 |
| Model Integration | 模型积分 | 时间积分求解模型方程的过程 |
| Restart | 重启动 | 从检查点继续运行的功能 |
| Checkpoint | 检查点 | 保存模型状态的文件 |
| Output Frequency | 输出频率 | 保存结果的时间间隔 |
| Wall Clock Time | 墙上时钟时间 | 实际运行时间 |

---

## 10. 数据分析和可视化 | Data Analysis and Visualization

### 数据分析 | Data Analysis
| English | 中文 | 注释 |
|---------|------|------|
| Time Series | 时间序列 | 按时间顺序排列的数据 |
| Climatology | 气候学 | 长期平均的气候状态 |
| Anomaly | 异常 | 相对于平均状态的偏差 |
| Trend Analysis | 趋势分析 | 分析数据长期变化趋势 |
| Correlation | 相关性 | 两个变量间的关联程度 |
| Statistical Significance | 统计显著性 | 检验结果是否具有统计意义 |

### 可视化 | Visualization
| English | 中文 | 注释 |
|---------|------|------|
| Contour Plot | 等值线图 | 显示等值线的图形 |
| Vector Field | 矢量场 | 用箭头表示的方向场 |
| Animation | 动画 | 显示时间演变的动态图像 |
| Color Map | 色彩映射 | 数值到颜色的对应关系 |

---

## 11. 常用缩写和缩略语 | Common Abbreviations and Acronyms

### 机构名称 | Organization Names
| English | 中文 | 注释 |
|---------|------|------|
| NASA | 美国国家航空航天局 | National Aeronautics and Space Administration |
| GISS | 戈达德空间研究所 | Goddard Institute for Space Studies |
| IPCC | 政府间气候变化专门委员会 | Intergovernmental Panel on Climate Change |
| CMIP | 耦合模式比较计划 | Coupled Model Intercomparison Project |

### 技术术语 | Technical Terms
| English | 中文 | 注释 |
|---------|------|------|
| ESM | 地球系统模型 | Earth System Model |
| GCM | 大气环流模型 | General Circulation Model |
| AOGCM | 大气海洋耦合环流模型 | Atmosphere-Ocean General Circulation Model |
| SST | 海表温度 | Sea Surface Temperature |
| TOA | 大气层顶 | Top of Atmosphere |
| LSF | 大尺度 forcing | Large Scale Forcing |
| PBL | 行星边界层 | Planetary Boundary Layer |
| KPP | K-剖面参数化 | K-Profile Parameterization |

---

## 12. 翻译质量标准 | Translation Quality Standards

### 术语一致性规则 | Terminology Consistency Rules
1. **严格使用标准译名**：所有专业术语必须使用本词典中的标准译名
2. **保持上下文一致性**：同一术语在不同上下文中应保持译名一致
3. **避免直译**：科学术语应采用学术界公认的译法，避免简单直译
4. **注意学科差异**：同一术语在不同学科中可能有不同译法

### 注释翻译规范 | Comment Translation Guidelines
1. **保持技术准确性**：翻译必须准确传达原意，不改变技术内容
2. **保持格式兼容性**：确保翻译后的注释格式符合Fortran语法要求
3. **简洁明了**：翻译应简洁明了，避免冗长表述
4. **补充必要说明**：对于文化特定的概念，可适当补充说明

### 质量检查清单 | Quality Control Checklist
- [ ] 术语使用是否与词典一致
- [ ] 技术内容是否准确无误
- [ ] 代码格式是否正确
- [ ] 编译是否通过
- [ ] 链接和引用是否正确
- [ ] 术语使用是否前后一致

---

**词典版本 | Dictionary Version**: v1.0
**创建日期 | Creation Date**: 2025-10-28
**最后更新 | Last Updated**: 2025-10-28
**维护者 | Maintainer**: ModelE2.1.2_Lazenca翻译团队

**使用说明 | Usage Notes**:
1. 本词典将根据翻译进展持续更新完善
2. 发现新的术语或有疑问的译法请及时反馈
3. 词典中的注释提供了术语的使用背景和注意事项
4. 翻译时应优先查阅本词典确保术语一致性