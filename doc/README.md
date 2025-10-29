# ModelE2.1.2_Lazenca 文档目录 / Documentation Directory

这是ModelE2.1.2_Lazenca项目的主文档目录，包含所有中文翻译文档和技术参考资料。

## 目录结构 / Directory Structure

### 📚 docs/ - 主文档目录 / Main Documentation Directory

#### 📖 user-guide/ - 用户指南 / User Guide
**状态**: 进行中 (In Progress)
**内容**: ModelE核心使用指南的中文翻译版本

**已完成文档 / Completed Documents**:
- `Compiling_the_model.md` - 模型编译指南
- `Running_the_model.md` - 模型运行指南
- `ModelE_rundeck.md` - 配置详解
- `Major_rundeck_parameters.md` - 参数详解
- `Configuring_modelE_on_your_machine.md` - 机器配置指南
- `Creating_a_rundeck.md` - 创建运行配置
- `Installing_NetCDF_library.md` - NetCDF库安装指南
- `System_requirements.md` - 系统要求
- `directory_structure.md` - 项目目录结构说明
- `DIAGNOSTICS_EXPLANATIONS.md` - 诊断输出说明文档

**计划翻译 / Planned Translation**:
- 诊断工具使用指南
- 代码获取指南
- 输入文件下载指南
- 示踪物配置指南
- 植被模型指南

#### 📋 technical-reference/ - 技术参考 / Technical Reference
**状态**: 进行中 (In Progress)
**内容**: 技术分析文档和ModelDescription翻译计划

**已完成文档**:
- `ARCHITECTURE_ANALYSIS.md` - 架构分析和模块依赖关系
- `README_COSP_MODELE.md` - COSP模式说明文档

**计划内容**:
- `atmosphere/` - 大气模块技术文档
  - 大气动力学
  - 辐射传输过程
  - 云微物理过程
  - 边界层过程
- `ocean-land/` - 海洋陆面模块文档
  - 海洋动力学
  - 陆面过程
  - 海冰模型
  - 生物地球化学循环

#### 🔧 development/ - 开发文档 / Development Documentation
**状态**: 计划中 (Planned)
**内容**: 开发相关的技术文档和代码注释指南

**计划内容**:
- 核心驱动模块注释翻译
- 物理过程模块注释翻译
- 诊断工具模块注释翻译
- 脚本工具翻译指南

#### 📊 quality-assurance/ - 质量保证 / Quality Assurance
**状态**: 进行中 (In Progress)
**内容**: 质量检查报告和项目分析文档

**已完成文档**:
- `PROJECT_ANALYSIS_REPORT.md` - 全面项目分析报告
- `PROJECT_MEMORY_INDEX.md` - 项目记忆系统索引

**计划内容**:
- 翻译质量检查报告
- 编译测试结果
- 用户测试反馈
- 术语一致性验证

---

### 📁 old-doc/ - 原始文档目录 / Original Documentation Directory

**说明**: 包含ModelE项目的原始英文文档，作为翻译参考和历史记录保存。

#### 📖 UserGuide/ - 原始用户指南
- 包含完整的英文UserGuide HTML文档
- 翻译工作的源材料

#### 📋 ModelDescription/ - 原始技术文档
- 大气、海洋、陆面等技术模块的英文文档
- 物理过程和数值方法的详细说明

#### 🔧 HOWTO/ - 操作指南
- Git使用指南
- 时间管理指南
- I/O操作指南

#### 📊 misc/ - 杂项文档
- 诊断说明文档
- 编码标准
- 目录结构说明

#### 🗂️ obsolete/ - 过时文档
- 旧版本的文档和指南
- 保留作为历史参考

---

## 翻译进度 / Translation Progress

### 已完成阶段 / Completed Stages
- ✅ **阶段0**: 项目启动与规划
- ✅ **阶段1**: 术语词典与工具配置
- ✅ **阶段1.1**: 根目录文件翻译
- ✅ **阶段1.2**: 核心UserGuide文档翻译 (8/8完成)

### 进行中阶段 / In Progress Stages
- 🔄 **阶段1.3**: UserGuide辅助文档翻译
- 🔄 **阶段2**: ModelDescription技术文档翻译

### 计划阶段 / Planned Stages
- ⏳ **阶段3-5**: Fortran代码注释翻译
- ⏳ **阶段6**: 全面质量检查
- ⏳ **阶段7**: 用户测试和反馈收集
- ⏳ **阶段8**: 最终优化和发布准备

---

## 翻译质量标准 / Translation Quality Standards

### 📏 质量控制
- **术语一致性**: 严格遵循术语词典v1.4
- **格式规范**: 中英对照叠放格式
- **技术准确性**: 所有命令、参数、路径100%保真
- **质量检查**: 四道闸质量检查机制

### 📊 质量评分
- **已完成文档平均分**: 95.7/100
- **目标质量标准**: ≥95分
- **用户满意度目标**: ≥90%

---

## 使用指南 / Usage Guidelines

### 🔍 如何使用翻译文档
1. **用户指南**: 从 `docs/user-guide/` 开始，按需阅读相关章节
2. **技术参考**: 查阅 `docs/technical-reference/` 了解深层技术细节
3. **开发指南**: 参考 `docs/development/` 进行代码开发和贡献
4. **原始文档**: 需要时查阅 `old-doc/` 中的英文原版

### 📝 贡献指南
- 翻译贡献请遵循项目翻译标准
- 术语使用请参考 `.claude/terminology-dictionary.md`
- 格式要求请遵循现有文档的规范
- 质量检查请使用 `.claude/quality-control-pipeline.py`

---

**文档维护**: 此文档随项目进展持续更新
**最后更新**: 2025-10-29
**项目版本**: ModelE2.1.2_Lazenca v0.1.2