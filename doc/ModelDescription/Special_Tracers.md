# Special Tracers / 特殊示踪物

Some special tracer physics come as standard in the model.
一些特殊的示踪物物理是模型中的标准配置。

These relate to tracers that are of special interest to some of the developers.
这些与一些开发者特别感兴趣的示踪物有关。

## Special tracer types / 特殊示踪物类型

- `#define TRACERS_SPECIAL_O18` - 为水同位素设置特殊物理。
  It requires `#define TRACERS_ON` and `#define TRACERS_WATER` to be set as well, and that `TRACERS_O18` be included in the object modules.
  它需要同时设置`#define TRACERS_ON`和`#define TRACERS_WATER`，并且`TRACERS_O18`必须包含在目标模块中。

- `#define TRACERS_SPECIAL_Lerner` - 用于研究平流层/对流层交换的示踪物。
  tracers for looking at stratospheric/tropospheric exchange.
  用于研究平流层/对流层交换的示踪物。
