# GISS ModelE User Guide

## GISS ModelE 用户指南

This document provides basic instructions on how to use GISS ModelE GCM, including getting the model code, configuring the model, running model simulations and obtaining information from model diagnostics. For more detailed description of the model, please refer to the upcoming Model Description documentation.

本文档提供了使用 GISS ModelE 大气环流模型（GCM）的基本说明，包括获取模型代码、配置模型、运行模型模拟以及从模型诊断输出获取信息。有关模型的更详细描述，请参考即将发布的模型描述文档。

## Table of contents
## 目录

1. Getting the code and configuring the model / 获取代码并配置模型
   1. [System requirements / 系统需求](1.1-System_requirements.md)
   2. [Getting the code from GISS repository / 从 GISS 代码仓库获取代码](1.2-Getting_the_code_from_GISS_repository.md)
   3. [Configuring modelE on your machine / 在本机配置 ModelE](1.3-Configuring_modelE_on_your_machine.md)

2. Quick start / 快速开始
   1. [Creating a rundeck / 创建运行配置（Rundeck）](2.1-Creating_a_rundeck.md)
   2. [Downloading necessary input files / 下载所需输入文件](2.2-Downloading_necessary_input_files.md)
   3. [Compiling the model and setting up a directory for model run / 编译模型并设置运行目录](2.3-Compiling_the_model.md)
   4. [Running the model / 运行模型](2.4-Running_the_model.md)
   5. [Looking at model output / 查看模型输出（占位符）](2.5-Looking_at_model_output.md)

3. ModelE rundeck / ModelE 运行配置（Rundeck）
   1. [General rundeck structure / 运行配置（Rundeck）的一般结构](3.1-General_rundeck_structure.md)
   2. [Major rundeck parameters / 运行配置（Rundeck）主要参数](3.2-Major_rundeck_parameters.md)
   3. [Input files / 输入文件（占位符）](3.3-Input_files.md)
   4. [Date and time / 日期与时间（占位符）](3.4-Date_and_time.md)
   5. [Choosing proper ISTART / 选择合适的ISTART](3.5-Choosing_proper_ISTART.md)

4. Setting up a particular modelE simulation / 配置特定的 ModelE 模拟
   1. [Setting up a Q-flux model with a single ocean layer / 配置单海洋层 Q-flux 模式（占位符）](4.1-Qflux_single_ocean.md)
   2. [Setting up a Q-flux model with diffusion into a deep ocean / 配置含深海扩散的 Q-flux 模式（占位符）](4.2-Qflux_deep_ocean.md)
   3. [Setting up a paleoclimate simulation / 配置古气候模拟（占位符）](4.3-Paleoclimate_simulation.md)
   4. [Using IRANDI to create an ensemble of runs / 使用 IRANDI 构建集合试验（占位符）](4.4-IRANDI_ensemble.md)
   5. [Altering the topography file consistently / 一致性修改地形文件（占位符）](4.5-Altering_topography.md)
   6. [Altering the land mask / 修改陆地掩膜（占位符）](4.6-Altering_land_mask.md)
   7. [Altering trace gas amounts / 调整痕量气体浓度（占位符）](4.7-Altering_trace_gases.md)

5. Running the model / 运行模型
   1. [Starting, stopping and restarting the model run / 启动、停止与重启模型运行（占位符）](5.1-Start_stop_restart.md)
   2. [Tuning model energy balance / 调整模型能量平衡（占位符）](5.2-Tuning_energy_balance.md)
   3. [Controlling numerical instabilities with rundeck parameters / 通过运行配置（Rundeck）参数控制数值不稳定性（占位符）](5.3-Controlling_instabilities.md)

6. Getting information from the diagnostics / 从诊断输出获取信息
   1. [Looking at the output / 查看输出](6.1-Looking_at_output.md)
   2. [Changing what is included in the printout / 调整打印输出内容](6.2-Changing_printout_content.md)
   3. [Producing daily/monthly or seasonal diagnostics / 生成日/月或季节诊断](6.3-Producing_diagnostics.md)
   4. [Controlling the format of the binary output (i.e. GISS/netcdf/hdf etc.) / 控制二进制输出格式（如 GISS/NetCDF/HDF 等）](6.4-Controlling_binary_output.md)
   5. [Calculating a model score / 计算模型评分](6.5-Calculating_model_score.md)

7. Modifying modelE code / 修改 ModelE 代码
   1. [ModelE coding standards / ModelE 编码规范（占位符）](7.1-Coding_standards.md)
   2. [Adding information for automatic documentation / 添加自动化文档信息](7.2-Adding_info_for_automatic_documentation.md)
   3. [Introducing a new rundeck parameter / 引入新的运行配置（Rundeck）参数（占位符）](7.3-New_rundeck_parameter.md)
   4. [Adding new diagnostics / 添加新的诊断（占位符）](7.4-New_diagnostics.md)
   5. [Reading an external file / 读取外部文件（占位符）](7.5-Reading_external_files.md)
   6. [Adding a new variable to the restart file / 向重启文件添加新变量（占位符）](7.6-New_restart_variable.md)

8. Testing and debugging your changes to the code / 测试与调试你的代码更改
   1. [Testing modeE reproducibility / 测试 ModelE 可复现性（占位符）](8.1-Testing_reproducibility.md)
   2. [Running the model with "traps" / 使用陷阱（traps）运行模型（占位符）](8.2-Running_with_traps.md)
   3. [Running the model in debugger / 在调试器中运行模型（占位符）](8.3-Running_in_debugger.md)

9. Tracers / 示踪物
   1. [Tracer Preprocessor Options / 示踪物预处理器选项](9.1-Tracer_Preprocessor_Options.md)
   2. [Tracer Rundeck Parameters / 示踪物运行配置（Rundeck）参数](9.2-Tracer_Rundeck_Parameters.md)

10. [Getting help / 获取帮助](10-Getting_help.md)

11. Appendix / 附录
    1. [Installing NetCDF library in your computer / 在你的计算机上安装 NetCDF 库](11.1-Installing_NetCDF_library.md)
    2. [Vegetation Guide / 植被指南](11.2-Vegetation_Guide.md)
