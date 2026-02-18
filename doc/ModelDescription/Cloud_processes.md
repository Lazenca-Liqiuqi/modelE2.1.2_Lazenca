# Cloud processes / 云过程

CONDSE is a driver that sets up the vertical arrays for the column models for moist convection, large scale condensation and stratiform clouds, and accumulates diagnostics and output for the radiation and other modules.
CONDSE是一个驱动程序，用于为湿润对流、大尺度凝结和层状云的柱模型设置垂直数组，并为辐射和其他模块累积诊断和输出。

### Moist convection / 湿润对流

The cumulus parameterization subroutine MSTCNV triggers convection when a parcel lifted one model level saturates and becomes buoyant.
积云参数化子程序MSTCNV在气块被抬升一个模型层级达到饱和并变得浮力时触发对流。

The mass flux closure assumes that sufficient mass is transported to stabilize the cloud base with respect to its environment over a specified convective adjustment time (Del Genio and Yao 1993).
质量通量闭合假设在指定的对流调整时间内输送足够的质量，以使云底相对于其环境稳定（Del Genio和Yao, 1993）。

The total mass flux is partitioned into two plumes that entrain at different rates (Del Genio et al. 2007); the less entraining plume has a mass based on the grid-scale convergence at cloud base, and the more entraining plume receives the remainder of the mass flux.
总质量通量被分成两个以不同速率卷入的羽流（Del Genio等, 2007）；卷入较少的羽流的质量基于云底的网格尺度辐合，卷入较多的羽流接收剩余的质量通量。

Convection can arise from multiple model levels.
对流可以从多个模型层级产生。

The cumulus updraft speed is diagnosed and plume ascent terminates when it goes to zero.
积云上升速度被诊断，当羽流上升速度变为零时终止。

Mass is detrained when the buoyancy becomes negative.
当浮力变为负值时，质量被夹卷。

A convective-scale downdraft is determined when an equal mixture of cloud and environmental air is negatively buoyant at any level.
当云和环境的等量混合物在任何层级负浮力时，确定对流尺度下沉气流。

Mass continuity is satisfied at each level by environmental subsidence which compensates the sum of mass flux of the updraft and downdraft.
质量连续性在每个层级得到满足，通过环境下沉补偿上升和下沉气流的质量通量之和。

Convective condensate formed by moist adiabatic uplift is partitioned into parts that are advected upward, detrained, and precipitated at each level, an updated version of Del Genio et al. (2005).
由湿绝热抬升形成的对流凝结物被分成向上平流、夹卷和在各层级降水的部分，这是Del Genio等（2005）的更新版本。

The precipitating part goes into the downdraft, where it can evaporate, but an option exists for a fraction to evaporate into the environment above and below cloud base.
降水部分进入下沉气流，在那里可以蒸发，但有一个选项允许一部分在云底上方和下方的环境中蒸发。

Detrained convective condensate is passed to the stratiform cloud subroutine LSCOND.
夹卷的对流凝结物被传递给层状云子程序LSCOND。

A moist convective cloud and an anvil cloud cover and optical thickness are calculated and passed to the radiation code.
湿润对流云和砧云的覆盖和光学厚度被计算并传递给辐射代码。

#### References / 参考文献

Del Genio, A.D., and M.-S. Yao, 1993: Efficient cumulus parameterization for long-term climate studies: The GISS scheme. In The Representation of Cumulus Convection in Numerical Models, AMS Meteor. Monograph. K.A. Emanuel and D.A. Raymond, Eds., vol. 24, no. 46. American Meteorological Society, pp. 181-184.

Del Genio, A.D., W. Kovari, M.-S. Yao, and J. Jonas, 2005: Cumulus microphysics and climate sensitivity. J. Climate, 18, 2376-2387, doi:10.1175/JCLI3413.1.

Del Genio, A.D., M.-S. Yao, and J. Jonas, 2007: Will moist convection be stronger in a warmer climate?. Geophys. Res. Lett., 34, L16703, doi:10.1029/2007GL030525.

The physics is also described in [this document](http://www.giss.nasa.gov/tools/modelE/docs/kim_moistconvection.pdf).
物理过程也在[此文档](http://www.giss.nasa.gov/tools/modelE/docs/kim_moistconvection.pdf)中描述。

#### The cumulus parameterization consists of the following subroutines / 积云参数化由以下子程序组成

**SUBROUTINE MSTCNV** - the primary subroutine in which moist convection calculations are performed and output diagnostics accumulated.
主子程序，在其中执行湿润对流计算并累积输出诊断。

MSTCNV calls a number of other subroutines; those specific to the CLOUDS2 module are listed below.
MSTCNV调用多个其他子程序；特定于CLOUDS2模块的子程序列在下面。

**SUBROUTINE ANVIL_OPTICAL_THICKNESS** - calculates the optical thickness associated with condensate detrained from convective updrafts; becomes moot if SUBROUTINE LSCOND decides that the anvil can be sustained in a sufficiently humid environment.
计算与从对流上升气流夹卷的凝结物相关的光学厚度；如果子程序LSCOND决定砧云可以在足够湿润的环境中维持，则变得无意义。

**SUBROUTINE MC_CLOUD_FRACTION** - calculates the fractional area of convective cloud that is passed to the radiation code, based on the cumulus mass flux and updraft speed.
根据积云质量通量和上升速度计算传递给辐射代码的对流云的分数面积。

**SUBROUTINE CONVECTIVE_MICROPHYSICS** - uses a Marshall-Palmer size distribution, the cumulus updraft speed, and size-fallspeed relationships for liquid, graupel, and ice to partition condensate into precipitating, detrained, and advected parts; uses FUNCTION PRECIP_MP.
使用Marshall-Palmer尺寸分布、积云上升速度以及液体、霰和冰的尺寸-下落速度关系，将凝结物分成降水、夹卷和平流部分；使用函数PRECIP_MP。

**SUBROUTINE MC_PRECIP_PHASE** - calculates the phase of convective precipitation associated with melting, re-freezing, etc.; the gridbox area into which precipitation is allowed to evaporate is also calculated in this subroutine.
计算与融化、再冻结等相关的对流降水的相；允许降水蒸发的网格盒面积也在该子程序中计算。

**FUNCTION PRECIP_MP** - integrates the cloud water content over ranges of the Marshall-Palmer distribution defined by critical sizes (determined by comparing updraft speed to fallspeed) to calculate the partitioning of convective condensate.
在由临界尺寸（通过比较上升速度和下落速度确定）定义的Marshall-Palmer分布范围内积分云水含量，以计算对流凝结物的分配。

**SUBROUTINE MASS_FLUX** - uses an iterative technique to estimate the mass flux required at cloud base to restore it to neutral stability (based on a virtual moist static energy criterion) via environmental subsidence; the mass flux is applied over a finite convective adjustment time.
使用迭代技术估计云底所需的质量通量，通过环境下沉将其恢复到中性稳定（基于虚拟湿静力能量准则）；质量通量在有限的对流调整时间内应用。

#### SUBROUTINE MSTCNV contains 7 primary physics loops / 子程序MSTCNV包含7个主要物理循环

**(1) CLOUD_BASE**: loops over successive potential cloud base levels (<tt>LMIN</tt>) from <tt>L=1</tt> to <tt>L=LMCM-1</tt>, where <tt>LMCM</tt> is the highest possible cloud base level for practical purposes (e.g., the tropopause) set in the rundeck, to test for initiation of moist convection; determines whether cloud base is unstable; if so, calls MASS_FLUX.
**云底循环**：从 <tt>L=1</tt> 到 <tt>L=LMCM-1</tt> 遍历连续的潜在云底层级（<tt>LMIN</tt>），其中 <tt>LMCM</tt> 是实际目的的最高可能云底层级（例如对流层顶）在rundeck中设置，以测试湿润对流的触发；确定云底是否不稳定；如果是，调用MASS_FLUX。

**(2) CLOUD_TYPES**: loops over the two convective plumes (<tt>ITYPE=2</tt>) into which the mass flux is partitioned to perform most of the convective physics; partitions gridbox into (convection + subsidence) and (stratiform cloud + clear sky) parts; executes CLOUD_TOP loop, DOWNDRAFT loop, environmental subsidence loop, EVAP_PRECIP loop.
**云型循环**：遍历质量通量分配的两个对流羽流（<tt>ITYPE=2</tt>），以执行大多数对流物理；将网格盒分成（对流+下沉）和（层状云+晴空）部分；执行云顶循环、下沉循环、环境下沉循环、蒸发降水循环。

**(3) CLOUD_TOP**: loops from the level above cloud base (<tt>LMIN+1</tt>) potentially to the top model level (<tt>LM</tt>), calculating properties of the updraft, but exits when cloud top is reached (<tt>LMAX</tt>); tests whether triggering conditions for convection are satisfied; lifts parcel moist adiabatically; determines condensate phase; condenses vapor, releases latent heat; advects condensate up from below; entrains environmental air into parcel; calculates convective momentum transport; detrains air when parcel buoyancy becomes negative; checks for downdraft initiation; computes cumulus updraft speed; calls CONVECTIVE_MICROPHYSICS; removes vertically advected condensate from total convective condensate.
**云顶循环**：从云底以上的层级（<tt>LMIN+1</tt>）到顶层模型层级（<tt>LM</tt>）循环，计算上升气流的属性，但在到达云顶时退出（<tt>LMAX</tt>）；测试对流的触发条件是否满足；湿绝热抬升气块；确定凝结物相；凝结水汽，释放潜热；从下部向上平流凝结物；将环境空气卷入气块；计算对流动量输送；当气块浮力变为负值时夹卷空气；检查下沉气流的触发；计算积云上升速度；调用CONVECTIVE_MICROPHYSICS；从总对流凝结物中移除垂直平流的凝结物。

**(4) DOWNDRAFT**: loops from downdraft formation level (<tt>LDRAFT</tt>) down to surface to determine how far downdraft penetrates and transport relevant properties; the downdraft is exposed to 50% the convective precipitation when <tt>FDDRT = 0.5</tt> and evaporates as much of it as necessary to remain saturated; evaporates convective condensate into downdraft; entrains environmental air; detrains mixture into environment if positively buoyant; calculates downdraft momentum transport; adds air to downdraft in next lower layer if still negatively buoyant.
**下沉循环**：从下沉形成层级（<tt>LDRAFT</tt>）向下到地面循环，以确定下沉气流渗透多远并输送相关属性；当 <tt>FDDRT = 0.5</tt> 时，下沉气流暴露于50%的对流降水，并蒸发尽可能多的降水以保持饱和；将对流凝结物蒸发到下沉气流中；卷入环境空气；如果正浮力，将混合物夹卷到环境中；计算下沉动量输送；如果在下一层仍为负浮力，则将空气添加到下沉气流中。

**(5) SUBSIDENCE**: loops between <tt>LMIN</tt> and <tt>LMAX</tt> to calculate changes of heat, moisture, momentum due to compensating environmental subsidence (adiabatic warming and drying); calculates subsidence mass as difference between updraft and downdraft; uses an upwind scheme for momentum and a quadratic updraft scheme for heat and moisture.
**补偿环境下沉循环**：在 <tt>LMIN</tt> 和 <tt>LMAX</tt> 之间循环，以计算由于补偿环境下沉（绝热增温和干燥）引起的热量、水分、动量的变化；计算下沉质量为上升和下沉气流质量通量之差；对动量使用迎风格式，对热量和水分使用二次迎风格式。

**(6) EVAP_PRECIP**: loops from the level below cloud top (<tt>LMAX-1</tt>) to the lowest model level to calculate precipitation flux and to evaporate falling precipitation; precipitation is allowed to evaporate into the environment above and below cloud base, and with the default setting <tt>FDDRT = 0.5</tt>, 50% of precipitation is first given a chance to evaporate into the downdraft; calls MC_CLOUD_FRACTION; defines gridbox area available for evaporation; calls MC_PRECIP_PHASE; evaporates condensate and cools air.
**蒸发降水循环**：从云顶以下的层级（<tt>LMAX-1</tt>）到最低模型层级循环，以计算降水通量并蒸发下落的降水；降水被允许在云底上方和下方的环境中蒸发，使用默认设置 <tt>FDDRT = 0.5</tt>，50%的降水首先有机会在下沉气流中蒸发；调用MC_CLOUD_FRACTION；定义可用于蒸发的网格盒面积；调用MC_PRECIP_PHASE；蒸发凝结物并冷却空气。

**(7) OPTICAL_THICKNESS**: loops over levels with convection to calculate the visible optical thicknesses of convective clouds and anvils that are passed to the radiation scheme; calculates optical thickness of precipitation below cloud; calls ANVIL_OPTICAL_THICKNESS.
**光学厚度循环**：遍历有对流的层级，以计算传递给辐射方案的对流云和砧云的可见光学厚度；计算云下降水的光学厚度；调用ANVIL_OPTICAL_THICKNESS。

### Stratiform clouds / 层状云

The stratiform cloud parameterization subroutine LSCOND is based originally on Del Genio et al. (1996), with updates described in Schmidt et al. (2006) and further updates for CMIP5.
层状云参数化子程序LSCOND最初基于Del Genio等（1996），在Schmidt等（2006）中描述了更新，并为CMIP5进行了进一步更新。

It calculates cloud fraction diagnostically as a function of relative humidity using a Sundqvist-type approach; cloud areal fraction is differentiated from cloud volume fraction based on convective stability in the free troposphere and the strength of cloud top entrainment in the boundary layer, i.e., in the absence of moist convection clouds are vertically subgrid-scale for estimating cloud fraction and optical thickness effects on radiation.
它使用Sundqvist型方法诊断性地计算云分数作为相对湿度的函数；云面积分数与云体积分数根据自由对流层中的对流稳定性和边界层中云顶卷入的强度进行区分，即在缺乏湿润对流的情况下，云在垂直上是次网格尺度的，用于估计云分数和光学厚度对辐射的影响。

The threshold relative humidity for cloud formation is a function of the grid-scale vertical velocity above the boundary layer, with a scale-aware correction for layer thickness; within the boundary layer the threshold relative humidity is based on an assumed Gaussian distribution of saturation deficit; both thresholds can be multiplied by scaling parameters to bring the model into global radiation balance.
云形成的阈值相对湿度是边界层上方网格尺度垂直速度的函数，具有对层厚的尺度感知修正；在边界层内，阈值相对湿度基于假设的高斯饱和亏损分布；两个阈值都可以乘以缩放参数以使模型达到全球辐射平衡。

Stratiform clouds do not form in subsaturated air below cloud top in the convective portion of the gridbox or below the cloud base of a boundary layer convective cloud.
在网格盒的对流部分云顶以下的次饱和空气中，或在边界层对流云的云底以下，不形成层状云。

In thermodynamically unfavorable conditions, complete stratiform cloud erosion by evaporation up to the threshold relative humidity is allowed.
在热力学不利条件下，允许通过蒸发完全侵蚀层状云直到阈值相对湿度。

Cloud water content is a prognostic variable, including sources due to large-scale condensation and convective detrainment, and sinks due to cloud-top entrainment, autoconversion, accretion, and evaporation.
云水含量是一个预报变量，包括由于大尺度凝结和对流夹卷的源，以及由于云顶卷入、自动转化、碰并和蒸发的汇。（原文拼写：autconversion）

The microphysics is single-moment for the NINT and TCAD versions of the model; for TCADI runs, cloud-aerosol interactions responsible for the first indirect effect are accounted for with a prognostic equation for droplet number concentration based on Morrison and Gettelman (2009).
对于模型的NINT和TCAD版本，微物理是单矩的；对于TCADI运行，基于Morrison和Gettelman（2009）的液滴数浓度预报方程，考虑了负责第一间接效应的云-气溶胶相互作用。

There is a single prognostic equation for cloud water; the mixed phase region extends down to a temperature of -35C, and in the mixed-phase temperature range the instantaneous phase is determined stochastically with a temperature-dependent probability of ice vs. liquid.
有一个云水的单一预报方程；混合相区域延伸到-35°C的温度，在混合相温度范围内，瞬时相随机确定，具有温度依赖的冰与液体的概率。

The phase in which cloud forms is maintained until the cloud dissipates unless supercooled liquid is glaciated by the Bergeron-Findeisen process; convective snow is not permitted to glaciate a supercooled stratiform cloud.
云形成的相被维持直到云消散，除非过冷液体被Bergeron-Findeisen过程冰川化；对流雪不被允许冰川化过冷层状云。

The probability of Bergeron-Findeisen glaciation depends on temperature and on the mass of ice falling into a layer of supercooled liquid cloud.
Bergeron-Findeisen冰川化的概率取决于温度和落入过冷液态云层的冰的质量。

Precipitation that forms from supercooled liquid has a temperature- and mass-dependent probability of existing as snow.
由过冷液体形成的降水具有温度和质量依赖的存在为雪的概率。

At temperatures colder than -35C the critical supersaturation for homogeneous nucleation of ice is based on Karcher and Lohmann (2002).
在低于-35°C的温度下，冰的均质成核的临界过饱和基于Karcher和Lohmann（2002）。

Cloud optical thickness is based on the predicted cloud water content, the subgrid cloud physical thickness, and an effective radius based on either assumed (NINT, TCAD) or predicted (TCADI) number concentrations; the optical thickness of precipitation is accounted for by the radiation by assuming an effective radius 5 times that of the cloud water from which it forms.
云光学厚度基于预测的云水含量、次网格云物理厚度和基于假设（NINT、TCAD）或预测（TCADI）数浓度的有效半径；降水的光学厚度通过假设有效半径为其形成的云水的5倍来考虑。

Cloud fraction and optical thickness are passed to the radiation subroutine, which uses a random number comparison to the calculated cloud fraction to assign clear or overcast conditions in each layer and timestep; the random number is varied so as to mimic the statistics of mixed maximum-random overlap.
云分数和光学厚度被传递给辐射子程序，后者使用随机数与计算云分数的比较来分配每层和时间步的晴空或阴天条件；随机数变化以模拟混合最大-随机重叠的统计。

#### References / 参考文献

Del Genio, A.D., M.-S. Yao, W. Kovari and K.K.-W. Lo, 1996: A prognostic cloud water parameterization for global climate models. J. Climate, 9, 270-304.

Schmidt, G. A., R. Ruedy, J.E. Hansen, I. Aleinov, N. Bell, M. Bauer, S. Bauer, B. Cairns, Y. Cheng, A. DelGenio, G. Faluvegi, A.D. Friend, T.M. Hall, Y. Hu, M. Kelley, N. Kiang, D. Koch, A.A. Lacis, J. Lerner, K.K. Lo, R.L. Miller, L. Nazarenko, V. Oinas, J. Perlwitz, J. Perlwitz, D. Rind, A. Romanou, G.L. Russell, M. Sato, D.T. Shindell, P.H. Stone, S. Sun, N. Tausnev, D. Thresher, and M.-S. Yao, 2006: Present day atmospheric simulations using GISS ModelE: Comparison to in-situ, satellite and reanalysis data. J. Clim., 19, 153-192.

#### SUBROUTINE LSCOND contains 3 primary physics loops / 子程序LSCOND包含3个主要物理循环

**(1) CLOUD_FORMATION**: Most stratiform cloud calculations are performed in a major loop over model layers from the 50 mb level down to the surface. Major calculations are executed in this loop in the following sequence: Determine vertical velocity for threshold relative humidity; calculate probability of ice formation, determine phase, and determine where Bergeron-Findeisen glaciation is active; determine the appropriate saturation reference for calculating relative humidity; release latent heat in the event of a cloud phase change; calculate relative humidity for the clear-sky portion of the gridbox; calculate the autconversion rate; compare gridbox relative humidity to threshold value, and if favorable for cloud formation calculate the large-scale convergence source of cloud water; calculate rain and cloud water evaporation; calculate the net latent heating and cloud water change due to any phase changes; calculate phase changes of precipitation due to melting or glaciation of rain falling into an ice cloud layer; compute the stratiform cloud fraction.
**云形成循环**：大多数层状云计算在从50 mb层级到地面的模型层级主循环中执行。主要计算在此循环中按以下顺序执行：确定阈值相对湿度的垂直速度；计算冰形成的概率，确定相，并确定Bergeron-Findeisen冰川化在何处活跃；确定用于计算相对湿度的适当饱和参考；在云相变的情况下释放潜热；计算网格盒晴空部分的相对湿度；计算自动转化率；将网格盒相对湿度与阈值比较，如果有利于云形成，则计算云水的大尺度辐合源；计算雨和云水蒸发；计算由于任何相变引起的净潜热加热和云水变化；计算由于雨落入冰云层融化或冰川化引起的降水相变；计算层状云分数。

**(2) CLOUD_TOP_ENTRAINMENT**: Following the major loop that determines cloud existence and water content in each layer, another loop is executed from 50 mb down to the surface that identifies each cloud top and calculates the temperature and total water content jump across the cloud top to determine the amount of cloud-top entrainment mixing; the mixing rate is proportional to the magnitude of the virtual moist static energy jump based on cloud-top entrainment instability studies; temperature, humidity, and momentum within the cloud top layer; cloud water mixed upward across the interface is evaporated in the first clear layer above.
**云顶卷入循环**：在确定每层云存在和水含量的主循环之后，执行另一个从50 mb到地面的循环，识别每个云顶并计算云顶处的温度和总水含量跃变，以确定云顶卷入混合的量；混合率与基于云顶卷入不稳定性研究的虚拟湿静力能量跃变的大小成正比；云顶层内的温度、湿度和动量；向上穿过界面混合的云水在上方第一个晴空层中蒸发。

**(3) OPTICAL_THICKNESS**: The next loop, going from the surface to 50 mb, calculates cloud particle effective radius and optical thickness based on either the assumed (NINT, TCAD) or predicted (TCADI) number concentration and the predicted cloud water content and phase.
**光学厚度循环**：下一个循环从地面到50 mb，基于假设（NINT、TCAD）或预测（TCADI）数浓度和预测的云水含量和相，计算云粒子有效半径和光学厚度。

For diagnostic purposes, the model also contains options to calculate an ISCCP simulator version of the cloud fraction and radiative properties (SUBROUTINE ISCCP_CLOUD_TYPES).
为了诊断目的，模型还包含计算云分数和辐射属性的ISCCP模拟器版本的选项（子程序ISCCP_CLOUD_TYPES）。

**Document End / 文档结束**
