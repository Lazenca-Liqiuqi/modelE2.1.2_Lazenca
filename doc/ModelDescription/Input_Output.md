# Input/Output / 输入输出

Apart from boundary condition files that are controlled by individual modules, restart file input and output is controlled by <TT>IORSF</TT>.
除由各模块控制的边界条件文件外，重启文件的输入输出由 <TT>IORSF</TT> 控制。

This is a driver routine that calls individual <TT>io_XYZ</TT> routines for each module.
这是一个驱动例程，为每个模块调用各自的 <TT>io_XYZ</TT> 例程。

This allows different versions of each module to control the I/O of the required prognostic variables.
这使得每个模块的不同版本能够控制所需预报变量的输入输出。

Depending on the value of <TT>iaction</TT> in the call, different kinds of I/O can be set (read or write, double or single precision, with or without tracers, with diagnostics or not).
根据调用中的 <TT>iaction</TT> 值，可以设置不同类型的输入输出（读取或写入、双精度或单精度、包含或不包含示踪物、包含诊断输出或不包含）。

**Document End / 文档结束**
