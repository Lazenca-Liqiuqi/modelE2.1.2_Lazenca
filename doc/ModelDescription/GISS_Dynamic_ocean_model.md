# GISS Dynamic ocean model / GISS动力学海洋模型

This model is a fully dynamic, non-Boussinesq, mass-conserving free surface ocean model (Russell et al, 1995, 2000, Liu et al 2002, 2003).
该模型是一个完全动力学、非Boussinesq、质量守恒的自由表面海洋模型（Russell等，1995，2000，Liu等，2002，2003）。

The dynamics is based on a modified Arakawa scheme on the C-grid, with a linear upstream scheme for advecting tracers.
动力学基于C网格上改进的Arakawa方案，使用线性迎风格式进行示踪物平流。

Vertical mixing uses the KPP scheme of Large et al (1996).
垂直混合使用Large等（1996）的KPP（K-剖面参数化）方案。

Momentum mixing is modelled as a spatially varying laplacian as in Wajsowicz (1993).
动量混合被建模为空间变化的拉普拉斯算子，如Wajsowicz（1993）所述。

The effects of mesoscale eddies and isopycnal diffusion are parameterised as in Gent and McWilliams (1996), but using variable coefficients (Visbeck et al, 1997), and coded as in Griffies (1998).
中尺度涡和等位密度扩散的效应按照Gent和McWilliams（1996）进行参数化，但使用变系数（Visbeck等，1997），并按Griffies（1998）编写代码。

The model contains up to 12 variable depth subgrid scale straits which connect ocean grid cells, which would not be connected at the resolution used.
该模型包含多达12个可变深度的次网格尺度海峡，这些海峡连接在所用分辨率下无法连接的海洋网格单元。

In particular, the Straits of Gibraltar, Hormuz, and Nares straits are so modelled.
特别是直布罗陀海峡、霍尔木兹海峡和纳雷斯海峡就是这样建模的。

All ocean components are fluxed through these straits as a function of the end to end pressure gradients, balanced against a drag proportional to the straits 'width' which serves as a tuning parameter to get reasonable fluxes.
所有海洋组分通过这些海峡的通量是端到端压力梯度的函数，与正比于海峡"宽度"的曳力相平衡，该宽度作为调整参数以获得合理的通量。

## Prognostic Variables / 预报变量

MO(I,J,L) (kg/m²) = salt water mass per unit area
MO(I,J,L) (kg/m²) = 单位面积的咸水质量

G0MO(I,J,L) (J) = potential enthalpy in grid cell
G0MO(I,J,L) (J) = 网格单元中的位焓

GXMO,GYMO,GZMO (J) = linear gradients of potential enthalpy
GXMO,GYMO,GZMO (J) = 位焓的线性梯度

GXXMO,GYYMO,GZZMO,GXYMO,GYZMO,GZXMO (J) = second order moments of potential enthalpy
GXXMO,GYYMO,GZZMO,GXYMO,GYZMO,GZXMO (J) = 位焓的二阶矩

S0MO(I,J,L) (kg) = salt mass in grid cell
S0MO(I,J,L) (kg) = 网格单元中的盐质量

SXMO,SYMO,SZMO (J) = linear gradients of salt
SXMO,SYMO,SZMO (J) = 盐的线性梯度

SXXMO,SYYMO,SZZMO,SXYMO,SYZMO,SZXMO (J) = second order moments of salt
SXXMO,SYYMO,SZZMO,SXYMO,SYZMO,SZXMO (J) = 盐的二阶矩

UO (I,J,L) (m/s) = eastward C-grid velocity centered at eastern edge of grid cell
UO (I,J,L) (m/s) = 网格单元东边缘中心的东向C网格速度

VO (I,J,L) (m/s) = northward C-grid velocity centered at northern edge of grid cell
VO (I,J,L) (m/s) = 网格单元北边缘中心的北向C网格速度

UOD (I,J,L) (m/s) = eastward D-grid velocity centered at northern edge of grid cell
UOD (I,J,L) (m/s) = 网格单元北边缘中心的东向D网格速度

VOD (I,J,L) (m/s) = northward D-grid velocity centered at eastern edge of grid cell
VOD (I,J,L) (m/s) = 网格单元东边缘中心的北向D网格速度

MUST (L,N) (kg/s) = mass flux of salt water through strait
MUST (L,N) (kg/s) = 通过海峡的咸水质量通量

G0MST (L,N) (J) = potential enthalpy in strait cell
G0MST (L,N) (J) = 海峡单元中的位焓

GXMST,GZMST (J) = linear gradients of potential enthalpy
GXMST,GZMST (J) = 位焓的线性梯度

S0MST (L,N) (kg) = salt mass in strait cell
S0MST (L,N) (kg) = 海峡单元中的盐质量

SXMST,SZMST (kg) = linear gradients of salt
SXMST,SZMST (kg) = 盐的线性梯度

Cross sectional area of salinity as a function of longitude in an ocean grid cell is:
海洋网格单元中盐度作为经度函数的横截面积为：

S (kg/kg) = S0MO / M + 2 * SXMO * m / M² + 6 * SXXMO * m² / M³ - .5 * SXXMO / M
S (kg/kg) = S0MO / M + 2 * SXMO * m / M² + 6 * SXXMO * m² / M³ - .5 * SXXMO / M

where M (kg) = MO * oDXYP and - .5 M < m < .5 M
其中 M (kg) = MO * oDXYP 且 - .5 M < m < .5 M

## Ocean Functions and the Equation of State / 海洋函数和状态方程

The following variables are defined for the ocean model:
以下变量为海洋模型定义：

C (J/kg°C) = specific heat capacity at constant pressure
C (J/kg°C) = 定压比热容

g (m/s²) = Earth's vertical gravitational acceleration
g (m/s²) = 地球垂直重力加速度

G (J/kg) = potential specific enthalpy
G (J/kg) = 位比焓

H (J/kg) = specific enthalpy
H (J/kg) = 比焓

m (kg/m²) = vertical coordinate = mass above minus mean atmospheric mass
m (kg/m²) = 垂直坐标 = 上方质量减去平均大气质量

P (Pa) = pressure above mean atmospheric pressure
P (Pa) = 高于平均大气压的压强

Po (Pa) = global mean atmospheric pressure at sea level (101325 Pa)
Po (Pa) = 海平面全球平均大气压（101325 Pa）

S (kg/kg) = salinity
S (kg/kg) = 盐度

T (°C) = in-situ temperature
T (°C) = 原位温度

α (m³/kg) = specific volume
α (m³/kg) = 比容

β (m³/kg) = potential specific volume
β (m³/kg) = 位比容

Γ (°C/Pa) = adiabatic lapse rate
Γ (°C/Pa) = 绝热递减率

Θ (°C) = potential temperature
Θ (°C) = 位温

G and S can be calculated at any location in the ocean from m and the prognostic variables.
G和S可以从m和预报变量计算海洋中任何位置的值。

The purpose of this section is to derive P, H, T, α and β from G, S and m or G, S and P.
本节的目的是从G、S和m或G、S和P推导P、H、T、α和β。

Remember that P = m·g.
记住P = m·g。

α(T,S,P), C(T,S,P) and Γ(T,S,P) are provided by Fofonoff and Millard [1983], but also see Fofonoff [1985].
α(T,S,P)、C(T,S,P)和Γ(T,S,P)由Fofonoff和Millard [1983]提供，另见Fofonoff [1985]。

H(T,S,P) is derived as follows:
H(T,S,P)推导如下：

∂H/∂P = α(T,S,P) (Eq. 1)
∂H/∂P = α(T,S,P) （方程1）

∂T/∂P = Γ(T,S,P) (Eq. 2)
∂T/∂P = Γ(T,S,P) （方程2）

are integrated simultaneously from P to Po at constant entropy and salinity to obtain H(T,S,P) - H(Θ,S,Po).
在恒定熵和盐度下从P积分到Po以获得H(T,S,P) - H(Θ,S,Po)。

Po is the reference pressure for potential temperature so that Θ = T at Po.
Po是位温的参考压强，因此在Po处Θ = T。

Next evaluate H(Θ,S,Po) - H(Θ,0,Po) at constant entropy and pressure which is provided by Millero and Leung [1976].
接下来在恒定熵和压强下计算H(Θ,S,Po) - H(Θ,0,Po)，这由Millero和Leung [1976]提供。

Finally, the differential equation:
最后，微分方程：

∂H/∂T = C(T,0,Po) (Eq. 3)
∂H/∂T = C(T,0,Po) （方程3）

is integrated from Θ to 0°C at constant salinity and pressure to obtain H(Θ,0,Po) - H(0,0,Po).
在恒定盐度和压强下从Θ积分到0°C以获得H(Θ,0,Po) - H(0,0,Po)。

The reference value for specific enthalpy is set by H(0,0,Po) = 0.
比焓的参考值由H(0,0,Po) = 0设定。

Thus H(T,S,P) is determined by the above formulas.
因此H(T,S,P)由上述公式确定。

Θ(T,S,P) and T(Θ,S,P) are derived by integrating (Eq. 2) from P to Po.
Θ(T,S,P)和T(Θ,S,P)通过从P到Po积分（方程2）推导。

The G of a parcel is defined to be the H of the parcel at Po were it raised adiabatically.
气块的G定义为该气块在Po处绝热抬升时的H。

Thus, G(T,S,P) = H(Θ(T,S,P),S,Po) = G(Θ,S).
因此，G(T,S,P) = H(Θ(T,S,P),S,Po) = G(Θ,S)。

Θ(G,S) is derived by inverting the first argument of G(Θ,S) which is possible because G and Θ are in a one-to-one relationship at constant S and Po.
Θ(G,S)通过反演G(Θ,S)的第一个参数推导，这是可能的，因为在恒定S和Po下G和Θ是一一对应关系。

T, H, α and β can now be derived as functions of G, S and P.
T、H、α和β现在可以推导为G、S和P的函数。

T(G,S,P) = T(G(Θ,S),S,P) = T(Θ,S,P)
T(G,S,P) = T(G(Θ,S),S,P) = T(Θ,S,P)

H(G,S,P) = H(G(Θ,S),S,P) = H(Θ,S,P) = H(Θ(T,S,P),S,P) = H(T,S,P)
H(G,S,P) = H(G(Θ,S),S,P) = H(Θ,S,P) = H(Θ(T,S,P),S,P) = H(T,S,P)

α(G,S,P) = α(G(Θ,S),S,P) = α(Θ,S,P) = α(Θ(T,S,P),S,P) = α(T,S,P)
α(G,S,P) = α(G(Θ,S),S,P) = α(Θ,S,P) = α(Θ(T,S,P),S,P) = α(T,S,P)

β(G,S) = α(G,S,Po)
β(G,S) = α(G,S,Po)

Evaluation of α(G,S,P), called the equation of state, is performed by linear interpolation within a look-up table in the ocean model's computer program.
α(G,S,P)的计算称为状态方程，通过海洋模型计算机程序中的查找表线性插值执行。

The increments in the table are 4000 (J/kg) for G, .001 for S, and 2·10⁵ (Pa) for P.
表中的增量为G的4000 (J/kg)、S的.001和P的2·10⁵ (Pa)。

## Ocean Pressure Gradient Force / 海洋压力梯度力

The pressure gradient force accelerates the velocity between two mass grid cells at the same layer.
压力梯度力加速同一层两个质量网格单元之间的速度。

The force in a layer has two terms: the gradient of the mean pressure multiplied by the average mean volume of the two cells and the gradient of the mean geopotential multiplied by the average mass of the two cells.
层中的力有两项：平均压力的梯度乘以两个单元的平均平均体积，以及平均位势的梯度乘以两个单元的平均质量。

Other gradients of potential enthalpy and salt are not used in calculating the above mean quantities, but the linear vertical gradients are used.
位焓和盐的其他梯度不用于计算上述平均量，但使用线性垂直梯度。

The mean vertical coordinate, m1, of a grid cell is the average of the top edge m and the bottom edge m.
网格单元的平均垂直坐标m1是顶边缘m和底边缘m的平均值。

Δm1 is the difference of m at the two edges.
Δm1是两个边缘处m的差值。

The mean pressure of a grid cell is P(m1) = m1·g, where g (m/s²) is the uniform effective gravity.
网格单元的平均压强为P(m1) = m1·g，其中g (m/s²)是均匀有效重力。

To calculate the mean specific volume of a grid cell we assume that α(G(m),S(m),P(m)) = α(m) fits a quadratic polynomial in m.
为了计算网格单元的平均比容，我们假设α(G(m),S(m),P(m)) = α(m)符合m的二次多项式。

The mean value of the quadratic α(m) from m1-Δm1/2 to m1+Δm1/2 is equal to [α(m1-x) + α(m1+x)]/2 where x = Δm1/√12.
二次多项式α(m)从m1-Δm1/2到m1+Δm1/2的平均值等于[α(m1-x) + α(m1+x)]/2，其中x = Δm1/√12。

The mean volume of a grid cell is equal to the mass multiplied by the mean specific volume which is calculated using quadratic precision using two evaluations of α(G,S,P) per grid cell at the vertical coordinates m1-x and m1+x.
网格单元的平均体积等于质量乘以平均比容，后者使用二次精度计算，在每个网格单元的垂直坐标m1-x和m1+x处对α(G,S,P)进行两次计算。

This shows how the first term of the pressure gradient term is modeled.
这显示了压力梯度项第一项的建模方式。

The second term is modeled as follows.
第二项建模如下。

We again assume that α(m) fits a quadratic in each grid cell.
我们再次假设α(m)在每个网格单元中符合二次多项式。

The height, h (meters), at the column bottom is specified by the bottom topography.
柱底部的高度h（米）由底部地形指定。

Integrating upwards, the change in h from the bottom layer edge to any level in a layer is equal to the integral of α(m) dm.
向上积分，从底层边缘到层中任何水平的h变化等于α(m) dm的积分。

The change in h to the top layer edge uses the two evaluations of α mentioned in the previous paragraph and is calculated with quadratic precision.
到顶层边缘的h变化使用前一段提到的α的两次计算，并用二次精度计算。

The top edge value of h of a layer becomes the bottom edge value of h for the layer above.
一层的h顶边缘值成为其上一层h的底边缘值。

The mean geopotential, Φ (m²/s²), of the layer is the mass weighted g·h throughout the layer which is a double integral of α(m) and is equal to
层的平均位势Φ (m²/s²)是整个层中质量加权的g·h，这是α(m)的二重积分，等于

```
∫m1+Δm1/2
Φ = 1/Δm1 ∫ g·h(m) dm =
∫m1-Δm1/2

∫m1+Δm1/2 [               ∫m1+Δm1/2         ]
= 1/Δm1 ∫ g [ h(m1+Δm1/2) + ∫ α(n) dn ] dm =
∫m1-Δm1/2 [               ∫m                ]

= g·h(m1+Δm1/2) + g[α(m1-x)(3-√3) + α(m1+x)(3+√3)]m1/12
```

The mean Φ is calculated with quadratic precision using the same two evaluations of α(G,S,P) as used in evaluating the first term.
平均Φ使用与计算第一项相同的α(G,S,P)两次计算，用二次精度计算。

Given an arbitrary quadratic polynomial in an interval [-Δm1/2,Δm1/2], the abcissas of the intersection points between the polynomial and the least square fit line that fits the polynomial in the interval are the points -x and x mentioned above.
给定区间[-Δm1/2,Δm1/2]中的任意二次多项式，该多项式与在该区间内拟合该多项式的最小二乘拟合线之间的交点的横坐标就是上述点-x和x。

These points do not depend on the coefficients of the polynomial.
这些点不依赖于多项式的系数。

Conversely, there are no two other points such that the mean value of an arbitrary quadratic polynomial can be derived from evaluating the polynomial at the two points.
相反，不存在其他两个点使得任意二次多项式的平均值可以从在这两个点计算多项式而得到。

This mathematical result is even more elegant because the double integral above can be calculated from an evaluation of the polynomial at the points -x and x.
这个数学结果更加优雅，因为上述二重积分可以通过在点-x和x处计算多项式来计算。
