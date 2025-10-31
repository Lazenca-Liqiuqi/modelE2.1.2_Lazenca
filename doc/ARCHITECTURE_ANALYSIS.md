# ModelE Architecture Analysis and Module Dependencies

## Executive Summary

ModelE is a complex Earth system model with a hierarchical, component-based architecture. The system is organized around physical processes and follows a modular design philosophy that separates concerns while maintaining data flow between components.
**ModelE是一个复杂的地球系统模型，采用分层、基于组件的架构。系统围绕物理过程进行组织，遵循模块化设计理念，在保持组件间数据流动的同时分离关注点。**

## Core Architecture
**核心架构**

### 1. Entry Points and Main Drivers
**1. 入口点和主驱动程序**

#### Main Program Flow
**主程序流程**
```text
main.F90
    ↓
modelE_mainDriver() (in MODELE.f)
    ↓
ATM_DRV.f (Atmospheric Driver)
    ↓
Various physics and dynamics modules
```

#### Key Driver Files
**关键驱动文件**
- **main.F90**: Simple entry point that calls the main driver
  **简单入口点，调用主驱动程序**

- **MODELE.f**: Main model controller, handles initialization, time stepping, and output
  **主模型控制器，处理初始化、时间步进和输出**

- **ATM_DRV.f**: Atmospheric process driver, orchestrates all atmospheric physics
  **大气过程驱动程序，协调所有大气物理过程**

- **OCN_DRV.f**: Ocean model driver (when coupled ocean is used)
  **海洋模型驱动程序（当使用耦合海洋时）**

- **GHY_DRV.f**: Land surface driver
  **陆面驱动程序**

### 2. Core Communication Modules
**2. 核心通信模块**

#### MODEL_COM.f
**中心模型状态模块**
- **Purpose**: Central model state and control variables
  **用途**: 中央模型状态和控制变量**

- **Key Variables**: Time management (Itime, ItimeI, ItimeE), run parameters, calendar
  **关键变量**: 时间管理(Itime, ItimeI, ItimeE)、运行参数、日历**

- **Dependencies**: Used by ALL other modules
  **依赖关系**: 被所有其他模块使用**

- **Role**: Provides global model context and timing information
  **作用**: 提供全局模型背景和计时信息**

#### ATM_COM.f
**大气状态模块**
- **Purpose**: Atmospheric state variables
  **用途**: 大气状态变量**

- **Key Variables**: 3D atmospheric fields (T, Q, U, V), mass, pressure
  **关键变量**: 3D大气场(T, Q, U, V)、质量、压力**

- **Dependencies**: Depends on MODEL_COM, used by all atmospheric modules
  **依赖关系**: 依赖MODEL_COM，被所有大气模块使用**

- **Role**: Central atmospheric state repository
  **作用**: 中央大气状态存储库**

#### FLUXES.f
**通量计算模块**
- **Purpose**: Surface flux calculations and energy/momentum exchange
  **用途**: 表面通量计算和能量/动量交换**

- **Key Variables**: Heat fluxes, momentum fluxes, water fluxes
  **关键变量**: 热通量、动量通量、水通量**

- **Dependencies**: Atmospheric modules, surface modules
  **依赖关系**: 大气模块、表面模块**

- **Role**: Interface between atmosphere and surface
  **作用**: 大气和表面之间的接口**

### 3. Component Architecture
**3. 组件架构**

#### Atmospheric Components
**大气组件**
```text
ATM_DRV.f (Main Driver)
    ├── ATMDYN.f (Dynamics Core)
    │   ├── DYNAM (B-grid dynamics)
    │   └── FV_INTERFACE (FV core dynamics)
    ├── RADIATION.f (Radiation Transfer)
    ├── CLOUDS2.F90 (Cloud Microphysics)
    ├── PBL.f (Planetary Boundary Layer)
    ├── convec.f (Convection)
    └── SURFACE.f (Surface Processes)
```

#### Surface Components
**表面组件**
```text
Surface Module System
    ├── GHY_DRV.f (Land Surface)
    │   ├── VEGETATION.f
    │   └── LAKES.f
    ├── SEAICE.f (Sea Ice)
    │   └── ICEDYN.f (Ice Dynamics)
    └── OCEAN.f (Ocean - when used)
```

#### Specialized Components
**专业组件**
- **Ent/**: Ent dynamic vegetation model
  **Ent/**: Ent动态植被模型**

- **giss_LSM/**: Land surface model components
  **giss_LSM/**: 陆面模型组件**

- **solvers/**: Numerical solvers for various equations
  **solvers/**: 各种方程的数值求解器**

- **shared/**: Common utilities and constants
  **shared/**: 公共工具和常数**

### 4. Data Flow Architecture
**4. 数据流架构**

#### Primary Data Flow
**主要数据流**
```text
Atmospheric State (ATM_COM)
    ↓
Dynamics (ATMDYN)
    ↓
Physics Processes (RADIATION, CLOUDS, PBL, etc.)
    ↓
Surface Fluxes (FLUXES)
    ↓
Surface Models (GHY_DRV, SEAICE, OCEAN)
    ↓
Updated Surface Conditions
    ↓
Back to Atmosphere (via fluxes)
```

#### Time Integration Loop
**时间积分循环**
1. **Dynamics Phase**: Update winds and mass via ATMDYN
   **动力学阶段**: 通过ATMDYN更新风和质量**

2. **Physics Phase**: Apply parameterizations (radiation, clouds, etc.)
   **物理阶段**: 应用参数化方案（辐射、云等）**

3. **Surface Phase**: Calculate surface-atmosphere exchanges
   **表面阶段**: 计算表面-大气交换**

4. **Diagnostic Phase**: Accumulate statistics and output
   **诊断阶段**: 积累统计和输出**

5. **Coupling Phase**: Exchange data with ocean/ice (if present)
   **耦合阶段**: 与海洋/冰交换数据（如果存在）**

### 5. Module Dependencies
**5. 模块依赖关系**

#### Dependency Hierarchy (Bottom-up)
**依赖层次结构（自下而上）**
```text
Level 1 (Base):
├── shared/ (Constants, utilities, time management)
└── MODEL_COM.f (Global model state)

Level 2 (Core):
├── ATM_COM.f (Atmospheric state)
├── RESOLUTION (Grid definitions)
└── GEOM (Geometry calculations)

Level 3 (Process modules):
├── ATMDYN.f (Dynamics)
├── RADIATION.f (Radiation)
├── CLOUDS2.F90 (Cloud physics)
└── PBL.f (Boundary layer)

Level 4 (Interface):
├── FLUXES.f (Surface fluxes)
├── SURFACE.f (Surface processes)
└── DIAG_COM.f (Diagnostics)

Level 5 (Drivers):
├── ATM_DRV.f (Main atmospheric driver)
├── GHY_DRV.f (Land driver)
└── OCEAN_DRV.f (Ocean driver)

Level 6 (Top-level):
└── MODELE.f (Main model controller)
```

#### Circular Dependencies
**循环依赖**
- The model carefully avoids circular dependencies through proper layering
  **模型通过适当的分层carefully避免循环依赖**

- Components only communicate through defined interfaces (fluxes, state variables)
  **组件仅通过定义的接口（通量、状态变量）通信**

- Time-stepping sequence prevents simultaneous updates that could cause issues
  **时间步进序列防止可能导致问题的同时更新**

### 6. Memory and Performance Architecture
**6. 内存和性能架构**

#### Memory Layout
**内存布局**
- **3D Arrays**: Organized as (layer, longitude, latitude) for cache efficiency
  **3D数组**: 为缓存效率组织为(层、经度、纬度)**

- **Halo Regions**: For parallel domain decomposition
  **Halo区域**: 用于并行域分解**

- **Temporary Arrays**: Minimized and reused to reduce memory footprint
  **临时数组**: 最小化并重用以减少内存占用**

- **State Management**: Centralized in COM modules
  **状态管理**: 在COM模块中集中化**

#### Parallel Architecture
**并行架构**
- **Domain Decomposition**: 2D horizontal decomposition for MPI
  **域分解**: MPI的2D水平分解**

- **OpenMP**: Shared memory parallelization within each MPI domain
  **OpenMP**: 每个MPI域内的共享内存并行化**

- **Hybrid**: MPI+OpenMP for large-scale parallel runs
  **混合**: 大规模并行运行的MPI+OpenMP**

### 7. Configuration and Build System
**7. 配置和构建系统**

#### Component Selection
**组件选择**
- Components are selected at compile time via makefile configuration
  **在编译时通过makefile配置选择组件**

- Optional features controlled via preprocessor directives
  **通过预处理器指令控制可选功能**

- Rundeck parameters control runtime behavior
  **Rundeck参数控制运行时行为**

#### Build Dependencies
**构建依赖**
- Components must be compiled in dependency order
  **组件必须按依赖顺序编译**

- Module files (.mod) used to manage Fortran 90 module dependencies
  **使用模块文件(.mod)管理Fortran 90模块依赖**

- Automatic dependency generation via make depend
  **通过make depend自动生成依赖**

### 8. Diagnostic System Architecture
**8. 诊断系统架构**

#### Diagnostic Accumulation
**诊断积累**
- **DIAG_COM.f**: Central diagnostic management
  **DIAG_COM.f**: 中央诊断管理**

- **Accumulation Arrays**: Time-averaged statistics
  **积累数组**: 时间平均统计**

- **Instantaneous Output**: Snapshots at specified intervals
  **瞬时输出**: 指定间隔的快照**

- **Budget Analysis**: Energy and water conservation checks
  **预算分析**: 能量和水量守恒检查**

#### Output Management
**输出管理**
- **POUT_netcdf.f**: NetCDF output interface
  **POUT_netcdf.f**: NetCDF输出接口**

- **POUT.f**: Traditional formatted output
  **POUT.f**: 传统格式化输出**

- **Diagnostic Pages**: Summary tables and plots
  **诊断页面**: 摘要表格和图表**

---

## 中文文档

# ModelE架构分析与模块依赖关系

## 执行摘要

ModelE是一个复杂的地球系统模型，采用分层、基于组件的架构。系统围绕物理过程进行组织，遵循模块化设计理念，在保持组件间数据流动的同时分离关注点。
**ModelE是一个复杂的地球系统模型，采用分层、基于组件的架构。系统围绕物理过程进行组织，遵循模块化设计理念，在保持组件间数据流动的同时分离关注点。**

## 核心架构
**核心架构**

### 1. 入口点和主驱动程序
**1. 入口点和主驱动程序**

#### 主程序流程
**主程序流程**
```text
main.F90
    ↓
modelE_mainDriver() (在MODELE.f中)
    ↓
ATM_DRV.f (大气驱动程序)
    ↓
各种物理和动力学模块
```

#### 关键驱动文件
**关键驱动文件**
- **main.F90**: 简单的入口点，调用主驱动程序
  **简单入口点，调用主驱动程序**

- **MODELE.f**: 主模型控制器，处理初始化、时间步进和输出
  **主模型控制器，处理初始化、时间步进和输出**

- **ATM_DRV.f**: 大气过程驱动程序，协调所有大气物理过程
  **大气过程驱动程序，协调所有大气物理过程**

- **OCN_DRV.f**: 海洋模型驱动程序（当使用耦合海洋时）
  **海洋模型驱动程序（当使用耦合海洋时）**

- **GHY_DRV.f**: 陆面驱动程序
  **陆面驱动程序**

### 2. 核心通信模块
**2. 核心通信模块**

#### MODEL_COM.f
**中心模型状态模块**
- **用途**: 中央模型状态和控制变量
  **用途**: 中央模型状态和控制变量**

- **关键变量**: 时间管理(Itime, ItimeI, ItimeE)、运行参数、日历
  **关键变量**: 时间管理(Itime, ItimeI, ItimeE)、运行参数、日历**

- **依赖关系**: 被所有其他模块使用
  **依赖关系**: 被所有其他模块使用**

- **作用**: 提供全局模型背景和计时信息
  **作用**: 提供全局模型背景和计时信息**

#### ATM_COM.f
**大气状态模块**
- **用途**: 大气状态变量
  **用途**: 大气状态变量**

- **关键变量**: 3D大气场(T, Q, U, V)、质量、压力
  **关键变量**: 3D大气场(T, Q, U, V)、质量、压力**

- **依赖关系**: 依赖MODEL_COM，被所有大气模块使用
  **依赖关系**: 依赖MODEL_COM，被所有大气模块使用**

- **作用**: 中央大气状态存储库
  **作用**: 中央大气状态存储库**

#### FLUXES.f
**通量计算模块**
- **用途**: 表面通量计算和能量/动量交换
  **用途**: 表面通量计算和能量/动量交换**

- **关键变量**: 热通量、动量通量、水通量
  **关键变量**: 热通量、动量通量、水通量**

- **依赖关系**: 大气模块、表面模块
  **依赖关系**: 大气模块、表面模块**

- **作用**: 大气和表面之间的接口
  **作用**: 大气和表面之间的接口**

### 3. 组件架构
**3. 组件架构**

#### 大气组件
**大气组件**
```text
ATM_DRV.f (主驱动程序)
    ├── ATMDYN.f (动力学核心)
    │   ├── DYNAM (B网格动力学)
    │   └── FV_INTERFACE (FV核心动力学)
    ├── RADIATION.f (辐射传输)
    ├── CLOUDS2.F90 (云微物理)
    ├── PBL.f (行星边界层)
    ├── convec.f (对流)
    └── SURFACE.f (表面过程)
```

#### 表面组件
**表面组件**
```text
表面模块系统
    ├── GHY_DRV.f (陆面)
    │   ├── VEGETATION.f
    │   └── LAKES.f
    ├── SEAICE.f (海冰)
    │   └── ICEDYN.f (冰动力学)
    └── OCEAN.f (海洋 - 使用时)
```

#### 专业组件
**专业组件**
- **Ent/**: Ent动态植被模型
  **Ent/**: Ent动态植被模型**

- **giss_LSM/**: 陆面模型组件
  **giss_LSM/**: 陆面模型组件**

- **solvers/**: 各种方程的数值求解器
  **solvers/**: 各种方程的数值求解器**

- **shared/**: 公共工具和常数
  **shared/**: 公共工具和常数**

### 4. 数据流架构
**4. 数据流架构**

#### 主要数据流
**主要数据流**
```text
大气状态 (ATM_COM)
    ↓
动力学 (ATMDYN)
    ↓
物理过程 (RADIATION, CLOUDS, PBL, 等)
    ↓
表面通量 (FLUXES)
    ↓
表面模型 (GHY_DRV, SEAICE, OCEAN)
    ↓
更新的表面条件
    ↓
返回大气（通过通量）
```

#### 时间积分循环
**时间积分循环**
1. **动力学阶段**: 通过ATMDYN更新风和质量
   **动力学阶段**: 通过ATMDYN更新风和质量**

2. **物理阶段**: 应用参数化方案（辐射、云等）
   **物理阶段**: 应用参数化方案（辐射、云等）**

3. **表面阶段**: 计算表面-大气交换
   **表面阶段**: 计算表面-大气交换**

4. **诊断阶段**: 积累统计和输出
   **诊断阶段**: 积累统计和输出**

5. **耦合阶段**: 与海洋/冰交换数据（如果存在）
   **耦合阶段**: 与海洋/冰交换数据（如果存在）**

### 5. 模块依赖关系
**5. 模块依赖关系**

#### 依赖层次结构（自下而上）
**依赖层次结构（自下而上）**
```text
第1层（基础）:
├── shared/ (常数、工具、时间管理)
└── MODEL_COM.f (全局模型状态)

第2层（核心）:
├── ATM_COM.f (大气状态)
├── RESOLUTION (网格定义)
└── GEOM (几何计算)

第3层（过程模块）:
├── ATMDYN.f (动力学)
├── RADIATION.f (辐射)
├── CLOUDS2.F90 (云物理)
└── PBL.f (边界层)

第4层（接口）:
├── FLUXES.f (表面通量)
├── SURFACE.f (表面过程)
└── DIAG_COM.f (诊断)

第5层（驱动程序）:
├── ATM_DRV.f (主大气驱动程序)
├── GHY_DRV.f (陆面驱动程序)
└── OCEAN_DRV.f (海洋驱动程序)

第6层（顶层）:
└── MODELE.f (主模型控制器)
```

#### 循环依赖
**循环依赖**
- 模型通过适当的分层carefully避免循环依赖
  **模型通过适当的分层carefully避免循环依赖**

- 组件仅通过定义的接口（通量、状态变量）通信
  **组件仅通过定义的接口（通量、状态变量）通信**

- 时间步进序列防止可能导致问题的同时更新
  **时间步进序列防止可能导致问题的同时更新**

### 6. 内存和性能架构
**6. 内存和性能架构**

#### 内存布局
**内存布局**
- **3D数组**: 为缓存效率组织为(层、经度、纬度)
  **3D数组**: 为缓存效率组织为(层、经度、纬度)**

- **Halo区域**: 用于并行域分解
  **Halo区域**: 用于并行域分解**

- **临时数组**: 最小化并重用以减少内存占用
  **临时数组**: 最小化并重用以减少内存占用**

- **状态管理**: 在COM模块中集中化
  **状态管理**: 在COM模块中集中化**

#### 并行架构
**并行架构**
- **域分解**: MPI的2D水平分解
  **域分解**: MPI的2D水平分解**

- **OpenMP**: 每个MPI域内的共享内存并行化
  **OpenMP**: 每个MPI域内的共享内存并行化**

- **混合**: 大规模并行运行的MPI+OpenMP
  **混合**: 大规模并行运行的MPI+OpenMP**

### 7. 配置和构建系统
**7. 配置和构建系统**

#### 组件选择
**组件选择**
- 在编译时通过makefile配置选择组件
  **在编译时通过makefile配置选择组件**

- 通过预处理器指令控制可选功能
  **通过预处理器指令控制可选功能**

- Rundeck参数控制运行时行为
  **Rundeck参数控制运行时行为**

#### 构建依赖
**构建依赖**
- 组件必须按依赖顺序编译
  **组件必须按依赖顺序编译**

- 使用模块文件(.mod)管理Fortran 90模块依赖
  **使用模块文件(.mod)管理Fortran 90模块依赖**

- 通过make depend自动生成依赖
  **通过make depend自动生成依赖**

### 8. 诊断系统架构
**8. 诊断系统架构**

#### 诊断积累
**诊断积累**
- **DIAG_COM.f**: 中央诊断管理
  **DIAG_COM.f**: 中央诊断管理**

- **积累数组**: 时间平均统计
  **积累数组**: 时间平均统计**

- **瞬时输出**: 指定间隔的快照
  **瞬时输出**: 指定间隔的快照**

- **预算分析**: 能量和水量守恒检查
  **预算分析**: 能量和水量守恒检查**

#### 输出管理
**输出管理**
- **POUT_netcdf.f**: NetCDF输出接口
  **POUT_netcdf.f**: NetCDF输出接口**

- **POUT.f**: 传统格式化输出
  **POUT.f**: 传统格式化输出**

- **诊断页面**: 摘要表格和图表
  **诊断页面**: 摘要表格和图表**

---

## 关键架构特性

### 优势
**优势**
1. **模块化设计**: 清晰的组件分离，便于维护和扩展
   **模块化设计**: 清晰的组件分离，便于维护和扩展**

2. **层次结构**: 避免循环依赖，保持代码清晰
   **层次结构**: 避免循环依赖，保持代码清晰**

3. **配置灵活**: 通过编译和运行时参数控制功能
   **配置灵活**: 通过编译和运行时参数控制功能**

4. **并行友好**: 支持多种并行化策略
   **并行友好**: 支持多种并行化策略**

### 挑战
**挑战**
1. **复杂性**: 大量模块和接口增加了理解难度
   **复杂性**: 大量模块和接口增加了理解难度**

2. **性能**: 老旧的代码结构可能影响现代处理器性能
   **性能**: 老旧的代码结构可能影响现代处理器性能**

3. **维护**: 大型代码库的维护需要大量工作
   **维护**: 大型代码库的维护需要大量工作**

4. **现代化**: 需要逐步更新到现代Fortran标准
   **现代化**: 需要逐步更新到现代Fortran标准**

### 改进机会
**改进机会**
1. **重构**: 逐步现代化关键模块
   **重构**: 逐步现代化关键模块**

2. **优化**: 改善内存访问模式和计算效率
   **优化**: 改善内存访问模式和计算效率**

3. **测试**: 增加自动化测试覆盖率
   **测试**: 增加自动化测试覆盖率**

4. **文档**: 持续改进代码和架构文档
   **文档**: 持续改进代码和架构文档**

---

*此文档基于ModelE v2.1.2/3.0代码分析，将根据代码发展持续更新。*
