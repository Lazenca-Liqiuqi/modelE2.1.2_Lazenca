# Tracers / 示踪物

ModelE comes with a full complement of tracer code that follows all mass transports in the model.
ModelE配备了完整的示踪物代码，用于跟踪模型中的所有质量输送。

All tracer fields are computed in mass units (not concentration) and thus are perfectly conserved (with one exception explained below).
所有示踪物场都以质量单位（非浓度）计算，因此完美守恒（下文解释了一个例外）。

There is a library of pre-coded physics for some common tracers that have been used historically with the GISS models.
存在一个预编码物理库，用于一些在GISS模型历史中使用的常见示踪物。

For the simplest applications, the relevant tracer code needs to be turned on using pre-processor directives in the rundeck (details below), and then by editing TRACER_COM.f the specific tracer can be coded for.
对于最简单的应用，需要在运行配置中使用预处理器指令开启相关的示踪物代码（详情见下文），然后通过编辑TRACER_COM.f来编码特定示踪物。

Some generic code is allowed for any tracers (such as radioactive decay, diagnostics etc.).
允许为任何示踪物使用一些通用代码（如放射性衰变、诊断等）。

Some specific tracers require special physics and these require some extra code (for instance water isotopes or chemistry).
某些特定示踪物需要特殊物理，这些需要一些额外代码（例如水同位素或化学）。

The tracers break naturally into five groups: atmospheric tracers that follow air mass, tracers that are either purely water based or have a soluble component, reactive gas or aerosol tracers that may interact with the hydrologic cycle, tracers that are purely oceanic, and special tracers.
示踪物自然分为五组：跟随气质量的示踪物、纯水基或具有可溶组分的示踪物、可能与水文循环相互作用的活性气体或气溶胶示踪物、纯海洋示踪物和特殊示踪物。

These are dealt with in turn below.
下面依次讨论这些示踪物。

## Tracer types / 示踪物类型

- [Air mass tracers](Air_mass_Tracers.md) - 气质量示踪物
- [Water mass tracers](Soluble_and_Water_mass_Tracers.md) - 水质量示踪物
- Reactive tracers - 活性示踪物
  - [Gas tracers](Gas_Tracers.md) - 气体示踪物
  - [Aerosol tracers](Aerosol_Tracers.md) - 气溶胶示踪物
- [Ocean tracers](Ocean_Tracers.md) - 海洋示踪物
- [Special tracers](Special_Tracers.md) - 特殊示踪物
