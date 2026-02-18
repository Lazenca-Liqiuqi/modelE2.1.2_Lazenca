# Documentation Navigation / ModelE2.1.2_Lazenca 文档导航

这是NASA GISS ModelE 2.1.2（Lazenca分支）的中文翻译文档库，涵盖大气环流模型(GCM)、海洋、陆面、海冰、化学等完整地球系统组件。

---

## 快速导航 / Quick Navigation

| 目录 | 说明 | 文档数 |
|------|------|--------|
| [UserGuide](#1-userguide-用户指南) | 用户指南：编译、运行、配置 | 42 |
| [ModelDescription](#2-modeldescription-模型描述) | 模型描述：技术文档 | 36 |
| [HOWTO](#3-howto-操作指南) | 操作指南：实用信息 | 4 |
| [misc](#4-misc-杂项文档) | 杂项文档：编码规范、变更历史 | 3 |
| [archive-old-doc](#5-archive-old-doc-原始文档存档) | 原始英文文档存档 | 93 |

---

## 1. UserGuide 用户指南

完整的ModelE使用指南，包括获取代码、配置、编译、运行和诊断输出。

### 1.1 获取代码并配置模型

| 文档 | 说明 |
|------|------|
| [System requirements](UserGuide/1.1-System_requirements.md) | 系统需求 |
| [Getting the code from GISS repository](UserGuide/1.2-Getting_the_code_from_GISS_repository.md) | 从GISS代码仓库获取代码 |
| [Configuring modelE on your machine](UserGuide/1.3-Configuring_modelE_on_your_machine.md) | 在本机配置ModelE |

### 1.2 快速开始

| 文档 | 说明 |
|------|------|
| [Creating a rundeck](UserGuide/2.1-Creating_a_rundeck.md) | 创建运行配置（Rundeck） |
| [Downloading necessary input files](UserGuide/2.2-Downloading_necessary_input_files.md) | 下载所需输入文件 |
| [Compiling the model](UserGuide/2.3-Compiling_the_model.md) | 编译模型并设置运行目录 |
| [Running the model](UserGuide/2.4-Running_the_model.md) | 运行模型 |
| [Looking at model output](UserGuide/2.5-Looking_at_model_output.md) | 查看模型输出 |

### 1.3 运行配置（Rundeck）

| 文档 | 说明 |
|------|------|
| [General rundeck structure](UserGuide/3.1-General_rundeck_structure.md) | 运行配置的一般结构 |
| [Major rundeck parameters](UserGuide/3.2-Major_rundeck_parameters.md) | 运行配置主要参数 |
| [Input files](UserGuide/3.3-Input_files.md) | 输入文件 |
| [Date and time](UserGuide/3.4-Date_and_time.md) | 日期与时间 |
| [Choosing proper ISTART](UserGuide/3.5-Choosing_proper_ISTART.md) | 选择合适的ISTART |

### 1.4 配置特定模拟

| 文档 | 说明 |
|------|------|
| [Qflux single ocean](UserGuide/4.1-Qflux_single_ocean.md) | 单海洋层Q-flux模式 |
| [Qflux deep ocean](UserGuide/4.2-Qflux_deep_ocean.md) | 含深海扩散的Q-flux模式 |
| [Paleoclimate simulation](UserGuide/4.3-Paleoclimate_simulation.md) | 古气候模拟 |
| [IRANDI ensemble](UserGuide/4.4-IRANDI_ensemble.md) | 使用IRANDI构建集合试验 |
| [Altering topography](UserGuide/4.5-Altering_topography.md) | 修改地形文件 |
| [Altering land mask](UserGuide/4.6-Altering_land_mask.md) | 修改陆地掩膜 |
| [Altering trace gases](UserGuide/4.7-Altering_trace_gases.md) | 调整痕量气体浓度 |

### 1.5 运行模型

| 文档 | 说明 |
|------|------|
| [Start stop restart](UserGuide/5.1-Start_stop_restart.md) | 启动、停止与重启模型运行 |
| [Tuning energy balance](UserGuide/5.2-Tuning_energy_balance.md) | 调整模型能量平衡 |
| [Controlling instabilities](UserGuide/5.3-Controlling_instabilities.md) | 控制数值不稳定性 |

### 1.6 诊断输出

| 文档 | 说明 |
|------|------|
| [Looking at output](UserGuide/6.1-Looking_at_output.md) | 查看输出 |
| [Changing printout content](UserGuide/6.2-Changing_printout_content.md) | 调整打印输出内容 |
| [Producing diagnostics](UserGuide/6.3-Producing_diagnostics.md) | 生成日/月或季节诊断 |
| [Controlling binary output](UserGuide/6.4-Controlling_binary_output.md) | 控制二进制输出格式 |
| [Calculating model score](UserGuide/6.5-Calculating_model_score.md) | 计算模型评分 |

### 1.7 修改代码

| 文档 | 说明 |
|------|------|
| [Coding standards](UserGuide/7.1-Coding_standards.md) | ModelE编码规范 |
| [Adding info for automatic documentation](UserGuide/7.2-Adding_info_for_automatic_documentation.md) | 添加自动化文档信息 |
| [New rundeck parameter](UserGuide/7.3-New_rundeck_parameter.md) | 引入新的运行配置参数 |
| [New diagnostics](UserGuide/7.4-New_diagnostics.md) | 添加新的诊断 |
| [Reading external files](UserGuide/7.5-Reading_external_files.md) | 读取外部文件 |
| [New restart variable](UserGuide/7.6-New_restart_variable.md) | 向重启文件添加新变量 |

### 1.8 测试与调试

| 文档 | 说明 |
|------|------|
| [Testing reproducibility](UserGuide/8.1-Testing_reproducibility.md) | 测试ModelE可复现性 |
| [Running with traps](UserGuide/8.2-Running_with_traps.md) | 使用陷阱运行模型 |
| [Running in debugger](UserGuide/8.3-Running_in_debugger.md) | 在调试器中运行模型 |

### 1.9 示踪物

| 文档 | 说明 |
|------|------|
| [Tracer Preprocessor Options](UserGuide/9.1-Tracer_Preprocessor_Options.md) | 示踪物预处理器选项 |
| [Tracer Rundeck Parameters](UserGuide/9.2-Tracer_Rundeck_Parameters.md) | 示踪物运行配置参数 |

### 1.10-11 帮助与附录

| 文档 | 说明 |
|------|------|
| [Getting help](UserGuide/10-Getting_help.md) | 获取帮助 |
| [Installing NetCDF library](UserGuide/11.1-Installing_NetCDF_library.md) | 安装NetCDF库 |
| [Vegetation Guide](UserGuide/11.2-Vegetation_Guide.md) | 植被指南 |

---

## 2. ModelDescription 模型描述

ModelE技术文档，描述大气、海洋、陆面、海冰、示踪物等完整地球系统组件。

### 2.1 整体模型结构

| 文档 | 说明 |
|------|------|
| [Overall_model_structure](ModelDescription/Overall_model_structure.md) | 整体模型结构 |
| [Source_code_and_directory_structure](ModelDescription/Source_code_and_directory_structure.md) | 源代码和目录结构 |
| [Initialisation](ModelDescription/Initialisation.md) | 初始化 |
| [Main_time_stepping_loop](ModelDescription/Main_time_stepping_loop.md) | 主时间步进循环 |
| [Diagnostics](ModelDescription/Diagnostics.md) | 诊断输出 |
| [Input_Output](ModelDescription/Input_Output.md) | 输入输出 |
| [Water_Budget](ModelDescription/Water_Budget.md) | 水预算和守恒 |

### 2.2 大气模型

| 文档 | 说明 |
|------|------|
| [Atmospheric_model](ModelDescription/Atmospheric_model.md) | 大气模型 |
| [Dynamics](ModelDescription/Dynamics.md) | 动力学 |
| [Cloud_processes](ModelDescription/Cloud_processes.md) | 云过程 |
| [Radiation](ModelDescription/Radiation.md) | 辐射 |
| [Surface_fluxes](ModelDescription/Surface_fluxes.md) | 地表通量（包括行星边界层物理） |
| [Turbulence_and_Dry_convection](ModelDescription/Turbulence_and_Dry_convection.md) | 湍流和干对流 |
| [Stratospheric_processes](ModelDescription/Stratospheric_processes.md) | 平流层过程（包括重力波曳力） |

### 2.3 陆面模型

| 文档 | 说明 |
|------|------|
| [Land_Surface_model](ModelDescription/Land_Surface_model.md) | 陆面模型 |
| [Ground_Hydrology](ModelDescription/Ground_Hydrology.md) | 地面水文 |
| [Snow_model](ModelDescription/Snow_model.md) | 雪模型 |
| [Vegetation_model](ModelDescription/Vegetation_model.md) | 植被模型 |
| [Lake_model](ModelDescription/Lake_model.md) | 湖泊模型 |
| [Rivers](ModelDescription/Rivers.md) | 河流 |

### 2.4 海洋模型

| 文档 | 说明 |
|------|------|
| [Ocean_models](ModelDescription/Ocean_models.md) | 海洋模型 |
| [Imposed_Sea_surface_conditions](ModelDescription/Imposed_Sea_surface_conditions.md) | 强迫海面条件 |
| [Q-flux_mixed_layer_model](ModelDescription/Q-flux_mixed_layer_model.md) | Q-flux（混合层模型） |
| [GISS_Dynamic_ocean_model](ModelDescription/GISS_Dynamic_ocean_model.md) | GISS动力学海洋模型 |
| [HYCOM](ModelDescription/HYCOM.md) | HYCOM等密度面模型 |

### 2.5 海冰模型

| 文档 | 说明 |
|------|------|
| [Sea_ice_model](ModelDescription/Sea_ice_model.md) | 海冰模型 |
| [Basic_thermodynamics](ModelDescription/Basic_thermodynamics.md) | 基础热力学 |
| [Ice_advection](ModelDescription/Ice_advection.md) | 海冰平流 |

### 2.6 示踪物

| 文档 | 说明 |
|------|------|
| [Tracers](ModelDescription/Tracers.md) | 示踪物 |
| [Air_mass_Tracers](ModelDescription/Air_mass_Tracers.md) | 气质量示踪物 |
| [Soluble_and_Water_mass_Tracers](ModelDescription/Soluble_and_Water_mass_Tracers.md) | 可溶性和水质量示踪物 |
| [Aerosol_Tracers](ModelDescription/Aerosol_Tracers.md) | 气溶胶示踪物 |
| [Gas_Tracers](ModelDescription/Gas_Tracers.md) | 气体示踪物 |
| [Ocean_Tracers](ModelDescription/Ocean_Tracers.md) | 海洋示踪物 |
| [Special_Tracers](ModelDescription/Special_Tracers.md) | 特殊示踪物 |

### 2.7 参考文献

| 文档 | 说明 |
|------|------|
| [References](ModelDescription/References.md) | 参考文献 |

---

## 3. HOWTO 操作指南

实用的操作指南和信息。

| 文档 | 说明 |
|------|------|
| [git_howto](HOWTO/git_howto.md) | 如何使用Git管理模型源代码 |
| [newio](HOWTO/newio.md) | 如何使用模型的最新I/O系统 |
| [SCM](HOWTO/SCM.md) | 如何以单列模式运行模型 |
| [time_management](HOWTO/time_management.md) | 如何使用时间管理系统 |

---

## 4. misc 杂项文档

辅助文档和参考资料。

| 文档 | 说明 |
|------|------|
| [CHANGES](misc/CHANGES.md) | 变更历史 |
| [ModelE_Coding_Standards](misc/ModelE_Coding_Standards.md) | 编码规范 |
| [rundeck](misc/rundeck.md) | Rundeck配置详解 |

---

## 5. archive-old-doc 原始文档存档

原始英文文档存档，包含：
- `HOWTO/` - 原始操作指南
- `ModelDescription/` - 原始技术文档
- `UserGuide/` - 原始用户指南
- `misc/` - 原始杂项文档
- `obsolete/` - 过时文档

---

## 文档统计 / Statistics

| 类别 | 数量 |
|------|------|
| 翻译文档总数 | 86个 .md 文件 |
| UserGuide | 42个 |
| ModelDescription | 36个 |
| HOWTO | 4个 |
| misc | 3个 |

---

## 翻译规范 / Translation Standards

- **格式**: 中英对照叠放格式（英文在上，中文在下）
- **标题**: `# English / 中文`
- **术语**: 遵循术语词典 v1.7
- **质量**: Codex审查均分 95+

---

## 版本信息 / Version

- **基础模型**: NASA GISS ModelE 2.1.2
- **分支版本**: Lazenca Fork
- **当前版本**: 0.4.0
- **最后更新**: 2026-02-17

---

**探索地球系统，理解气候变化 | Explore Earth Systems, Understand Climate Change**

**Document End / 文档结束**
