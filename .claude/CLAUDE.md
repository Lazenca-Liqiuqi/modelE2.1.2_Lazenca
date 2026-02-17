# ModelE2.1.2_Lazenca - NASA GISS地球系统模型中文翻译

## 项目背景信息

ModelE2.1.2_Lazenca是基于NASA GISS ModelE 2.1.2的个人fork分支，专注于地球系统模型的中文翻译和本地化。项目涵盖大气环流模型(GCM)、海洋、陆面、海冰、化学等完整地球系统组件，主要服务于气候变化研究、古气候模拟和天气气候过程分析。

**项目类型**: 大气环流模型(GCM)/地球系统模型
**主要语言**: Fortran 90/95, 部分C代码
**代码规模**: 超过33万行代码
**翻译范围**: 620+ 文件（HTML文档、Fortran代码、脚本、配置文件）

## 目录结构

```
modelE2.1.2_Lazenca/
├── model/              # 核心模型源代码
├── doc/                # 文档目录
├── config/             # 编译配置文件
├── decks/              # 运行配置目录
├── _aux/               # 辅助程序
├── exec/               # 执行脚本
├── init_cond/          # 初始条件
├── diags/              # 诊断输出
└── tests/              # 测试文件
```

[详细信息见项目记忆系统的repomix打包文件]

## 技术栈与技术路线

### 地球系统模型组件
- **大气模块**: ATM_DRV.f（驱动）、ATMDYN.f（动力学）、RADIATION.f（辐射）、CLOUDS2.F90（云微物理）
- **海洋模块**: OCNDYN.f（动力学）、OCNKPP.f（KPP混合）、OCN_TRACER.f（示踪物）
- **陆面模块**: GHY_DRV.f（驱动）、LAKES.f（湖泊）、VEG_DRV.f（植被）
- **海冰模块**: SEAICE.f（热力学）、ICEDYN.f（动力学）
- **化学模块**: TRACERS_DRV.f（传输）、TRCHEM_Shindell_COM.f（化学反应）

### 编译与运行环境
- **编译器**: gfortran, intel, pgi
- **并行**: MPI/OpenMP混合并行
- **库依赖**: NetCDF, LAPACK, BLAS
- **平台**: Linux, macOS, Windows(WSL)
- **数据来源**: NASA GISS官方数据集、初始条件文件

### 翻译技术路线
- **翻译引擎**: Claude 3.5 Sonnet大模型驱动
- **术语管理**: 500+专业术语词典，12个领域覆盖
- **格式保持**: Python算法确保Fortran注释100%编译兼容
- **质量检查**: 多维度自动化验证（术语、格式、内容、编译）

## 工作流程与常用命令

### 模型构建流程
```bash
make config COMPILER=gfortran  # 配置编译环境
cd decks                       # 进入工作目录
gmake rundeck RUN=run_name     # 创建运行配置
gmake setup RUN=run_name       # 编译和设置
../exec/runE run_name          # 运行模型
```

### 翻译工作流程
1. **任务规划**: 使用shrimp task manager管理26个翻译任务
2. **并行开发**: Git worktree支持多任务并行翻译
3. **质量控制**: Codex审查机制，平均评分95+
4. **自动化验证**: 术语一致性、格式规范、编译兼容性检查

### 版本控制策略
- **主要分支**: master（稳定翻译版本）
- **开发分支**: feature/*（功能模块翻译）
- **发布策略**: 语义版本控制（主版本.次版本.修订版本）

## 资源

### 官方文档
- [NASA GISS ModelE用户指南](http://simplex.giss.nasa.gov/gcm/doc/UserGuide/index.html)
- [项目GitHub仓库](https://github.com/Lazenca-Liqiuqi/modelE2.1.2_Lazenca)

### 技术文档
- [项目分析报告](doc/PROJECT_ANALYSIS_REPORT.md) - 技术债务评估和现代化路线图
- [项目记忆索引](doc/PROJECT_MEMORY_INDEX.md) - 记忆系统使用指南

### 学术文献
- Schmidt, G.A., et al. (2014). Configuration and assessment of the GISS ModelE2 contributions to the CMIP5 archive

## 工作阶段

#### ✅ 已完成的任务
- [x] **项目启动与规划**: 建立翻译计划和管理系统
- [x] **术语词典与工具配置**: 建立翻译基础设施
- [x] **根目录文件翻译**: README.md, Makefile等核心文件
- [x] **UserGuide核心文档翻译**: 编译、运行、配置、参数指南
- [x] **UserGuide辅助文档翻译**: 诊断、示踪物、入门指南
- [x] **版本0.2.0发布**: UserGuide体系重构完成

#### ✅ 已完成的任务（新增）
- [x] **ModelDescription技术文档翻译**: 全部36个文档翻译完成（33个核心技术文档 + 3个辅助文档），覆盖大气、陆面、海洋、海冰、示踪物、系统架构等完整模块，质量评估≥95/100

#### ✅ 已完成的任务（新增）
- [x] **第二阶段支持文档翻译**: HOWTO目录4个文档 + misc目录3个文档全部完成
  - HOWTO: SCM.md, git_howto.md, time_management.md, newio.md（Codex审查96/100）
  - misc: ModelE_Coding_Standards.md, rundeck.md, CHANGES.md（Codex审查95/100）

#### ✅ 已完成的任务（新增）
- [x] **文档翻译收尾与目录整合**: 完成剩余文档翻译，整合目录结构，创建统一导航
  - 翻译HYCOM.md（海洋模型文档）
  - old-doc → doc/archive-old-doc（93个文件存档）
  - 创建doc/README.md统一导航（86个翻译文档）
  - 删除重复内容和子目录索引（6个文件）
  - Codex审查87/100，问题已修正
- [x] **根目录清理**: 删除翻译辅助工具和空目录

#### ⏳ 待执行的任务

**📋 后续工作**
- [ ] **术语词典扩展**: 覆盖地球系统模型专业术语
- [ ] **全面质量检查和一致性验证**: 确保翻译质量和术语一致性

## 当前状态

- **版本**: 0.4.1（以CHANGELOG为准）
- **进度**: 文档翻译100%完成（86个翻译文档）
- **阶段**: 文档翻译完成，目录整合完毕
- **质量**: Codex审查均分95+
- **统计更新**: 2026-02-17
- **词典版本**: v1.7（700+术语）

## 项目进展

### 最新版本概览

#### 0.4.1 2026.02.17 文档翻译收尾与目录整合 - 项目完善
- **结果**: 完成剩余文档翻译，整合目录结构，创建统一导航，清理根目录
- **质量**: Codex审查87/100，所有问题已修正
- **变更**: old-doc迁移到doc/archive-old-doc，删除重复内容和空目录
- **影响**: 项目结构清晰，文档导航统一，翻译工作圆满完成

[查看详情 → CHANGELOG.md#0.4.1]

#### 0.4.0 2026.02.07 支持文档翻译完成 - 项目里程碑
- **结果**: 完成HOWTO和misc目录翻译，支持文档翻译阶段圆满完成
- **质量**: Codex审查均分95.5，术语词典升级至v1.7
- **变更**: 7个支持文档翻译完成，LaTeX→Markdown转换规范建立
- **影响**: 项目进度达68.3%，为文档翻译收尾奠定基础

[查看详情 → CHANGELOG.md#0.4.0]

#### 0.2.0 2025.11.12 UserGuide翻译完成 - 项目里程碑
- **结果**: UserGuide 18篇翻译完成，用户引导体系闭环，为ModelDescription翻译建立流水线
- **质量**: Codex审查均分95+，四重校验（术语、格式、内容、编译）稳定通过
- **协作**: Git worktree并行工作流成熟，术语词典v1.4完整覆盖
- **影响**: 翻译基础设施全面就绪，支撑后续620+文件的高效翻译

[查看详情 → CHANGELOG.md#0.2.0]

### 历史里程碑
- **0.1.4** 2025.10.30 阶段1.3辅助文档翻译完成，UserGuide体系达18篇 [详情]
- **0.1.3** 2025.10.29 阶段1.2核心翻译完成，编译/运行/配置/参数指南就绪 [详情]
- **0.1.2** 2025.10.28 根目录文件翻译完成，项目入口中英对照优化 [详情]
- **0.1.1** 2025.10.28 翻译基础设施完成，术语词典与工具链就绪 [详情]

### 下一步计划与风险提示

- **当前状态**: 🎉 **文档翻译全部完成！** 86个翻译文档，统一导航就绪
- **目录结构**: old-doc已迁移到doc/archive-old-doc存档
- **导航入口**: doc/README.md是唯一的文档导航入口
- **后续工作**: 术语词典扩展、质量检查、版本发布
- **质量保障**: Codex审查均分95+，四重校验稳定通过

[详细信息见CHANGELOG.md]