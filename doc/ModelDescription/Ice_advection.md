# Ice advection / 海冰平流

Ice advection is a function of the atmosphere-ice and ice-ocean momentum stress and the sea surface gradient.
海冰平流是大气-冰和冰-海洋动量应力以及海表梯度的函数。

The internal ice pressures and rheology are estimated using the Flato-Hibler viscous-plastic rheology as coded by Zhang and Rothrock, 1999.
内部冰压力和流变学使用Zhang和Rothrock（1999）编码的Flato-Hibler粘-塑性流变学来估算。

Due to the requirement that the surface type fractions don't vary over the surface flux calculation we calculate the ice velocities and ice-ocean momentum stress at the beginning of the calculation (in DYNSI), but the ice mass fluxes are not applied until afterwards (in ADVSI).
由于要求地表类型分数在地表通量计算期间不变化，我们在计算开始时（在DYNSI中）计算冰速度和冰-海洋动量应力，但冰质量通量直到之后才应用（在ADVSI中）。

The advection is done using the linear upstream scheme in the two horizontal directions.
平流在两个水平方向上使用线性迎风格式完成。

This code is turned on by using the ICEDYN_DRV ICEDYN modules instead of the ICEDYN_DUM module, and works with any ocean configuration.
通过使用ICEDYN_DRV ICEDYN模块而不是ICEDYN_DUM模块来开启此代码，并且适用于任何海洋配置。

In the fixed SST case, using the ice advection does not change the ice variables, but does allow the ice and energy convergences due to advection to be calculated, and subsequently used in the q-flux model.
在固定SST情况下，使用海冰平流不会改变冰变量，但允许计算由于平流导致的冰和能量辐合，随后在q-flux模型中使用。

The q-fluxes need to be consistent with the ice advection, and so if ICEDYN_DRV ICEDYN is used in the spin-up, it must also be used in the q-flux model (and vice versa).
q-flux需要与海冰平流保持一致，因此如果在spin-up中使用ICEDYN_DRV ICEDYN，则必须在q-flux模型中也使用（反之亦然）。
