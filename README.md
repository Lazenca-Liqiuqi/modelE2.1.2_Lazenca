# ModelE2.1.2_Lazenca - NASA GISS Earth System Model (Lazenca Fork)

[![GitHub release](https://img.shields.io/github/release/Lazenca-Liqiuqi/modelE2.1.2_Lazenca.svg)](https://github.com/Lazenca-Liqiuqi/modelE2.1.2_Lazenca)
[![License](https://img.shields.io/badge/License-NASA%20Open%20Source-blue.svg)](LICENSE)
[![Fortran](https://img.shields.io/badge/Fortran-90%2F95-blue.svg)](https://en.wikipedia.org/wiki/Fortran)
[![Version](https://img.shields.io/badge/Version-v0.2.0-green.svg)](https://github.com/Lazenca-Liqiuqi/modelE2.1.2_Lazenca)

**基于NASA GISS ModelE 2.1.2的个人分支 | Personal fork based on NASA GISS ModelE 2.1.2**

---

## 📚 文档导航 | Documentation Navigation

> **⚠️ 重要提示 | Important Notice**
>
> **完整文档位置 | Full Documentation Location**:
>
> - 📁 本地文档 | Local: [UserGuide_Index](doc/UserGuide/0-index.md)
> - 🌐 在线文档 | Online: http://simplex.giss.nasa.gov/gcm/doc/UserGuide/index.html
>
> **本README仅为摘要，可能不完整或不是最新 | This README is only a summary and may not be complete or up-to-date**
>
> **请务必阅读完整文档 - 它真的会让你的生活更轻松！**
> **PLEASE READ THE FULL DOCUMENTATION - IT REALLY WILL MAKE YOUR LIFE EASIER!**

---

## 📁 项目结构 | Project Structure

```text
modelE2.1.2_Lazenca
├── 📁 model/          # 核心模型源代码 | Core GCM model source code
├── 📁 _aux/           # 辅助程序（预处理/后处理） | Auxiliary programs (pre/post-processing)
├── 📁 exec/           # 编译和设置脚本 | Compilation and setup scripts
├── 📁 doc/            # 文档目录 | Documentation directory
├── 📁 decks/          # 运行配置目录 | Rundecks directory
│   ├── 📄 <run_name_1>.R        # 运行配置 | Rundeck for run
│   ├── 📁 <run_name_1>_bin/     # 二进制文件目录 | Binaries directory
│   └── 🔗 <run_name_1>          # 运行目录链接 | Run directory link
├── 📁 config/         # 配置文件 | Configuration files
├── 📁 init_cond/      # 初始条件 | Initial conditions
├── 📁 diags/          # 诊断输出 | Diagnostic output
└── 📁 tests/          # 测试文件 | Test files
```

---

## 🚀 快速开始 | Quick Start

### 1️⃣ 系统配置 | System Configuration

**工作目录 | Working Directory**: `modelE2.1.2_Lazenca/decks`

```bash
# 配置系统（以 gfortran 为例）
# 注意：推荐使用 gmake，如果系统只支持 make 也可以使用
# Note: Recommend using gmake; if your system only supports make, that works too
gmake config COMPILER=gfortran ModelE_Support=$HOME/ModelE_Support
```

**此命令会 | This command will**:
- ✅ 创建默认的 `~/.modelErc` 配置文件 | Create default `~/.modelErc` file
- ✅ 创建 `ModelE_Support` 支持目录 | Create `ModelE_Support` directory
- ⚙️ **需要编辑配置文件 | Need to edit config file**:
  - 运行输出路径 | Run output paths
  - Rundeck 库位置 | Rundeck library locations
  - 编译选项 | Compilation options (multi-processing, compiler name, NetCDF libraries)

---

## 🔧 编译和运行指南 | Compilation and Running Guide

### 基本工作流程 | Basic Workflow

> **所有操作都应在 `decks` 目录中进行 | All operations should be performed in the `decks` directory**

```bash
cd decks    # 进入工作目录 | Enter working directory
```

#### 步骤 1 | Step 1: 创建 Rundeck
```bash
gmake rundeck RUN=my_run     # 创建运行配置 | Create rundeck
```

#### 步骤 2 | Step 2: 编辑配置
编辑 `my_run.R` 文件以选择适当的配置
Edit the `my_run.R` file to choose appropriate configuration

#### 步骤 3 | Step 3: 编译和设置
```bash
gmake setup RUN=my_run       # 编译模型并准备运行目录 | Compile model and prepare run directory
```

#### 步骤 4 | Step 4: 运行模型
```bash
# 从初始条件开始 | Start from initial conditions
../exec/runE my_run -cold-restart

# 从保存的检查点继续 | Continue from saved checkpoint
../exec/runE my_run
```

---

## 📋 Makefile 命令参考 | Makefile Command Reference

| 命令 | Command | 功能描述 | Description |
|------|---------|----------|-------------|
| `config` | ✅ | 复制默认配置到主目录 | Copy default config to home directory |
| `rundeck` | 🔨 | 创建新的运行配置 | Create new rundeck |
| `depend` | 🔗 | 为指定运行创建依赖关系 | Create dependencies for specified rundeck |
| `gcm` | 🚀 | 编译对象文件并构建可执行文件 | Compile object files and build executable |
| `aux` | 🛠️ | 编译标准辅助程序 | Compile standard auxiliary programs |
| `auxqflux` | 🌡️ | 编译计算 qflux 的辅助程序 | Compile auxiliary programs for computing qflux |
| `auxdeep` | 🌊 | 编译设置深海的辅助程序 | Compile auxiliary programs for setting deep ocean |
| `setup` | ⚙️ | 编译可执行文件并准备运行目录 | Compile executable and prepare run directory |
| `clean` | 🧹 | 删除对象文件、.mod 文件和依赖关系 | Remove object files, .mod files and dependencies |
| `newstart` | 🔄 | 删除运行目录中的所有文件 | Remove all files in run directory |
| `exe` | 📦 | 编译 gcm 并将可执行文件放入运行目录 | Compile gcm and put executable into run directory |
| `htmldoc` | 📄 | 为此运行创建基于 Web 的文档 | Create web-based documentation for this run |

> **💡 提示 | Tip**: 运行 `gmake` 不带参数将显示简短帮助信息
> Running `gmake` without arguments will print short help

---

## 📊 项目文档系统 | Project Documentation System

### 🏗️ 文档架构 | Documentation Architecture

本项目采用完整的现代化文档系统，中英对照段落格式：
This project has a complete modernized documentation system with paragraph-level bilingual format:

| 文档 | Document | 描述 | Description |
|------|----------|------|-------------|
| 📄 **CLAUDE.md** | 🤖 AI 技术概览 | AI-readable project technical overview |
| 📄 **README.md** | 👥 用户指南 | Human-friendly project usage guide (this file) |
| 📄 **CHANGELOG.md** | 📝 版本历史 | Complete version change history |

### 🔬 技术文档 | Technical Documents

| 文档 | Document | 内容 | Content |
|------|----------|------|---------|
| 📄 **doc/ARCHITECTURE_ANALYSIS.md** | 🏛️ | 详细的 ModelE 架构分析和模块依赖关系 | Detailed ModelE architecture analysis and module dependencies |
| 📄 **doc/PROJECT_ANALYSIS_REPORT.md** | 📊 | 全面项目分析报告和现代化路线图 | Comprehensive project analysis report and modernization roadmap |
| 📄 **doc/PROJECT_MEMORY_INDEX.md** | 🗂️ | 项目记忆系统索引和使用指南 | Project memory system index and usage guide |

### 📈 当前状态 | Current Status

- **版本 | Version**: ModelE Fork v0.1.1 (基于 modelE-3-0 v2.1.2)
- **文档更新 | Documentation Update**: 2025-10-28
- **文档格式 | Documentation Format**: 段落级中英对照 | Paragraph-level bilingual format
- **维护状态 | Maintenance Status**: 活跃维护，持续改进 | Active maintenance, continuous improvement

### 📖 翻译项目状态 | Translation Project Status

- **项目类型 | Project Type**: NASA GISS 地球系统模型中文翻译 | NASA GISS Earth System Model Chinese Translation
- **翻译范围 | Translation Scope**: 620+ 文件（HTML文档、Fortran代码、脚本、配置文件）| 620+ files (HTML docs, Fortran code, scripts, config files)
- **当前阶段 | Current Phase**: 阶段0完成 ✅ | Phase 0 Completed ✅
- **完成进度 | Completion Progress**: 2/18 任务完成 (11.1%) | 2/18 tasks completed (11.1%)
- **基础设施状态 | Infrastructure Status**: 完全就绪 | Fully Ready

### 🛠️ 翻译基础设施 | Translation Infrastructure

- **✅ 术语词典系统**: 500+ 专业术语，12个类别
- **✅ 翻译工具链**: Claude 3.5 Sonnet + 术语一致性控制
- **✅ 格式保持算法**: Fortran注释100%编译兼容
- **✅ 质量检查流水线**: 多维度自动化检查
- **✅ 测试验证系统**: 完整的测试样本和验证流程

---

## 🛠️ 开发环境要求 | Development Requirements

### 必需软件 | Required Software

| 软件 | Software | 版本要求 | Version Requirement |
|------|----------|----------|-------------------|
| 🔨 Fortran 编译器 | Compiler | gfortran 4.8+, Intel 15+, PGI 15+ |
| 🌐 MPI | MPI Implementation | OpenMPI 1.6+, MPICH 3.0+ |
| 📊 NetCDF | NetCDF Libraries | 4.0+ |
| 🔢 LAPACK/BLAS | Linear Algebra Libraries | 3.0+ |

### 支持平台 | Supported Platforms

- 🐧 **Linux** - 主要支持平台 | Primary platform
- 🍎 **macOS** - 支持 | Supported
- 🪟 **Windows** - 通过 WSL 支持 | Supported via WSL

---

## 🚨 重要提醒 | Important Notes

### ⚠️ 运行注意事项 | Running Notes

1. **创建 Rundeck 优先 | Create Rundeck First**
   - 在运行任何其他命令之前，必须先使用 `gmake rundeck RUN=run_name` 创建 rundeck
   - Before running any other commands, must first create rundeck using `gmake rundeck RUN=run_name`

2. **二进制文件位置 | Binary Files Location**
   - 所有由 `gmake` 创建的二进制文件都存储在 `decks/<RUN>_bin/` 中
   - All binaries created by `gmake` are stored in `decks/<RUN>_bin/`

3. **配置文件编辑 | Configuration File Editing**
   - 务必编辑 `~/.modelErc` 文件以正确设置编译选项和路径
   - Be sure to edit `~/.modelErc` file to properly set compilation options and paths

---

## 🤝 项目信息 | Project Information

### 📋 项目详情 | Project Details

- **项目名称 | Project Name**: ModelE2.1.2_Lazenca
- **基础项目 | Base Project**: NASA GISS ModelE 2.1.2
- **开发者 | Developer**: Lazenca
- **许可证 | License**: NASA Open Source License
- **仓库地址 | Repository**: https://github.com/Lazenca-Liqiuqi/modelE2.1.2_Lazenca
- **项目类型 | Project Type**: 大气环流模型(GCM)/地球系统模型 | GCM/Earth System Model
- **代码规模 | Code Size**: 超过33万行代码 | Over 330,000 lines of code
- **主要语言 | Primary Language**: Fortran 90/95, 部分C代码

### 🌟 项目用途 | Project Purpose

ModelE2.1.2_Lazenca 是 NASA GISS ModelE 2.1.2 的个人分支版本，主要用于：
ModelE2.1.2_Lazenca is a personal fork of NASA GISS ModelE 2.1.2, primarily used for:

- 🌡️ 气候变化研究和预测 | Climate change research and prediction
- 🦕 古气候模拟 | Paleoclimate simulation
- 🌤️ 天气和气候过程研究 | Weather and climate process research
- 🌍 地球系统相互作用分析 | Earth system interaction analysis

---

## 📞 支持与联系 | Support & Contact

### 🐛 问题报告 | Issue Reporting

如果遇到问题，请通过以下方式报告：
If you encounter issues, please report them via:

- 🌐 [GitHub Issues](https://github.com/Lazenca-Liqiuqi/modelE2.1.2_Lazenca/issues)
- 📧 直接联系开发者 | Contact developer directly

### 📚 更多资源 | Additional Resources

- 🔬 [NASA GISS ModelE 官方网站](https://www.giss.nasa.gov/tools/modelE/)
- 📖 [完整用户指南](doc/UserGuide/index.html)
- 📋 [项目变更记录](CHANGELOG.md)

---

<div align="center">

**🌍 探索地球系统，理解气候变化 | Explore Earth Systems, Understand Climate Change 🌍**

*基于 NASA GISS ModelE 2.1.2 | Based on NASA GISS ModelE 2.1.2*

</div>

---
---
**📖 README 文件结束 | End of README file**
