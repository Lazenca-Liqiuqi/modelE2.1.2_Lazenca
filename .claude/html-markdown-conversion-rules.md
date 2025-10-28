# HTML到Markdown转换详细规则 | Detailed HTML to Markdown Conversion Rules

**版本 | Version**: v1.0
**创建日期 | Creation Date**: 2025-10-28
**适用范围 | Scope**: UserGuide文档翻译项目
**基于 | Based on**: Codex深度分析结果

---

## 转换原则 | Conversion Principles

### 核心原则 | Core Principles
1. **结构保持优先 | Structure Preservation Priority**: 确保HTML结构信息完整转移到Markdown
2. **代码保真原则 | Code Fidelity Principle**: 所有代码块、命令行、占位符必须100%保持不变
3. **链接有效原则 | Link Validity Principle**: 所有锚点和链接必须保持有效性
4. **中英对照格式 | Bilingual Format**: 采用段落级中英叠放格式

---

## 特殊HTML元素处理规则 | Special HTML Element Processing Rules

### 1. 定义列表处理 | Definition Lists Processing

#### HTML结构
```html
<dl>
  <dt>术语1</dt>
  <dd>术语1的解释说明</dd>
  <dt>术语2</dt>
  <dd>术语2的解释说明</dd>
</dl>
```

#### Markdown转换规则
```markdown
**术语1**: 术语1的解释说明
**术语2**: 术语2的解释说明
```

#### 注意事项
- 使用粗体标记术语，冒号后跟解释
- 每个定义项单独一行，行末添加两个空格确保换行
- 保持定义的完整性，不拆分到多行

### 2. 锚点处理 | Anchor Processing

#### HTML结构
```html
<h2><a name="section1"></a>章节标题</h2>
<a href="#section1">链接到章节1</a>
```

#### Markdown转换规则
```markdown
## 章节标题 {#section1}
[链接到章节1](#section1)
```

#### 特殊处理
- **页内锚点**: 保留原始锚点名称，使用Pandoc风格的`{#id}`语法
- **标题锚点**: 自动生成中文翻译的英文锚点，同时保留原始HTML锚点（如需要）
- **复杂锚点**: 对于特殊字符锚点，保留原始HTML格式：`<a name="year"></a>`

### 3. 内联代码处理 | Inline Code Processing

#### HTML结构
```html
<tt>代码文本</tt>
<code>代码文本</code>
```

#### Markdown转换规则
```markdown
`代码文本`
```

#### 注意事项
- `<tt>`和`<code>`都转换为行内反引号
- 代码文本内容保持不变，包括大小写和特殊字符
- 避免在代码块前后添加额外的空格

### 4. 代码块处理 | Code Block Processing

#### HTML结构
```html
<pre><code>
command line 1
command line 2
</code></pre>
```

#### Markdown转换规则
```markdown
```bash
command line 1
command line 2
```
```

#### 语言标识规则
- **Shell命令**: 使用`bash`
- **配置文件**: 不指定语言或使用`text`
- **未知类型**: 使用`text`或不指定语言
- **Fortran代码**: 使用`fortran`

### 5. 列表处理 | List Processing

#### 有序列表
```html
<ol>
  <li>第一项</li>
  <li>第二项</li>
</ol>
```
```markdown
1. 第一项
2. 第二项
```

#### 无序列表
```html
<ul>
  <li>项目一</li>
  <li>项目二</li>
</ul>
```
```markdown
- 项目一
- 项目二
```

### 6. 强调和格式处理 | Emphasis and Formatting

```html
<strong>粗体</strong> → **粗体**
<b>粗体</b> → **粗体**
<em>斜体</em> → *斜体*
<i>斜体</i> → *斜体*
```

---

## 中英对照格式规范 | Bilingual Format Specifications

### 段落级对照格式 | Paragraph-level Parallel Format

#### 标准格式
```markdown
**English original text**
英文翻译文本

**English original paragraph**
英文翻译段落
```

#### 格式要求
- 英文原文使用粗体标记
- 中文翻译紧跟英文，空一行分隔
- 英文和中文段落数量必须严格相等
- 保持原有的段落结构

### 标题处理 | Heading Processing

```markdown
## Chapter Title / 章节标题

### Section Title / 节标题

#### Subsection Title / 小节标题
```

### 代码块双语处理 | Code Block Bilingual Processing

```markdown
**Command example**
```bash
make setup RUN=<RunID>
```

**命令说明**
使用make命令编译模型并设置运行目录...
```

---

## 保真性检查清单 | Fidelity Checklist

### 代码保真检查 | Code Fidelity Check
- [ ] 所有命令行文本保持完全一致
- [ ] 占位符（如`<RunID>`, `-np`, `%np`）保持不变
- [ ] 文件路径和扩展名保持原样
- [ ] 代码块的语言标识正确
- [ ] 内联代码使用反引号标记

### 结构保真检查 | Structure Fidelity Check
- [ ] 定义列表转换正确
- [ ] 锚点和链接保持有效
- [ ] 列表项数量一致
- [ ] 标题层级结构正确
- [ ] 段落分隔正确

### 术语保真检查 | Terminology Fidelity Check
- [ ] 使用标准化术语词典中的译名
- [ ] 专业术语保持一致性
- [ ] 新术语已添加到词典
- [ ] 缩写词处理正确

---

## 质量控制流程 | Quality Control Process

### 四道闸检查机制 | Four-Gate Inspection Mechanism

#### 第一闸：结构检查 | Structure Check
- 段落配对计数器验证（英文段落数 = 中文段落数）
- 标题数量和层级对比
- 列表项数量验证

#### 第二闸：保真检查 | Fidelity Check
- 代码块Token白名单校验
- 命令行完整性检查
- 占位符格式验证

#### 第三闸：术语检查 | Terminology Check
- 术语词典一致性检查
- 新术语收录验证
- 上下文术语一致性

#### 第四闸：链接检查 | Link Check
- 页内锚点有效性测试
- 跨文档链接验证
- 引用完整性检查

---

## 特殊情况处理 | Special Case Handling

### 平台差异处理 | Platform Difference Handling

#### 命令兼容性
```markdown
**Platform note**:
以下命令示例基于Linux/CentOS环境，其他系统可能需要调整包管理器和路径设置。
```

#### 版本说明
```markdown
**Version note**:
示例中的gcc49、devtoolset-6等版本号来自原文历史环境，请根据本地环境替换为等效版本。
```

### 复杂表格处理 | Complex Table Processing

对于复杂HTML表格，如果标准Markdown表格语法无法表达，采用以下策略：
1. 简化表格结构
2. 使用列表格式重新组织内容
3. 必要时保留HTML表格格式

---

## 工具和脚本 | Tools and Scripts

### 自动化检查脚本 | Automated Inspection Scripts

#### 代码保真检查
```bash
# 检查命令行是否被修改
grep -n "make\|gmake\|MPI\|<RunID>" output.md
```

#### 术语一致性检查
```bash
# 检查术语使用
grep -n "rundeck\|checkpoint\|restart" output.md
```

#### 链接有效性检查
```bash
# 检查Markdown链接
grep -n "\[.*\](#.*)" output.md
```

---

**更新记录 | Update Log**:
- v1.0 (2025-10-28): 基于Codex分析结果制定初始版本

**维护者 | Maintainer**: ModelE2.1.2_Lazenca翻译团队