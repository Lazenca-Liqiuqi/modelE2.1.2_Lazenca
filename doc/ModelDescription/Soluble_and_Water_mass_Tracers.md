# Soluble and Water mass Tracers / 可溶性和水质量示踪物

If the tracer interacts with the hydrologic cycle the preprocessor directive `#define TRACERS_WATER` should be set in the rundeck in addition to `#define TRACERS_ON`.
如果示踪物与水文循环相互作用，则应在运行配置中设置预处理器指令 `#define TRACERS_WATER`，以及 `#define TRACERS_ON`。

This allows for a separate tracer budget in all water reservoirs (cloud liquid water, precipitation, sea ice, lakes, ground water, glaciers and oceans (if a non-trivial ocean model is used)).
这允许在所有水体储库（云液态水、降水、海冰、湖泊、地下水、冰川和海洋（如果使用非简化海洋模型））中建立单独的示踪物预算。

There can be complicated interactions in the clouds between the in air and in water tracers, and any tracer amount in precip is followed through it's subsequent travels.
在空气中与水中的示踪物之间，云中可能存在复杂的相互作用，并且降水中的任何示踪物量都会被追踪其后续传输路径。

These tracers are useful for soluble gases and water tracers themselves (isotopes, age, source).
这些示踪物适用于可溶性气体和水示踪物本身（同位素、年龄、来源）。

**Document End / 文档结束**
