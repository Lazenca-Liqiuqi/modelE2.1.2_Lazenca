# 审查请求 | Review Request

## 一、项目基本信息

**项目名称**: ModelE2.1.2_Lazenca - NASA GISS地球系统模型中文翻译
**当前版本**: 0.2.2
**项目类型**: 大气环流模型(GCM)/地球系统模型翻译
**主要语言**: Fortran 90/95, 部分C代码
**翻译范围**: 620+ 文件（HTML文档、Fortran代码、脚本、配置文件）

**项目目录结构**:
```
modelE2.1.2_Lazenca/
├── model/              # 核心模型源代码
├── doc/                # 文档目录
│   ├── UserGuide/      # 用户指南翻译
│   └── technical-reference/  # 技术参考翻译（新增）
├── old-doc/            # 原始英文文档
└── .claude/            # 项目记忆和配置
```

## 二、项目状态与进展

### 当前状态
- **版本**: 0.2.2（2025.11.12发布）
- **Git状态**: 干净，领先origin/master 7个提交
- **翻译进度**: 2/14任务完成（14.3%）

### 已完成任务
1. ✅ **任务#7**: 翻译大气基础模型文档（3个文件，1.4KB）
   - Atmospheric_model.md
   - Dynamics.md
   - Radiation.md

2. ✅ **任务#10**: 翻译陆面基础模型文档（3个文件，1.4KB）
   - Land_Surface_model.md
   - Ground_Hydrology.md
   - Snow_model.md

### 术语标准
严格遵循 `.claude/terminology-dictionary.md v1.4`，包含500+专业术语，覆盖12个领域。

## 三、用户原始需求

**需求类型**: 翻译质量审查

**用户请求**: "创建审查请求"

**背景**: 完成任务#10（陆面基础模型文档翻译）后，请求Codex进行质量审查，确保翻译质量符合项目标准。

## 四、本次工作内容与交付物

### 工作内容
翻译陆面模块基础技术文档，将HTML格式转换为Markdown中英对照格式。

### 交付物清单

#### 1. Land_Surface_model.md
**位置**: `doc/technical-reference/land/Land_Surface_model.md`
**内容**: 仅标题
**原文大小**: 14行HTML
**译文大小**: 3行Markdown

```markdown
# Land Surface model / 陆面模型
```

#### 2. Ground_Hydrology.md
**位置**: `doc/technical-reference/land/Ground_Hydrology.md`
**内容**: 地下水文学描述 + MathJax公式测试部分
**原文大小**: 35行HTML（含LaTeX公式）
**译文大小**: 30行Markdown

**关键术语**:
- Ground Hydrology → 地下水文学
- soils → 土壤
- bare and vegetated soil → 裸土和植被土
- canopy layer → 冠层
- variable depth layers → 变深度层
- Evapotransiration → 蒸散发
- surface pools → 地表蓄水层
- rooting depths → 根深
- Runoff → 径流
- TOPmodel approach → TOPmodel方法

#### 3. Snow_model.md
**位置**: `doc/technical-reference/land/Snow_model.md`
**内容**: 雪模型技术描述
**原文大小**: 16行HTML
**译文大小**: 3行Markdown

**关键术语**:
- Snow model → 雪模型
- 3-layer snow model → 3层雪模型
- variable extent → 可变范围

## 五、审查目标与范围

### 审查目标文件
1. `doc/technical-reference/land/Land_Surface_model.md`
2. `doc/technical-reference/land/Ground_Hydrology.md`
3. `doc/technical-reference/land/Snow_model.md`

### 源文件（参考）
1. `old-doc/ModelDescription/Land_Surface_model.html`
2. `old-doc/ModelDescription/Ground_Hydrology.html`
3. `old-doc/ModelDescription/Snow_model.html`

### 术语标准参考
`.claude/terminology-dictionary.md v1.4`

### 格式参考
`doc/UserGuide/2.3-Compiling_the_model.md`（中英对照叠放格式示例）

## 六、审查要点与检查清单

### 1. 术语一致性检查（权重30%）

**检查项**:
- [ ] 所有专业术语是否与术语词典v1.4一致
- [ ] 同一术语在不同文件中是否保持一致
- [ ] 新术语（如TOPmodel、canopy layer）的翻译是否准确
- [ ] 数值方法术语是否符合学术规范

**关键术语核对**:
- Evapotransiration → 蒸散发 ✓/✗
- Runoff → 径流 ✓/✗
- canopy layer → 冠层 ✓/✗
- variable depth layers → 变深度层 ✓/✗
- surface pools → 地表蓄水层 ✓/✗

### 2. 翻译准确性检查（权重30%）

**检查项**:
- [ ] 技术内容是否准确传达原意
- [ ] 语句逻辑是否通顺
- [ ] 是否有遗漏或误译
- [ ] 引用格式是否保持不变（Stieglitz, 1994）

**重点审查段落**:
> "Evapotransiration takes water from the surface pools, and from below as a function of rooting depths."
> 译文："蒸散发从地表蓄水层和下部（作为根深函数的）获取水分。"

### 3. 格式规范性检查（权重20%）

**检查项**:
- [ ] Markdown语法是否正确
- [ ] 中英对照格式是否符合项目标准
- [ ] 标题层级是否清晰（#, ##, ###）
- [ ] 列表和段落格式是否规范

**格式标准**:
- 标题：`# English / 中文`
- 段落：英文原文 + 空行 + 中文译文
- 保留原有段落结构

### 4. 特殊内容处理检查（权重10%）

**检查项**:
- [ ] LaTeX公式格式是否正确保留
- [ ] MathJax测试部分的翻译是否合理
- [ ] 文献引用格式是否保持不变

**MathJax公式审查**:
```markdown
Here is an example of in-line formula: $W_i = x$
这是一个行内公式示例：$W_i = x$
```
- 公式本身未翻译 ✓/✗
- 说明文字已翻译 ✓/✗

### 5. 文档完整性检查（权重10%）

**检查项**:
- [ ] 是否有遗漏的内容
- [ ] 文件编码是否正确（UTF-8）
- [ ] 文件命名是否规范
- [ ] 目录结构是否合理

## 七、审查评分标准

### 综合评分构成
- **技术维度**（50%）: 术语一致性 + 翻译准确性
- **格式维度**（30%）: Markdown格式 + 中英对照格式
- **完整性维度**（20%）: 内容完整 + 特殊内容处理

### 评分等级
- **90-100分**: 优秀，建议通过
- **80-89分**: 良好，小幅修改后通过
- **70-79分**: 合格，需要重要修改
- **60-69分**: 及格，需要大量修改
- **<60分**: 不及格，建议退回重做

### 通过标准
- 综合评分 ≥ 90分
- 且Codex建议"通过"
- 且所有核心检查项（术语、准确性、格式）无重大缺陷

## 八、审查输出要求

请Codex提供：

1. **技术维度评分**（代码质量、测试覆盖、规范遵循）
   - 术语一致性评分（0-50分）
   - 翻译准确性评分（0-50分）

2. **格式维度评分**（需求匹配、架构一致、风险评估）
   - Markdown格式评分（0-30分）
   - 中英对照格式评分（0-30分）

3. **完整性维度评分**（0-20分）

4. **综合评分**（0-100分）

5. **明确建议**（通过/退回）
   - 支持论据
   - 关键发现
   - 完整结构化输出

6. **修改记录**
   - 发现的问题列表
   - 具体修改建议
   - 优先级排序

## 九、附加说明

### 翻译难点
1. **TOPmodel**: 专有名词，保留英文还是翻译？
2. **Evapotransiration**: 原文拼写错误（正确为Evapotranspiration），如何处理？
3. **MathJax测试部分**: 是否需要翻译，还是保持原样？

### 项目特殊情况
- 陆面模块文档内容极简，部分文件仅有标题
- 原HTML文件包含测试内容（MathJax测试），不确定是否需要翻译
- 项目采用中英对照叠放格式，与纯翻译有所不同

### 审查重点
请特别关注：
1. 术语使用的准确性和一致性
2. 技术内容传达的准确性
3. 中英对照格式的规范性
4. Markdown语法的正确性

---

**审查请求创建时间**: 2025-11-12
**请求创建者**: Claude Code
**会话类型**: 任务#10完成后的质量审查
**预期审查者**: Codex AI
