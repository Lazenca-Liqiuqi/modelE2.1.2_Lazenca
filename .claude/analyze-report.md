# UserGuide核心文档翻译分析报告

**分析时间**: 2025-10-28 21:54
**任务**: 阶段1.2：UserGuide核心文档翻译 - 编译和运行指南
**分析工具**: Codex (GPT-5)
**分析基准**: `.claude/request.md`

## 技术复杂度与难度评估

### 总体难点
- **并行与编译链条交织**: Make+Perl+m4+Fortran模块依赖+MPI切换
- **平台差异与老旧指令混用**: MacPorts/yum/devtoolset、`module load`、Slurm/MPICH/OpenMPI
- **运行时约定与作业系统**: `runE`/`sswE`、`QSUB_STRING`模板
- **Rundeck结构与命名惯例**: 分节顺序/组件库/覆盖选项/namelist与参数块
- **气候科学参数语义与跨年控制**: `master_yr`、`ghg_yr`、`volc_yr`、轨道参数、日序偏移

### 文档逐项复杂度（高→中）
**高复杂度**:
- `ModelE_rundeck.html`、`Major_rundeck_parameters.html`
  - 复杂结构+大量术语+参数语义依赖模型物理，跨文件引用密集

**中高复杂度**:
- `Configuring_modelE_on_your_machine.html`、`Compiling_the_model.html`、`Running_the_model.html`
  - 跨平台指令、MPI/批处理、冷启动/重启流程、示例参数与实操一致性要求高

**中等复杂度**:
- `System_requirements.html`、`Installing_NetCDF_library.html`、`Creating_a_rundeck.html`
  - 主要为前置与流程拼接，强调术语与示例准确保持

### 翻译敏感点
- **"MPI threads"语义**: 常指进程，译名需与词典规则一致以避免误导
- **名称/占位符/变量**: `<RunID>`、`NPES`、`-np`、`%np`、`QSUB_STRING`、`&&PARAMETERS`、`&INPUTZ`绝不可翻译或变形
- **代码保真**: 代码/命令/路径/扩展名/大小写需完全保真
- **结构保持**: 内联代码（`<tt>`/`<code>`）和定义列表（`<dl><dt><dd>`）需保形

## 主要风险与对应方案

### HTML→Markdown结构丢失
**风险**: 定义列表、锚点、内联`<tt>`、命令/代码块语言标识在转换中丢失或合并

**解决方案**:
- `<dl><dt><dd>`→"术语：说明"两行对；保留锚点为显式`{#id}`或原始HTML块内嵌
- `<tt>/<code>`→行内反引号；`<pre><code>`→三反引号代码块（指定`bash`/无语言）
- 标题锚点保持英文原文生成；必要时并行插入显式`<a name>`以保兼容

### 命令兼容与可执行性
**风险**: `make`/`gmake`混用；平台包名与版本老旧；模块系统差异

**解决方案**:
- 翻译中加入"平台注记"小贴士，不改动原命令
- 主路径以原文为准，提供"Linux/CentOS/Slurm示例仅供参考"的译注

### 术语歧义与一致性
**风险**: "checkpoint/restart file"、"threads/processes"、"rundeck/模板/组件/对象模块"、"namelist"易不一致

**解决方案**:
- 强制对齐 `.claude/terminology-dictionary.md`
- 新增未覆盖词条并设CI术语lint

### 链接与交叉引用
**风险**: 页内锚点与相对链接在Markdown中的自动锚规则不一致，导致跳转失效

**解决方案**:
- 转换后跑链接检查器
- 对关键锚点使用显式HTML锚或Pandoc风格id，必要时保留原HTML块

## 执行优化建议

### 最优翻译顺序（由易到难）
1. `System_requirements.html`
2. `Installing_NetCDF_library.html`
3. `Configuring_modelE_on_your_machine.html`
4. `Creating_a_rundeck.html`
5. `Compiling_the_model.html`
6. `Running_the_model.html`
7. `ModelE_rundeck.html`
8. `Major_rundeck_parameters.html`

### 角色分工
- **中级译者**: 1–6（流程型文档）
- **高级/领域译者**: 7–8（结构/物理语义密集）

### 关键术语处理
**参考词典已覆盖**: Rundeck(运行配置)、MPI、NetCDF、Checkpoint/Restart

**建议新增**:
- Namelist（Fortran名录/参数名录）
- QSUB_STRING（作业提交模板字符串，勿译名）
- OpenMPI/Intel MPI/MPICH/MVAPICH2/SCALI/mpt（保留英文专名）
- `&INPUTZ`（重启与计时参数名录，保留原名并中文解释）
- Preprocessor Options（预处理选项）/Object modules（对象模块）/Components（组件库）
- ESMF（地球系统建模框架，保留简称+中文注释）
- "MPI 进程"优于"MPI 线程"

## 质量控制策略

### 四道闸机制
1. **结构闸**: 段落配对计数器（英文段落=中文段落）
2. **保真闸**: 代码/命令/占位符Token白名单校验
3. **术语闸**: CI术语lint（严格/宽松两级），新增术语申请单
4. **链接闸**: 页内/跨页锚点扫描（含`#year`等命名）

### 可执行性核查清单
- **文档级干跑**: 按文档顺序"读命令→检查依赖→确认路径→预期输出描述"
- **场景级核查**: 冷启动一小时→检查`.PRT`日志→重启长跑流程描述闭环

### 用户体验优化
- 在中文段加入"平台差异提示"与"版本示例说明（历史环境）"的轻量注记
- 避免误导；不改动原文命令

## 与现有翻译基础设施的协调性

### 格式标准一致
- 段落级中英叠放、代码块保留英文原样、标题对译、列表逐项对译
- HTML保留策略：必要处以内联HTML保留源结构，其余转为标准Markdown

### 术语词典联动
- 使用现有500+词条
- 新增术语提案集中到词典补充段，审后再生效，保证一致性

### 工具链对齐
- "格式保持算法"需补充规则：`dl/dt/dd`、内联`<tt>`、显式锚
- 转换后运行结构/链接/代码保真检查脚本

## 面向译者的实操提示

### 并行开关与规模
- **编译并行**: `make setup RUN=<RunID> MPI=YES`
- **运行并行**: `runE <RunID> -np <NP>`；批作业通过`QSUB_STRING`替换

### 冷启动与重启
- **冷启动**: `-cold-restart`
- **`&INPUTZ`控制**: 首次短跑与长跑结束时间

### 配置关键点
- `~/.modelErc` 中明确 `COMPILER/NETCDFHOME/MPIDISTR/MPIDIR...`

### Rundeck核心结构
- 固定顺序的分节+组件库/对象模块/覆盖选项/参数名录

### 年份/情景控制
- `master_yr`、`*_yr`族、`variable_orb_par`、`orb_par_year_bp`、`*_day`

## 结论与执行建议

**复杂度评估**: 可控但对"结构保真+术语一致+可执行性"要求高，整体风险可通过规则化转换与CI校验化解

**执行策略**: 建议按"平台→安装→配置→rundeck→编译→运行→参数语义"的顺序推进，7–8由资深译者把关

**准备工作**: 建议在开工前补齐转换规则与术语lint，以减少返工

**最终建议**: **通过（进入执行）**

---

## 建议新增/确认术语清单

### 核心技术术语
- **Namelist**: Fortran名录/参数名录，保留 Namelist 并附中文注
- **QSUB_STRING**: 作业提交模板字符串，保留英文
- **ESMF**: 地球系统建模框架
- **`&INPUTZ`**: 重启与计时参数名录节名

### 并行计算术语
- **OpenMPI / Intel MPI / MPICH / MVAPICH2 / SCALI / mpt**: 专名保留
- **"MPI进程"**: 优先于"MPI线程"

### 编译构建术语
- **Preprocessor Options**: 预处理选项
- **Object modules**: 对象模块
- **Components**: 组件库

### 模型参数术语
- **`master_yr`/`*_yr`/`*_day`**: 参数名保留+中文解释

---

**文件参考**:
- `.claude/request.md`
- `.claude/translation-format-standard.md`
- `.claude/terminology-dictionary.md`
- `doc/UserGuide/*.html` (8个核心文档)