# Vegetation Model User Guide
# 植被模型用户指南

**This document describes rundeck specifications required to run different configurations of the Ent Terrestrial Biosphere Model coupled to ModelE2. This includes different initialization options for different levels of dynamics. These options include:**
本文描述了运行与ModelE2耦合的Ent陆地生物圈模型不同配置所需的运行配置规范。这包括不同动力学水平的不同初始化选项。这些选项包括：

**(1) Ent biophysics (surface fluxes) only, with Matthews (1983) and Rosenzweig & Abramopoulos (1997) prescribed seasonality of leaf area index (LAI) by vegetation type. This requires only cover initialization (VEG and CROPS) and other vegetation structure is prescribed.**
(1) 仅Ent生物物理（表面通量），使用Matthews (1983)和Rosenzweig & Abramopoulos (1997)按植被类型规定的叶面积指数(LAI)季节性。这只需要覆盖初始化(VEG和CROPS)，其他植被结构是预设的。

**(2) (AVAILABLE TO DEVELOPERS) Ent biophysics and Ent prognostic phenology (interactive seasonal plant growth). This configuration can be initialized as in (1), but it is best to initialize additionally with geographically varying files for initial LAI, canopy height, and canopy maximum LAI. Data sets for these values can be obtained from Nancy Kiang.**
(2) (开发者可用)Ent生物物理和Ent预报物候学（交互式季节性植物生长）。此配置可以像(1)那样初始化，但最好另外使用地理变化的文件进行初始LAI、冠层高度和冠层最大LAI的初始化。这些值的数据集可以从Nancy Kiang处获得。

**Sample rundecks in templates directory:**
**模板目录中的示例运行配置：**
`E1M20iEnt.R`
`E4F40iEnt.R`

**Components:**
**组件：**
`Ent giss_LSM`

**Component Options:**
**组件选项：**
`OPTS_Ent = ONLINE=YES PS_MODEL=FBB PFT_MODEL=ENT`

**Description:**
**说明：**
- **OPTS_Ent:** `model/Ent/`目录中Ent物理模块的编译选项
  - **PS_MODEL (FBB):** FBB=Ent的Farquhar/Ball-Berry生物物理；这即将成为默认设置。如果未设置，Friend & Kiang (2005)生物物理方案在代码中仍然可用。
  - **PFT_MODEL (ENT):** 运行Ent 16种植物功能型。如果未设置，Matthews (1983) 8种生物群系类型仍然可用，但Ent 16种PFT具有当前支持。

- **OPTS_giss_LSM:** `model/giss_LSM/`目录中陆地水文物理模块的编译选项

**INPUT_FILES required include all the ground hydrology boundary conditions required for any ModelE runs:**
**所需INPUT_FILES包括任何ModelE运行所需的所有陆地水文边界条件：**
- **TOPO** - 海洋、湖泊、地面、冰的分数，厚度，地形。GISS层格式。
- **SOIL** - ModelE土壤边界条件文件。网格数组二进制文件，无标题。
- **TOP_INDEX** - 如果使用TOP_MODEL径流，则为地形指数。GISS层格式。
- **VEG** - 每种植物功能型(PFT)的覆盖分数全球数组。GISS层格式。
- **CROPS** - 按年份的历史作物覆盖全球数组。GISS层格式。
- **CD_coef** - 地表粗糙度长度全球数组。GISS层格式。

**Additional INPUT_FILES required for Ent**
**Ent所需的额外INPUT_FILES**
- **soil_textures** - 土壤生物地球化学所需的土壤表层30厘米土壤质地（沙、粉砂、粘土分数）全球数组。
- **SOILCARB_global** (可选) - 用于初始化土壤生物地球化学的每平方米总土壤碳全球数组。如果PARAMETER `do_soilinit=.true.`时使用。
- **LAImax** - 按PFT分类的地理年最大冠层LAI全球数组。用于设置植物种群密度。如果PARAMETER `do_phenology_activegrowth=TRUE`或`do_init_geo=TRUE`时使用。
- **LAIinit** - 如果运行预报季节性，按PFT分类的初始叶面积指数(LAI)全球数组。如果PARAMETER `do_phenology_activegrowth=TRUE`或`do_init_geo=TRUE`时需要。
- **HITEent** - 按PFT分类的地理冠层高度全球数组。如果PARAMETER `do_phenology_activegrowth=TRUE`或`do_init_geo=TRUE`时使用。

**PARAMETERS**
**参数**
- **force_VEG** - 逻辑值，是否从文件强制使用LAI值（如果运行预报物候学，设置为`.false.`）
- **do_soilinit** - 逻辑值，从文件初始化土壤碳（`.true.`（默认）或`.false.`）
- **do_phenology_activegrowth** - 逻辑值，模拟季节性生长（叶、细根、边材）和LAI（默认=`.true.`）
- **do_structuralgrowth** - 逻辑值，模拟木本结构生长（茎、粗根）和高度变化（默认=`.false.`）
- **do_init_geo** - 逻辑值，从文件初始化冠层高度和最大LAI的地理变化（默认=`.true.`）。这些用于计算冠层结构（植物几何和密度）。否则，使用Rosenzweig & Abramopoulos (1997)的PFT冠层高度和最大LAI规定（无地理变化）。

**Diagnostics**
**诊断**
**Ent的诊断包括：**

**Carbon fluxes (mass/area/time)**
**碳通量（质量/面积/时间）**
- **GPP** - 总初级生产力，碳的总吸收
- **IPP** - 植被异戊二烯排放
- **RAUTO** - 自养呼吸，植被呼吸
- **SOILRESP** - 土壤呼吸

**Carbon stocks (mass/area)**
**碳储量（质量/面积）**
- **CLAB** - 植物可溶性碳，植物中的碳储备
- **SOILCPOOLSUM** - 土壤有机碳

- **LAI** - 叶面积指数（叶面积/地面面积）

**References**
**参考文献**
Friend, A. D. and N. Y. Kiang (2005). "Land Surface Model Development for the GISS GCM: Effects of Improved Canopy Physiology on Simulated Climate." Journal of Climate 18(15): 2883-2902.

Rosenzweig, C. and F. Abramopoulos (1997). "Land-surface model development for the GISS GCM." Journal of Climate 10: 2040-2054.