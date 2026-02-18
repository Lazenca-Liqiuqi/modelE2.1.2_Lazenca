# Surface fluxes / 表面通量

Surface fluxes are calculated separately for each land surface type (open water, ice, earth and land ice).
表面通量分别为每种陆面类型（开阔水域、冰、陆地和陆地冰）单独计算。

For each type, a different high resolution PBL calculation is done to extrapolate the first layer atmospheric properties to the surface (defined as 10m above the ground).
对于每种类型，进行不同的高分辨率PBL（行星边界层）计算，将第一层大气属性外推到表面（定义为地面以上10米处）。

The diffusion parameters in the PBL layers are functions of the local turbulence closure scheme (Hartke and Rind, 1997; Cheng et al, 2002) and are iterated to get a robust estimate of the surface properties (temperature, humidity, and tracer concentration) and fluxes.
PBL层中的扩散参数是局地湍流闭合方案的函数（Hartke和Rind, 1997; Cheng等, 2002），并通过迭代获得表面属性（温度、湿度和示踪物浓度）和通量的稳健估计。

Generally, 2 or 4 surface flux time steps are done every hour, depending on the vertical resolution.
通常，每小时进行2或4个表面通量时间步，取决于垂直分辨率。

Between the surface and the middle of the first GCM layer, instead of applying the usual interpolation scheme using the similarity laws, the model integrates closure equations for velocity, potential temperature, humidity and other scalars over the subgrid levels, to find their surface values.
在表面和第一GCM层中部之间，模型不使用相似律的常规插值方案，而是在次网格层级上对速度、位温、湿度和其他标量的闭合方程进行积分，以求得它们的表面值。

This procedure, which is unique among the GCMs, is convenient for adding more physics and allows coarse vertical resolutions near the surface.
这一过程在GCM中是独特的，便于添加更多物理过程，并允许表面附近采用较粗的垂直分辨率。

### References / 参考文献

Brutsaert, W.H., 1982, Evaporation into the Atmosphere, D. Reidel, Norwell, Mass., 1982.

Cheng, Y., V.M. Canuto, and A.M. Howard, 2002: An improved model for the turbulent PBL. J. Atmos. Sci., 59, 1550-1565.

Emanuel KA and Zivkovic-Rothman M, 1999: Development and evaluation of a convection scheme for use in climate models, J. Atmos. Sci., 56, 1766-1782.

Hartke, G.J., and D. Rind, 1997: Improved surface and boundary layer models for the Goddard Institute for Space Studies general circulation model. J. Geophys. Res., 102, 16407-16442.

Moeng, C.-H., and P. P. Sullivan, 1994: A comparison of shear- and buoyancy-driven planetary boundary layer flows. J. Atmos. Sci., 51, 999-1022.

Nakanishi, M., 2001: Improvement of the Mellor-Yamada turbulence closure model based on large-eddy simulation data. Bound.-Layer Meteor., 99, 349-378.

Redelsperger, J.L., F. Guichard, and S. Mondon, 2000: A parameterization of mesoscale enhancement of surface fluxes for large-scale models. J. Climate, 13, 402-421.

### Description of PBL_DRV.f / PBL_DRV.f描述

#### MODULE PBL_DRV / 模块PBL_DRV

This module is to compute the turbulent transport of momentum, heat and moisture between the surface and the middle of the first GCM layer to find the values of the various PBL variables at the surface.
该模块用于计算表面和第一GCM层中部之间的动量、热量和水分的湍流输送，以求得各种PBL变量在表面的值。

It contains the subroutine PBL.
它包含子程序PBL。

#### SUBROUTINE PBL / 子程序PBL

contains code common for all surface.
包含所有表面通用的代码。

It calculates pbl profiles, for each surface type, to find the values of the various PBL variables at the surface, and accumulates diagnostics and output.
它为每种表面类型计算PBL廓线，以求得各种PBL变量在表面的值，并累积诊断和输出。

It is called from within the subroutine SURFCE (for itype=1, 2 and 3, i.e., surface types ocean, seaice and landice respectively, in SURFACE.f), and from within the subroutine earth (for itype=4, i.e., surface type land, in GHY_DRV.f).
它从子程序SURFCE内部调用（对于itype=1、2和3，即SURFACE.f中的表面类型海洋、海冰和陆地冰），并从子程序earth内部调用（对于itype=4，即GHY_DRV.f中的表面类型陆地）。

Dynamic equations for the mean turbulent variables are integrated over npbl(=8) sublayers between the surface (sublayer 1) and the middle of the first GCM layer (sublayer npbl), using tridiagonal method.
平均湍流变量的动力学方程在表面（子层1）和第一GCM层中部（子层npbl）之间的npbl（=8）个子层上使用三对角方法进行积分。

PBL_DRV.f also contains the following subroutines:
PBL_DRV.f还包含以下子程序：

#### SUBROUTINE INIT_PBL / 子程序INIT_PBL

sets up the initialization of wind, virtual potential temperature, and specific humidity fields in the boundary layer (between the surface and the middle of the first GCM layer).
设置边界层（表面和第一GCM层中部之间）中风、虚拟位温和比湿场的初始化。

The initial values of these fields are obtained by solving the static equations for these fields using the turbulence model of Cheng et al. (2002).
这些场的初始值通过使用Cheng等（2002）的湍流模型求解这些场的静态方程获得。

These initial values are used when starting from a restart file that does not have these data stored.
当从没有存储这些数据的重启文件开始时，使用这些初始值。

It is called by subroutine INPUT (in MODELE.f).
它由子程序INPUT调用（在MODELE.f中）。

#### SUBROUTINE LOADBL / 子程序LOADBL

initializes boundary layer calculation each surface time step.
每个表面时间步初始化边界层计算。

It checks to see if ice has melted or frozen out of one grid box (i,j).
检查某个网格盒（i,j）中的冰是否融化或冻结析出。

It is called from subroutine SURFCE (in SURFACE.f).
它由子程序SURFCE调用（在SURFACE.f中）。

#### SUBROUTINE SETBL / 子程序SETBL

initializes variables in the boundary layer for one surface type using values of another surface type, in one grid box (i,j).
在一个网格盒（i,j）中，使用另一种表面类型的值初始化一种表面类型的边界层变量。

It is called from subroutine loadbl.
它由子程序loadbl调用。

#### SUBROUTINE GETZTOP / 子程序GETZTOP

computes the value of ztop, the height in meters of the middle of the first GCM layer.
计算ztop的值，即第一GCM层中部的高度（以米为单位）。

It is called by subroutine init_pbl.
它由子程序init_pbl调用。

#### SUBROUTINE CHECKPBL / 子程序CHECKPBL

checks whether PBL data are reasonable (to check if the data contain NaN/INF).
检查PBL数据是否合理（检查数据是否包含NaN/INF）。

It is called by subroutine CHECKT, the latter is called from PROGRAM GISS_modelE (in MODELE.f).
它由子程序CHECKT调用，后者由程序GISS_modelE调用（在MODELE.f中）。

### Description of PBL.f / PBL.f描述

#### MODULE SOCPBL / 模块SOCPBL

This module defines subroutines and variables associated with the boundary layer physics.
该模块定义与边界层物理相关的子程序和变量。

It sets up npbl(=8) sublayers between the surface (sublayer 1) and the middle of the first GCM layer (sublayer npbl), and integrates, over these sublayers, the dynamic equations for the mean turbulent variables using turbulence models, to find the surface values of these variables and related fluxes.
它在表面（子层1）和第一GCM层中部（子层npbl）之间设置npbl（=8）个子层，并使用湍流模型在这些子层上对平均湍流变量的动力学方程进行积分，以求得这些变量的表面值和相关通量。

t_pbl_args is a derived type structure which contains all input/output arguments for PBL.
t_pbl_args是一个派生类型结构，包含PBL的所有输入/输出参数。

SOCPBL contains the following subroutines:
SOCPBL包含以下子程序：
```
advanc,stars,getl,dflux,simil,griddr,tfix
ccoeff0,getk,e_eqn,t_eqn,q_eqn,uv_eqn,
t_eqn_sta,q_eqn_sta,uv_eqn_sta,
inits,tcheck,ucheck,check1,output,rtsafe.
```

#### SUBROUTINE ADVANC / 子程序ADVANC

time steps the solutions for the boundary layer variables.
对边界层变量的解进行时间步进。

It is called from within the subroutine pbl (in PBL_DRV.f).
它由子程序pbl调用（在PBL_DRV.f中）。

All its outputs are contained in the structure pbl_args (an instance of t_pbl_args).
其所有输出包含在结构pbl_args中（t_pbl_args的实例）。

```
US     = x component of surface wind, positive eastward (m/s)
        表面风x分量，向东为正（米/秒）
VS     = y component of surface wind, positive northward (m/s)
        表面风y分量，向北为正（米/秒）
WSGCM  = magnitude of the GCM surface wind - ocean currents (m/s)
        GCM表面风的大小 - 洋流（米/秒）
WSPDF  = mean surface wind calculated from PDF of wind speed (m/s)
        根据风速PDF计算的平均表面风（米/秒）
WS     = magn of GCM surf wind - ocean curr + buoyancy + gust (m/s)
        GCM表面风的大小 - 洋流 + 浮力 + 阵风（米/秒）
TSV    = virtual potential temperature of the surface (K)
        表面虚拟位温（开尔文）
QS     = surface value of the specific moisture
        比湿的表面值
DBL    = boundary layer height (m)
        边界层高度（米）
KMS    = momentum transport coefficient at ZGS (m**2/s)
        ZGS处的动量输送系数（平方米/秒）
KHS    = heat transport coefficient at ZGS (m**2/s)
        ZGS处的热量输送系数（平方米/秒）
KHQ    = moist transport coefficient at ZGS (m**2/s)
        ZGS处的水分输送系数（平方米/秒）
PPBL   = pressure at DBL (mb)
        DBL处的气压（毫巴）
USTAR  = friction speed (square root of momentum flux) (m/s)
        摩擦速度（动量通量的平方根）（米/秒）
CM     = drag coefficient (dimensionless surface momentum flux)
        曳力系数（无量纲表面动量通量）
CH     = Stanton number   (dimensionless surface heat flux)
        Stanton数（无量纲表面热通量）
CQ     = Dalton number    (dimensionless surface moisture flux)
        Dalton数（无量纲表面水分通量）
```

#### SUBROUTINE STARS / 子程序STARS

computes the friction speed, ustar, the virtual potential temperature scale, tstar, and the specific humidity scale, qstar.
计算摩擦速度ustar、虚拟位温尺度tstar和比湿尺度qstar。

Note that:
注意：
```
surface momentum flux = ustar*ustar
表面动量通量 = ustar*ustar
surface heat flux     = ustar*tstar
表面热通量     = ustar*tstar
surface moisture flux = ustar*qstar
表面水分通量 = ustar*qstar
```

It also calculates and outputs the Monin-Obukhov length, lmonin, the roughness lengths (z0m,z0h,z0q), the drag coefficient (cm), the Stanton number (ch) and the Dalton number (cq) by calling subroutine dflux.
它还通过调用子程序dflux计算并输出Monin-Obukhov长度lmonin、粗糙长度（z0m,z0h,z0q）、曳力系数（cm）、Stanton数（ch）和Dalton数（cq）。（原文拼写：Monin-Obukov）

#### SUBROUTINE GETL1 / 子程序GETL1

estimates the master length scale, lscale, of the turbulence model on the secondary grid, zhat.
估计次网格zhat上湍流模型的主长度尺度lscale。

#### SUBROUTINE GETL / 子程序GETL

computes the master length scale, lscale, of the turbulence model on the secondary grid, zhat, using the formulas by Nakanishi (2001) from the LES data.
使用Nakanishi（2001）根据LES数据的公式计算次网格zhat上湍流模型的主长度尺度lscale。

#### SUBROUTINE DFLUX / 子程序DFLUX

computes the dimensionless surface fluxes of momentum, heat and moisture (drag coefficient Cm , Stanton number Ch, and Dalton number Cq), with explicit Schmidt number (Sc) and Prandtl number (Pr) dependence and flexibility for water isotopes.
计算动量、热量和水分的无量纲表面通量（曳力系数Cm、Stanton数Ch和Dalton数Cq），具有明确的施密特数（Sc）和普朗特数（Pr）依赖关系以及对水同位素的灵活性。

It also computes the roughness lengths for momentum, z0m (for itype=1 or 2, i.e., surface type ocean or seaice), for temperature, z0h, and for water vapor, z0q, all in meters (Hartke and Rind, 1997).
它还计算动量的粗糙长度z0m（对于itype=1或2，即表面类型海洋或海冰）、温度的粗糙长度z0h和水汽的粗糙长度z0q，均以米为单位（Hartke和Rind, 1997）。

It is called from within subroutine stars.
它由子程序stars调用。

#### SUBROUTINE GETZHQ / 子程序GETZHQ

calculates the roughness lengths for heat (z0h) and for humidity (z0q), modified from Eqs 5.24, 5.27 and 5.35 in Brutsaert (1982).
计算热量（z0h）和湿度（z0q）的粗糙长度，修改自Brutsaert（1982）中的公式5.24、5.27和5.35。

It is called from within subroutine dflux.
它由子程序dflux调用。

#### SUBROUTINE GETCM / 子程序GETCM

calculates the drag coefficient for momentum (cm) (Hartke and Rind, 1997).
计算动量的曳力系数（cm）（Hartke和Rind, 1997）。

It is called from within subroutine dflux.
它由子程序dflux调用。

#### SUBROUTINE GETCHQ / 子程序GETCHQ

calculates the drag coefficients for heat/water (chq) (Hartke and Rind, 1997).
计算热量/水分的曳力系数（chq）（Hartke和Rind, 1997）。

it is called from within subroutine dflux.
它由子程序dflux调用。

#### SUBROUTINE SIMIL / 子程序SIMIL

calculates the similarity solutions for wind speed, virtual potential temperature, and moisture mixing ratio at main grid height z.
计算主网格高度z处的风速、虚拟位温和水分混合比的相似解。

It is called from within the subroutine out for diagnostic purposes.
它由子程序out调用，用于诊断目的。

#### SUBROUTINE GRIDDR / 子程序GRIDDR

computes altitudes on the vertical grid.
计算垂直网格上的高度。

The xi coordinates are uniformly spaced and are mapped in a log-linear fashion onto the z grid.
xi坐标均匀分布，并以对数-线性方式映射到z网格上。

(The z's are the physical coords.)
（z是物理坐标。）

Also computes the altitudes on the secondary grid, zhat, and the derivatives dxi/dz evaluated at both all z and zhat.
还计算次网格zhat上的高度以及在所有z和zhat处计算的导数dxi/dz。

z and zhat are staggered: mean quantities are calculated at z, turbulent kinetic energy and fluxes are calculated at zhat.
z和zhat交错：平均量在z处计算，湍流动能和通量在zhat处计算。

#### SUBROUTINE TFIX / 子程序TFIX

linearly interpolates between the ground temperature tgrnd and the virtual potential temperature at the middle of the first GCM layer to reset the T(z) profile.
在地面温度tgrnd和第一GCM层中部的虚拟位温之间进行线性插值，以重置T(z)廓线。

It is called when the T(z) profile becomes irregular.
当T(z)廓线变得不规则时调用它。

#### SUBROUTINE CCOEFF0 / 子程序CCOEFF0

sets/calculates model coefficients for the GISS 2002 turbulence model (Cheng et al., 2002).
设置/计算GISS 2002湍流模型的模型系数（Cheng等, 2002）。

#### SUBROUTINE GET_TV / 子程序GET_TV

converts temperature T to virtual temperature Tv.
将温度T转换为虚拟温度Tv。

#### SUBROUTINE GETK / 子程序GETK

computes the turbulent diffusivities for momentum, Km, for heat, Kh, for moisture, Kq and for kinetic energy, Ke, at the secondary grids, using the GISS second order closure model (Cheng et al., 2000).
使用GISS二阶闭合模型（Cheng等, 2000）计算次网格上的动量湍流扩散系数Km、热量Kh、水分Kq和动能Ke。

u,v,t,q,ke are calculated at the primary grid z, while e,lscale,km,kh,gm,gh are calculated at the secondary grid zhat.
u,v,t,q,ke在主网格z处计算，而e,lscale,km,kh,gm,gh在次网格zhat处计算。

#### SUBROUTINE E_EQN / 子程序E_EQN

integrates differential eqns for the turbulent kinetic energy, e, using tridiagonal method over npbl-1(=7) sublayer edges (i.e., the secondary grids).
使用三对角方法在npbl-1（=7）个子层边缘（即次网格）上对湍流动能e的微分方程进行积分。

The boundary condition near the bottom is:
底部附近的边界条件是：
```
e(1)=(1/2)*B1**(2/3)*ustar**2.
```

At the top secondary grid, nearest to the middle of the first GCM layer, e is prescribed.
在最接近第一GCM层中部的顶部次网格处，e是指定的。

#### SUBROUTINE E_LES / 子程序E_LES

finds the turbulent kinetic energy, e, at the secondary grids, according to the parameterization of the LES data by Moeng and Sullivan (1994) and the turbulence model of Cheng et al. (2002).
根据Moeng和Sullivan（1994）的LES数据参数化和Cheng等（2002）的湍流模型，在次网格处求得湍流动能e。

#### SUBROUTINE T_EQN / 子程序T_EQN

integrates differential eqns for the virtual potential temperature, T, using tridiagonal method over npbl(=8) sublayers between the surface (sublayer 1) and the middle of the first GCM layer (sublayer npbl).
使用三对角方法在表面（子层1）和第一GCM层中部（子层npbl）之间的npbl（=8）个子层上对虚拟位温T的微分方程进行积分。

The boundary condition at the bottom is:
底部的边界条件是：
```
kh * dt/dz = ch * ( usurf*(t1 - tgrnd)
             +(1+xdelt*q1)*(usurf-usurf0)*tprime )
```

which includes the effects on the surface flux due to the moist convection wind gustiness and the downdraft temperature perturbation (Redelsperger et al. 2000; Emanuel and Zivkovic 1999), where
其中包括由于湿润对流风阵风性和下沉温度扰动对表面通量的影响（Redelsperger等, 2000; Emanuel和Zivkovic, 1999），其中
```
tprime=tdns-t1/(1+xdelt*q1),
```

t1, q1 are the T and Q at the surface, and tdns is the downdraft temperature in K at (i,j), which is calculated in subroutines CONDSE (in CLOUDS2_DRV.f) and PBL (in PBL_DRV.f).
t1, q1是表面处的T和Q，tdns是（i,j）处的下沉温度（开尔文），在子程序CONDSE（在CLOUDS2_DRV.f中）和PBL（在PBL_DRV.f中）计算。

At the top, i.e., the middle of the first GCM layer, T is prescribed.
在顶部，即第一GCM层中部，T是指定的。

#### SUBROUTINE Q_EQN / 子程序Q_EQN

integrates differential eqns for the specific humidity, Q, using tridiagonal method over npbl(=8) sublayers between the surface (sublayer 1) and the middle of the first GCM layer (sublayer npbl).
使用三对角方法在表面（子层1）和第一GCM层中部（子层npbl）之间的npbl（=8）个子层上对比湿Q的微分方程进行积分。

The boundary condition at the bottom is:
底部的边界条件是：
```
kq * dq/dz = min ( cq * usurf * (q1 - qgrnd)
             + cq * (usurf-usurf0) * qprime ,
  fr_sat * ( cq * usurf * (q1 - qgrnd)
             + cq * (usurf-usurf0) * qprime )
             - ( 1 - fr_sat ) * flux_max ),
```

which includes the effects on the surface flux due to the moist convection wind gustiness and the downdraft specific humidity perturbation (Redelsperger et al. 2000; Emanuel and Zivkovic 1999), where qprime=qdns-q1, q1 is Q at the surface and qdns is the downdraft humidity in kg/kg, (i,j), which is calculated in subroutines CONDSE (in CLOUDS2_DRV.f) and PBL (in PBL_DRV.f).
其中包括由于湿润对流风阵风性和下沉比湿扰动对表面通量的影响（Redelsperger等, 2000; Emanuel和Zivkovic, 1999），其中qprime=qdns-q1，q1是表面处的Q，qdns是（i,j）处的下沉湿度（千克/千克），在子程序CONDSE（在CLOUDS2_DRV.f中）和PBL（在PBL_DRV.f中）计算。

At the top, i.e., the middle of the first GCM layer, Q is prescribed.
在顶部，即第一GCM层中部，Q是指定的。

#### SUBROUTINE TR_EQN / 子程序TR_EQN

integrates differential eqns for the tracers, TR, using tridiagonal method over npbl(=8) sublayers between the surface (sublayer 1) and the middle of the first GCM layer (sublayer npbl).
使用三对角方法在表面（子层1）和第一GCM层中部（子层npbl）之间的npbl（=8）个子层上对示踪物TR的微分方程进行积分。

The boundary condition at the bottom is:
底部的边界条件是：
```
kq * dtr/dz = sfac * trs - constflx,
i.e. for moisture, sfac=cq*usurf, constflx=cq*usurf*qg,
to get:  kq * dq/dz = cq * usurf * (qs - qg);
for new moisture (including downdraft effects),
sfac=cq*(usurf-dusurf), constflx=cq*(usurf*qg + dusurf*qdns),
or sfac=cq*usurf0, constflx=cq*(usurf*(qg+qdns)-usurf0*qdns),
to get:  kq * dq/dz = cq*(usurf*(qs-qg) + dusurf*(qdns-qs)).
```

This should be flexible enough to deal with most situations.
这应该足够灵活以处理大多数情况。

At the top, i.e., the middle of the first GCM layer, TR is prescribed.
在顶部，即第一GCM层中部，TR是指定的。

#### SUBROUTINE UV_EQN / 子程序UV_EQN

integrates differential eqns for mean velocity u and v using tridiagonal method over npbl(=8) sublayers between the surface (sublayer 1) and the middle of the first GCM layer (sublayer npbl).
使用三对角方法在表面（子层1）和第一GCM层中部（子层npbl）之间的npbl（=8）个子层上对平均速度u和v的微分方程进行积分。

The boundary condition at the bottom is:
底部的边界条件是：
```
km * du/dz = cm * usurf * u and
km * dv/dz = cm * usurf * v.
```

At the top, i.e., the middle of the first GCM layer, u, v are prescribed.
在顶部，即第一GCM层中部，u, v是指定的。

#### SUBROUTINE T_EQN_STA / 子程序T_EQN_STA

computes the static solutions of the virtual potential temperature, T, between the surface and the first GCM layer.
计算表面和第一GCM层之间虚拟位温T的静态解。

The boundary condition at the bottom is:
底部的边界条件是：
```
kh * dt/dz = ch * usurf * (t - tg).
```

At the top, T is prescribed.
在顶部，T是指定的。

It is called only at the initialization (from within subroutine inits).
仅在初始化时调用（从子程序inits内部）。

#### SUBROUTINE Q_EQN_STA / 子程序Q_EQN_STA

computes the static solutions of the specific humidity, Q, between the surface and the first GCM layer.
计算表面和第一GCM层之间比湿Q的静态解。

The boundary condition at the bottom is:
底部的边界条件是：
```
kq * dq/dz = cq * usurf * (q - qg).
```

At the top, Q is prescribed.
在顶部，Q是指定的。

It is called only at the initialization (from within subroutine inits).
仅在初始化时调用（从子程序inits内部）。

#### SUBROUTINE UV_EQN_STA / 子程序UV_EQN_STA

computes the static solutions of the wind components, u and v, between the surface and the first GCM layer.
计算表面和第一GCM层之间风分量u和v的静态解。

The boundary conditions at the bottom are:
底部的边界条件是：
```
km * du/dz = cm * usurf * u,
km * dv/dz = cm * usurf * v.
```

At the top, u and v are prescribed.
在顶部，u和v是指定的。

It is called only at the initialization (from within subroutine inits).
仅在初始化时调用（从子程序inits内部）。

#### SUBROUTINE LEVEL2 / 子程序LEVEL2

computes the turbulent kinetic energy e (Cheng et al., 2002).
计算湍流动能e（Cheng等, 2002）。

#### SUBROUTINE INITS / 子程序INITS

initializes the winds, virtual potential temperature, and humidity by solving their differential equations for the static solutions, using tridiagonal method over npbl(=8) sublayers between the surface (sublayer 1) and the middle of the first GCM layer (sublayer npbl).
通过求解静态解的微分方程来初始化风、虚拟位温和湿度，使用三对角方法在表面（子层1）和第一GCM层中部（子层npbl）之间的npbl（=8）个子层上。

(Cheng et a., 2002).
（Cheng等, 2002）。

It is called by subroutine init_pbl (in PBL_DRV.f), and the latter (init_pbl) is called by subroutine INPUT (in MODELE.f).
它由子程序init_pbl调用（在PBL_DRV.f中），后者（init_pbl）由子程序INPUT调用（在MODELE.f中）。

#### SUBROUTINE OUTPUT / 子程序OUTPUT

produces output for diagnostic purposes.
产生诊断输出。

#### SUBROUTINE FGRID2 / 子程序FGRID2

fgrid2 computes functional relationship of z and xi; it is used in function rtsafe(fgrid2,x1,x2,xacc), the latter is called by subroutine griddr.
fgrid2计算z和xi的函数关系；它用于函数rtsafe(fgrid2,x1,x2,xacc)中，后者由子程序griddr调用。

**Document End / 文档结束**
