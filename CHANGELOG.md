# ModelE2.1.2_Lazenca版本变更记录

## 当前版本
- **Version**: ModelE2.1.2_Lazenca v0.0.2 (基于 ModelE 2.1.2)
- **Release Date**: 2025-10-23
- **Developer**: Lazenca
- **Status**: 基于ModelE 2.1.2的个人fork分支，增强文档系统
- **Status**: Personal fork branch based on ModelE v2.1.2 with enhanced documentation system

---

## Version v0.0.2 - Documentation Enhancement (2025-10-23)

### 主要变更 | Key Changes

1. **项目记忆系统建立 | Project Memory System Establishment**
   - 创建完整的项目记忆系统，遵循三组件架构
   - 建立CLAUDE.md、README.md、CHANGELOG.md核心记忆组件
   - Created complete project memory system following three-component architecture
   - Established CLAUDE.md, README.md, CHANGELOG.md core memory components

2. **文档格式现代化 | Documentation Format Modernization**
   - 将传统.txt文档转换为现代Markdown格式
   - 采用段落级中英对照格式，便于国际科研合作
   - Converted legacy .txt documents to modern Markdown format
   - Implemented paragraph-level bilingual format for international research collaboration

3. **技术文档完善 | Technical Documentation Enhancement**
   - 创建全面的架构分析文档(ARCHITECTURE_ANALYSIS.md)
   - 完成项目分析报告(PROJECT_ANALYSIS_REPORT.md)
   - 建立文档索引系统(PROJECT_MEMORY_INDEX.md)
   - Created comprehensive architecture analysis document (ARCHITECTURE_ANALYSIS.md)
   - Completed project analysis report (PROJECT_ANALYSIS_REPORT.md)
   - Established documentation index system (PROJECT_MEMORY_INDEX.md)

4. **文件组织优化 | File Organization Optimization**
   - 根目录保留核心记忆组件，技术文档归档至doc目录
   - 删除4个过时.txt文件，新增9个现代化Markdown文档
   - Root directory maintains core memory components, technical documents archived in doc directory
   - Removed 4 outdated .txt files, added 9 modernized Markdown documents

### 技术改进 | Technical Improvements

- **中英对照格式 | Bilingual Format**: 英语段落+中文翻译，支持连续阅读
- **版本管理 | Version Management**: 建立语义版本控制体系
- **文档标准化 | Documentation Standardization**: 统一格式规范和维护流程
- **Bilingual Format**: English paragraph + Chinese translation, supporting continuous reading
- **Version Management**: Established semantic version control system
- **Documentation Standardization**: Unified format specifications and maintenance processes

---

## Version modelE-3-0 (AR5) - 当前版本

### English Documentation
Changes from modelE (AR4) to modelE (AR5)
=========================================

- Higher resolution versions available (2x2.5)

- Cubed Sphere dynamics and grid (C90) resolution

- Multiple changes to cloud schemes

- Incorporation of Menon et al aerosol/cloud microphysics

- Full atmosphere gas phase chemistry

- Ocean biology and full carbon cycle

- Coupler layer for different ocean grids

- Fuller diagnostic output

(note these are a very condensed summary of the differences).

### 中文文档
从modelE (AR4)到modelE (AR5)的变更
=========================================

- 提供更高分辨率版本（2×2.5度）

- 立方体球面动力学和网格（C90分辨率）

- 云方案的多次改进

- 整合了Menon等人的气溶胶/云微物理方案

- 完整的大气气相化学机制

- 海洋生物和完整碳循环

- 针对不同海洋网格的耦合层

- 更完整的诊断输出

（注意这些只是差异的非常简化的摘要）

---

## Version modelE-3.0 (AR4)

### English Documentation
Changes from modelE-2-3-4+ to modelE1 (or 3.0) (AR4)
====================================================

- big expansion of tracer coding

- relative humidity sensitivity of aerosol optical thickness

- new cloud micro-physics

- better separation of convective and stratiform cloud

- more interactions between tracer fields and radiation

- NUDGING facility for trying to reproduce field experiments

- full use of atmospheric turbulence

- improved historical fields for ozone, aerosols

- new conductance scheme for evapo-transpiration

- extended sub-daily diagnostics

- new diag Hdirun for time series of all fields over last month for
  selected grid boxes

- option to run with smaller physics time step

### 中文文档
从modelE-2-3-4+到modelE1（或3.0）（AR4）的变更
====================================================

- 示踪物代码的大幅扩展

- 气溶胶光学厚度的相对湿度敏感性

- 新的云微物理方案

- 更好的对流云和层状云分离

- 示踪物场与辐射之间更多的相互作用

- NUDGING功能用于尝试重现野外实验

- 充分利用大气湍流

- 改进的臭氧、气溶胶历史场

- 新的蒸腾传导方案

- 扩展的亚日诊断

- 新的诊断Hdirun，用于选定网格盒子上月所有场的时间序列

- 使用更小物理时间步长的选项

---

## Version modelE-2-3-4+

### English Documentation
Changes from modelE-2-3 to modelE-2-3-4+
=======================================

- new conductance scheme option for land surface

- preliminary incorporation of wet and dry deposition for gases and
  aerosols

- angular momentum conservation for UV filter and GW drag

- better modularisation of snow model

- improved option for sea ice albedo (Hansen)

- minor bug fixes and diagnostic improvements

### 中文文档
从modelE-2-3到modelE-2-3-4+的变更
=======================================

- 陆地表面的新传导方案选项

- 气体和气溶胶的干湿沉降的初步整合

- UV滤波器和重力波拖曳的角动量守恒

- 更好的雪模型模块化

- 改进的海冰反照率选项（Hansen方案）

- 小错误修复和诊断改进

---

## Version modelE-2-3

### English Documentation
Major changes from version modelE-2-1 to modelE-2-3
===================================================

- Glacial melt (icebergs) now available as input into ocean

- time varying crop fraction possible

- monthly files for the CH4 oxidation into stratosphere

- Further extensions to sub-daily diagnostics to cover all
  geopotential heights, temperatures and velocities, and tropopause
  height

- New scoring statistic for comparsion to observations

- Tested versions at 2x2.5 and 8x10 horizontal resolutions

- More options in stratospheric drag formulation.

- snowice formation now an option

- zenith angle dependence for all snow/ice albedos

- New ISCCP cloud optical depth/height histograms diagnostics.

- water tracer code in soils

- orbital parameter calculations based on paleo-year

- surface velocities (ice, ocean) no used as input into surface
  boundary conditions.

### 中文文档
从modelE-2-1到modelE-2-3的主要变更
===================================================

- 冰川融化（冰山）现在可作为海洋输入

- 可能的随时间变化的作物比例

- CH4氧化进入平流层的月度文件

- 进一步扩展亚日诊断以覆盖所有位势高度、温度和速度，以及对流层高度

- 用于与观测比较的新评分统计

- 在2×2.5和8×10水平分辨率下测试版本

- 平流层拖曳公式中的更多选项

- 雪冰形成现在是一个选项

- 所有雪/冰反照率的天顶角依赖性

- 新的ISCCP云光学厚度/高度直方图诊断

- 土壤中的水示踪物代码

- 基于古年份的轨道参数计算

- 表面速度（冰、海洋）不用作表面边界条件的输入

---

## Version modelE-2-1

### English Documentation
Major changes from version modelE-2-0-1 to modelE-2-1
=====================================================

- Qflux model now has option to include ice advection.

- new options for controling cloud optical thickness

- Energy conservation now guaranteed

- New physics for deciding on phase of precip (i.e. how quickly
  super-cooled precip turns to ice)

- New coding for ground hydrology

- Small corrections for q-flux/seaice modules

- Improved conservation diagnostics (including new text demonstrating
  conservation properties "conserv.txt")

- Extension to sub-daily diagnostics to include cloud cover (low, mid, high)
  and relative humidity values.

- Enhanced diagnostics of cloud radiative properties

- Code is now compatible with PGI (Portland Group) compiler.

### 中文文档
从modelE-2-0-1到modelE-2-1的主要变更
=====================================================

- Qflux模型现在有包含冰平流的选项

- 控制云光学厚度的新选项

- 现在保证能量守恒

- 决定降水相态的新物理学（即过冷降水转变为冰的速度）

- 地面水文学的新编码

- q-flux/海冰模块的小修正

- 改进的守恒诊断（包括展示守恒属性的新文本"conserv.txt"）

- 扩展亚日诊断以包括云量（低、中、高）和相对湿度值

- 增强的云辐射特性诊断

- 代码现在与PGI（Portland Group）编译器兼容

---

## Version modelE-2-0-1

### English Documentation
Major changes from version modelE-2-0 to modelE-2-0-1
=====================================================

 - Minor fixes to almost all components

 - New options for snow-age definitions, Sea-ice and SST cycling.

 - netcdf output now fully functional

 - Changes to makefiles for compilation using Linux compilers (Absoft
   + Lahey/Fujitsu)

### 中文文档
从modelE-2-0到modelE-2-0-1的主要变更
=====================================================

- 几乎所有组件的小修复

- 雪龄定义、海冰和SST循环的新选项

- netcdf输出现在完全可用

- 使用Linux编译器（Absoft + Lahey/Fujitsu）编译的makefile更改

---

## Version modelE-2-0

### English Documentation
Major changes from version modelE-1-3-3 to modelE-2-0
=====================================================

Atmospheric Model:

 - Advection of Q now done outside dynamics loop

 - New sea ice albedo scheme (pudlling and snowage replaced with
   prognostic melt-pond fraction and wet/dry snow flag).

 - solar radiation penetration through sea ice now wavelength dependent

 - the basal fluxes between the ice and ocean are calculated using a new
   turbulence scheme. New routines UNDERICE, iceocean, icelake.

 - parallelisation directives for atmospheric model

 - changes to boundary layer cloud specifications

 - improvements to turbulence calculations (including a fix of a bug
   that caused problems when the first layer was too thin)

 - fix for mass fluxes over topography to prevent unrealistic
   precipitation hotspots

 - Multiple vertical resolutions available

 - new interface for radiation to allow more control of greenhouse
   gases, aerosols etc. from rundeck.

 - Adjustable input of CH4 related stratospheric water vapour

 - Numerous parameters for the gravity wave drag  adjustable from the rundeck

Coupled Model:

 - Gary's ocean model now fully coupled (plug and play option)

 - Ice dynamics now a completely separate module

 - Ocean heat transport diagnostic in printout

 - much more extensive ocean diagnostics

Tracer code:

 - tracer code for air mass and water mass tracers (uses preprocessing
   directives set from the run deck)

 - wet/dry deposition code for general tracers (aerosols, particles,
   water and soluble gases)

 - multiple example tracers pre-coded

Diagnostics:

 - Numerous errors in diagnostic printout fixed

 - Re-arrangement of budget pages to provide more relevant info.

 - Conservation diagnostics for AM and KE actually add up.

 - Configurable daily and sub-daily diagnsotic output for selected quantities

Run Envrionment:

 - .modelErc file in home directory to enable a configuration to set
   up a local distribution on any machine

 - automatic compilation of online documentation for any particular
   configuration.

 - new 'lock' file method for preventing un-intended writing over of files.

 - MUST USE COMMANDS 'runE' and 'sswE' to start and stop model

 - automatic re-starting with smaller timestep for some crashes (set from
   initial rundeck)

### 中文文档
从modelE-1-3-3到modelE-2-0的主要变更
=====================================================

大气模型：

- Q的平流现在在动力学循环之外完成

- 新的海冰反照率方案（水坑和雪龄被预测性融池比例和湿/干雪标志取代）

- 太阳辐射穿透海冰现在依赖于波长

- 冰和海洋之间的基底通量使用新的湍流方案计算。新程序UNDERICE、iceocean、icelake

- 大气模型的并行化指令

- 边界层云规范的更改

- 湍流计算的改进（包括修复第一层太薄时引起问题的错误）

- 修复地形上的质量通量以防止不现实的降水热点

- 可用的多重垂直分辨率

- 辐射的新界面，允许从rundeck更多地控制温室气体、气溶胶等

- CH4相关平流层水汽的可调输入

- 可从rundeck调整的重力波拖曳的众多参数

耦合模型：

- Gary的海洋模型现在完全耦合（即插即用选项）

- 冰动力学现在是一个完全独立的模块

- 打印输出中的海洋热量输送诊断

- 更广泛的海洋诊断

示踪物代码：

- 空气质量和水质量示踪物的示踪物代码（使用从运行牌组设置的预处理指令）

- 一般示踪物（气溶胶、颗粒物、水和可溶性气体）的干湿沉降代码

- 多个预编码的示例示踪物

诊断：

- 修复诊断打印输出中的众多错误

- 重新安排预算页面以提供更相关的信息

- AM和KE的守恒诊断确实相加

- 所选数量的可配置日和亚日诊断输出

运行环境：

- 主目录中的.modelErc文件，使配置能够在任何机器上设置本地分发

- 任何特定配置的在线文档的自动编译

- 新的'锁'文件方法，防止意外覆盖文件

- 必须使用命令'runE'和'sswE'来启动和停止模型

- 对于某些崩溃，使用更小时间步长的自动重启（从初始rundeck设置）

---

## Historical Version Model II' to modelE-1-3-3

### English Documentation
Major Changes from Model II' to modelE-1-3-3
============================================

Variable name changes/re-definitions:

 - FDATA replaced with FLAND/FOCEAN/FLICE/FLAKE/FEARTH

 - GDATA replaced with:
   SNOWI,HSI  (sea ice)
   SNOWE,TEARTH,WEARTH,AIEARTH,SNOAGE (earth)
   TLANDI, SNOWLI (land ice)

 - ODATA replaced with: TOCEAN, RSI and MSI (TLAKE over land)

 - Second order moments are condensed to one array. Whether the
   quadratic or linear upstream scheme is required now only requires
   a change in the QUSCOM/QUSDEF modules. Multiple advection routines
   replaced with one general purpose routine.

 - Arrays that are used for column physics only are now written with
   the column index first (i.e. L,I,J) for performance improvement

 - Ground temperatures for SURFCE/RADIA and PBL are now saved in the
   GTEMP array.

 - parameters for both the model and all sub modules are now saved in a
   parameter block that is of variable length and self-documenting
   (replacing JC/RC in the old code).

Structural and Fortran 90 related changes

 - Common blocks replaced with physics-related MODULEs

 - Model common block (i.e. BB399xyz.COM) now MODEL_COM MODULE

 - physical constants all defined in CONSTANT module

 - Each physical submodule (ie. ice, snow, ocean, land, land ice,
   clouds,etc.) has it's own fortran MODULE. As far as possible,
   different modules interact only through fluxes.

 - initialisation of each sub-module is now in init_PHYS (if required)

 - daily processes moved into daily_PHYS (if needed)

 - Many errors in diagnostics and in the seaice/Qflux model corrected

 - lakes are seperated from ocean variables/code.

 - sea ice now seperated from ocean/lakes code. All fluxes are now passed.

 - Explicit use of B-grid velocity points is now implicit.

Diagnostics

 - pdE (used to print diagnostics) is now just an alternate entry to
   the model, and thus cannot be out of date.

 - diagnostic arrays now addressed by name, not number

Input/Output

 - Named files in rundeck instead of unit numbers

 - FILEMANAGER module to allocate unit numbers

 - input/output decentralized to io_PHYS routines for each PHYS submodule

Runtime environment

 - compiling/linking/setup now under control of an automatic makefile process

 - NAMELIST input:
     TAUI/E replaced with YEARI/E,MONTHI/E,DATEI/E,HOURI/E (alt. IHOURE)
     NDPRNT/NDZERO replaced with NIPRNT and NMONAV
     DT related variables such as NRAD etc, now relate to DTsrc
     (=1hour)
     SIGE setting replaced with PLTOP (pressure at the top of
     the level) - SIGE is now computed.
     U00 replaced with U00wtr and U00ice (separate numbers for
     ice and water clouds)

 - Local parameters are now stored in the parameter database which mainly
   supplants the NAMELIST input.

New physics

 - Sea ice over the ocean is now formed at TFO (=-1.8 deg).

 - Solar radiation now penetrates into (and through) the sea ice.

 - Sea ice salinity is now a prognostic variable (though not yet
   fully coupled to the thermodynamics).

 - lake temperature/ice cover are now predicted using a two layer
   energy/mass conserving model.

 - Turbulence can now be applied throughtout the atmosphere (ATURB.f).

### 中文文档
从Model II'到modelE-1-3-3的主要变更
============================================

变量名更改/重新定义：

- FDATA被FLAND/FOCEAN/FLICE/FLAKE/FEARTH取代

- GDATA被替换为：
  SNOWI,HSI  (海冰)
  SNOWE,TEARTH,WEARTH,AIEARTH,SNOAGE (地球)
  TLANDI, SNOWLI (陆地冰)

- ODATA被替换为：TOCEAN, RSI和MSI（陆地上的TLAKE）

- 二阶矩被压缩到一个数组中。现在只需要更改QUSCOM/QUSDEF模块就可以确定需要二次还是线性上游方案。多个平流程序被一个通用程序取代。

- 仅用于柱物理的数组现在首先写入列索引（即L,I,J）以提高性能

- SURFCE/RADIA和PBL的地面温度现在保存在GTEMP数组中。

- 模型和所有子模块的参数现在保存在可变长度和自记录的参数块中（替换旧代码中的JC/RC）。

结构和Fortran 90相关更改

- 公共块被与物理相关的MODULES取代

- 模型公共块（即BB399xyz.COM）现在是MODEL_COM MODULE

- 物理常数都在CONSTANT模块中定义

- 每个物理子模块（即冰、雪、海洋、陆地、陆地冰、云等）都有自己的fortran MODULE。尽可能不同模块仅通过通量相互作用。

- 每个子模块的初始化现在在init_PHYS中（如果需要）

- 日过程移动到daily_PHYS中（如果需要）

- 诊断和海冰/Q通量模型中的许多错误得到纠正

- 湖泊与海洋变量/代码分离。

- 海冰现在与海洋/湖泊代码分离。所有通量现在都传递。

- B网格速度点的显式使用现在是隐式的。

诊断

- pdE（用于打印诊断）现在只是模型的另一个入口点，因此不会过时。

- 诊断数组现在按名称而不是数字寻址

输入/输出

- rundeck中的命名文件而不是单元号

- 用于分配单元号的FILEMANAGER模块

- 输入输出分散到每个PHYS子模块的io_PHYS程序

运行环境

- 编译/链接/设置现在在自动makefile过程的控制下

- NAMELIST输入：
    TAUI/E被YEARI/E,MONTHI/E,DATEI/E,HOURI/E取代（备选IHOURE）
    NDPRNT/NDZERO被NIPRNT和NMONAV取代
    DT相关变量如NRAD等，现在与DTsrc相关（=1小时）
    SIGE设置被PLTOP（层顶部的压力）取代 - SIGE现在计算。
    U00被U00wtr和U00ice取代（冰云和水云的单独数字）

- 局部参数现在存储在参数数据库中，主要取代NAMELIST输入。

新物理学

- 海洋上的海冰现在在TFO（=-1.8度）形成。

- 太阳辐射现在穿透（并通过）海冰。

- 海冰盐度现在是预测变量（虽然尚未完全与热力学耦合）。

- 湖泊温度/冰覆盖现在使用两层能量/质量守恒模型预测。

- 湍流现在可以应用于整个大气层（ATURB.f）。

---

*本变更记录持续更新中，记录了ModelE从早期版本到当前v2.1.2/3.0版本的所有重要变更。*