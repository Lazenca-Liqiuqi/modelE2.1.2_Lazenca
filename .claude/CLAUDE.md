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

**🎉 文档翻译与排版优化全部完成！** 86个翻译文档，统一导航就绪，Codex审查100/100满分

#### ✅ 已完成
- [x] 翻译基础设施建立（术语词典v1.7、工具链、质量检查）
- [x] UserGuide翻译（42个文档）
- [x] ModelDescription翻译（36个文档）
- [x] HOWTO + misc翻译（7个文档）
- [x] 目录整合与统一导航（doc/README.md）
- [x] 文档排版优化（86个文档，统一结束标记）

#### ⏳ 后续工作
- [ ] 术语词典扩展
- [ ] 全面质量检查和一致性验证

## 项目进展

### 最新版本概览

- **0.5.0** 2026.02.17 文档排版优化完成 - 质量提升
- **0.4.1** 2026.02.17 文档翻译收尾与目录整合 - 项目完善
- **0.4.0** 2026.02.07 支持文档翻译完成 - 项目里程碑
- **0.3.0** 2026.02.05 ModelDescription翻译完成 - 项目里程碑
- **0.2.0** 2025.11.12 UserGuide翻译完成 - 项目里程碑

[详细信息见CHANGELOG.md]

## 当前状态

- **版本**: 0.5.0
- **进度**: 文档翻译与排版优化100%完成（86个翻译文档）
- **阶段**: 文档翻译与排版优化完成
- **质量**: Codex审查100/100（满分）
- **词典版本**: v1.7（700+术语）
- **统计更新**: 2026-02-17