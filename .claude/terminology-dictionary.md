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

## 12. 编译和系统配置术语 | Compilation and System Configuration Terminology

### Fortran编译相关 | Fortran Compilation Related
| English | 中文 | 注释 |
|---------|------|------|
| Namelist | Fortran名录/参数名录 | Fortran语言中用于参数输入的特殊格式，保留Namelist并附中文注释 |
| Preprocessor Options | 预处理选项 | 编译前的代码处理选项，通常以#开头 |
| Object modules | 对象模块 | 编译生成的目标文件模块 |
| Components | 组件库 | 模型中可复用的功能组件集合 |

### 并行计算术语 | Parallel Computing Terms
| English | 中文 | 注释 |
|---------|------|------|
| MPI进程 | MPI进程 | Message Passing Interface的并行执行单元，优先使用"进程"而非"线程" |
| OpenMPI | OpenMPI | 开源MPI实现的一种，保留英文专名 |
| Intel MPI | Intel MPI | Intel公司的MPI实现，保留英文专名 |
| MPICH | MPICH | MPI的标准实现之一，保留英文专名 |
| MPICH2 | MPICH2 | MPICH的第二代版本，与MPICH基本同义，保留英文专名 |
| MVAPICH2 | MVAPICH2 | 基于InfiniBand的MPI实现，保留英文专名 |
| SCALI | SCALI | 并行计算通信库，保留英文专名 |
| mpt | mpt | MPI并行传输工具，保留英文专名 |

### 系统配置术语 | System Configuration Terms
| English | 中文 | 注释 |
|---------|------|------|
| MacPorts | MacPorts | macOS系统的包管理器，保留英文专名 |
| devtoolset-6 | devtoolset-6 | CentOS开发工具集第6版，保留英文专名 |
| module load | 模块加载命令 | Linux模块系统命令，保留英文不翻译 |
| SCL | 软件集合 | Software Collections，软件版本管理工具，保留英文缩写 |
| scl enable | SCL启用命令 | 启用特定软件集合版本的命令，保留英文不翻译 |
| QSUB_STRING | 作业提交模板字符串 | 用于批量作业系统提交的命令模板，保留英文不翻译 |
| ESMF | 地球系统建模框架 | Earth System Modeling Framework的缩写，保留简称+中文注释 |
| checkpoint file | 检查点文件 | 保存模型计算状态的文件，用于重启 |
| restart file | 重启文件 | 从检查点恢复计算的文件 |

### 模型配置参数 | Model Configuration Parameters
| English | 中文 | 注释 |
|---------|------|------|
| &INPUTZ | 重启与计时参数名录节 | 控制重启和时间的参数节名称，保留原名并中文解释 |
| master_yr | 主控制年份 | 模型运行的主控年份参数，保留参数名+中文解释 |
| ghg_yr | 温室气体年份 | 温室气体浓度参考年份参数 |
| volc_yr | 火山年份 | 火山气溶胶参考年份参数 |
| *_yr | 各类年份参数 | 各种参考年份参数的通用表示模式 |
| transient simulation | 瞬态模拟 | 从起始年份到结束年份的时间变化模拟 |
| JYEAR | 当前模拟年份 | 模型代码中访问当前模拟年份的变量 |
| *_day | 各类天数参数 | 各种天数相关参数的通用表示模式 |
| variable_orb_par | 可变轨道参数 | 控制地球轨道参数变化的开关 |
| orb_par_year_bp | 轨道参数距今年份 | 轨道参数的参考年份（距今年份） |

---

## 13. 翻译质量标准 | Translation Quality Standards

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

## 14. 第6批次新增术语 | Batch 6 New Terminology

### 平流层物理术语 | Stratospheric Physics Terms
| English | 中文 | 注释 |
|---------|------|------|
| stratospheric drag | 平流层曳力 | 平流层中大尺度波动对平均流的阻力 |
| Rayleigh damping | 瑞利阻尼 | 一种简化的波动阻尼参数化方案 |
| gravity-wave drag | 重力波曳力 | 重力波破碎对平均流的动量 deposition |
| moist convection | 湿润对流 | 包含凝结相变的对流过程（与"湿对流"统一） |
| mountain waves | 地形波 | 山地激发的重力波 |
| shear | 剪切 | 流速梯度的动力学效应 |
| deformation | 变形 | 流体元的形变 |
| wave breaking | 波破碎 | 重力波振幅过大导致的湍流混合 |
| STRATDYN | 平流层动力学模块 | 计算平流层重力和波曳力的模块名 |

### 海冰动力学术语 | Sea Ice Dynamics Terms
| English | 中文 | 注释 |
|---------|------|------|
| ice advection | 海冰平流 | 海冰的平流输送过程 |
| atmosphere-ice momentum stress | 大气-冰动量应力 | 大气作用在海冰上的动量通量 |
| ice-ocean momentum stress | 冰-海洋动量应力 | 海冰作用在海洋上的动量通量 |
| sea surface gradient | 海表梯度 | 海表高度或性质的空间变化率 |
| internal ice pressures | 内部冰压力 | 海冰内部的应力状态 |
| rheology | 流变学 | 研究材料流动和变形的科学 |
| Flato-Hibler viscous-plastic rheology | Flato-Hibler粘-塑性流变学 | 一种常用的海冰流变学参数化方案 |
| surface type fractions | 地表类型分数 | 网格单元内不同地表类型（冰、水、陆）的占比 |
| surface flux calculation | 地表通量计算 | 地表面能量、动量、物质通量的计算 |
| ice velocities | 冰速度 | 海冰运动速度 |
| ice mass fluxes | 冰质量通量 | 海冰质量输送通量 |
| fixed SST | 固定海表温度 | 海表温度不随时间变化的边界条件 |
| ice and energy convergences | 冰和能量辐合 | 海冰平流导致的质量和能量汇聚 |
| DYNSI | 海冰动力学初始化模块 | 计算冰速度和应力的模块名 |
| ADVSI | 海冰平流模块 | 海冰平流输送计算的模块名 |
| spin-up | spin-up/预平衡运行 | 模型从初始状态调整到平衡态的过程（保留英文） |

### 海洋强迫术语 | Ocean Forcing Terms
| English | 中文 | 注释 |
|---------|------|------|
| imposed sea surface conditions | 强迫海面条件 | 从外部数据 prescribed的海表条件 |
| fixed (annually repeating) climatology | 固定（年度循环）气候态 | 重复每年的平均季节循环 |
| transient (monthly varying) realisation | 瞬变（月变化）实现 | 随时间变化的真实数据集 |
| monthly means | 月均值 | 每月的平均值 |
| end of month values | 月末值 | 每月最后时刻的值 |
| quadratic approximation | 二次近似 | 使用二次多项式插值的方法 |
| interpolate | 插值 | 估计数据点之间值的方法 |
| sea ice concentration | 海冰密集度 | 网格单元中海冰覆盖的分数 |
| sea ice thickness | 海冰厚度 | 海冰的厚度 |
| local scaling | 局地缩放 | 基于局部关系的调整方法 |
| coupled model simulation | 耦合模型模拟 | 多个组件模型相互作用的模拟 |
| ZSI file | ZSI文件 | 海冰厚度输入文件（Zonal Sea Ice） |

### 水预算术语 | Water Budget Terms
| English | 中文 | 注释 |
|---------|------|------|
| water budget | 水预算 | 系统中水质量的收支平衡 |
| water reservoirs | 水体储库 | 储存水分的组成部分（水库易误解） |
| atmosphere grid | 大气网格 | 大气模型的离散化网格 |
| ocean grid | 海洋网格 | 海洋模型的离散化网格 |
| prognostic variables | 预报变量 | 模型预测的状态变量（已收录） |
| salt water mass | 咸水质量 | 含盐水的质量 |
| subroutines | 子程序 | Fortran中执行特定任务的程序单元 |
| flux array | 通量数组 | 临时存储物质通量的数组 |
| dew | 露 | 水汽凝结的液态水 |
| evaporation | 蒸发 | 液态水转化为气态水的过程（已收录） |
| mass balance | 质量平衡 | 系统输入输出质量的守恒关系 |
| AtmosQ | 大气水质量 | 大气柱中的总水质量 |
| Clouds | 云水质量 | 云中的液态水质量 |
| LandIce | 陆冰质量 | 陆地冰盖的质量 |
| Ground | 地下水质量 | 土壤中的液态水质量 |
| LakeIce | 湖冰质量 | 湖泊冰的质量 |
| LiqLake | 湖泊液态水质量 | 湖泊中的液态水质量 |
| SeaIce | 海冰质量 | 海冰的质量 |
| LiqOcen | 海洋液态水质量 | 海洋中的液态水质量 |
| MELTI | 融冰通量 | 冰融化产生的液态水通量 |
| PREC | 降水通量 | 降水过程的水通量 |
| RUNPSI | 海冰径流通量 | 从海冰表面流走的径流通量 |
| RUNOLI | 陆冰径流通量 | 从陆冰表面流走的径流通量 |
| RUNOE | 地下径流通量 | 从土壤流走的径流通量 |
| EVAPOR | 蒸发通量 | 蒸发过程的水通量 |

### 水文循环术语 | Hydrologic Cycle Terms
| English | 中文 | 注释 |
|---------|------|------|
| hydrologic cycle | 水文循环 | 水在地球各圈层中的循环过程（已收录） |
| water reservoirs | 水体储库 | 储存水分的组成部分（避免"水库"歧义） |
| cloud liquid water | 云液态水 | 云中液态水滴 |
| precipitation | 降水 | 大液态水或固态水从大气降落到地面（已收录） |
| sea ice | 海冰 | 海洋中冻结的冰（已收录） |
| ground water | 地下水 | 土壤和岩石孔隙中的水 |
| glaciers | 冰川 | 大陆上长期存在的冰体 |
| in air and in water tracers | 空气中和水中的示踪物 | 分别存在于大气和相水中的示踪物 |
| precip | 降水 | 简写形式的降水（已收录） |
| soluble gases | 可溶性气体 | 能溶于水的气体 |
| water tracers | 水示踪物 | 用于追踪水运动的示踪物 |
| isotopes | 同位素 | 相同元素但中子数不同的原子 |
| age | 年龄 | 示踪物或水体的时间属性 |
| source | 来源 | 示踪物的来源地或来源过程 |

---

**词典版本 | Dictionary Version**: v1.4 → v1.5
**创建日期 | Creation Date**: 2025-10-28
**最后更新 | Last Updated**: 2026-02-05
**更新内容 | Update Notes**:
- v1.1添加12个编译和系统配置相关术语
- v1.2基于Codex审查结果添加MacPorts、module load、scl enable等5个系统配置术语
- v1.3添加MPICH2术语以确保文档与词典一致性
- v1.4为Day 2-3任务添加transient simulation、JYEAR等关键参数术语
- **v1.5为第6批次添加约65个新术语**，涵盖平流层物理、海冰动力学、海洋强迫、水预算、水文循环等领域
**维护者 | Maintainer**: ModelE2.1.2_Lazenca翻译团队

**使用说明 | Usage Notes**:
1. 本词典将根据翻译进展持续更新完善
2. 发现新的术语或有疑问的译法请及时反馈
3. 词典中的注释提供了术语的使用背景和注意事项
4. 翻译时应优先查阅本词典确保术语一致性