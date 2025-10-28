# ModelE2.1.2_Lazenca项目概览

## 项目基本信息

**项目名称**: ModelE2.1.2_Lazenca - NASA GISS地球系统模型Lazenca分支
**版本**: v0.1.1 (基于ModelE 2.1.2的独立分支)
**开发者**: Lazenca (基于NASA GISS ModelE 2.1.2)
**项目类型**: 大气环流模型(GCM)/地球系统模型
**主要语言**: Fortran 90/95, 部分C代码
**代码规模**: 超过33万行代码
**许可证**: NASA开源许可证
**Fork性质**: 基于ModelE 2.1.2的个人分支，版本自主管理

## 项目用途

ModelE2.1.2_Lazenca是NASA GISS ModelE 2.1.2的个人分支版本，主要用于：
- 气候变化研究和预测
- 古气候模拟
- 天气和气候过程研究
- 地球系统相互作用分析

## 项目架构

### 目录结构
```
modelE2.1.2_Lazenca/
├── model/          # 核心模型源代码
│   ├── main.F90    # 主程序入口
│   ├── ATM_DRV.f   # 大气驱动程序
│   ├── ATMDYN.f    # 大气动力学核心
│   ├── RADIATION.f # 辐射传输模块
│   ├── CLOUDS2.F90 # 云微物理过程
│   ├── OCEAN.f     # 海洋模块
│   ├── GHY_DRV.f   # 陆面过程驱动
│   ├── SEAICE.f    # 海冰模块
│   ├── TRACERS_DRV.f # 示踪物传输
│   └── shared/     # 共享工具模块
├── config/         # 编译配置文件
├── decks/          # 运行配置目录
├── doc/           # 文档目录
├── aux/           # 辅助程序
├── exec/          # 执行脚本
├── init_cond/     # 初始条件
├── diags/         # 诊断工具
└── tests/         # 测试文件
```

### 核心组件

#### 1. 大气模块 (Atmosphere)
- **ATM_DRV.f**: 大气过程主驱动
- **ATMDYN.f**: 动力学核心（支持B-grid和FV核心）
- **RADIATION.f**: 长波和短波辐射计算
- **CLOUDS2.F90**: 云微物理和宏观物理过程
- **PBL.f**: 行星边界层过程
- **convec.f**: 对流参数化

#### 2. 海洋模块 (Ocean)
- **OCNDYN.f**: 海洋动力学
- **OCNKPP.f**: KPP垂直混合方案
- **OCNQUS.f**: 准地转方案
- **OCN_TRACER.f**: 海洋示踪物

#### 3. 陆面模块 (Land Surface)
- **GHY_DRV.f**: 陆面过程驱动
- **LAKES.f**: 湖泊模型
- **VEG_DRV.f**: 植被过程
- **LANDICE.f**: 冰盖模型

#### 4. 海冰模块 (Sea Ice)
- **SEAICE.f**: 海冰热力学和动力学
- **ICEDYN.f**: 海冰动力学

#### 5. 化学和气溶胶模块
- **TRACERS_DRV.f**: 示踪物传输主程序
- **TRCHEM_Shindell_COM.f**: 化学反应机制
- **TOMAS_drv.f**: 气溶胶微物理过程

## 构建系统

### 编译要求
- **编译器**: 支持gfortran, intel, pgi等
- **并行**: MPI/OpenMP混合并行
- **库依赖**: NetCDF, LAPACK, BLAS
- **平台**: Linux, macOS, Windows(WSL)

### 构建流程
1. `make config COMPILER=gfortran` - 配置编译环境
2. `cd decks` - 进入工作目录
3. `gmake rundeck RUN=run_name` - 创建运行配置
4. `gmake setup RUN=run_name` - 编译和设置
5. `../exec/runE run_name` - 运行模型

## 模型配置

### 分辨率选项
- **2°×2.5°**: 144×90网格
- **4°×5°**: 72×46网格
- **8°×10°**: 36×24网格
- **立方体球面**: C90等分辨率

### 垂直层次
- **低分辨率**: 12层
- **标准分辨率**: 40层
- **高分辨率**: 53层, 100层

## 当前状态

### 版本历史
- **v2.1.2/3.0**: 当前版本，包含完整的地球系统组件
- **主要改进**: 相比AR4版本增加了立方体球面动力学、完整化学机制、海洋生物地球化学循环

### 已知问题
1. 编译系统较为传统，缺乏现代CI/CD支持
2. 测试覆盖率有限
3. 文档需要系统性整理
4. 部分模块代码复杂度较高

### 维护状态
- **活跃度**: 中等（主要维护者为NASA GISS团队）
- **社区**: 学术研究用户为主
- **更新频率**: 不定期，主要针对科学需求更新

## 使用建议

### 新用户学习路径
1. 阅读官方用户指南 (doc/UserGuide/index.html)
2. 从标准配置开始，逐步理解各模块功能
3. 使用诊断工具验证结果
4. 根据研究需求修改配置

### 开发者注意事项
1. 遵循现有代码规范和模块化设计
2. 注意数值稳定性和能量守恒
3. 充分测试修改对物理过程的影响
4. 保持与原有接口的兼容性

## 技术特性

### 数值方法
- **时间积分**: 显式/隐式混合方案
- **平流**: 有限差分/谱方法
- **求解器**: 多重网格、共轭梯度法

### 物理过程
- **辐射**: δ-Eddington二流近似
- **云微物理**: 体积水方案
- **边界层**: 湍流K理论
- **陆面过程**: 简化水文模型

### 并行化
- **域分解**: 水平方向MPI分解
- **OpenMP**: 共享内存并行
- **混合并行**: MPI+OpenMP模式

## 相关资源

### 官方文档
- 用户指南: http://simplex.giss.nasa.gov/gcm/doc/UserGuide/index.html
- 代码仓库: NASA内部CVS系统

### 学术文献
- Schmidt, G.A., et al. (2014). Configuration and assessment of the GISS ModelE2 contributions to the CMIP5 archive.
- 相关期刊论文和技术报告

### 社区支持
- 邮件列表: modelE-users
- 学术会议: AGU, EGU等

## 项目记忆系统 | Project Memory System

### 记忆组件架构 | Memory Component Architecture
本项目遵循标准项目记忆技能规范，采用三组件架构：
**This project follows standard project memory skill specifications, adopting a three-component architecture:**

- **CLAUDE.md** (根目录) - AI可读的项目技术概览，包含架构、模块、构建系统信息
**CLAUDE.md** (Root directory) - AI-readable project technical overview, including architecture, modules, build system information
- **README.md** (根目录) - 人类友好的项目使用指南，重点关注使用指导
**README.md** (Root directory) - Human-friendly project usage guide, focusing on usage instructions
- **CHANGELOG.md** (根目录) - 版本历史和主要变更记录
**CHANGELOG.md** (Root directory) - Version history and major change records

### 技术文档扩展 | Technical Documentation Extension
- **doc/ARCHITECTURE_ANALYSIS.md** - 详细架构分析，模块依赖关系，数据流分析
**doc/ARCHITECTURE_ANALYSIS.md** - Detailed architecture analysis, module dependencies, data flow analysis
- **doc/PROJECT_ANALYSIS_REPORT.md** - 全面项目分析，包含技术债务评估和现代化路线图
**doc/PROJECT_ANALYSIS_REPORT.md** - Comprehensive project analysis, including technical debt assessment and modernization roadmap
- **doc/PROJECT_MEMORY_INDEX.md** - 项目记忆系统索引和使用指南
**doc/PROJECT_MEMORY_INDEX.md** - Project memory system index and usage guide

### 当前项目状态 | Current Project Status
- **版本信息 | Version Information**: ModelE2.1.2_Lazenca v0.1.1 (基于 ModelE 2.1.2)
- **文档系统 | Documentation System**: 段落级中英对照格式，支持连续阅读
**Documentation System**: Paragraph-level bilingual format, supporting continuous reading
- **维护状态 | Maintenance Status**: 活跃维护，文档系统持续完善
**Maintenance Status**: Active maintenance, documentation system continuously improved
- **技术债务 | Technical Debt**: 识别的关键问题包括代码现代化、测试基础设施、构建系统改进
**Technical Debt**: Key identified issues include code modernization, testing infrastructure, build system improvements
- **GitHub仓库 | GitHub Repository**: https://github.com/Lazenca-Liqiuqi/modelE2.1.2_Lazenca
- **项目类型 | Project Type**: 基于NASA GISS ModelE 2.1.2的个人fork分支
**Project Type**: Personal fork branch based on NASA GISS ModelE 2.1.2

### 近期工作重点 | Recent Work Focus
1. **文档系统建立 | Documentation System Establishment** - 完整的现代化文档架构
**Complete modernized documentation architecture**
2. **格式标准化 | Format Standardization** - 统一的中英对照段落格式
**Unified bilingual paragraph format**
3. **技术分析 | Technical Analysis** - 深度代码分析和架构评估
**In-depth code analysis and architecture assessment**
4. **知识组织 | Knowledge Organization** - 系统性信息管理和检索
**Systematic information management and retrieval**
5. **翻译项目规划 | Translation Project Planning** - 全面翻译计划制定
**Comprehensive translation project planning for 620+ files**
6. **任务管理系统 | Task Management System** - shrimp task manager配置
**shrimp task manager configuration with 18 detailed tasks**
7. **翻译策略制定 | Translation Strategy Development** - 中英对照格式确立
**Bilingual translation format establishment and quality control system**
8. **翻译基础设施完成 | Translation Infrastructure Completion** - 完整工具链和质量系统
**Complete translation toolchain and quality control system with 500+ terminology dictionary**

### 翻译基础设施 | Translation Infrastructure
- **术语词典系统 | Terminology Dictionary**: 包含500+专业术语，涵盖气候科学、Fortran编程等12个类别
**500+ professional terms covering climate science, Fortran programming, and 12 other categories**
- **翻译工具链 | Translation Toolchain**: 基于Claude 3.5 Sonnet的专业翻译系统，包含术语一致性控制
**Professional translation system based on Claude 3.5 Sonnet with terminology consistency control**
- **格式保持算法 | Format Preservation Algorithm**: 600+行Python代码，确保Fortran注释100%编译兼容
**600+ lines of Python code ensuring 100% compilation compatibility for Fortran comments**
- **质量检查流水线 | Quality Control Pipeline**: 多维度自动化检查系统，包含术语、格式、内容、编译验证
**Multi-dimensional automated inspection system including terminology, format, content, and compilation validation**
- **测试验证系统 | Testing and Validation**: 完整的测试样本库和自动化验证流程
**Complete test sample library and automated validation workflow**

### 当前翻译状态 | Current Translation Status
- **已完成任务 | Completed Tasks**:
  - 项目启动与规划（18个任务规划完成）
  - 阶段0：术语词典与工具配置（翻译基础设施完成）
- **下一阶段 | Next Phase**: 阶段1.1 - UserGuide核心文档翻译（编译和运行指南）
**Phase 1.1: UserGuide Core Document Translation (Compiling and Running Guide)**
- **总体进度 | Overall Progress**: 2/18个任务完成（11.1%）
**2/18 tasks completed (11.1%)**

---

*此文档为项目记忆系统的一部分，将根据项目发展和分析结果持续更新。*
*This document is part of the project memory system and will be continuously updated based on project development and analysis results.*