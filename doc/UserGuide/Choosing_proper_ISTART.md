# Choosing proper ISTART
# 选择合适的ISTART

**ISTART controls how the model first picks up the initial conditions to start the run. We have a number of options depending on how much information is already available.**
ISTART控制模型如何首先获取初始条件来开始运行。我们根据已有信息的多少提供了多个选项。

1. **`ISTART=1`** Default start. This sets atmospheric variables to constants and requires input files for ground values (a GIC file), and ocean values (OIC) if required.
   默认启动。这将大气变量设置为常数，并需要地面值（GIC文件）的输入文件，如果需要还需要海洋值（OIC）。

2. **`ISTART=2`** Observed start. This sets atmospheric values to observations, based on a particular format of AIC file. As for ISTART=1, input files are required for ground and ocean variables.
   观测启动。这将大气值设置为基于特定格式AIC文件的观测值。与ISTART=1一样，需要地面和海洋变量的输入文件。

3. **`ISTART=3`** Not used.
   未使用。

4. **`ISTART=4`** A restart from an rsf file from a previous run, but the ocean is reinitialised. Needs an initial OIC file (for fully coupled models).
   从之前运行的rsf文件重新启动，但海洋会重新初始化。需要初始OIC文件（对于完全耦合的模型）。

5. **`ISTART=5`** A restart from an rsf file from a previous run, but no tracers. This is only useful for tracer runs that need to be initialised with a particular model state.
   从之前运行的rsf文件重新启动，但没有示踪物。这只对需要用特定模型状态初始化的示踪物运行有用。

6. **`ISTART=6`** A restart from an rsf file from a previous run that might not have had the same land-ocean mask. This makes sure to reset snow values, pbl (planetary boundary layer) values and ocean values accordingly.
   从之前可能没有相同陆-海掩码的运行的rsf文件重新启动。这确保相应地重置雪值、行星边界层(PBL)值和海洋值。

7. **`ISTART=7`** A restart from an rsf file from a previous run with the same land-ocean mask. This still makes sure to set snow values and ocean values. This is used mainly for converted model II' data.
   从具有相同陆-海掩码的之前运行的rsf文件重新启动。这仍然确保设置雪值和海洋值。这主要用于转换的model II'数据。

8. **`ISTART=8`** This is a restart from a model configuration identical to the run now starting. This is for perturbation experiments etc. See note below.
   从与现在启动的运行相同的模型配置重新启动。这用于扰动实验等。见下面的说明。

9. **`ISTART=9`** This is a restart from this model run. (i.e. a continuation, or a backtrack to an older rsf file).
   从这个模型运行重新启动（即继续运行，或回退到更早的rsf文件）。

10. **`ISTART=10`** This is used internally to pick up from the instantaneous rsf file (the later of fort.1 and fort.2). Does not ever need to be set in the rundeck.
    这在内部用于从瞬时rsf文件（fort.1和fort.2中较新的一个）获取。不需要在运行配置中设置。

11. **`ISTART=11`** This is used internally to pick up from an instantaneous rsf file (fort.1). Only rarely used.
    这在内部用于从瞬时rsf文件（fort.1）获取。很少使用。

12. **`ISTART=12`** This is used internally to pick up from an instantaneous rsf file (fort.2). Only rarely used.
    这在内部用于从瞬时rsf文件（fort.2）获取。很少使用。

13. **`ISTART=13`** This is used internally to pick up from the instantaneous rsf file (the earlier of fort.1 and fort.2). Only rarely used.
    这在内部用于从瞬时rsf文件（fort.1和fort.2中较早的一个）获取。很少使用。

14. **`ISTART<0`** This option is used by the post-processing program to run the model to generate nice diagnostics. This should never need to be set manually.
    这个选项被后处理程序用来运行模型以生成良好的诊断信息。这永远不需要手动设置。

**Please note that if you get this wrong i.e. you use an ISTART that is not compatible with the AIC, GIC or OIC files in the rundeck, the model is not guaranteed to crash nicely. In fact, the opposite is likely. Strange crashes on start up are very often related to this.**
请注意，如果这个设置错误，即你使用的ISTART与运行配置中的AIC、GIC或OIC文件不兼容，模型不能保证优雅地崩溃。事实上，很可能相反。启动时的奇怪崩溃通常与此相关。

**Note for ISTART=8:** Since `itime_tr0` defaults to `Itime`, tracers will be reinitialized. To have them keep their settings from the rsf file, set `itime_tr0` to < `ItimeI` (e.g. 0) for all tracers in the rundeck parameters. If you use tracers that depend on (`Itime-itime_tr0`), you need to set `itime_tr0` to the starting time of the rsf file for continuity.
**ISTART=8的说明：**由于`itime_tr0`默认为`Itime`，示踪物将被重新初始化。要让它们保持来自rsf文件的设置，请在运行配置参数中将所有示踪物的`itime_tr0`设置为< `ItimeI`（例如0）。如果你使用依赖于(`Itime-itime_tr0`)的示踪物，你需要将`itime_tr0`设置为rsf文件的开始时间以保持连续性。