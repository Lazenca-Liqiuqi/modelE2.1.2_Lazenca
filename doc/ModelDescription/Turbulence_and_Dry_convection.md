# Turbulence and Dry convection / 湍流和干对流

There are two methods of vertical mixing outside of the surface layer: Complete mixing is performed if two boxes are statically unstable (using the virtual potential temperature) (DRYCNV); otherwise a turbulence closure is used to estimate the amount of mixing based on the grid-scale properties and available TKE (ATURB).
在表面层外有两种垂直混合方法：如果两个盒子静力不稳定（使用虚拟位温），则执行完全混合（DRYCNV）；否则使用湍流闭合来估计基于网格尺度属性和可用TKE的混合量（ATURB）。

Turbulence effectively transfers heat, moisture, and momentum between the surface and the lower atmosphere, and modifies the atmospheric stability and vertical distributions of these quantities.
湍流有效地在表面和低层大气之间传递热量、水分和动量，并修改这些量的大气稳定度和垂直分布。

In earlier GISS GCMs, dry convective adjustment (using DRYCNV.f instead of ATURB_E1.f or ATURB.f, in the rundeck) was applied to perform the role of turbulence (Hansen et al. 1983).
在早期的GISS GCM中，干对流调整（在rundeck中使用DRYCNV.f代替ATURB_E1.f或ATURB.f）被应用来执行湍流的作用（Hansen等, 1983）。

Since the 1990's turbulence scheme (second order closure scheme plus semi-empirical scheme) have been implemented in the GISS GCM.
自1990年代以来，湍流方案（二阶闭合方案加半经验方案）已在GISS GCM中实现。

There are two versions of the turbulence scheme currently in use.
目前有两个版本的湍流方案在使用。

The older version is contained in ATURB_E1,f, the newer version is in ATURB.f.
旧版本包含在ATURB_E1.f中，新版本在ATURB.f中。（原文拼写：ATURB_E1,f）

They are characterized by:
它们的特点是：

1. a nonlocal vertical transport scheme for virtual potential temperature, specific humidity, and other scalars following Holtslag and Moeng (1991) in ATURB_E1.f, and following Holtslag and Boville (1993) in ATURB.f;
   虚拟位温、比湿和其他标量的非局部垂直输送方案，在ATURB_E1.f中遵循Holtslag和Moeng（1991），在ATURB.f中遵循Holtslag和Boville（1993）；

2. employment of the second-order closure (SOC) scheme of Cheng et al. (2002) that improves several aspects of the standard Mellor-Yamada model (Mellor and Yamada 1982) and in particular, allows mixing at weak turbulence levels (Canuto et al., 2008);
   采用Cheng等（2002）的二阶闭合（SOC）方案，改善了标准Mellor-Yamada模型（Mellor和Yamada, 1982）的几个方面，特别是允许在弱湍流水平下混合（Canuto等, 2008）；

3. diagnosis and use of the nonlocal vertical profile of the turbulent kinetic energy (TKE) according to the large eddy simulation (LES) studies of Moeng and Sullivan (1994);
   根据Moeng和Sullivan（1994）的大涡模拟（LES）研究，诊断和使用湍流动能（TKE）的非局部垂直廓线；

4. a formulation of the turbulence length scale that is similar to (in ATURB_E1.f), or a generalization of (in ATURB.f), that of Holtslag and Boville (1993); ATURB.f also employs a length scale formula for different stabilities by Nakanishi(2001) based on the Large Eddy Simulation (LES) data;
   湍流长度尺度的公式类似于（在ATURB_E1.f中）或推广（在ATURB.f中）Holtslag和Boville（1993）的公式；ATURB.f还采用Nakanishi（2001）基于大涡模拟（LES）数据的不同稳定度的长度尺度公式；

5. calculation of the PBL height using the TKE criterion (in ATURB_E1.f), or the bulk Richardson number criterion (in ATURB.f).
   使用TKE准则（在ATURB_E1.f中）或总体理查森数准则（在ATURB.f中）计算PBL高度。

ATURB.f has significant improvements in cloud and radiation simulations, especially over the subtropical eastern oceans and the southern oceans, over ATURB_E1.f, while the latter yields deeper vertical transports of heat and moisture in the tropics (Yao and Cheng, 2012).
与ATURB_E1.f相比，ATURB.f在云和辐射模拟方面有显著改善，特别是在副热带东部海洋和南部海洋，而后者在热带产生更深的垂直热量和水分输送（Yao和Cheng, 2012）。

### References / 参考文献

Cheng, Y., V.M. Canuto, and A.M. Howard, 2002: An improved model for the turbulent PBL. J. Atmos. Sci., 59, 1550-1565.

Canuto, V.M., Y. Cheng, A.M. Howard, and E.N. Essau, 2008: Stably stratified flows: A model with no Ri(cr). J. Atmos. Sci., 65, 2437-2447.

Hansen, J. E., G. L. Russell, D. Rind, P. Stone, A. Lacis, R. Ruedy, and L. Travis, 1983: Efficient three-dimensional models for climate studies. Mon. Wea. Rev., 111, 609-662.

Holtslag, A. A. M., and C.-H. Moeng, 1991: Eddy diffusivity and countergradient transport in the convective atmospheric boundary layer. J. Atmos. Sci., 48, 1690-1700.

Holtslag, A. A. M., and B. A. Boville, 1993: Local versus nonlocal boundary layer diffusion in a global climate model. J. Climate, 6, 1825-1842.

Mellor, G. L., and T. Yamada, 1982: Development of a turbulence closure model for geophysical fluid problems. Rev. Geophys. Space Phys., 20, 851-875.

Moeng, C.-H., and P. P. Sullivan, 1994: A comparison of shear- and buoyancy-driven planetary boundary layer flows. J. Atmos. Sci., 51, 999-1022.

Nakanishi, M., 2001: Improvement of the Mellor-Yamada turbulence closure model based on large-eddy simulation data. Bound.-Layer Meteor., 99, 349-378.

Yao, M.-S., and Y. Cheng, 2012: Cloud simulations in response to turbulence parameterizations in the GISS Model E GCM. J. Climate, 25, 4963-4974.

### Description of ATURB.f / ATURB.f描述

**SUBROUTINE ATM_DIFFUS** - updates the mean velocity components, potential temperature, and specific humidity (u,v,t and q) due to turbulent transport throughout all GCM layers, using turbulence models for the turbulent transport of momentum, heat and moisture.
更新平均速度分量、位温和比湿（u,v,t和q），由于湍流输送贯穿所有GCM层，使用湍流模型进行动量、热量和水分的湍流输送。

It is called from within the subroutine SURFCE.
它由子程序SURFCE调用。

ATM_DIFFUS consists of the following subroutines:
ATM_DIFFUS由以下子程序组成：
```
getdz,dout,de_solver_main,de_solver_edge,l_gcm,k_gcm,
e_gcm,find_pbl_top,zze,apply_fluxes_to_atm
```

**SUBROUTINE ZZE** - finds the layer middle and edge heights, z and ze.
找到层中点和边缘高度，z和ze。

Note that z(L) is between ze(L) and ze(L+1).
注意z(L)在ze(L)和ze(L+1)之间。

**SUBROUTINE L_GCM** - calculates the turbulent length scale (lscale, in meters).
计算湍流长度尺度（lscale，以米为单位）。

Within the PBL, it is according to Nakanishi(2001); above the PBL, we generalized and employed a formula by Holtslag and Boville (1993).
在PBL内，根据Nakanishi（2001）；在PBL上方，我们推广并采用了Holtslag和Boville（1993）的公式。

**SUBROUTINE K_GCM** - computes the turbulent stability functions Km (for momentum) and Kh (for heat and moisture), as well as the fluxes (local and non-local).
计算湍流稳定性函数Km（用于动量）和Kh（用于热量和水分），以及通量（局地和非局地）。

Within the convective PBL, it is according to Holtslag and Boville (1993); within the stable PBL or above the PBL, it is according to Cheng et al. (2002).
在对流PBL内，根据Holtslag和Boville（1993）；在稳定PBL内或PBL上方，根据Cheng等（2002）。

**SUBROUTINE E_GCM** - finds the turbulent kinetic energy (e, in m^2/s^2).
找到湍流动能（e，单位m^2/s^2）。

Within the PBL, e is determined according to the parameterization of the Large Eddy Simulation (LES) data (Moeng and Sullivan, 1994), above the PBL, e is calculated by the second order closure model of Cheng et al. (2002).
在PBL内，e根据大涡模拟（LES）数据的参数化确定（Moeng和Sullivan, 1994），在PBL上方，e由Cheng等（2002）的二阶闭合模型计算。

**SUBROUTINE FIND_PBL_TOP** - finds the PBL height (dbl, in meters) and the closest corresponding main level (ldbl), using the bulk Richardson number criterion (Holtslag and Boville, 1993).
找到PBL高度（dbl，以米为单位）和最近对应的主层级（ldbl），使用总体理查森数准则（Holtslag和Boville, 1993）。

**SUBROUTINE GETDZ** - computes the 3-d finite difference dz and dze as well as the 3-d density rho (at layer middle) and rhoe (at layer edge).
计算三维有限差分dz和dze以及三维密度rho（在层中点）和rhoe（在层边缘）。

It is called at the primary grid (A-grid).
它在主网格（A网格）上调用的。

**SUBROUTINE DOUT** - writes out monitoring diagnostics at i=itest,j=jtest if call_diag=.true.
如果call_diag=.true，则在i=itest,j=jtest处写出监控诊断。

**SUBROUTINE DE_SOLVER_MAIN** - differential equation solver using tridiagonal method.
使用三对角方法的微分方程求解器。

The differential equation is expressed as
微分方程表示为
```
d/dt x = d/dz (P1 d/dz x) + P4
```
where x is the unknown to be solved, x and P4 are at the layer middle z, while P1 is at the layer edge ze.
其中x是要求解的未知数，x和P4在层中点z处，而P1在层边缘ze处。

**SUBROUTINE DE_SOLVER_EDGE** - differential equation solver using tridiagonal method.
使用三对角方法的微分方程求解器。

The differential equation is expressed as
微分方程表示为
```
d/dt x = d/dz (P1 d/dz x) - P3 x + P4
```
where x is the unknown to be solved, x, P3 and P4 are at the layer edge ze, while P1 is at the layer middle z.
其中x是要求解的未知数，x、P3和P4在层边缘ze处，而P1在层中点z处。

**SUBROUTINE APPLY_FLUXES_TO_ATM** - a dummy subroutine that replaces the real one needed by DRYCNV.
一个虚拟子程序，替换DRYCNV所需的真实子程序。

### Description of ATURB_E1.f / ATURB_E1.f描述

**SUBROUTINE ATM_DIFFUS** - updates the mean velocity components, potential temperature, and specific humidity (u,v,t and q) due to turbulent transport throughout all GCM layers, using turbulence models for the turbulent transport of momentum, heat and moisture.
更新平均速度分量、位温和比湿（u,v,t和q），由于湍流输送贯穿所有GCM层，使用湍流模型进行动量、热量和水分的湍流输送。

It is called from within the subroutine SURFCE.
它由子程序SURFCE调用。

ATM_DIFFUS consists of the following subroutines:
ATM_DIFFUS由以下子程序组成：
```
getdz,dout,de_solver_main,de_solver_edge,l_gcm,k_gcm,
e_gcm,find_pbl_top,zze,apply_fluxes_to_atm
```

**SUBROUTINE ZZE** - finds the layer edge height, ze.
找到层边缘高度ze。

Note that z(L) is between ze(L) and ze(L+1).
注意z(L)在ze(L)和ze(L+1)之间。

**SUBROUTINE L_GCM** - calculates the turbulent length scale (lscale, in meters) according to Holtslag and Boville (1993).
根据Holtslag和Boville（1993）计算湍流长度尺度（lscale，以米为单位）。

**SUBROUTINE K_GCM** - computes the turbulent stability functions Km (for momentum) and Kh (for heat and moisture), as well as the fluxes (local and non-local).
计算湍流稳定性函数Km（用于动量）和Kh（用于热量和水分），以及通量（局地和非局地）。

Within the PBL, it is according to Holtslag and Moeng (1991); above the PBL, it is according to Cheng et al. (2002).
在PBL内，根据Holtslag和Moeng（1991）；在PBL上方，根据Cheng等（2002）。

**SUBROUTINE E_GCM** - finds the turbulent kinetic energy (e, in m^2/s^2).
找到湍流动能（e，单位m^2/s^2）。

Within the PBL, e is determined according to the parameterization of the Large Eddy Simulation (LES) data (Moeng and Sullivan, 1994), above the PBL, e is calculated by the second order closure model of Cheng et al. (2002).
在PBL内，e根据大涡模拟（LES）数据的参数化确定（Moeng和Sullivan, 1994），在PBL上方，e由Cheng等（2002）的二阶闭合模型计算。

**SUBROUTINE FIND_PBL_TOP** - finds the pbl height, dbl=z(ldbl), in meters, where ldbl is a main layer number, using the TKE criterion.
找到pbl高度dbl=z(ldbl)，以米为单位，其中ldbl是主层编号，使用TKE准则。

**SUBROUTINE GETDZ** - computes the 3-d finite difference dz and dze as well as the 3-d density rho (at layer middle) and rhoe (at layer edge).
计算三维有限差分dz和dze以及三维密度rho（在层中点）和rhoe（在层边缘）。

It is called at the primary grid (A-grid).
它在主网格（A网格）上调用的。

**SUBROUTINE DOUT** - writes out monitoring diagnostics at i=itest,j=jtest if call_diag=.true.
如果call_diag=.true，则在i=itest,j=jtest处写出监控诊断。

**SUBROUTINE DE_SOLVER_MAIN** - differential equation solver using tridiagonal method.
使用三对角方法的微分方程求解器。

The differential equation is expressed as
微分方程表示为
```
d/dt x = d/dz (P1 d/dz x) + P4
```
where x is the unknown to be solved, x and P4 are at the layer middle z, while P1 is at the layer edge ze.
其中x是要求解的未知数，x和P4在层中点z处，而P1在层边缘ze处。

**SUBROUTINE DE_SOLVER_EDGE** - differential equation solver using tridiagonal method.
使用三对角方法的微分方程求解器。

The differential equation is expressed as
微分方程表示为
```
d/dt x = d/dz (P1 d/dz x) - P3 x + P4
```
where x is the unknown to be solved, x, P3 and P4 are at the layer edge ze, while P1 is at the layer middle z.
其中x是要求解的未知数，x、P3和P4在层边缘ze处，而P1在层中点z处。

**SUBROUTINE APPLY_FLUXES_TO_ATM** - a dummy subroutine that replaces the real one needed by DRYCNV.
一个虚拟子程序，替换DRYCNV所需的真实子程序。
