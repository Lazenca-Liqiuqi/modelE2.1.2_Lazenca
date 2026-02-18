# Diagnostics / 诊断输出

Almost all diagnostics in the model are accumulated and only averaged in the post-processing (or for the end of month printout). Budget page diagnostics are accumulated in the relevant (atmospheric or sea ice) routines, along with relevant atmospheric lat-lon diags. Constant pressure lat-height diagnostics are only calculated in DIAGA, called from within DYNAM. Calculation and print out of the diagnostics is done from print_diags.
模型中的几乎所有诊断都是累积的，仅在后处理中（或在月底打印输出中）进行平均。预算页诊断在相关的（大气或海冰）例程中累积，以及相关的大气纬度-经度诊断。等压纬度-高度诊断仅在DIAGA中计算，该例程从DYNAM内部调用。诊断的计算和打印输出从print_diags完成。

**Document End / 文档结束**
