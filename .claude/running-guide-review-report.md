运行指南翻译深度技术审查报告 — Running_the_model.html
时间：2025-10-29 09:27

一、审查概览
- 审查对象：doc/UserGuide/Running_the_model.html（中英对照叠放）
- 覆盖主题：runE脚本使用、批处理作业提交（QSUB_STRING/Slurm）、MPI线程配置（-np）、运行时间控制（-t）、检查点文件与停止流程（sswE）
- 参考请求：.claude/running-guide-review-request.md
- 总体结论：内容完整、结构清晰、保真度高，存在少量术语与表述细节可优化。

二、结构化评分
- 技术维度：93/100
  - HTML结构：标签闭合正确、UTF-8声明、语义层级（H3/H4/P/pre/dl/dt/dd）合理；中英对照通过额外段落/定义项实现，结构稳定。
  - 保真性：命令、参数、路径、变量保真（runE/sswE、-np/-t/-cold-restart/-d/-q/-l/-s、modelE/exec、~/.modelErc、QSUB_STRING、QSUB_STRING_tag、Slurm示例）均与英文一致。
  - 术语一致性：基本遵循词典v1.4（“检查点文件”“MPI线程”“rundeck”“runE脚本”）；个别细节不完全一致（见问题清单）。
  - 规范细节：双语段落未标注中文块语言属性；个别中文用语略书面化/不够自然。

- 战略维度：95/100
  - 需求匹配：读者可据中文说明完成初始化短时运行→校验日志→从检查点续跑→批作业提交→优雅停止的完整闭环。
  - 架构一致：与常见编译/运行流程术语匹配（rundeck/INPUTZ、ISTART、MPI线程、Slurm）；不引入新概念。
  - 风险控制：强调先短跑+检查日志；指出批作业需本地化QSUB_STRING配置；停止流程明确会写检查点后退出。

- 综合评分：94/100

三、四道闸质量检查
- 结构：通过 — HTML结构与中英叠放模式规范、可渲染稳定。
- 保真：通过 — 命令/参数/路径/占位符示例与英文一一对应。
- 术语：基本通过 — 2处需统一（“检查点（重启）文件”、namelist译法）。
- 链接：通过 — 无破链；外部依赖仅样式表modele.css。

四、问题清单（证据与影响）
1) 术语一致性
  - 位置：首段中文 “检查点（重启）文件”
  - 证据：英文 “checkpoint (restart) file”；词典v1.4：checkpoint file → 检查点文件
  - 影响：与词典不一致，降低术语统一性；“（重启）”属解释性补充，非标准术语。
  - 建议：统一为“检查点文件”，必要时在首次出现处以脚注或括注解释“用于重启（restart）”。

2) 名词/概念译法
  - 位置：段落中 “<code>INPUTZ</code> 参数名录节”
  - 证据：英文 “section with INPUTZ namelist parameters”
  - 影响：“名录节”不常见，读者可能误解；常规写法为“namelist 参数节/段”。
  - 建议：改为“rundeck 中 <code>INPUTZ</code> namelist 参数节”。

3) 语言属性与可访问性
  - 位置：整页 <HTML lang=en>，中文块未标注语言。
  - 影响：屏幕阅读器/搜索引擎对中英混排语料的语言判定不精确；微弱影响可访问性与可检索性。
  - 建议：为中文标题与段落添加 lang="zh-CN"（或在包含“【中文翻译】”的元素上标注）。示例：<H3 lang="zh-CN">【中文翻译】运行模型</H3>。

4) 表述自然度
  - 位置：“否则没有影响”、“您必须查看特定计算机的本地信息”
  - 影响：语气略生硬；不影响理解但影响阅读体验。
  - 建议：分别改为“否则不生效/否则不起作用”、“请参考所用计算机的本地使用说明/平台文档”。

5) 说明明确性
  - 位置：英文 “the ending time for a longer run is specified on the line above it” 的中文对应
  - 影响：对新手略抽象；易产生“上方哪一行”的疑惑。
  - 建议：补充提示语如“长时间运行的结束时间在其上一行（紧邻上一行）指定”。若允许，可附一个INPUTZ片段示例更直观。

6) 结构实现细节
  - 位置：<dl> 内以双 <dd>（英+中）承载释义
  - 影响：语义上合法；若需样式区分/折叠，建议为中文 <dd> 添加 class（如 class="i18n-zh"），便于CSS控制。
  - 建议：非必要优化，按现有渲染风格可保持不变。

7) 环境提示（信息增强，非错误）
  - 位置：-d（调试）说明
  - 影响：默认 gdb + xterm 依赖图形会话；在部分HPC无X转发/无xterm环境下不可用。
  - 建议：可补一行“若环境无xterm，请改设 DEBUG_COMMAND 为无图形调试器或移除此选项”。

五、保真核对要点（逐项核验）
- 命令行：runE <RunID> [-np NP] [-t time] [-cold-restart] [-d] [-q] [-l logfile] [-s tag] — 一致。
- 选项释义：-np/-t/-cold-restart/-d/-q/-l/-s — 含义与英文一致，未遗漏或改写。
- 路径/文件：modelE/exec/runE、modelE/exec/sswE、~/.modelErc、<RunID>.PRT — 一致。
- 变量/占位符：QSUB_STRING、QSUB_STRING_tag、%np、%t、account_name — 一致。
- 示例：Slurm sbatch 行 — 一致。

六、改进建议（按优先级）
P0（术语一致性）
- 统一“checkpoint file”译法为“检查点文件”；移除“（重启）”字样或以脚注说明。
- 将“参数名录节”改为“namelist 参数节”。

P1（可用性与可访问性）
- 为所有中文标题/段落加 lang="zh-CN" 属性；或在中文块外包裹 <div lang="zh-CN">。
- 优化两处中文表述：“否则不生效/不起作用”、“请参考所用计算机的本地使用说明/平台文档”。

P2（信息增强）
- -d 选项处补充无xterm环境的提示。
- 可在“长时间运行结束时间”说明后附一个最小 rundeck INPUTZ 片段示例（可选）。

七、最终结论
- 建议：需讨论（Minor）
- 结论说明：当前版本已可用，满足读者按中文说明完成运行；为达成“术语词典v1.4完全一致/验收≥95”的目标，建议按上文P0/P1小改。预计微调后综合分可提升至97+。

八、评分汇总
- 技术维度：93/100
- 战略维度：95/100
- 综合评分：94/100

九、文件参考
- doc/UserGuide/Running_the_model.html:1
- .claude/running-guide-review-request.md:1

