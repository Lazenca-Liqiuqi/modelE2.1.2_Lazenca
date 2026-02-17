# ModelE2.1.2_Lazenca - NASA GISS Earth System Model (Lazenca Fork)

[![GitHub release](https://img.shields.io/github/release/Lazenca-Liqiuqi/modelE2.1.2_Lazenca.svg)](https://github.com/Lazenca-Liqiuqi/modelE2.1.2_Lazenca)
[![License](https://img.shields.io/badge/License-NASA%20Open%20Source-blue.svg)](LICENSE)
[![Fortran](https://img.shields.io/badge/Fortran-90%2F95-blue.svg)](https://en.wikipedia.org/wiki/Fortran)
[![Version](https://img.shields.io/badge/Version-0.4.1-green.svg)](https://github.com/Lazenca-Liqiuqi/modelE2.1.2_Lazenca)

**基于NASA GISS ModelE 2.1.2的个人分支 | Personal fork based on NASA GISS ModelE 2.1.2**

---

## 文档导航

> **⚠️ 重要提示**
>
> **完整文档位置**:
>
> - 📁 本地文档: [doc/README.md](doc/README.md)（统一文档导航）
> - 🌐 在线文档: http://simplex.giss.nasa.gov/gcm/doc/UserGuide/index.html
>
> **本README仅为摘要，请务必阅读完整文档**

---

## 项目结构

```text
modelE2.1.2_Lazenca
├── model/          # 核心模型源代码
├── _aux/           # 辅助程序（预处理/后处理）
├── exec/           # 编译和设置脚本
├── doc/            # 文档目录
├── decks/          # 运行配置目录
├── config/         # 配置文件
├── init_cond/      # 初始条件
├── diags/          # 诊断输出
└── tests/          # 测试文件
```

---

## 快速开始

### 系统配置

**工作目录**: `modelE2.1.2_Lazenca/decks`

```bash
# 配置系统（以 gfortran 为例）
gmake config COMPILER=gfortran ModelE_Support=$HOME/ModelE_Support
```

**此命令会**:
- ✅ 创建默认的 `~/.modelErc` 配置文件
- ✅ 创建 `ModelE_Support` 支持目录
- ⚙️ **需要编辑配置文件**: 运行输出路径、Rundeck 库位置、编译选项

---

## 编译和运行指南

### 基本工作流程

> 所有操作都应在 `decks` 目录中进行

```bash
cd decks    # 进入工作目录
```

#### 步骤1: 创建 Rundeck
```bash
gmake rundeck RUN=my_run     # 创建运行配置
```

#### 步骤2: 编辑配置
编辑 `my_run.R` 文件以选择适当的配置

#### 步骤3: 编译和设置
```bash
gmake setup RUN=my_run       # 编译模型并准备运行目录
```

#### 步骤4: 运行模型
```bash
# 从初始条件开始
../exec/runE my_run -cold-restart

# 从保存的检查点继续
../exec/runE my_run
```

---

## Makefile 命令参考

| 命令 | 功能描述 |
|------|----------|
| `config` | 复制默认配置到主目录 |
| `rundeck` | 创建新的运行配置 |
| `depend` | 为指定运行创建依赖关系 |
| `gcm` | 编译对象文件并构建可执行文件 |
| `aux` | 编译标准辅助程序 |
| `auxqflux` | 编译计算 qflux 的辅助程序 |
| `auxdeep` | 编译设置深海的辅助程序 |
| `setup` | 编译可执行文件并准备运行目录 |
| `clean` | 删除对象文件、.mod 文件和依赖关系 |
| `newstart` | 删除运行目录中的所有文件 |
| `exe` | 编译 gcm 并将可执行文件放入运行目录 |
| `htmldoc` | 为此运行创建基于 Web 的文档 |

> 提示: 运行 `gmake` 不带参数将显示简短帮助信息

---

## 项目文档系统

### 文档架构

本项目采用完整的现代化文档系统：

| 文档 | 描述 |
|------|------|
| **CLAUDE.md** | AI 技术概览 |
| **README.md** | 用户指南 (this file) |
| **CHANGELOG.md** | 版本历史 |

### 技术文档

| 文档 | 内容 |
|------|---------|
| **doc/PROJECT_ANALYSIS_REPORT.md** | 全面项目分析报告和现代化路线图 |
| **doc/PROJECT_MEMORY_INDEX.md** | 项目记忆系统索引和使用指南 |

### 翻译项目状态

#### 已完成的任务
- [x] **项目启动与规划**: 建立翻译计划和管理系统
- [x] **术语词典与工具配置**: 建立翻译基础设施
- [x] **根目录文件翻译**: README.md, Makefile等核心文件
- [x] **UserGuide核心文档翻译**: 编译、运行、配置、参数指南
- [x] **UserGuide辅助文档翻译**: 诊断、示踪物、入门指南
- [x] **版本0.2.0发布**: UserGuide体系重构完成
- [x] **ModelDescription技术文档翻译**: 36个文档全部完成，质量≥95/100
- [x] **第二阶段支持文档翻译**: HOWTO目录4个文档 + misc目录3个文档全部完成
  - HOWTO: SCM.md, git_howto.md, time_management.md, newio.md（Codex审查96/100）
  - misc: ModelE_Coding_Standards.md, rundeck.md, CHANGES.md（Codex审查95/100）

#### 待执行的任务
- [ ] **文档结构优化和导航建立**: 建立完整的文档导航系统
- [ ] **全面质量检查和一致性验证**: 确保翻译质量和术语一致性
- [ ] **最终优化和发布准备**: 完整性检查和版本发布

---

## 当前状态

- **版本**: 0.4.0（以CHANGELOG为准）
- **进度**: 43/63（68.3%）——口径：支持文档翻译阶段
- **阶段**: 2.2（第二阶段支持文档翻译）——✅ **HOWTO+misc全部完成**
- **质量**: Codex审查均分95.5+
- **词典版本**: v1.7（700+术语）
- **统计更新**: 2026-02-07

### 项目进展

#### 🎉 最新里程碑

##### 第二阶段支持文档翻译完成 - 2026.02.07
- **结果**: HOWTO目录4个文档 + misc目录3个文档全部翻译完成，涵盖Git使用指南、时间管理、NEW_IO系统、Fortran编程规范、运行配置、版本历史等领域
- **质量**: Codex审查评分95.5/100（优秀）
  - HOWTO批次：96/100（newio.md达到97/100，P0文档）
  - misc批次：95/100（LaTeX→Markdown转换成功）
- **新术语**: 约145个专业术语，涵盖Git版本控制、单列模型、时间管理、I/O系统、编程规范、配置文件、版本历史等领域
- **词典**: 术语词典更新至v1.7
- **影响**: 支持文档翻译阶段圆满完成，为项目完善阶段奠定基础

#### 历史里程碑
- **0.1.4** 2025.10.30 阶段1.3辅助文档翻译完成，UserGuide体系达18篇 [详情]
- **0.1.3** 2025.10.29 阶段1.2核心翻译完成，编译/运行/配置/参数指南就绪 [详情]
- **0.1.2** 2025.10.28 根目录文件翻译完成，项目入口中英对照优化 [详情]
- **0.1.1** 2025.10.28 翻译基础设施完成，术语词典与工具链就绪 [详情]

#### 下一步计划与风险提示
- **当前任务**: 🎉 **ModelDescription阶段完成！** 36个文档全部翻译完毕，质量评估≥95/100
- **下一阶段**: 支持文档翻译（misc目录、HOWTO目录）
- **待办事项**: 术语词典已更新至v1.5（补录第6批次约65个术语）
- **版本同步**: 已完成整体审查请求生成与问题修复
- **质量保障**: 建立CLAUDE↔CHANGELOG一致性校验，确保版本/日期/路径准确
- **技术风险**: 术语一致性保障，地球系统专业术语覆盖

[详细信息见CHANGELOG.md]

#### 翻译基础设施
- **术语词典系统**: 500+ 专业术语，12个类别完整覆盖
- **翻译工具链**: Claude 3.5 Sonnet驱动，术语一致性自动控制
- **格式保持算法**: Python实现，Fortran注释100%编译兼容
- **质量检查流水线**: 四重校验（术语、格式、内容、编译）
- **AI审查机制**: Codex深度分析，持续质量改进

---

## 开发环境要求

### 必需软件

| 软件 | 版本要求 |
|------|----------|
| Fortran 编译器 | gfortran 4.8+, Intel 15+, PGI 15+ |
| MPI | OpenMPI 1.6+, MPICH 3.0+ |
| NetCDF | 4.0+ |
| LAPACK/BLAS | 3.0+ |

### 支持平台

- **Linux** - 主要支持平台
- **macOS** - 支持
- **Windows** - 通过 WSL 支持

---

## 重要提醒

### 运行注意事项

1. **创建 Rundeck 优先**
   - 在运行任何其他命令之前，必须先使用 `gmake rundeck RUN=run_name` 创建 rundeck

2. **二进制文件位置**
   - 所有由 `gmake` 创建的二进制文件都存储在 `decks/<RUN>_bin/` 中

3. **配置文件编辑**
   - 务必编辑 `~/.modelErc` 文件以正确设置编译选项和路径

---

## 项目信息

### 项目详情

- **项目名称**: ModelE2.1.2_Lazenca
- **基础项目**: NASA GISS ModelE 2.1.2
- **开发者**: Lazenca
- **许可证**: NASA Open Source License
- **仓库地址**: https://github.com/Lazenca-Liqiuqi/modelE2.1.2_Lazenca
- **项目类型**: 大气环流模型(GCM)/地球系统模型
- **代码规模**: 超过33万行代码
- **主要语言**: Fortran 90/95, 部分C代码

### 项目用途

ModelE2.1.2_Lazenca 是 NASA GISS ModelE 2.1.2 的个人分支版本，主要用于：

- 气候变化研究和预测
- 古气候模拟
- 天气和气候过程研究
- 地球系统相互作用分析

---

## 支持与联系

### 问题报告

如果遇到问题，请通过以下方式报告：

- [GitHub Issues](https://github.com/Lazenca-Liqiuqi/modelE2.1.2_Lazenca/issues)
- 直接联系开发者

### 更多资源

- [NASA GISS ModelE 官方网站](https://www.giss.nasa.gov/tools/modelE/)
- [完整用户指南](doc/UserGuide/0-index.md)
- [项目变更记录](CHANGELOG.md)

---

<div align="center">

**探索地球系统，理解气候变化 | Explore Earth Systems, Understand Climate Change**

*基于 NASA GISS ModelE 2.1.2 | Based on NASA GISS ModelE 2.1.2*

</div>