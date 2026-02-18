# Air mass Tracers / 气质量示踪物

The code for tracers of mass transport in the atmosphere is initialised by setting `#define TRACERS_ON` in the rundeck.
大气中质量输送示踪物的代码通过在运行配置中设置`#define TRACERS_ON`来初始化。

These tracers are mostly insoluble gases or ideal tracers such as air mass age or source.
这些示踪物大多数是不溶性气体或理想示踪物，如气质量龄或来源。

All changes in air mass (by advection, convection, the sea level pressure filter) and parameterised mixing (stratospheric diffusion, atmospheric turbulence) are followed by the tracers.
所有气质量的变化（通过平流、对流、海平面气压滤波器）和参数化混合（平流层扩散、大气湍流）都由示踪物跟踪。

There is one exception for the pure 'Air' tracer: this must follow the mass field identically, but during the operation of the sea level pressure filter, a conservation of mass implies a change in concentration.
纯'Air'示踪物有一个例外：它必须完全跟随质量场，但在海平面气压滤波器操作期间，质量守恒意味着浓度变化。

For most tracers, conservation of mass is more important, but for 'Air' concentration is conserved.
对于大多数示踪物，质量守恒更重要，但对于'Air'浓度是守恒的。

**Document End / 文档结束**
