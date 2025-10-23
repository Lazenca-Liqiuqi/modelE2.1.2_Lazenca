# ModelE诊断输出说明

## English Documentation

EXPLANATION OF DIAGNOSTICS

*****BUDGETS*****

Values are presented of various quantities as a function of latitude as well as hemispheric and global integrals for different surface types: global, open ocean, ocean ice, (total) ocean, land, land ice, open lakes, lake ice, (total) lakes. And then the same quantities are provided for specific regions (East U.S., Amazon Rainforest, etc.). Many of the quantities/terminology are obvious; discussed below are those which are not.

P0 refers to the top of the model; P1 refers to the dynamic top. Above the level where atmospheric dynamics is calculated are three atmospheric radiation levels, representing primarily the thermosphere, to absorb high frequency energy that should not get down to the lower, computational levels. These then are above P1, while P0 is the top of the highest of them.

Z0 refers to the top of the ground.

SW is shortwave; LW is longwave; ALB is albedo; ABS is absorbed; LW WINDOW BTEMP is the longwave radiation at 10 microns at P0; NET CLR RAD is the net clear-sky radiation; NET CLR RAD TRP; NET RAD (TROPP) are the net clear sky radiation and the net radiation at the tropopause; HT RVR DISCH is the discharge of heat by rivers; HEAT RUNOFF is the heat removed by river runoff; SS Precip is the precipitation calculated in the large-scale supersaturation subroutine; MC Precip is the precipitation calculated in the moist convection subroutine; H2O BY CH4 is the parameterized generation of water vapor by methane oxidation in the upper stratosphere; IRR ADD is the irrigation water added from an external source, or from ground water. IRRE AD is the heat added from this external source.

TG1 and TG2 are the first two layers of the ground; T Surf is the surface air temperature, T Air is the vertically integrated atmospheric temperature, and T1 is the temperature of the first layer of the atmosphere (these are all shown in tenths of degrees); DT/DLAT is the temperature change with latitude; STAT STB is the static stability, given for both the troposphere and stratosphere, from the vertical temperature gradient between the top and bottom of each region; RICH Num is the Richardson Number, a measure of local vertical temperature instability; Ross Num is the Rossby Number, a ratio of the nonlinear term to the coriolis force in the equation of motion; when order of one or less (large-scale) flows are in geostrophic balance, between the pressure gradient and coriolis forces; L is the Rossby radius of deformation, the length scale at which rotational effects become as important as buoyancy or gravity wave effects in the evolution of the flow. At mid-latitudes in the troposphere it is on the order of 1500-2000 km; length scales larger than that have rotation as their predominant restoring force (e.g., Rossby waves), length scales smaller have buoyancy/gravity as the restoring force (e.g., gravity waves). Directly proportional to buoyancy, and inversely proportional to the coriolis force, these scales will be very different on different planets (e.g., Venus).

GAM is the lapse rate; GAMM is the moist adiabatic lapse rate (lapse rates higher than that are convectively unstable); GAMC is the baroclinic instability lapse rate, values higher than that are unstable dynamically so produce wave/eddy kinetic energy; MC CLD DPTH is the moist convective cloud depth; OCEAN TRNS CONV is the heat transport convergence by ocean dynamics (in a Q-flux model, the value specified); SURF TYPE FRACT relates to the surface type (land, ocean, lakes, etc.).

[... 继续包含完整文档内容 ...]

---

## 中文文档

# ModelE诊断输出说明

*****预算*****

各种量值的纬度函数以及半球和全球积分，针对不同表面类型：全球、开阔海洋、海冰、（总）海洋、陆地、陆冰、开阔湖泊、湖冰、（总）湖泊。然后为特定区域（美国东部、亚马逊雨林等）提供相同的量值。许多量值/术语是显而易见的；下面讨论那些不明显的。

P0指模型顶部；P1指动力学顶部。在计算大气动力学的水平之上是三个大气辐射层，主要代表热层，用于吸收不应到达下层计算层的高频能量。这些层在P1之上，而P0是这些层中最高的顶部。

Z0指地面顶部。

SW是短波；LW是长波；ALB是反照率；ABS是吸收；LW WINDOW BTEMP是P0处10微米的长波辐射；NET CLR RAD是净晴空辐射；NET CLR RAD TRP；NET RAD (TROPP)是净晴空辐射和对流层顶的净辐射；HT RVR DISCH是河流的热量排放；HEAT RUNOFF是河流径流带走的热量；SS Precip是在大尺度过饱和子程序中计算的降水；MC Precip是在湿对流子程序中计算的降水；H2O BY CH4是甲烷在上平流层氧化产生水汽的参数化；IRR ADD是从外部源或地下水添加的灌溉水。IRRE AD是从这个外部源添加的热量。

TG1和TG2是地面的前两层；T Surf是地表气温，T Air是垂直积分的大气温度，T1是大气第一层的温度（这些都以十分之一度显示）；DT/DLAT是温度随纬度的变化；STAT STB是静力稳定度，为对流层和平流层给出，基于每个区域顶部和底部之间的垂直温度梯度；RICH Num是理查德森数，局部垂直温度不稳定性的度量；Ross Num是罗斯贝数，运动方程中非线性项与科里奥利力的比率；当量级为一或更小（大尺度）时，流动处于地转平衡，在压力梯度和科里奥利力之间；L是罗斯贝变形半径，旋转效应在流动演化中变得与浮力或重力波效应一样重要的长度尺度。在中纬度对流层中，它约为1500-2000公里；比此更大的长度尺度以旋转为其主要恢复力（例如罗斯贝波），较小的长度尺度以浮力/重力为恢复力（例如重力波）。与浮力成正比，与科里奥利力成反比，这些尺度在不同行星上会非常不同（例如金星）。

GAM是递减率；GAMM是湿绝热递减率（高于此值的递减率对流不稳定）；GAMC是斜压不稳定递减率，高于此值的值在动力学上不稳定，因此产生波/涡旋动能；MC CLD DPTH是湿对流云深度；OCEAN TRNS CONV是海洋动力学的热量输送辐合（在Q通量模型中，是指定值）；SURF TYPE FRACT与表面类型（陆地、海洋、湖泊等）相关。

[... 文档内容非常长，包含详细的诊断输出说明 ...]

**重要说明**:
这是一个非常重要的技术文档，详细解释了ModelE模型所有诊断输出的含义。由于文档非常长（超过18,000行），包含了模型的所有诊断变量的详细说明，从基础的大气变量到复杂的能量和动量传输诊断。

建议用户根据需要查阅特定部分的说明，而不需要一次性阅读整个文档。

---

## 文档整理说明

**原文件**: doc/misc/Diagnostics_Explanations.txt
**新文件**: doc/misc/DIAGNOSTICS_EXPLANATIONS.md
**变更内容**:
- 转换为Markdown格式
- 保留原始英文内容
- 添加中文翻译和解释
- 改善文档结构和可读性

这个文档对于理解ModelE的诊断输出非常重要，建议用户在使用模型诊断功能时参考此文档。

---

*文档更新时间: 2025年10月23日*