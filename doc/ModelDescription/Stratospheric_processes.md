# Stratospheric processes / 平流层过程

Stratospheric drag is applied in two ways.
平流层曳力以两种方式施加。

Firstly, using a simple formulation as a Rayleigh damping near the top of the model (SDRAG).
首先，在模型顶部附近使用简单公式作为瑞利阻尼（SDRAG）。

Secondly, and generally only if the stratosphere is being properly resolved, we have a physically-based estimate of gravity-wave drag determined from the model simulation of moist convection, mountain waves, shear and deformation (in STRATDYN) (Rind et al, 1988).
其次，并且通常只有在平流层被适当解析的情况下，我们才有基于物理的重力波曳力估计，该估计来自模型对湿润对流、地形波、剪切和变形的模拟（在STRATDYN中）（Rind等，1988）。

When gravity waves break, there is also some vertical mixing associated with that.
当重力波破碎时，也会产生与之相关的一些垂直混合。

Both GWDRAG and SDRAG are applied within the dynamical leap-frog time steps to improve stability.
GWDRAG和SDRAG都在动力学蛙跳时间步内应用，以提高稳定性。

**Document End / 文档结束**
