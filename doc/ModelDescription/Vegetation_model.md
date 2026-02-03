# Vegetation model / 植被模型

## The Ent Dynamic Terrestrial Biosphere Model / Ent动态陆地生物圈模型

(More details and diagrams may be found [here](http://www.giss.nasa.gov/projects/ent))
（更多详情和图表可在[此处](http://www.giss.nasa.gov/projects/ent)找到）

### Introduction and Background / 介绍与背景

The Ent Terrestrial Biosphere Model (Ent TBM) is a standalone dynamic global vegetation model (DGVM) compatible with the Earth System Modeling Framework (ESMF).
Ent陆地生物圈模型（Ent TBM）是一个独立的动态全球植被模型（DGVM），与地球系统建模框架（ESMF）兼容。

It is designed to couple biophysics (fluxes of water, energy, carbon, and nitrogen) with land surface models and atmospheric general circulations models (GCMs); biogeochemistry (seasonal growth and decay of vegetation); and biogeography or ecological dynamics (decadal- to century-scale vegetation cover change due to mortality, establishment, and disturbance).
它旨在将生物物理（水、能量、碳和氮的通量）与陆面模型和大气环流模型（GCMs）耦合；生物地球化学（植被的季节生长和衰亡）；以及生物地理学或生态动力学（由死亡、建立和干扰导致的十年到百年尺度的植被覆盖变化）。

Dynamics in Ent are integrated in a consistent, prognostic, process-based manner, in a way that is both biologically realistic and computationally efficient, and suitable for two-way coupling and parallel computing in GCMs.
Ent中的动力学以一致的、预报性的、基于过程的方式集成，既符合生物学实际又计算高效，并适用于GCMs中的双向耦合和并行计算。

The original development platform is the NASA Goddard Institute for Space Studies (GISS) GCM.
最初的开发平台是NASA戈达德太空研究所（GISS）GCM。

Ent's distinguishing feature from previous DGVMs that couple to GCMs is the representation of mixed vegetation canopies rather than mosaicked.
Ent与先前耦合到GCMs的DGVMs的区别在于它表示混合植被冠层而非镶嵌结构。

The biophysics of Ent utilizes the well-known photosynthesis functions of Farqhuar, von Caemmerer, and Berry (1980) and Farqhuar and von Caemmerer (1982), and stomatal conductance of Ball and Berry (1985, 1987).
Ent的生物物理利用了Farquhar、von Caemmerer和Berry（1980）以及Farquhar和von Caemmerer（1982）的著名光合作用函数，以及Ball和Berry（1985, 1987）的气孔导度。（原文拼写：Farqhuar）

For canopy radiative transfer for changing canopies, Ent introduces new algorithms to calculate the clumping of foliage in mixed, vertically layered canopies (Ni-Meister et al., 2010; Yang et al., 2010).
针对变化冠层的冠层辐射传输，Ent引入了新算法来计算混合垂直分层冠层中的叶片聚集（Ni-Meister等, 2010; Yang等, 2010）。

Phenology is based on temperature, drought, and radiation cues, and growth is via allocation of carbon from labile carbohydrate reserve storage to different plant components.
物候基于温度、干旱和辐射信号，生长通过将碳从易变碳水化合物储备分配到不同植物组分来实现。

Soil biogeochemistry is based on the Carnegie-Ames-Stanford (CASA) model of Potter et al. (1993), and we introduce variable Q10 values for soil respiration response to moisture and temperature based on data from Del Grosso et al. (2005); a deep soil layer is optional.
土壤生物地球化学基于Potter等（1993）的Carnegie-Ames-Stanford（CASA）模型，我们根据Del Grosso等（2005）的数据引入了可变Q10值来描述土壤呼吸对湿度和温度的响应；深层土壤是可选的。

Ent's subgrid plant communities are structured to adopt the ecological dynamics approach of the Ecosystem Demography (ED) model (Medvigy et al., 2009; Moorcroft et al., 2001), which captures light competition due to vertical heterogeneity in mixed canopies, and subgrid heterogeneity from patch disturbance dynamics.
Ent的次网格植物群落结构采用生态系统人口统计（ED）模型的生态动力学方法（Medvigy等, 2009; Moorcroft等, 2001），该方法捕捉了混合冠层中垂直异质性导致的光竞争，以及斑块干扰动力学产生的次网格异质性。

The Ent TBM is set up to capture these mixed canopy processes within dynamically changing linked-list data structures.
Ent TBM被设置为在动态变化的链表数据结构中捕捉这些混合冠层过程。

The Ent TBM can run at different spatial scales (column or site, ij boundaries, and global), and with different levels of dynamics turned on or off (biophysics, biogeochemistry, biogeography).
Ent TBM可以在不同空间尺度（柱或站点、ij边界和全球）运行，并可以开启或关闭不同水平的动力学（生物物理、生物地球化学、生物地理）。

The functionality of Ent available in ModelE2 currently is only the biophysics portion for calculating fluxes of carbon dioxide and water vapor at the physical time step of the GCM.
ModelE2中当前可用的Ent功能仅是生物物理部分，用于在GCM的物理时间步计算二氧化碳和水汽的通量。

Prognostic seasonal growth is undergoing testing and is available only to developers.
预报性季节生长正在测试中，仅对开发者开放。

ED dynamics are to be introduced in 2013.
ED动力学将于2013年引入。

This document describes the Ent framework and the biophysics.
本文档描述了Ent框架和生物物理。

### Model Overview / 模型概述

### Ent Interfaces and Submodels / Ent接口和子模型

The Ent TBM is designed as a stand-alone model that can be forced by observed soil and atmospheric meteorology, or coupled to a land surface hydrology model or atmospheric GCM.
Ent TBM被设计为一个独立模型，可以由观测的土壤和大气气象强迫驱动，或与陆面水文模型或大气GCM耦合。

The land hydrology drivers or model provide soil and canopy temperature, snow and soil albedo, and soil moisture, and Ent returns vegetation cover leaf area index (LAI), total canopy albedo (including snow and soil), and water vapor conductance.
陆面水文驱动程序或模型提供土壤和冠层温度、雪和土壤反照率以及土壤湿度，Ent返回植被覆盖叶面积指数（LAI）、总冠层反照率（包括雪和土壤）以及水汽导度。

The atmospheric drivers or model provide pressure, vapor pressure, atmospheric CO₂ concentration, surface air temperature, downwelling shortwave and photosynthetically active radiation, the fraction of direct beam vs. diffuse radiation, and precipitation, and Ent provides surface albedo, surface flux of CO₂ and other mass exchanges of interest, such as isoprene.
大气驱动程序或模型提供气压、水汽压、大气CO₂浓度、地表气温、下行短波和光合有效辐射、直射光与漫射光的比例以及降水，Ent提供表面反照率、CO₂表面通量以及其他感兴趣的质量交换，如异戊二烯。

### Ent subgrid heterogeneity / Ent次网格异质性

Ent represents a grid cell or catchment hydrologic subregion as an "ent cell", and subgrid heterogeneity as dynamic patches of vegetation communities, comprised of cohorts of plants that are ensembles of identical individuals.
Ent将网格单元或流域水文子区域表示为"ent单元"，并将次网格异质性表示为植被群落的动态斑块，由植物队列组成，这些队列是相同个体的集合。

Patches dynamically open or merge according to disturbances and development of plant communities.
斑块根据干扰和植物群落的发展动态打开或合并。

Canopy conductances from each patch are summed to the ent cell level to couple with the atmosphere.
来自每个斑块的冠层导度被汇总到ent单元层级以与大气耦合。

All patches in one ent cell experience the same atmospheric conditions.
一个ent单元中的所有斑块经历相同的大气条件。

Currently, conductances of water vapor from each patch are summed over the ent cell, such that all patches then share the same soil water balance.
目前，来自每个斑块的水汽导度在ent单元上汇总，使得所有斑块共享相同的土壤水分平衡。

Subgrid heterogeneity of water balances is a development area.
水分平衡的次网格异质性是一个开发领域。

### Ent plant and landscape structure / Ent植物和景观结构

#### Individuals / 个体

Ent does not simulate individual plants, but instead simulates cohorts that are ensembles of identical individuals that are distinguished by plant functional type and size (geometry, biomass pools).
Ent不模拟单个植物，而是模拟队列，这些队列是相同个体的集合，由植物功能型和大小（几何形状、生物量库）区分。

The biomass pools are constrained by fixed allometry, with seasonally varying foliage and fine roots limited within this allometry.
生物量库受到固定异速生长的约束，季节性变化的叶片和细根被限制在这个异速生长范围内。

The allometry relations are taken from many sources further documented in a full technical report for Ent.
异速生长关系取自多个来源，并在Ent的完整技术报告中进一步记录。

Biomass pools for woody plants consist of carbon pools for foliage, live and dead stem, sapwood, fine and coarse roots, and a labile storage pool to which photosynthetic uptake (and eventually retranslocated nitrogen) is stored and from which growth is allocated.
木本植物的生物量库包括叶片、活茎和死茎、边材、细根和粗根的碳库，以及一个易变储存库，光合作用吸收（以及最终再转运的氮）储存在其中，生长从中分配。

Herbaceous plants have only foliage, fine root, and labile pools.
草本植物只有叶片、细根和易变库。

Nitrogen content is currently specified by fixed carbon:nitrogen ratios by PFT and carbon pool.
氮含量目前由PFT和碳库的固定碳氮比指定。

#### Cohorts / 队列

Cohorts of ensembles of identical individuals in a patch community are organized in linked list data structures, from tallest to shortest.
斑块群落中相同个体集合的队列在链表数据结构中组织，从最高到最低排列。

This stratification organizes the cohorts in their competition for light.
这种分层组织了队列在光竞争中的排列。

Horizontal spatial distribution of individuals is statistical and not explicit, with a constraint that crowns do not overlap (see Section on canopy radiative transfer).
个体的水平空间分布是统计性的而非显式的，有一个约束条件是树冠不重叠（见冠层辐射传输章节）。

The number of cohorts per patch may be restricted as an option if necessary.
如果有必要，每个斑块的队列数量可以作为选项进行限制。

Utilities for managing cohorts include reading, for reading in prescribed land cover from a data file; insertion, for read in or newly established cohorts; deletion, for dead cohorts; sorting, when cohort growth leads to change in their height order; and merging, for cohorts that grow to have the same characteristics.
管理队列的工具包括：读取，用于从数据文件读取规定的土地覆盖；插入，用于读入或新建立的队列；删除，用于死亡的队列；排序，当队列生长导致其高度顺序发生变化时；合并，用于生长到具有相同特征的队列。

These management routines need to be called only during initialization of the vegetation cover, or when algorithms deem that there is significant enough structural change to make a difference in canopy radiative transfer parameters or community dynamics.
这些管理例程只需要在植被覆盖初始化期间调用，或者当算法认为结构变化足够显著以至于会影响冠层辐射传输参数或群落动力学时调用。

In addition, a utility to write cohort data to a text file is provided.
此外，还提供了一个将队列数据写入文本文件的工具。

Routines to summarize cohort properties to the patch level are called half-hourly for fluxes, daily for biomass pools, and intermittently for significant community structural changes.
将队列属性汇总到斑块级别的例程每半小时调用一次用于通量，每天调用一次用于生物量库，间歇性调用用于重大的群落结构变化。

#### Patch communities / 斑块群落

Patches of subgrid areas within an ent cell contain communities of plant cohorts.
ent单元内次网格区域的斑块包含植物队列的群落。

Patches are not spatially explicit within an ent cell, but are organized in linked lists, stratified by age, that is, the time since the disturbance that opened a patch area as bare soil.
斑块在ent单元内不是空间显式的，而是在链表中组织，按年龄分层，即干扰将斑块区域开放为裸土壤之后的时间。

The number of patches in a grid cell may be restricted as an option if necessary; experience with the ED model indicates that a grid cell generally requires ~10 patches to capture a realistic level of surface heterogeneity and dynamics.
如果有必要，网格单元中的斑块数量可以作为选项进行限制；ED模型的经验表明，网格单元通常需要约10个斑块来捕捉现实的表面异质性和动力学水平。

For land surface models with representations of different hydrological zones of catchments, since this level of land surface heterogeneity is described by the hydrological model, Ent can be set with static patches that correspond to each catchment zone.
对于具有流域不同水文区域表示的陆面模型，由于这种陆面异质性水平由水文模型描述，Ent可以设置对应于每个流域区域的静态斑块。

Utilities for managing patches include reading, for reading in prescribed land cover from a data file; insertion, for new patches; partitioning, for when disturbance (fire) leads to new patches due to clearing parts of existing patches; and merging, and when ecosystem dynamics lead to similar communities on different patches, such that managing them separately is redundant.
管理斑块的工具包括：读取，用于从数据文件读取规定的土地覆盖；插入，用于新斑块；分割，当干扰（火灾）由于清除现有斑块的部分而导致的斑块时；合并，当生态系统动力学导致不同斑块上出现相似群落，使得单独管理它们变得冗余时。

In addition, a utility to write patch data to a text file is provided.
此外，还提供了一个将斑块数据写入文本文件的工具。

Routines to summarize patch properties to the Ent cell level (grid cell) are called half-hourly for fluxes, daily for soil carbon and nitrogen pools, and intermittently according to occurrence of disturbance and patch merging.
将斑块属性汇总到Ent单元级别（网格单元）的例程每半小时调用一次用于通量，每天调用一次用于土壤碳和氮库，根据干扰和斑块合并的发生间歇性调用。

#### Ent cells / Ent单元

Ent cells correspond to the basic unit of the land surface hydrology model, which may be a GCM grid cell or a catchment zone.
Ent单元对应于陆面水文模型的基本单元，可能是GCM网格单元或流域区域。

At the Ent cell level, atmospheric drivers and surface temperature are supplied to Ent, and Ent returns vegetation conductance of water vapor and fluxes of CO₂, as diagrammed in Figure 1.
在Ent单元级别，大气驱动程序和表面温度提供给Ent，Ent返回水汽的植被导度和CO₂通量，如图1所示。

Soil depth structure for soil moisture also follows that of the land surface scheme (see Section on land surface model coupling).
土壤湿度的土壤深度结构也遵循陆面方案的结构（见陆面模型耦合章节）。

Note that the Ent model does not calculate energy balances, but relies on the land surface and atmosphere model to calculate canopy temperature and soil temperature.
请注意，Ent模型不计算能量平衡，而是依赖陆面和大气模型来计算冠层温度和土壤温度。

Ent cells are stored in an array and are set up at initialization of the model according to the land surface hydrology model's structure.
Ent单元存储在数组中，并在模型初始化时根据陆面水文模型的结构设置。

The Ent cell array and soil moisture vertical structure interface requires customized setup through a driver file according to different land surface schemes.
Ent单元数组和土壤湿度垂直结构接口需要根据不同的陆面方案通过驱动文件进行自定义设置。

The cell-level meteorological drivers are all stored in the Ent cell data structure for access by Ent modules that perform operations at the patch and cohort levels.
单元级别的气象驱动程序都存储在Ent单元数据结构中，供在斑块和队列级别执行操作的Ent模块访问。

Pointers between a parent Ent cell, its children patches, and their children cohorts, allow straightforward access to and passing of driver data.
父Ent单元、其子斑块及其子队列之间的指针允许直接访问和传递驱动数据。

### Ent vertical and horizontal soil structure / Ent垂直和水平土壤结构

Soil type in Ent depends on the soil types specified by the land surface hydrology model to which Ent is coupled, which must provide sand, silt, and clay fractions, and soil depth.
Ent中的土壤类型取决于Ent所耦合的陆面水文模型指定的土壤类型，该模型必须提供沙、粉砂和黏土比例以及土壤深度。

Soil type is expected to of one kind in an ent cell.
预期ent单元中的土壤类型为一种。

Ent soil biogeochemistry requires distinction of soil temperature, moisture, and texture in a 0-30 cm layer, and optionally in a 30-100 cm deep layer.
Ent土壤生物地球化学需要区分0-30厘米层中的土壤温度、湿度和质地，以及可选的30-100厘米深层。

Ent canopy conductance requires interfacing vertical root distributions with the layering scheme of the land surface model to calculate soil moisture stress; the layering of vertical root distributions is currently based on continuous functions by Rosenszweig and Abramopoulos (1997) and so can be scaled according to the land surface scheme.
Ent冠层导度需要将垂直根分布与陆面模型的分层方案接口以计算土壤水分胁迫；垂直根分布的分层目前基于Rosenszweig和Abramopoulos（1997）的连续函数，因此可以根据陆面方案进行缩放。

### Plant functional types / 植物功能型

Ent supports 16 plant functional types (PFTs), as listed below.
Ent支持16种植物功能型（PFT），如下所列。

[Planned update: Ent will later support a 17th PFT, C3 crops].
[计划更新：Ent稍后将支持第17种PFT，C3作物]。

Following the rationale first advocated by Defries et al. (1995) and adopted by all vegetation models since to varying degrees, Ent's PFTs distinguish physiogonomic characteristics: photosynthetic pathway (C3, C4), leaf type (broadleaf, needleleaf), growth form (woody, herbaceous), phenotype (evergreen, cold deciduous, drought deciduous; for herbs, annual vs. perennial), and cultivated (crops).
遵循Defries等（1995）首次倡导并被所有植被模型不同程度采用的基本原理，Ent的PFT区分形态学特征：光合途径（C3、C4）、叶型（阔叶、针叶）、生长型（木本、草本）、表型（常绿、冷落叶、干旱落叶；对于草本，一年生vs多年生）和栽培（作物）。

To better capture community dynamics in mixed canopies, Ent optionally can distinguish early and late successional species through differences in leaf life span, following the approach of the Ecosystem Demography (ED) model (Moorcroft, et al., 2001), which is based on leaf physiological relations found in Reich et al. (1997).
为了更好地捕捉混合冠层中的群落动力学，Ent可以选择通过叶片寿命的差异区分早期和晚期演替物种，遵循生态系统人口统计（ED）模型的方法（Moorcroft等, 2001），该方法基于Reich等（1997）中的叶片生理关系。

#### Ent plant functional types / Ent植物功能型

| | |
|---|---|
| 1. evergreen broadleaf early successional | 1. 常绿阔叶早期演替种 |
| 2. evergreen broadleaf late successional | 2. 常绿阔叶晚期演替种 |
| 3. evergreen needleleaf early successional | 3. 常绿针叶早期演替种 |
| 4. evergreen needleleaf late successional | 4. 常绿针叶晚期演替种 |
| 5. cold deciduous broadleaf early successional | 5. 冷落叶阔叶早期演替种 |
| 6. cold deciduous broadleaf late successional | 6. 冷落叶阔叶晚期演替种 |
| 7. drought deciduous broadleaf（原文拼写：decidous） | 7. 干旱落叶阔叶 |
| 8. decidous needleleaf | 8. 落叶针叶 |
| 9. cold adapted shrub | 9. 冷适应灌木 |
| 10. arid adapted shrub | 10. 干旱适应灌木 |
| 11. C3 grass - perennial | 11. C3草 - 多年生 |
| 12. C4 grass - perennial | 12. C4草 - 多年生 |
| 13. C3 grass arctic | 13. C3草北极种 |
| 14. C3 grass annual | 14. C3草一年生 |
| 15. crops - C4 herbaceous | 15. 作物 - C4草本 |
| 16. crops - broadleaf woody | 16. 作物 - 阔叶木本 |
| TBA crops - C3 herbaceous | 待定作物 - C3草本 |

### Biophysics / 生物物理

Photosynthesis and conductance in Ent are calculated at the leaf level using the well-known Michaelis-Menten photosynthesis relationships of of Farquhar, von Caemmerer and Berry (1980) and Farquhar and von Caemmerer (1982) and stomatal conductance of Ball and Berry (1985, 1987).
Ent中的光合作用和导度使用Farquhar、von Caemmerer和Berry（1980）以及Farquhar和von Caemmerer（1982）的著名Michaelis-Menten光合作用关系以及Ball和Berry（1985, 1987）的气孔导度在叶片级别计算。

Photosynthetic capacity varies according to immediate temperature, and phenology.
光合能力根据即时温度和物候而变化。

The solution to the coupled photosynthesis-conductance equations utilizes leaf boundary conductances similarly to the approach by Collatz et al. (1991) but with the boundary layer conductance derived from canopy surface layer conductance; equations for a cubic solution are propose a variation on the approaches by Baldocchi (1994), Su et al. (1996), and Zhan et al. (2003).
耦合光合作用-导度方程的求解利用叶片边界导度，类似于Collatz等（1991）的方法，但边界层导度从冠层表面层导度导出；三次解的方程提出了Baldocchi（1994）、Su等（1996）和Zhan等（2003）方法的变体。

Photosynthetic uptake of CO₂ is accumulated into a carbon reserve pool, from which other processes may allocate uses.
CO₂的光合吸收被累积到碳储备库中，其他过程可以从中分配用途。

Scaling of the leaf to canopy level is through stratification of canopy light levels and leaf area profiles as in (Friend and Kiang, 2005).
从叶片到冠层级别的缩放是通过冠层光水平和叶面积剖面的分层进行的，如（Friend和Kiang, 2005）所述。

This will soon be replaced by the Analytical Clumped Two-Stream scheme (ACTS) of (Ni-Meister et al., 2010; Yang et al., 2010), which accounts for foliage clumping and stem effects.
这很快将被（Ni-Meister等, 2010; Yang等, 2010）的解析聚集双流方案（ACTS）取代，该方案考虑了叶片聚集和树干效应。

Coupling of the canopy fluxes and physical properties to the atmosphere consists of specification of canopy fluxes of CO₂, conductance of water vapor, canopy heat capacity, and canopy roughness length.
冠层通量和物理性质与大气的耦合包括CO₂冠层通量的规定、水汽导度、冠层热容量和冠层粗糙长度。

Autotrophic respiration consists of 1) maintenance respiration as a function of plant biomass pool size, its carbon:nitrogen ratio, with an Arrhenius temperature response and acclimation to 10-day average temperature; 2) growth respiration as a function of photosynthetic activity; and 3) growth respiration resulting from tissue growth.
自养呼吸包括：1）维持呼吸，作为植物生物量库大小及其碳氮比的函数，具有Arrhenius温度响应和对10天平均温度的适应；2）生长呼吸，作为光合作用的函数；以及3）由组织生长产生的生长呼吸。

The latter is calculated once a day when tissue turnover and growth are calculated, and the resulting respiration fluxes are distributed uniformly at the physical time step over the next day.
后者在计算组织周转和生长时每天计算一次，产生的呼吸通量在第二天的物理时间步内均匀分布。

More details on the leaf and photosynthetic parameters used in Ent are documented in an Ent Technical Report.
关于Ent中使用的叶片和光合参数的更多细节记录在Ent技术报告中。

### Seasonality / 季节性

Seasonal variation in carbon stocks due to plant growth and decay (soil respiration) can be either prescribed or prognostic.
由植物生长和衰亡（土壤呼吸）引起的碳库季节变化可以是规定的或预报的。

Soil biogeochemistry in either case is driven by litterfall from the seasonal change in plant carbon pools.
无论哪种情况，土壤生物地球化学都由植物碳库季节变化产生的凋落物驱动。

When prescribed, the time course of leaf area index is either read from a file or determined by simple seasonal curves that are insensitive to climate drivers or carbon balances as in Rosenzweig & Abramopoulos (1997).
当规定时，叶面积指数的时间过程要么从文件读取，要么由简单的季节曲线确定，这些曲线对气候驱动或碳平衡不敏感，如Rosenzweig和Abramopoulos（1997）所述。

With prescribed seasonal leaf area, leaf mass is not driven by uptake of CO₂ by photosynthesis; therefore in this mode a closed carbon cycle is not simulated, but the prescribed leaf area is be expedient for capturing water vapor feedbacks to climate from vegetation.
对于规定的季节性叶面积，叶片质量不是由光合作用吸收CO₂驱动的；因此在这种模式下不模拟闭合碳循环，但规定的叶面积对于捕捉植被对气候的水汽反馈是方便的。

With prognostic seasonal leaf area, seasonal leaf dynamics are driven by CO₂ uptake and by climate cues.
对于预报性季节性叶面积，季节性叶片动力学由CO₂吸收和气候信号驱动。

Therefore, a closed carbon cycle can be simulated.
因此，可以模拟闭合碳循环。

Since this mode does not include community dynamics or cover change (competition, mortality, establishment, disturbance), to prevent woody plants from unlimited increase in size, any allocation of carbon that would have been for woody structural growth or reproduction is dumped into litterfall so that the carbon cycle is closed.
由于此模式不包括群落动力学或覆盖变化（竞争、死亡、建立、干扰），为了防止木本植物无限增加大小，任何用于木本结构生长或繁殖的碳分配都被倾倒入凋落物中，以使碳循环闭合。

This is equivalent to assuming that the given vegetation structure is at an equilibrium with the climate, such that the community structure is at a steady-state.
这等价于假设给定的植被结构与气候处于平衡状态，使得群落结构处于稳态。

### Soil biogeochemistry / 土壤生物地球化学

The soil biogeochemistry submodel of Ent is based largely on the CASA' biosphere submodel used in the NCAR LSM and CSM 1.4 (Bonan, 1996; Randerson et al., 1997; Fung et al., 2005; Doney et al., 2006), which itself is a modified version of the original NASA-CASA biosphere model (Potter et al., 1993).
Ent的土壤生物地球化学子模型主要基于NCAR LSM和CSM 1.4中使用的CASA'生物圈子模型（Bonan, 1996; Randerson等, 1997; Fung等, 2005; Doney等, 2006），该模型本身是原始NASA-CASA生物圈模型（Potter等, 1993）的修改版本。

Modifications have been made to for soil respiration response to moisture and temperature based on data from Del Grosso et al. (2005).
根据Del Grosso等（2005）的数据，对土壤呼吸对湿度和温度的响应进行了修改。

The soil model mechanistically determines terrestrial soil carbon (and nitrogen) pools and CO₂ fluxes from microbial respiration.
土壤模型机械地确定陆地土壤碳（和氮）库以及来自微生物呼吸的CO₂通量。

Ent combines soil respiration, photosynthesis, and autotrophic respiration to predict net ecosystem exchange (NEE) of carbon with the atmosphere.
Ent结合土壤呼吸、光合作用和自养呼吸来预测与大气碳的净生态系统交换（NEE）。

### Meteorological drivers to Ent / Ent的气象驱动

#### Table: Input variables from the atmosphere and land surface hydrology models to the Ent TBM ("patch"=subgrid cover fraction).
#### 表：大气和陆面水文模型向Ent TBM的输入变量（"patch"=次网格覆盖分数）。

| Inputs to Ent / Ent的输入 | Variable / 变量 | Units / 单位 | Spatial resolution / 空间分辨率 |
|---|---|---|---|
| **From atmosphere / 来自大气** | Air pressure / 气压 | millibar / 毫巴 | Ent cell / Ent单元 |
| | Air temperature / 气温 | Celsius / 摄氏度 | Ent cell / Ent单元 |
| | Vapor pressure mixing ratio at foliage surface / 叶片表面水汽压混合比 | kg/kg / 千克/千克 | Ent cell / Ent单元 |
| | Atmospheric CO₂ concentration / 大气CO₂浓度 | mol/m³ / 摩尔/立方米 | Ent cell / Ent单元 |
| | Cosine of solar zenith angle / 太阳天顶角余弦 | cosine / 余弦 | Ent cell / Ent单元 |
| | Incident direct photosynthetically active radiation / 入射直射光合有效辐射 | W/m² / 瓦/平方米 | Ent cell / Ent单元 |
| | Incident diffuse photosynthetically active radiation / 入射漫射光合有效辐射 | W/m² / 瓦/平方米 | Ent cell / Ent单元 |
| | Wind speed / 风速 | m/s / 米/秒 | Ent cell / Ent单元 |
| | Ground to surface layer heat transfer coefficient / 地面到表面层热传递系数 | dimensionless / 无量纲 | Ent cell / Ent单元 |
| **From land surface model / 来自陆面模型** | Soil texture (sand, silt, clay) / 土壤质地（沙、粉砂、黏土） | fractions (init.) / 比例（初始） | Ent cell / Ent单元 |
| | Soil albedo / 土壤反照率 | fraction by band (init.) / 按波段比例（初始） | Ent cell / Ent单元 |
| | Soil temperature / 土壤温度 | Celsius / 摄氏度 | Ent cell / Ent单元 |
| | Soil moisture / 土壤湿度 | saturated fraction / 饱和分数 | Ent cell / Ent单元 |
| | Soil ice fraction of soil water / 土壤水中土壤冰比例 | fraction by layer / 按层分数 | Ent cell / Ent单元 |
| | Canopy temperature / 冠层温度 | Celsius / 摄氏度 | Ent cell / Ent单元 |
| | Snow albedo / 雪反照率 | fraction by band / 按波段分数 | Ent cell / Ent单元 |
| | Canopy wetness / 冠层湿度 | fraction of leaf area / 叶面积分数 | patch / 斑块 |

#### Table: Outputs from the Ent TBM to the atmospheric and land surface hydrology models.
#### 表：Ent TBM向大气和陆面水文模型的输出。

| Inputs to Ent / Ent的输入 | Variable / 变量 | Units / 单位 | Spatial Resolution / 空间分辨率 |
|---|---|---|---|
| **To atmosphere / 向大气** | Canopy albedo / 冠层反照率 | fraction (bands) / 分数（波段） | patches avg. to Ent cell / 斑块平均到Ent单元 |
| | Net CO₂ flux / 净CO₂通量 | kg-C/m²-ground/s / 千克-碳/平方米-地面/秒 | patches sum to Ent cell / 斑块求和到Ent单元 |
| | Canopy height / 冠层高度 | m (daily) / 米（日） | patch / 斑块 |
| | (Roughness length TBA) / （粗糙长度待定） | m (daily) / 米（日） | patch / 斑块 |
| | (Aerosols from fire TBA) / （火灾气溶胶待定） | TBA / 待定 | patches sum to Ent cell / 斑块求和到Ent单元 |
| | (Volatile organic carbons TBA) / （挥发性有机碳待定） | TBA / 待定 | patches sum to Ent cell / 斑块求和到Ent单元 |
| **To land surface model / 向陆面模型** | Canopy conductance of water vapor / 水汽冠层导度 | m/s / 米/秒 | patch / 斑块 |
| | Plant water stress / 植物水分胁迫 | fraction (0-1) by layer / 按层分数（0-1） | patch / 斑块 |
| | Vegetation structure - leaf area index (LAI) / 植被结构 - 叶面积指数 | m²/m² (daily) / 平方米/平方米（日） | patch / 斑块 |
| | Vegetation structure - root depth distribution / 植被结构 - 根系深度分布 | fraction biomass per layer / 按层生物量分数 | cohorts avg. to patch / 队列平均到斑块 |
| | Transmittance of shortwave to the ground / 到地面的短波透射率 | fraction / 分数 | patch / 斑块 |

### References / 参考文献

Baldocchi, D. (1994). "An analytical solution for coupled leaf photosynthesis and stomatal conductance models." Tree Physiology 14(7-9): 1069-1079.

Ball, J. T. and J. A. Berry (1987). A model predicting stomatal conductance and its contribution to photosynthesis under different environmental conditions. Progress in Photosynthesis Research. I. Biggins. Nijhoff, Dordrecht, Netherlands. IV: 110-112.

Ball, T. and J. Berry (1985). "A Simple Empirical Model of Stomatal Control." Plant Physiology 77(n. Supplement 4): 91.

Bonan, G. B. (1996). A land surface model (LSM Version 1.0) for ecological, hydrological, and atmospheric studies: technical description and user's guide. Boulder, Colorado, National Center of Atmospheric Research: 122.

Collatz, G. J., J. T. Ball, C. Grivet and J. A. Berry (1991). "Physiological and environmental regulation of stomatal conductance, photosynthesis and transpiration: a model that includes a laminar boundary layer." Agricultural and Forest Meteorology 54: 107-136.

Defries, R. S., C. B. Field, I. Fung, C. O. Justice, S. O. Los, P. A. Matson, E. Matthews, H. A. Mooney, C. Potter, K. C. Prentice, P. J. Sellers, J. Townshend, C. J. Tucker, S. L. Ustin and P. Vitousek (1995). "Mapping the land surface for global atmosphere-biosphere models - toward continuous distributions of vegetation's functional properties." Journal of Geophysical Research - Atmospheres 100(D10): 20,867-20,882.

Del Grosso, S. J., W. J. Parton, A. R. Mosier, E. A. Holland, E. Pendall, D. S. Schimel and D. S. Ojima (2005). "Modeling soil CO2 emissions from ecosystems." Biogeochemistry 73: 71-91

Doney, S.C., Lindsay, K., Fung, I., John, J. (2006) Natural variability in a stable, 1000-yr global coupled climate-carbon cycle simulation. Journal of Climate 19, 3033-3052.

Farquhar, G. D. and S. von Caemmerer (1982). 16 Modelling photosynthetic response to environmental conditions. Encyclopedia of Plant Physiology (NS). P. S. N. O.L. Lange, C.B. Osmond, H. Ziegler. Berlin, Springer. 12B: 549-587.

Farquhar, G. D., S. von Caemmerer and J. A. Berry (1980). "A biochemical model of photosynthetic CO2 assimilation in leaves of C3 species." Planta 149: 78-90.

Friend, A. D. and N. Y. Kiang (2005). "Land Surface Model Development for the GISS GCM: Effects of Improved Canopy Physiology on Simulated Climate." Journal of Climate 18(15): 2883-2902.

Fung I, Doney S, Lindsay K, John J (2005) Evolution of carbon sinks in a changing climate. Proc Nat Acad Sci 102: 11201-11206

Matthews, E. (1983). "Global vegetation and land use: new high-resolution data bases for climate studies." Journal of Climate and Applied Meteorology 22: 474-487.

Medvigy, D., Munger, S.C.W.a.J.W., Hollinger, D.Y., Moorcroft, P.R. (2009) Mechanistic scaling of ecosystem function and dynamics in space and time: Ecosystem Demography model version 2. Journal of Geophysical Research-Atmospheres 114, G01002.

Moorcroft, P., G. C. Hurtt and S. W. Pacala (2001). "A method for scaling vegetation dynamics: The Ecosystem Demography Model (ED)." Ecological Monographs 71(4): 557-586.

Ni-Meister, W., Yang, W.Z., Kiang, N.Y. (2010) A clumped-foliage canopy radiative transfer model for a global dynamic terrestrial ecosystem model. I: Theory. Agricultural and Forest Meteorology 150, 881-894.

Potter, C. S., J. T. Randerson, C. B. Field, P. A. Matson, P. M. Vitousek, H. A. Mooney and S. A. Klooster (1993). "Terrestrial ecosystem production: a process model based on global satellite and surface data." Global Biogeochemical Cycles 7(4): 811-841.

Randerson, J. T., T. M.V., T. J. Conway, I. Y. Fung and C. B. Field (1997). "The contribution of terrestrial sources and sinks to trends in the seasonal cycle of atmospheric carbon dioxide." Global Biogeochemical Cycles 11(4): 535-560.

Rosenzweig, C. and F. Abramopoulos (1997). "Land-surface model development for the GISS GCM." Journal of Climate 10: 2040-2054.

Su, H.-B., K. T. Paw and R. H. Shaw (1996). "Development of a coupled leaf and canopy model for the simulation of plant-atmosphere interaction." Journal of Applied Meteorology 35(5): 733-748.

Yang, W.Z., Ni-Meister, W., Kiang, N.Y., Moorcroft, P.R., Strahler, A.H., Oliphant, A. (2010) A clumped-foliage canopy radiative transfer model for a Global Dynamic Terrestrial Ecosystem Model II: Comparison to measurements. Agricultural and Forest Meteorology 150, 895-907.

Zhan, X. W., Y. K. Xue and G. J. Collatz (2003). "An analytical approach for estimating CO2 and heat fluxes over the Amazonian region." Ecological Modelling 162(1-2): 97-117.
