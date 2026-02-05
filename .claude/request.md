# ModelE2.1.2_Lazenca HOWTO翻译审查请求

**审查类型**: 批次翻译质量审查
**审查范围**: HOWTO目录翻译文档（4个文件）
**生成时间**: 2026-02-05
**翻译者**: Claude Code
**词典版本**: v1.5

---

## 一、项目基本信息

### 项目概况
- **项目名称**: ModelE2.1.2_Lazenca - NASA GISS地球系统模型中文翻译
- **项目类型**: 大气环流模型(GCM)/地球系统模型文档翻译
- **翻译范围**: 支持文档翻译（HOWTO目录）
- **当前版本**: 0.3.0
- **翻译批次**: 第1-2批次（支持文档翻译阶段）

### 项目结构
```
modelE2.1.2_Lazenca/
├── doc/HOWTO/              # 翻译输出目录
│   ├── SCM.md              ✅ 第1批次
│   ├── git_howto.md        ✅ 第1批次
│   ├── time_management.md  ✅ 第2批次
│   └── newio.md            ✅ 第2批次（P0关键文档）
├── old-doc/HOWTO/          # 原始文档
│   ├── SCM.txt
│   ├── git_howto.html
│   ├── time_management.txt
│   └── newio.html
└── .claude/
    ├── terminology-dictionary.md v1.5  # 术语词典
    └── translation-standards.md v1.3   # 翻译规范
```

---

## 二、项目状态与进展

### 当前状态
- **阶段**: 第二阶段：支持文档翻译（HOWTO目录）
- **完成度**: 4/8 文档（50%）
- **质量目标**: Codex审查均分 ≥ 95/100
- **P0文档目标**: newio.md ≥ 96/100

### 翻译批次历史

| 批次 | 文件数 | 优先级 | 主要内容 | 状态 |
|------|--------|--------|----------|------|
| 第1批 | 2个 | P1-P2 | SCM单列模型、Git使用指南 | ✅ 完成 |
| 第2批 | 2个 | P1-P0 | 时间管理、NEW_IO系统 | ✅ 完成 |
| 第3批 | 1个 | P2 | Fortran编程规范（LaTeX） | ⏳ 待进行 |
| 第4批 | 2个 | P1 | 运行配置、版本历史 | ⏳ 待进行 |

---

## 三、用户原始需求

> 用户请求：创建审查请求，审查HOWTO里面的所有文档。

### 任务背景
完成第1-2批次翻译（4个文档），需要对这4个翻译文档进行Codex质量审查，确保翻译质量符合项目标准后继续后续批次。

---

## 四、本次工作内容与交付物

### 翻译完成的文档（4个）

| # | 文件名 | 源文件 | 目标文件 | 优先级 | 行数 | 内容概述 |
|---|--------|--------|----------|--------|------|----------|
| 1 | SCM | old-doc/HOWTO/SCM.txt | doc/HOWTO/SCM.md | P2 | 67 | 单列模型使用指南 |
| 2 | git_howto | old-doc/HOWTO/git_howto.html | doc/HOWTO/git_howto.md | P1 | 311 | Git版本控制使用指南 |
| 3 | time_management | old-doc/HOWTO/time_management.txt | doc/HOWTO/time_management.md | P1 | 113 | 时间管理系统架构 |
| 4 | newio | old-doc/HOWTO/newio.html | doc/HOWTO/newio.md | **P0** | 739 | NEW_IO系统完整指南 |

### 交付物
- **4个Markdown翻译文档**: 采用中英对照叠放格式
- **新术语识别**: 约35-53个新术语（待补录到词典v1.6/v1.7）
- **格式转换**: HTML→Markdown，保持原有结构

### 内容特点

**SCM.md**（67行）:
- 单列模型（SCM）配置和使用
- 输入文件格式要求（netCDF）
- 运行时参数说明
- 现有运行配置模板

**git_howto.md**（311行）:
- Git分布式版本控制系统概念
- 安装和配置指南
- 常用Git命令（clone/commit/push/pull等）
- 分支管理
- CVS模拟模式

**time_management.md**（113行）:
- 时间管理系统的重要性
- 典型用法（访问时间信息）
- 实现细节（面向对象设计）
- 主要类和职责（Rational/BaseTime/Calendar等）

**newio.md**（739行，P0关键文档）:
- 运行配置和环境设置
- 重启文件检查和比较
- 保存量到重启文件
- 获取缩放诊断输出
- 时间平均和重映射
- 打印诊断表
- 文件格式转换
- 19个完整章节

---

## 五、审查目标与范围

### 审查目标

1. **验证术语一致性**: 检查与词典v1.5的一致性，新术语处理的合理性
2. **验证翻译准确性**: 技术内容准确传达，语句流畅性
3. **验证格式规范性**: Markdown格式、中英对照叠放格式
4. **验证完整性**: 内容完整、结构保真
5. **质量评估**: 生成质量评分和改进建议

### 审查范围

#### 文件范围（4个文档）
1. `doc/HOWTO/SCM.md`
2. `doc/HOWTO/git_howto.md`
3. `doc/HOWTO/time_management.md`
4. `doc/HOWTO/newio.md`（P0关键文档）

#### 参考文件
- `.claude/rules/translation-standards.md` - 翻译规范v1.3
- `.claude/rules/terminology-dictionary.md` - 术语词典v1.5
- 源文件：`old-doc/HOWTO/*.txt`, `old-doc/HOWTO/*.html`

---

## 六、审查要点与检查清单

### 6.1 术语一致性检查（权重30%）

#### 检查方法
- 验证已知术语与词典v1.5的一致性
- 评估新术语选择的合理性
- 检查跨文档术语使用的一致性
- 验证Git相关术语的统一性
- 验证时间管理术语的准确性
- 验证I/O系统术语的规范性

#### 关键术语类别

**Git术语（15个）**:
| English | 期望译法 | 词典v1.5 |
|---------|----------|----------|
| revision control system | 版本控制系统 | ✅ |
| distributed | 分布式 | - |
| clone | 克隆 | - |
| commit | 提交 | - |
| push | 推送 | - |
| pull | 拉取 | - |
| checkout | 检出 | - |
| branch | 分支 | - |
| master branch | 主分支 | - |
| repository | 仓库 | - |
| remote branch | 远程分支 | - |
| local branch | 本地分支 | - |
| track | 跟踪 | - |
| conflict | 冲突 | - |
| merge | 合并 | - |

**SCM术语（10个）**:
| English | 期望译法 | 词典v1.5 |
|---------|----------|----------|
| single-column model | 单列模型 | - |
| SCM | 单列模型 | - |
| forcing | 强迫 | ✅ |
| nudging | 松弛 | - |
| profile | 廓线 | - |
| sensible heat flux | 感热通量 | ✅ |
| latent heat flux | 潜热通量 | ✅ |
| geostrophic wind | 地转风 | ✅ |
| radiative heating rate | 辐射加热率 | - |
| friction velocity | 摩擦速度 | - |

**时间管理术语（15个）**:
| English | 期望译法 | 词典v1.5 |
|---------|----------|----------|
| time evolution | 时间演化 | - |
| orbital parameters | 轨道参数 | - |
| calendar properties | 日历属性 | - |
| encapsulation | 封装 | - |
| object-oriented programming | 面向对象编程 | ✅ |
| class | 类 | ✅ |
| subclass | 子类 | ✅ |
| base class | 基类 | - |
| rational number | 有理数 | - |
| epoch | 纪元 | - |
| time boundary | 时间边界 | - |
| pseudo-Julian calendar | 伪儒略历 | - |
| exoplanet | 系外行星 | - |
| subcycling | 子循环 | - |
| timestep | 时间步 | ✅ |

**I/O系统术语（25个）**:
| English | 期望译法 | 词典v1.5 |
|---------|----------|----------|
| NEW_IO | NEW_IO系统 | - |
| rundeck | 运行配置 | ✅ |
| restart file | 重启文件 | ✅ |
| accumulation array | 累加数组 | - |
| scaled diagnostics | 缩放诊断输出 | - |
| netcdf | NetCDF格式 | ✅ |
| parallel-netcdf | 并行NetCDF | - |
| cubed-sphere grid | 立方体球面网格 | ✅ |
| native grid | 原生网格 | - |
| remapping | 重映射 | - |
| lat-lon | 经纬度 | - |
| budget page | 预算页 | - |
| diagnostic category | 诊断类别 | - |
| postprocessing | 后处理 | - |
| metadata | 元数据 | - |
| subdaily | 亚日 | - |
| time average | 时间平均 | - |

#### 检查项
- [ ] 所有已知术语与词典v1.5一致
- [ ] 新术语选择合理、符合学科规范
- [ ] Git术语在git_howto.md中统一
- [ ] SCM术语在SCM.md中准确
- [ ] 时间管理术语在time_management.md中准确
- [ ] I/O术语在newio.md中规范
- [ ] 跨4个文档术语使用一致
- [ ] 避免口语化表达

### 6.2 翻译准确性检查（权重30%）

#### 检查方法
- 验证技术内容准确传达原意
- 检查命令行参数准确性
- 验证代码示例保真度
- 检查中文表述流畅性
- 验证无遗漏或误译

#### 重点检查文档

**newio.md**（P0文档，739行）:
- 19个章节内容完整性
- 20个诊断类别准确性
- I/O命令正确性
- 文件格式转换流程
- 配置参数说明清晰度

**git_howto.md**（311行）:
- Git工作流程描述准确性
- 命令使用示例正确性
- 分支管理流程清晰度

**time_management.md**（113行）:
- OOP概念准确传达
- 类设计描述准确性
- 时间管理机制清晰度

**SCM.md**（67行）:
- 单列模型配置准确性
- 输入文件格式说明清晰度
- 运行时参数说明准确性

#### 检查项
- [ ] 技术内容准确传达原意
- [ ] 命令行参数准确无误
- [ ] 代码示例100%保真
- [ ] 中文表述通顺流畅
- [ ] 无直译+括号解释模式
- [ ] 无内容遗漏或误译

### 6.3 格式规范性检查（权重20%）

#### 检查方法
- 验证Markdown语法正确性
- 检查中英对照叠放格式
- 验证HTML→Markdown转换完整性
- 检查代码块格式
- 验证列表和表格格式

#### 检查项
- [ ] 标题格式：`# English / 中文`或`# English`后换行`# 中文`
- [ ] 段落格式：英文在上，中文在下，空行分隔
- [ ] 代码块格式：使用 ```fortran 或 ```bash
- [ ] 列表格式：Markdown列表语法正确（- 或 1.）
- [ ] 链接格式：[text](url) 或 <url>
- [ ] 表格格式：Markdown表格语法正确
- [ ] HTML标签正确转换（HTML→Markdown）

#### 特殊格式检查

**git_howto.md**:
- HTML列表→Markdown列表转换
- 代码块格式正确
- 链接格式正确

**newio.md**:
- 目录链接正确
- 表格格式正确
- 代码示例格式正确
- 章节标题层级清晰

### 6.4 完整性检查（权重10%）

#### 检查内容
- 验证所有4个文档存在
- 检查内容无遗漏
- 验证文件编码正确（UTF-8）
- 检查文件命名符合规范
- 验证目录位置正确

#### 检查项
- [ ] SCM.md存在且完整（67行源文件）
- [ ] git_howto.md存在且完整（311行源文件）
- [ ] time_management.md存在且完整（113行源文件）
- [ ] newio.md存在且完整（739行源文件）
- [ ] 文件编码为UTF-8
- [ ] 文件命名符合规范（.html→.md）
- [ ] 目录位置正确（doc/HOWTO/）

### 6.5 特殊处理检查（权重10%）

#### 检查内容
- 原文拼写错误处理
- 代码注释翻译准确性
- 专有名词保留
- 缩写词处理
- URL和路径保留

#### 重点检查

**time_management.md原文错误**:
- `repsonsibilities` → `responsibilities`
- `AbsractCalendar` → `AbstractCalendar`
- `currenTime` → `currentTime`
- 翻译中是否正确处理并标注

#### 检查项
- [ ] 原文拼写错误已更正并标注
- [ ] 专有名词正确保留（NASA GISS、DOE ARM等）
- [ ] 缩写词处理合理（SCM、I/O、PBL等）
- [ ] URL和路径完整保留
- [ ] 文件名和命令正确保留
- [ ] 代码注释未翻译（保持原样）

---

## 七、评分标准

### 综合评分构成

- **术语一致性（30%）**: 与词典一致性、新术语合理性
- **翻译准确性（30%）**: 技术准确、语句流畅
- **格式规范性（20%）**: Markdown格式、对照格式
- **完整性（10%）**: 内容完整、结构保真
- **特殊处理（10%）**: 错误处理、专有名词

### 通过标准

| 文档 | 优先级 | 目标评分 | 状态 |
|------|--------|----------|------|
| SCM.md | P2 | ≥ 95/100 | 待审查 |
| git_howto.md | P1 | ≥ 95/100 | 待审查 |
| time_management.md | P1 | ≥ 95/100 | 待审查 |
| newio.md | **P0** | **≥ 96/100** | 待审查 |
| **整体平均** | - | **≥ 95/100** | 待审查 |

### 评分等级
- **96-100分**: 优秀，直接通过
- **90-95分**: 良好，小修改后通过
- **80-89分**: 一般，需修改后复审
- **<80分**: 不合格，需重新翻译

### 评分参考（ModelDescription历史）
| 批次 | 评分 | 评级 |
|------|------|------|
| 第1批 | ≥90/100 | 优秀 |
| 第2批 | ≥90/100 | 优秀 |
| 第3批 | ≥90/100 | 优秀 |
| 第4批 | ≥90/100 | 优秀 |
| 第5批 | 96/100 | 优秀 |
| 第6批 | ≥98/100 | 优秀 |
| **整体目标** | **≥95/100** | **优秀** |

---

## 八、特殊关注事项

### 8.1 P0文档：newio.md

**为什么是P0**:
- 第2批次关键文档（739行）
- 涉及I/O系统核心概念和配置
- 20个诊断类别详细说明
- 质量目标：≥ 96/100

**需要特别关注**:
- 诊断类别名称准确性（aj/aij/aijl等）
- I/O命令准确性（scaleacc/sumfiles/diffreport等）
- 文件格式转换流程清晰度
- 配置参数说明准确性
- 19个章节结构完整性

### 8.2 Git术语一致性

**挑战**:
- git_howto.md涉及大量Git术语
- 需要确保译法统一

**关键术语**:
- clone/commit/push/pull/checkout
- branch（分支）/merge（合并）
- repository（仓库）/remote（远程）
- track（跟踪）/conflict（冲突）

### 8.3 新术语识别

**预计新增术语**:
- 第1批次：约15-18个（Git+SCM）
- 第2批次：约20-35个（时间管理+I/O）
- **总计**：约35-53个新术语

**需要评估**:
- 新术语译法合理性
- 是否符合学科规范
- 是否需要补录到词典v1.6/v1.7

### 8.4 原文错误处理

**time_management.txt错误**:
- `repsonsibilities`（原文拼写错误）
- `AbsractCalendar`（原文拼写错误）
- `currenTime`（原文拼写错误）

**期望处理**:
- 在译文中使用正确拼写
- 在中文译文后添加"（原文拼写：xxx）"说明
- 确保读者可以回溯到原文

---

## 九、审查输出要求

### 审查报告结构

请生成`.claude/review-report.md`，包含以下内容：

#### 1. 综合评估
- 整体质量评价
- 综合评分（0-100）
- 通过/退回建议
- 关键发现摘要

#### 2. 分维度评分
- **术语一致性（30%）**：评分、问题列表、改进建议
- **翻译准确性（30%）**：评分、问题列表、改进建议
- **格式规范性（20%）**：评分、问题列表、改进建议
- **完整性（10%）**：评分、问题列表、改进建议
- **特殊处理（10%）**：评分、问题列表、改进建议

#### 3. 文档级详细审查
对每个文档进行详细分析：

**SCM.md**:
- 评分（目标≥95）
- 主要问题（如有）
- 修改建议（如有）

**git_howto.md**:
- 评分（目标≥95）
- 主要问题（如有）
- 修改建议（如有）

**time_management.md**:
- 评分（目标≥95）
- 主要问题（如有）
- 修改建议（如有）

**newio.md**（P0文档）:
- 评分（目标≥96）
- 主要问题（如有）
- 修改建议（如有）
- **特别说明**：P0文档审查意见

#### 4. 术语补录建议
列出需要补录到词典v1.6/v1.7的新术语：
- Git术语
- SCM术语
- 时间管理术语
- I/O系统术语

#### 5. 修改记录
提供具体修改建议，包括：
- 文件路径
- 行号（如有）
- 原文
- 建议修改
- 修改理由

---

## 十、审查完成后的后续步骤

### 如果通过（≥95分）
1. 根据建议进行小修改（如有）
2. 补录新术语到词典v1.6/v1.7
3. 更新任务状态（任务#1-4完成）
4. 继续第3批次翻译（ModelE_Coding_Standards.tex）

### 如果退回（<95分）
1. 根据修改记录进行修改
2. 重新提交Codex审查
3. 直至通过标准

---

## 附录：关键文件路径

### 翻译规范
- `.claude/rules/translation-standards.md` - 翻译规范v1.3
- `.claude/rules/terminology-dictionary.md` - 术语词典v1.5

### 审查文件
- `.claude/request.md` - 本次审查请求
- `.claude/review-report.md` - 审查报告（待生成）

### 翻译文档
- `doc/HOWTO/SCM.md`
- `doc/HOWTO/git_howto.md`
- `doc/HOWTO/time_management.md`
- `doc/HOWTO/newio.md`

### 源文档
- `old-doc/HOWTO/SCM.txt`
- `old-doc/HOWTO/git_howto.html`
- `old-doc/HOWTO/time_management.txt`
- `old-doc/HOWTO/newio.html`

---

**请求生成者**: Claude Code
**请求生成时间**: 2026-02-05
**期望审查完成时间**: 尽快
**审查者**: Codex AI

---

[CONVERSATION_ID]: 019c2813-f6f6-7322-b30b-f6ff83c96711
