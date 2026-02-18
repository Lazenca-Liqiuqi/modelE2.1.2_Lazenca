# Gas Tracers / 气体示踪物

The `TRACERS_SPECIAL_Shindell` selection of tracers, in conjunction with the option `SHINDELL_STRAT_CHEM` is described in Shindell et al., 2012 as follows:
`TRACERS_SPECIAL_Shindell`示踪物选择与`SHINDELL_STRAT_CHEM`选项结合，在Shindell等，2012中描述如下。

The chemical mechanism is fully embedded within modelE, so that chemical constituents are treated consistently with the physics of other parts of the model such as surface fluxes of fundamental physical quantities (e.g. heat) and with transport of momentum and other constituents such as water vapor.
化学机制完全嵌入modelE中，因此化学成分与模型其他部分的物理处理一致，如基本物理量的表面通量（例如热）以及动量和其他成分（如水汽）的输送。

Tropospheric chemistry includes basic NOx-HOx-Ox-CO-CH4 chemistry as well as PANs and the hydrocarbons isoprene, alkyl nitrates, aldehydes, alkenes, and paraffins.
对流层化学包括基本的NOx-HOx-Ox-CO-CH4化学以及PANs和烃类异戊二烯、烷基硝酸酯、醛类、烯烃和烷烃。

The lumped hydrocarbon family scheme was derived from the Carbon Bond Mechanism-4 (CBM-4) [Gery et al., 1989] and from the more extensive Regional Atmospheric Chemistry Model (RACM) [Stockwell et al., 1997], following [Houweling et al., 1998].
集总烃族方案源自碳键机制-4（CBM-4）[Gery等，1989]和更广泛的大气区域化学模型（RACM）[Stockwell等，1997]，遵循[Houweling等，1998]。

To represent stratospheric chemistry, the model includes chlorine- and bromine-containing compounds, and CFC and N2O source gases (as well as an 'age-of-air' passive tracer).
为了表示平流层化学，模型包括含氯和含溴化合物，以及CFC和N2O源气体（以及"空气龄"被动示踪物）。

Aerosol species and chemistry are also included, and chemistry and aerosols are fully integrated, so that these components interact with each other and with the physics of the climate model.
气溶胶物种和化学也包括在内，化学和气溶胶完全集成，使这些组件相互之间以及与气候模型的物理相互作用。

The model contains 51 species for gas-phase chemistry interacting via 156 reactions.
模型包含51个气相化学物种，通过156个反应相互作用。

We use a chemical time step of 1/2 hour, including the calculation of photolysis rates using the Fast-J2 scheme [H. Bian and Prather, 2002].
我们使用1/2小时的化学时间步长，包括使用Fast-J2方案计算光解速率[H. Bian和Prather，2002]。

We include transport and phase transformations of soluble species within convective plumes, scavenging within and below updrafts, rainout within both convective and large-scale clouds, washout below precipitating regions, evaporation of falling precipitation, and both detrainment and evaporation from convective plumes.
我们包括对流羽流中可溶物种的输送和相变、上升气流内和下方的清除、对流云和大尺度云中的雨洗、降水区域下方的冲刷、下降降水的蒸发，以及从对流羽流的夹出和蒸发。

A full description is given in Shindell et al. [2006] and references therein.
完整描述见Shindell等[2006]及其中的参考文献。

The only substantial chemistry changes since [D T Shindell et al., 2006] are as follows: acetone chemistry has been added to the model [Houweling et al., 1998], we have incorporated a newly identified reaction channel of OH + NO2 to form HNO3 whose branching ratio is pressure and temperature dependent [Butkovskaya et al., 2007], polar stratospheric cloud (PSC) formation in the stratosphere is now dependent upon water vapor, temperature and HNO3 [Hanson and Mauersberger, 1988], the heterogeneous hydrolysis of N2O5 on sulfate now follows [Kane et al., 2001] and [Hallquist et al., 2003], and the model now includes terpene emissions and oxidation by OH, O3 and NO3 [Tsigaridis et al., 2005].
自[D T Shindell等，2006]以来的唯一重大化学变化如下：丙酮化学已添加到模型中[Houweling等，1998]，我们纳入了新发现的OH + NO2形成HNO3的反应通道，其分支比依赖于压强和温度[Butkovskaya等，2007]，平流层极地平流层云（PSC）的形成现在依赖于水汽、温度和HNO3[Hanson和Mauersberger，1988]，N2O5在硫酸盐上的非均相水解现在遵循[Kane等，2001]和[Hallquist等，2003]，模型现在包括萜烯排放和被OH、O3和NO3氧化[Tsigaridis等，2005]。

Another development is that now light attenuation by modeled aerosol tracers affects the photolysis rates of gases, following Bian et al. [2003].
另一个发展是，现在模拟气溶胶示踪物的光衰减影响气体的光解速率，遵循Bian等[2003]。

Modeled aerosol optical depths are passed to the photolysis code at every timestep, while the tabulated optical properties required for different aerosol types (extinction efficiency, single scattering albedo, scattering phase function expansion terms) are prescribed according to prior calculations to be consistent with what is used in the model's radiation code.
模拟的气溶胶光学厚度在每个时间步传递给光解代码，而不同气溶胶类型所需的列表光学性质（消光效率、单次散射反照率、散射相函数展开项）根据先前的计算规定，以与模型辐射代码中使用的相一致。

## Main Reference / 主要参考文献

Shindell, D.T., O. Pechony, A. Voulgarakis, G. Faluvegi, L. Nazarenko, J.-F. Lamarque, K. Bowman, G. Milly, B. Kovari, R. Ruedy, and G. Schmidt, 2012: Interactive ozone and methane chemistry in GISS-E2 historical and future climate simulations. Atmos. Chem. Phys., submitted, doi:10.5194/acpd-12-23513-2012.

## Other References / 其他参考文献

Bian, H., and M. Prather (2002), Fast-J2: Accurate simulations of photolysis in global climate models, J. Atmos. Chem., 41, 281-296.

Bian, H., M. Prather, and T. Takemura (2003), Tropospheric aerosol impacts on trace gas budgets through photolysis, Journal of Geophysical Research-Atmospheres, 108(D8), doi:10.1029/2002JD002743|10.1029/2002JD002743.

Butkovskaya, N., A. Kukui, and G. Le Bras (2007), HNO3 Forming Channel of the HO2 + NO Reaction as a Function of Pressure and Temperature in the Ranges of 72-600 Torr and 223-323 K J. Phys. Chem. A, 111, 9047-9053.

Gery, M. W., G. Z. Whitten, J. P. Killus, and M. C. Dodge (1989), A photochemical kinetics mechanism for urban and regional scale computer modeling, J. Geophys. Res., 94, 925-956.

Hallquist, M., D. J. Stewart, S. K. Stephenson, and R. A. Cox (2003), Hydrolysis of N2O5 on sub-micron sulfate aerosols, Phys. Chem. Chem. Phys., 5, 3453-3463.

Hanson, D., and K. Mauersberger (1988), Laboratory studies of the nitric acid tridydrate: Implications for the south polar stratosphere, Geophys. Res. Lett., 15, 855-858.

Houweling, S., F. Dentener, and J. Lelieveld (1998), The impact of non-methane hydrocarbon compounds on tropospheric photochemistry, J. Geophys. Res., 103, 10673-10696.

Kane, S. M., F. Caloz, and M.-T. Leu (2001), Heterogeneous Uptake of Gaseous N2O5 by (NH4)2SO4, NH4HSO4, and H2SO4 Aerosols, J. Phys. Chem. A, 105, 6465-6470.

Shindell, D. T., G. Faluvegi, N. Unger, E. Aguilar, G. A. Schmidt, D. Koch, S. E. Bauer, and R. L. Miller (2006), Simulations of preindustrial, present-day, and 2100 conditions in the NASA GISS composition and climate model G-PUCCINI, Atmos. Chem. Phys., 6, 4427-4459.

Stockwell, W. R., F. Kirchner, M. Kuhn, and S. Seefeld (1997), A new mechanism for regional atmospheric chemistry modeling, 102, 25847-25879.

Tsigaridis, K., J. Lathiere, M. Kanakidou, and D. Hauglustaine (2005), Naturally driven variability in the global secondary organic aerosol over a decade, Atmospheric Chemistry and Physics, 5, 1891-1904.

**Document End / 文档结束**
