# Using GISS ModelE in single-column mode (master branch only) / 在单列模式下使用GISS ModelE（仅限master分支）

Source code files dedicated to single-column model (SCM) are as follows:
单列模型（SCM）专用源代码文件如下：

-- SCM_COM.F90: common variables for single-column model simulations
-- SCM_COM.F90：单列模型模拟的公共变量

-- SCM.F90: code for reading and processing single-column model input data
-- SCM.F90：用于读取和处理单列模型输入数据的代码

-- ATMDYN_SCM{,_EXT}.f: code for replacing large-scale dynamics with forcing terms
-- ATMDYN_SCM{,_EXT}.f：用强迫项替代大尺度动力学的代码

It is possible to run ModelE in single-column model mode with several options for initialization and forcing.
ModelE可以以单列模型模式运行，并提供多种初始化和强迫选项。

Current options handle atmosphere-only runs, with prescribed surface conditions and large-scale tendencies specified in the run deck.
当前选项处理仅大气运行，并在运行配置中指定地表条件和大尺度趋势。

Set preprocessor option #define SCM.
设置预处理器选项 #define SCM。

Include object modules SCM_COM, SCM, ATMDYN_SCM, and ATMDYN_SCM_EXT prior to CLOUDS_COM.
在CLOUDS_COM之前包含对象模块 SCM_COM、SCM、ATMDYN_SCM 和 ATMDYN_SCM_EXT。

User-supplied input files may currently include the following:
用户提供的输入文件当前可包括以下内容：

-- SCM_NML: namelist containing all input variable names and unit conversions (required)
-- SCM_NML：包含所有输入变量名和单位转换的Fortran名录（必需）

-- SCM_PS: surface pressure (required)
-- SCM_PS：地表气压（必需）

-- SCM_TEMP or SCM_THETA: atmospheric temperature profile (required)
-- SCM_TEMP 或 SCM_THETA：大气温度廓线（必需）

-- SCM_WVMR: water vapor mixing ratio profile (required)
-- SCM_WVMR：水汽混合比廓线（必需）

-- SCM_TSKIN: surface skin temperature
-- SCM_TSKIN：地表皮肤温度

-- SCM_SFLUX: surface sensible and latent heat fluxes
-- SCM_SFLUX：地表感热和潜热通量

-- SCM_WIND: horizontal wind profiles
-- SCM_WIND：水平风廓线

-- SCM_GEO: horizontal geostrophic wind profiles
-- SCM_GEO：水平地转风廓线

-- SCM_W or SCM_OMEGA: large-scale vertical wind or pressure tendency profiles
-- SCM_W 或 SCM_OMEGA：大尺度垂直风或气压倾向廓线

-- SCM_QRAD: radiative heating rate profiles
-- SCM_QRAD：辐射加热率廓线

-- SCM_LS_V: large-scale heat and moisture vertical flux divergence profiles
-- SCM_LS_V：大尺度热量和水汽垂直通量散度廓线

-- SCM_LS_H: large-scale heat and moisture horizontal flux divergence profiles
-- SCM_LS_H：大尺度热量和水汽水平通量散度廓线

-- SCM_FNUDGE: thermodynamic nudging strength profile
-- SCM_FNUDGE：热力学松弛强度廓线

Each netCDF input file must contain UTC "year", "month", "day", and "hour" variables as integer time series with dimension "nt".
每个netCDF输入文件必须包含UTC "year"、"month"、"day" 和 "hour" 变量，作为维度 "nt" 的整数时间序列。

If floating point time series (such as surface pressure) contain only one time, the value will be fixed for all simulation times.
如果浮点时间序列（如地表气压）只包含一个时间，该值将在所有模拟时间内固定。

Input files containing a profile variable must contain a pressure grid as a floating point variable "lev" in units of hPa or mb with dimension "lev".
包含廓线变量的输入文件必须包含气压网格，作为单位为 hPa 或 mb 的浮点变量 "lev"，维度为 "lev"。

For each profile variable, the pressure grid must be fixed in time if more than one time is provided, but each variable may be on its own pressure grid.
对于每个廓线变量，如果提供多个时间，气压网格必须在时间上固定，但每个变量可以在其自己的气压网格上。

Profile variables can be combined in a single input file if they share the same pressure grid.
如果廓线变量共享相同的气压网格，可以在一个输入文件中组合。

Run-time parameters include the following:
运行时参数包括以下内容：

-- SCM_lon: location longitude (required)
-- SCM_lon：位置经度（必需）

-- SCM_lat: location latitude (required)
-- SCM_lat：位置纬度（必需）

-- SCM_area: nominal grid box area for calculation of extrinsic mass fluxes (required)
-- SCM_area：用于计算外源质量通量的名义网格盒面积（必需）

-- SCM_sfc: 1=land, 2=ocean
-- SCM_sfc：1=陆地，2=海洋

-- SCM_ustar: surface friction velocity
-- SCM_ustar：地表摩擦速度

-- SCM_z0m: surface roughness height
-- SCM_z0m：地表粗糙高度

-- SCM_alb: surface mid-visible albedo
-- SCM_alb：地表可见光波段反照率

-- SCM_BeersLaw: Beer's law coefficients for radiative flux divergence
-- SCM_BeersLaw：辐射通量散度的比尔定律系数

-- SCM_tau: nudging time constant for temperature and moisture profiles
-- SCM_tau：温度和湿度廓线的松弛时间常数

The shell script modelE/exec/extract_scm.sh uses SCM_lat and SCM_lon to extract ancillary input data for a given SCM run location.
Shell脚本 modelE/exec/extract_scm.sh 使用 SCM_lat 和 SCM_lon 为给定SCM运行位置提取辅助输入数据。

Run-time success reading and processing individual input files is reported to .PRT within the output run directory.
运行时读取和处理各个输入文件的成功情况报告到输出运行目录内的 .PRT 文件。

Diagnostics are obtained using the GCM-native subdaily diagnostics system.
诊断输出使用GCM原生的亚日诊断系统获得。

Diagnostics made available using this system are opt-in, with variable names specified in SUBDD{,1,2,3,etc} strings within the run deck.
此系统提供的诊断输出是可选启用的，变量名在运行配置的 SUBDD{,1,2,3,etc} 字符串中指定。

Existing run-deck templates include the following:
现有的运行配置模板包括以下内容：

-- SCM.R: DOE ARM Southern Great Plains case with VARANAL data (www.arm.gov)
-- SCM.R：使用VARANAL数据的DOE ARM南大平原案例（www.arm.gov）

-- SCM_BOMEX.R: BOMEX case study described by Siebesma et al. (2003)
-- SCM_BOMEX.R：Siebesma等人（2003）描述的BOMEX案例研究

-- SCM_DYCOMS-II-RF02.R: DYCOMS case study described by Ackerman et al. (2009)
-- SCM_DYCOMS-II-RF02.R：Ackerman等人（2009）描述的DYCOMS案例研究

**Document End / 文档结束**
