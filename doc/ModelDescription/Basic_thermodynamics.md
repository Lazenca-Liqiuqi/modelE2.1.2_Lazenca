# Basic thermodynamics / 基础热力学

The sea ice model can be thought of as consisting of two mass layers made up of an upper layer which has a constant thickness (10cm) ice layer and an arbitrary snow amount. The second layer mass has a minimum thickness of 10 cm, but can grow arbitrarily thick. There are two thermal layers in each mass layer which consist of a fixed ratio of the mass. Salinity and tracer values are also calculated on the same mass ratio, with the exception that salinity is assumed to be zero in the snow. At the surface, heat and mass fluxes calculated in the SURFCE routine and the precipitation are applied first to the snow layer and then to the ice. There is advection of heat, salt and mass as a function of the regridding of the mass layers in order to preserve the fixed ratios, i.e. there is a sigma-coordinate for sea ice properties.
海冰模型可以被认为由两个质量层组成，上层由具有恒定厚度（10厘米）的冰层和任意量的雪组成。第二层质量的最小厚度为10厘米，但可以任意增厚。每个质量层中有两个热力层，由质量的一定比例组成。盐度和示踪物值也按相同的质量比例计算，但假设雪中的盐度为零。在表面，SURFCE例程中计算的热通量和质量通量以及降水首先应用于雪层，然后应用于冰层。由于质量层的重新划分，存在热量、盐分和质量的平流，以保持固定比例，即海冰属性存在一个σ坐标。

The basal fluxes are calculated in the ocean only for the configurations where ice thickness is prognostic (i.e. not for the fixed SST cases). This is done in routine UNDERICE. The fluxes are then applied to both the ice and ocean modules. Similarly, lateral fluxes are calculated in MELT_SI. This is done prior to any surface fluxes calculation to avoid the problem of changing the surface type fractions in the midst of the calculation.
底部通量仅在冰厚度为预报的配置中在海洋中计算（即不适用于固定SST的情况）。这是在UNDERICE例程中完成的。然后，这些通量被应用于冰和海洋模块。类似地，侧向通量在MELT_SI中计算。这是在任何表面通量计算之前完成的，以避免在计算过程中改变表面类型比例的问题。

Frazil ice formation can occur in the ocean and lakes in open water conditions and under ice. This ice mass formation rate (and it's associated salt (for the ocean) and energy flux are calculated in either the lake or ocean component and added to the sea ice by routine FORM_SI. There is a minimum lead fraction which is a function of the ice thickness.
冰花形成可能发生在海洋和湖泊的开阔水域条件和冰下。这种冰质量形成率（及其相关的盐分（对于海洋）和能量通量）在湖泊或海洋组件中计算，并通过FORM_SI例程添加到海冰中。存在一个最小的冰缝比例，它是冰厚度的函数。

Snow can be compacted into ice by accumulating over a maximum thickness, or by rain or surface melting. Surface melting is kept track of since it is used to estimate melt pond formation for the albedo calculation. No specific snow-ice formation is yet included.
雪可以通过积累超过最大厚度，或通过降雨或表面融化而压实成冰。表面融化被跟踪，因为它被用于估算反照率计算中的融池形成。尚未包含具体的雪冰形成过程。
