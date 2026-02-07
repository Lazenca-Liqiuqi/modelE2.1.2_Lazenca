# ModelE Version Changes / ModelE 版本变更历史

本文档记录ModelE从早期版本到AR5版本的主要变更历史。

---

## Changes from modelE (AR4) to modelE (AR5) / 从modelE (AR4)到modelE (AR5)的变更

- Higher resolution versions available (2x2.5)
  提供更高分辨率版本（2x2.5度）

- Cubed Sphere dynamics and grid (C90) resolution
  立方体球面动力学和网格（C90分辨率）

- Multiple changes to cloud schemes
  云方案的多次改进

- Incorporation of Menon et al aerosol/cloud microphysics
  整合Menon等人的气溶胶/云微物理方案

- Full atmosphere gas phase chemistry
  完整的大气气相化学机制

- Ocean biology and full carbon cycle
  海洋生物和完整碳循环

- Coupler layer for different ocean grids
  支持不同海洋网格的耦合层

- Fuller diagnostic output
  更完整的诊断输出

> （注：这些是差异的非常精简的摘要）

---

## Changes from modelE-2-3-4+ to modelE1 (or 3.0) (AR4) / 从modelE-2-3-4+到modelE1（或3.0）(AR4)的变更

- big expansion of tracer coding
  示踪物编码的大规模扩展

- relative humidity sensitivity of aerosol optical thickness
  气溶胶光学厚度的相对湿度敏感性

- new cloud micro-physics
  新的云微物理方案

- better separation of convective and stratiform cloud
  更好地分离对流云和层状云

- more interactions between tracer fields and radiation
  示踪物场与辐射之间更多相互作用

- NUDGING facility for trying to reproduce field experiments
  用于尝试重现野外实验的松弛（nudging）功能

- full use of atmospheric turbulence
  全面使用大气湍流方案

- improved historical fields for ozone, aerosols
  改进的臭氧、气溶胶历史场

- new conductance scheme for evapo-transpiration
  蒸散发的新导度方案

- extended sub-daily diagnostics
  扩展的亚日诊断输出

- new diag Hdirun for time series of all fields over last month for selected grid boxes
  新的diag Hdirun，用于所选网格盒上月所有字段的时间序列

- option to run with smaller physics time step
  使用更小物理时间步长的运行选项

---

## Changes from modelE-2-3 to modelE-2-3-4+ / 从modelE-2-3到modelE-2-3-4+的变更

- new conductance scheme option for land surface
  陆面的新导度方案选项

- preliminary incorporation of wet and dry deposition for gases and aerosols
  初步整合气体和气溶胶的湿沉降和干沉降

- angular momentum conservation for UV filter and GW drag
  UV滤波和重力波拖曳的角动量守恒

- better modularisation of snow model
  雪模型的更好模块化

- improved option for sea ice albedo (Hansen)
  改进的海冰反照率选项（Hansen方案）

- minor bug fixes and diagnostic improvements
  小型bug修复和诊断改进

---

## Major changes from version modelE-2-1 to modelE-2-3 / 从modelE-2-1到modelE-2-3的主要变更

- Glacial melt (icebergs) now available as input into ocean
  冰川融水（冰山）现在可作为输入进入海洋

- time varying crop fraction possible
  可能实现随时间变化的作物比例

- monthly files for the CH4 oxidation into stratosphere
  CH4氧化进入平流层的月度文件

- Further extensions to sub-daily diagnostics to cover all geopotential heights, temperatures and velocities, and tropopause height
  进一步扩展亚日诊断以覆盖所有位势高度、温度和风速，以及对流层顶高度

- New scoring statistic for comparsion to observations
  用于与观测比较的新评分统计

- Tested versions at 2x2.5 and 8x10 horizontal resolutions
  在2x2.5和8x10水平分辨率下测试的版本

- More options in stratospheric drag formulation.
  平流层拖曳公式中的更多选项。

- snowice formation now an option
  雪冰形成现在是一个选项

- zenith angle dependence for all snow/ice albedos
  所有雪/冰反照率的天顶角依赖性

- New ISCCP cloud optical depth/height histograms diagnostics.
  新的ISCCP云光学厚度/高度直方图诊断。

- water tracer code in soils
  土壤中的水示踪物代码

- orbital parameter calculations based on paleo-year
  基于古年份的轨道参数计算

- surface velocities (ice, ocean) no used as input into surface boundary conditions.
  表面速度（冰、海洋）现在用作表面边界条件的输入。

---

## Major changes from version modelE-2-0-1 to modelE-2-1 / 从modelE-2-0-1到modelE-2-1的主要变更

- Qflux model now has option to include ice advection.
  Qflux模型现在有包含冰平流的选项。

- new options for controling cloud optical thickness
  控制云光学厚度的新选项

- Energy conservation now guaranteed
  现在保证能量守恒

- New physics for deciding on phase of precip (i.e. how quickly super-cooled precip turns to ice)
  决定降水相态的新物理学（即过冷降水转变为冰的速度）

- New coding for ground hydrology
  地面水文学的新编码

- Small corrections for q-flux/seaice modules
  q-flux/海冰模块的小修正

- Improved conservation diagnostics (including new text demonstrating conservation properties "conserv.txt")
  改进的守恒诊断（包括展示守恒特性的新文本"conserv.txt"）

- Extension to sub-daily diagnostics to include cloud cover (low, mid, high) and relative humidity values.
  扩展亚日诊断以包括云量（低、中、高）和相对湿度值。

- Enhanced diagnostics of cloud radiative properties
  增强的云辐射特性诊断

- Code is now compatible with PGI (Portland Group) compiler.
  代码现在与PGI（Portland Group）编译器兼容。

---

## Major changes from version modelE-2-0 to modelE-2-0-1 / 从modelE-2-0到modelE-2-0-1的主要变更

- Minor fixes to almost all components
  几乎所有组件的小型修复

- New options for snow-age definitions, Sea-ice and SST cycling.
  雪龄定义、海冰和SST循环的新选项。

- netcdf output now fully functional
  netcdf输出现在完全可用

- Changes to makefiles for compilation using Linux compilers (Absoft + Lahey/Fujitsu)
  使用Linux编译器（Absoft + Lahey/Fujitsu）编译的makefile变更

---

## Major changes from version modelE-1-3-3 to modelE-2-0 / 从modelE-1-3-3到modelE-2-0的主要变更

### Atmospheric Model / 大气模型

- Advection of Q now done outside dynamics loop
  Q的平流现在在动力学循环外完成

- New sea ice albedo scheme (pudlling and snowage replaced with prognostic melt-pond fraction and wet/dry snow flag).
  新的海冰反照率方案（融池和雪龄被预报性融池比例和湿/干雪标志取代）

- solar radiation penetration through sea ice now wavelength dependent
  太阳辐射穿透海冰现在依赖于波长

- the basal fluxes between the ice and ocean are calculated using a new turbulence scheme. New routines UNDERICE, iceocean, icelake.
  冰和海洋之间的基底通量使用新的湍流方案计算。新例程UNDERICE、iceocean、icelake。

- parallelisation directives for atmospheric model
  大气模型的并行化指令

- changes to boundary layer cloud specifications
  边界层云规范的变更

- improvements to turbulence calculations (including a fix of a bug that caused problems when the first layer was too thin)
  湍流计算的改进（包括修复当第一层太薄时引起问题的bug）

- fix for mass fluxes over topography to prevent unrealistic precipitation hotspots
  修复地形上的质量通量以防止不切实际的降水热点

- Multiple vertical resolutions available
  提供多种垂直分辨率

- new interface for radiation to allow more control of greenhouse gases, aerosols etc. from rundeck.
  辐射的新接口，允许从rundeck更多地控制温室气体、气溶胶等。

- Adjustable input of CH4 related stratospheric water vapour
  可调节的CH4相关平流层水汽输入

- Numerous parameters for the gravity wave drag adjustable from the rundeck
  可从rundeck调节的重力波拖曳众多参数

### Coupled Model / 耦合模型

- Gary's ocean model now fully coupled (plug and play option)
  Gary的海洋模型现已完全耦合（即插即用选项）

- Ice dynamics now a completely separate module
  冰动力学现在是一个完全独立的模块

- Ocean heat transport diagnostic in printout
  打印输出中的海洋热量输送诊断

- much more extensive ocean diagnostics
  更广泛的海洋诊断

### Tracer code / 示踪物代码

- tracer code for air mass and water mass tracers (uses preprocessing directives set from the run deck)
  空气质量和水质量示踪物的示踪物代码（使用运行配置设置的预处理指令）

- wet/dry deposition code for general tracers (aerosols, particles, water and soluble gases)
  通用示踪物（气溶胶、颗粒物、水和可溶性气体）的湿/干沉降代码

- multiple example tracers pre-coded
  多个预编码的示例示踪物

### Diagnostics / 诊断输出
- Numerous errors in diagnostic printout fixed
  修复诊断打印输出中的众多错误

- Re-arrangement of budget pages to provide more relevant info.
  重新排列预算页面以提供更相关的信息。

- Conservation diagnostics for AM and KE actually add up.
  AM和KE的守恒诊断实际上加起来了。

- Configurable daily and sub-daily diagnsotic output for selected quantities
  所选量的可配置日和亚日诊断输出

### Run Environment / 运行环境

- .modelErc file in home directory to enable a configuration to set up a local distribution on any machine
  主目录中的.modelErc文件，使配置能够在任何机器上设置本地分发

- automatic compilation of online documentation for any particular configuration.
  任何特定配置的在线文档自动编译。

- new 'lock' file method for preventing un-intended writing over of files.
  新的'锁'文件方法，防止意外覆盖文件。

- MUST USE COMMANDS 'runE' and 'sswE' to start and stop model
  必须使用命令'runE'和'sswE'来启动和停止模型

- automatic re-starting with smaller timestep for some crashes (set from initial rundeck)
  某些崩溃时使用较小时间步长自动重新启动（从初始rundeck设置）

---

## Major Changes from Model II' to modelE-1-3-3 / 从Model II'到modelE-1-3-3的主要变更

### Variable name changes/re-definitions / 变量名变更/重新定义

- FDATA replaced with FLAND/FOCEAN/FLICE/FLAKE/FEARTH
  FDATA被FLAND/FOCEAN/FLICE/FLAKE/FEARTH取代

- GDATA replaced with:
  GDATA被以下取代：
  - SNOWI,HSI (sea ice / 海冰)
  - SNOWE,TEARTH,WEARTH,AIEARTH,SNOAGE (earth / 地球)
  - TLANDI, SNOWLI (land ice / 陆地冰)

- ODATA replaced with: TOCEAN, RSI and MSI (TLAKE over land)
  ODATA被以下取代：TOCEAN、RSI和MSI（陆地上的TLAKE）

- Second order moments are condensed to one array. Whether the quadratic or linear upstream scheme is required now only requires a change in the QUSCOM/QUSDEF modules. Multiple advection routines replaced with one general purpose routine.
  二阶矩被压缩到一个数组中。现在只需要在QUSCOM/QUSDEF模块中更改即可选择二次或线性上游方案。多个平流例程被一个通用例程取代。

- Arrays that are used for column physics only are now written with the column index first (i.e. L,I,J) for performance improvement
  仅用于柱物理的数组现在首先写入列索引（即L,I,J）以提高性能

- Ground temperatures for SURFCE/RADIA and PBL are now saved in the GTEMP array.
  SURFCE/RADIA和PBL的地面温度现在保存在GTEMP数组中。

- parameters for both the model and all sub modules are now saved in a parameter block that is of variable length and self-documenting (replacing JC/RC in the old code).
  模型和所有子模块的参数现在保存在可变长度和自文档的参数块中（取代旧代码中的JC/RC）。

### Structural and Fortran 90 related changes / 结构和Fortran 90相关变更

- Common blocks replaced with physics-related MODULEs
  公共块被与物理相关的MODULE取代

- Model common block (i.e. BB399xyz.COM) now MODEL_COM MODULE
  模型公共块（即BB399xyz.COM）现在是MODEL_COM MODULE

- physical constants all defined in CONSTANT module
  物理常数全部在CONSTANT模块中定义

- Each physical submodule (ie. ice, snow, ocean, land, land ice, clouds,etc.) has it's own fortran MODULE. As far as possible, different modules interact only through fluxes.
  每个物理子模块（即冰、雪、海洋、陆地、陆地冰、云等）都有自己的fortran MODULE。尽可能，不同模块仅通过通量相互作用。

- initialisation of each sub-module is now in init_PHYS (if required)
  每个子模块的初始化现在在init_PHYS中（如果需要）

- daily processes moved into daily_PHYS (if needed)
  日过程移入daily_PHYS（如果需要）

- Many errors in diagnostics and in the seaice/Qflux model corrected
  诊断和海冰/Qflux模型中的许多错误得到纠正

- lakes are seperated from ocean variables/code.
  湖泊与海洋变量/代码分离。

- sea ice now seperated from ocean/lakes code. All fluxes are now passed.
  海冰现在与海洋/湖泊代码分离。所有通量现在都传递。

- Explicit use of B-grid velocity points is now implicit.
  B网格速度点的显式使用现在是隐式的。

### Diagnostics / 诊断输出
- pdE (used to print diagnostics) is now just an alternate entry to the model, and thus cannot be out of date.
  pdE（用于打印诊断）现在只是模型的另一个入口点，因此不会过时。

- diagnostic arrays now addressed by name, not number
  诊断数组现在按名称寻址，而不是按编号

### Input/Output / 输入/输出

- Named files in rundeck instead of unit numbers
  rundeck中的命名文件而不是单元编号

- FILEMANAGER module to allocate unit numbers
  FILEMANAGER模块用于分配单元编号

- input/output decentralized to io_PHYS routines for each PHYS submodule
  输入/输出分散到每个PHYS子模块的io_PHYS例程

### Runtime environment / 运行时环境

- compiling/linking/setup now under control of an automatic makefile process
  编译/链接/设置现在由自动makefile过程控制

- NAMELIST input:
  NAMELIST输入：
  - TAUI/E replaced with YEARI/E,MONTHI/E,DATEI/E,HOURI/E (alt. IHOURE)
    TAUI/E被YEARI/E、MONTHI/E、DATEI/E、HOURI/E（替代IHOURE）取代
  - NDPRNT/NDZERO replaced with NIPRNT and NMONAV
    NDPRNT/NDZERO被NIPRNT和NMONAV取代
  - DT related variables such as NRAD etc, now relate to DTsrc (=1hour)
    DT相关变量如NRAD等，现在与DTsrc相关（=1小时）
  - SIGE setting replaced with PLTOP (pressure at the top of the level) - SIGE is now computed.
    SIGE设置被PLTOP（层顶压力）取代 - SIGE现在计算。
  - U00 replaced with U00wtr and U00ice (separate numbers for ice and water clouds)
    U00被U00wtr和U00ice取代（冰云和水云的独立编号）

- Local parameters are now stored in the parameter database which mainly supplants the NAMELIST input.
  局部参数现在存储在参数数据库中，主要取代NAMELIST输入。

### New physics / 新物理学

- Sea ice over the ocean is now formed at TFO (=-1.8 deg).
  海洋上的海冰现在在TFO（=-1.8度）形成。

- Solar radiation now penetrates into (and through) the sea ice.
  太阳辐射现在穿透（并通过）海冰。

- Sea ice salinity is now a prognostic variable (though not yet fully coupled to the thermodynamics).
  海冰盐度现在是一个预报变量（尽管尚未与热力学完全耦合）。

- lake temperature/ice cover are now predicted using a two layer energy/mass conserving model.
  湖泊温度/冰覆盖现在使用双层能量/质量守恒模型预测。

- Turbulence can now be applied throughtout the atmosphere (ATURB.f).
  湍流现在可应用于整个大气（ATURB.f）。

---

**Document End / 文档结束**

