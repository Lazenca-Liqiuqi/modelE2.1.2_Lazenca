# GISS ModelE User Guide

## GISS ModelE 用户指南

This document provides basic instructions on how to use GISS ModelE GCM, including getting the model code, configuring the model, running model simulations and obtaining information from model diagnostics. For more detailed description of the model you may refer to [Model Description](../ModelDescription/index_zh.md) document.

本文档提供了使用 GISS ModelE 大气环流模型（GCM）的基本说明，包括获取模型代码、配置模型、运行模型模拟以及从模型诊断输出获取信息。有关模型的更详细描述，请参考[模型描述](../ModelDescription/index_zh.md)文档。

## Table of contents
## 目录

1. [Getting the code and configuring the model｜获取代码并配置模型](Getting_the_code_form_GISS_repository.md)
   1. [System requirements｜系统需求](placeholder_zh.md)
   2. [Getting the code form GISS repository｜从 GISS 代码仓库获取代码](placeholder_zh.md)
   3. [Configuring modelE on your machine｜在本机配置 ModelE](placeholder_zh.md)

2. [Quick start｜快速开始](placeholder_zh.md)
   1. [Creating a rundeck｜创建运行配置（Rundeck）](placeholder_zh.md)
   2. [Downloading necessary input files｜下载所需输入文件](Downloading_necessary_input_files.md)
   3. [Compiling the model and setting up a directory for model run｜编译模型并设置运行目录](placeholder_zh.md)
   4. [Running the model｜运行模型](placeholder_zh.md)
   5. [Looking at model output｜查看模型输出](placeholder_zh.md)

3. [ModelE rundeck｜ModelE 运行配置（Rundeck）](placeholder_zh.md)
   1. [General rundeck structure｜运行配置（Rundeck）的一般结构](ModelE_rundeck_zh.md)
   2. [Major rundeck parameters｜运行配置（Rundeck）主要参数](Major_rundeck_parameters_zh.md)
   3. [Input files｜输入文件](placeholder_zh.md)
   4. [Date and time｜日期与时间](placeholder_zh.md)
   5. [Choosing proper ISTART｜选择合适的ISTART](Choosing_proper_ISTART_zh.md)

4. [Setting up a particular modelE simulation｜配置特定的 ModelE 模拟](placeholder_zh.md)
   1. [Setting up a Q-flux model with a single ocean layer｜配置单海洋层 Q-flux 模式](placeholder_zh.md)
   2. [Setting up a Q-flux model with diffusion into a deep ocean｜配置含深海扩散的 Q-flux 模式](placeholder_zh.md)
   3. [Setting up a paleoclimate simulation｜配置古气候模拟](placeholder_zh.md)
   4. [Using IRANDI to create an ensemble of runs｜使用 IRANDI 构建集合试验](placeholder_zh.md)
   5. [Altering the topography file consistently｜一致性修改地形文件](placeholder_zh.md)
   6. [Altering the land mask｜修改陆地掩膜](placeholder_zh.md)
   7. [Altering trace gas amounts｜调整痕量气体浓度](placeholder_zh.md)

5. [Running the model｜运行模型](placeholder_zh.md)
   1. [Starting, stopping and restarting the model run｜启动、停止与重启模型运行](placeholder_zh.md)
   2. [Tuning model energy balance??｜调整模型能量平衡](placeholder_zh.md)
   3. [Controlling numerical instabilities with rundeck parameters｜通过运行配置（Rundeck）参数控制数值不稳定性](placeholder_zh.md)

6. [Getting information from the diagnostics｜从诊断输出获取信息](diagnostics_zh.md)
   1. [Looking at the output｜查看输出](diagnostics_zh.md#part2_1)
   2. [Changing what is included in the printout｜调整打印输出内容](diagnostics_zh.md#part2_2)
   3. [Producing daily/monthly or seasonal diagnostics｜生成日/月或季节诊断](diagnostics_zh.md#part2_3)
   4. [Controlling the format of the binary output (i.e. GISS/netcdf/hdf etc.)｜控制二进制输出格式（如 GISS/NetCDF/HDF 等）](diagnostics_zh.md#part2_4)
   5. [Calculating a model score｜计算模型评分](diagnostics_zh.md#part2_5)

7. [Modifying modelE code｜修改 ModelE 代码](placeholder_zh.md)
   1. [ModelE coding standards｜ModelE 编码规范](placeholder_zh.md)
   2. [Adding information for automatic documentation｜添加自动化文档信息](Adding_info_for_automatic_documentation_zh.md)
   3. [Introducing a new rundeck parameter｜引入新的运行配置（Rundeck）参数](placeholder_zh.md)
   4. [Adding new diagnostics｜添加新的诊断](placeholder_zh.md)
   5. [Reading an external file｜读取外部文件](placeholder_zh.md)
   6. [Adding a new variable to the restart file｜向重启文件添加新变量](placeholder_zh.md)

8. [Testing and debugging your changes to the code｜测试与调试你的代码更改](placeholder_zh.md)
   1. [Testing modeE reproducibility｜测试 ModelE 可复现性](placeholder_zh.md)
   2. [Running the model with "traps"｜使用陷阱（traps）运行模型](placeholder_zh.md)
   3. [Running the model in debugger｜在调试器中运行模型](placeholder_zh.md)

9. [Tracers｜示踪物](placeholder_zh.md)
   1. [Tracer Preprocessor Options｜示踪物预处理器选项](Tracer_Preprocessor_Options_zh.md)
   2. [Tracer Rundeck Parameters｜示踪物运行配置（Rundeck）参数](Tracer_Rundeck_Parameters_zh.md)

10. [Getting help?｜获取帮助？](placeholder_zh.md)

11. [Appendix｜附录](placeholder_zh.md)
    1. [Installing NetCDF library in your computer｜在你的计算机上安装 NetCDF 库](Installing_NetCDF_library_zh.md)