# Index / ModelE2.1.2_Lazenca 模型描述文档索引

本文档提供NASA GISS ModelE 2.1.2（Lazenca分支）的完整技术描述。

---

## 项目概述

ModelE2.1.2_Lazenca是基于NASA GISS ModelE 2.1.2的个人分支，专注于地球系统模型的中文翻译和本地化。该模型涵盖大气环流模型(GCM)、海洋、陆面、海冰、化学等完整地球系统组件，主要服务于气候变化研究、古气候模拟和天气气候过程分析。

模型开发是一个持续的任务。随着新物理过程的引入、旧bug的发现和新应用的开发，代码几乎不断地进行小幅度的、有时是重大的重构。因此，对模型的任何固定描述都可能在其发布之日就已过时。考虑到这一点，我们将努力尽可能紧密地维护本文档的Web版本，使其与当前版本保持一致，但不可避免的是，此处的某些讨论偶尔会落后于开发。

GISS GCM模型开发过程已有25年以上的历史。不可避免的是，在过程早期做出的决定和存在的约束对后续仍有影响。虽然模型的大部分后续重构减少了这些历史影响，但模型的某些部分仍然可以追溯到打孔卡片、Fortran 66和行式打印机输出的时代。一个宽容的解释是，在接受新技术（Fortran 90/95、多处理、netcdf等）的同时，我们努力维护一些更无害的GISS传统（有些人可能称之为怪癖），以保持与以前从事模型工作的人员的连续性精神。另一方面，一些早期决定（例如关于诊断或守恒性质）证明是非常有远见的，是GISS系列模型继续在GCM模拟世界中发挥有用和重要作用的主要原因之一。我们希望通过继续使GISS模型更容易获得和更好地记录，我们将能够在这个方向上继续至少25年。

---

## 文档目录

### 1. 整体模型结构

- [Overall_model_structure](Overall_model_structure.md) - 整体模型结构
  - [Source_code_and_directory_structure](Source_code_and_directory_structure.md) - 源代码和目录结构
  - [Initialisation](Initialisation.md) - 初始化
  - [Main_time_stepping_loop](Main_time_stepping_loop.md) - 主时间步进循环
  - [Diagnostics](Diagnostics.md) - 诊断输出
  - [Input_Output](Input_Output.md) - 输入输出
  - [Water_Budget](Water_Budget.md) - 水预算和守恒

### 2. 大气模型

- [Atmospheric_model](Atmospheric_model.md) - 大气模型
  - [Dynamics](Dynamics.md) - 动力学
  - [Cloud_processes](Cloud_processes.md) - 云过程
  - [Radiation](Radiation.md) - 辐射
  - [Surface_fluxes](Surface_fluxes.md) - 地表通量（包括行星边界层物理）
  - [Turbulence_and_Dry_convection](Turbulence_and_Dry_convection.md) - 湍流和干对流
  - [Stratospheric_processes](Stratospheric_processes.md) - 平流层过程（包括重力波曳力）

### 3. 陆面模型

- [Land_Surface_model](Land_Surface_model.md) - 陆面模型
  - [Ground_Hydrology](Ground_Hydrology.md) - 地面水文
  - [Snow_model](Snow_model.md) - 雪模型
  - [Vegetation_model](Vegetation_model.md) - 植被模型
  - [Lake_model](Lake_model.md) - 湖泊模型
  - [Rivers](Rivers.md) - 河流

### 4. 海洋模型

- [Ocean_models](Ocean_models.md) - 海洋模型
  - [Imposed_Sea_surface_conditions](Imposed_Sea_surface_conditions.md) - 强迫海面条件
  - [Q-flux_mixed_layer_model](Q-flux_mixed_layer_model.md) - Q-flux（混合层模型）
  - [GISS_Dynamic_ocean_model](GISS_Dynamic_ocean_model.md) - GISS动力学海洋模型
  - HYCOM - HYCOM等密度面模型（备选模型）

### 5. 海冰模型

- [Sea_ice_model](Sea_ice_model.md) - 海冰模型
  - [Basic_thermodynamics](Basic_thermodynamics.md) - 基础热力学
  - [Ice_advection](Ice_advection.md) - 海冰平流

### 6. 示踪物

- [Tracers](Tracers.md) - 示踪物
  - [Air_mass_Tracers](Air_mass_Tracers.md) - 气质量示踪物
  - [Soluble_and_Water_mass_Tracers](Soluble_and_Water_mass_Tracers.md) - 可溶性和水质量示踪物
  - [Aerosol_Tracers](Aerosol_Tracers.md) - 气溶胶示踪物
  - [Ocean_Tracers](Ocean_Tracers.md) - 海洋示踪物
  - [Special_Tracers](Special_Tracers.md) - 特殊示踪物

### 7. 参考文献

- [References](References.md) - 参考文献

---

## 使用说明

### 文档格式

所有技术文档采用**中英对照叠放格式**：
- 标题：`# English / 中文`
- 段落：英文在上，中文在下
- 术语：保持专业术语的准确性和一致性

### 快速导航

如果您是首次使用ModelE，建议按以下顺序阅读：
1. **整体模型结构** → 了解模型的基本架构
2. **大气模型** → 理解大气过程和动力学
3. **陆面模型** → 学习陆面-大气相互作用
4. **海洋模型** → 掌握海洋动力学和热力学
5. **海冰模型** → 了解海冰热力学和动力学
6. **示踪物** → 熟悉示踪物系统（气溶胶、化学物质等）

### 编译和运行

详细的编译和运行指南，请参阅：
- [UserGuide索引](../UserGuide/0-index.md)
- [编译模型](../UserGuide/2.3-Compiling_the_model.md)
- [运行模型](../UserGuide/2.4-Running_the_model.md)

---

## 版本信息

- **基础模型**: NASA GISS ModelE 2.1.2
- **分支版本**: Lazenca Fork
- **当前版本**: 0.2.2
- **翻译完成度**: 33/33 核心技术文档（100%）
- **最后更新**: 2026-02-05

---

## 联系方式

### 项目仓库
- [GitHub: Lazenca-Liqiuqi/modelE2.1.2_Lazenca](https://github.com/Lazenca-Liqiuqi/modelE2.1.2_Lazenca)

### 官方资源
- [NASA GISS ModelE官方网站](https://www.giss.nasa.gov/tools/modelE/)
- [NASA GISS ModelE用户指南](http://simplex.giss.nasa.gov/gcm/doc/UserGuide/index.html)

### 技术支持
- 问题报告：[GitHub Issues](https://github.com/Lazenca-Liqiuqi/modelE2.1.2_Lazenca/issues)
- 技术文档：见本文档各章节

---

**探索地球系统，理解气候变化 | Explore Earth Systems, Understand Climate Change**

*基于NASA GISS ModelE 2.1.2 | Based on NASA GISS ModelE 2.1.2*
