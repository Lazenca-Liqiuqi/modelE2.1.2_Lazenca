# ModelE2.1.2_Lazenca 翻译工具链配置 | Translation Toolchain Configuration
# 大模型翻译工具设置和参数优化 | Large Language Model Translation Tool Settings and Parameter Optimization

## 配置概述 | Configuration Overview

本配置文件定义了ModelE2.1.2_Lazenca项目翻译工作所需的大模型翻译工具链，包括API配置、专业领域参数、质量控制设置等。
This configuration file defines the large language model translation toolchain required for the ModelE2.1.2_Lazenca project translation, including API configuration, professional domain parameters, and quality control settings.

---

## 1. 翻译工具架构 | Translation Tool Architecture

### 工具链组件 | Toolchain Components
```
翻译请求 → 术语预处理 → 大模型翻译 → 格式后处理 → 质量检查 → 输出结果
    ↓           ↓           ↓           ↓           ↓           ↓
 Claude Code → 术语词典 → API调用 → 格式保持 → 质量验证 → 最终译文
```

### 主要模块 | Main Modules
1. **术语预处理模块**：在翻译前识别和标记专业术语
2. **大模型翻译模块**：执行核心翻译任务
3. **格式保持模块**：确保代码和注释格式兼容
4. **质量检查模块**：验证翻译质量
5. **后处理模块**：最终格式调整和优化

---

## 2. 大模型API配置 | Large Language Model API Configuration

### 模型选择 | Model Selection
| 模型名称 | 用途 | 优势 | 适用场景 |
|---------|------|------|---------|
| Claude 3.5 Sonnet | 主翻译模型 | 强大的专业翻译能力，支持长上下文 | HTML文档、复杂技术文档 |
| Claude 3 Haiku | 快速翻译模型 | 速度快，成本低 | 简单注释、重复性内容 |
| GPT-4 | 备用翻译模型 | 专业术语处理能力强 | 特殊专业术语、质量验证 |
| Codex | 代码相关翻译 | 深度理解代码结构 | Fortran代码注释翻译 |

### API参数设置 | API Parameter Settings

#### Claude 3.5 Sonnet 配置
```yaml
claude_35_sonnet:
  model: "claude-3-5-sonnet-20241022"
  max_tokens: 8192
  temperature: 0.1  # 低温度确保翻译一致性
  top_p: 0.95
  context_window: 200000  # 支持长文档翻译
  system_prompt: |
    你是专业的科学计算和气候模型翻译专家，专门负责NASA GISS ModelE地球系统模型的技术文档翻译任务。

    翻译原则：
    1. 严格遵循ModelE专业术语词典，确保术语一致性
    2. 保持技术内容的准确性和完整性
    3. 采用中英对照格式，便于技术交流
    4. 保持代码注释的格式兼容性
    5. 确保科学概念的专业性和准确性

    专业领域：气候科学、大气物理学、海洋学、数值计算、Fortran编程
    目标读者：气候科学研究人员、模型开发者、研究生
```

#### Claude 3 Haiku 配置
```yaml
claude_3_haiku:
  model: "claude-3-haiku-20240307"
  max_tokens: 4096
  temperature: 0.0  # 零温度确保完全一致性
  top_p: 0.9
  context_window: 100000
  system_prompt: |
    你是专门的术语标准化翻译助手，负责快速翻译标准化的技术内容。
    严格按照提供的术语词典进行翻译，确保术语完全一致。
```

#### GPT-4 配置
```yaml
gpt_4:
  model: "gpt-4-turbo-preview"
  max_tokens: 4096
  temperature: 0.2
  top_p: 0.9
  context_window: 128000
  system_prompt: |
    你是气候科学和Fortran编程的专业翻译顾问，负责处理复杂的专业术语和技术概念翻译。
    重点关注：
    1. 专业术语的准确翻译
    2. 技术概念的清晰表达
    3. 学术语言的规范性
```

---

## 3. 专业领域参数优化 | Professional Domain Parameter Optimization

### 领域特定指令 | Domain-Specific Instructions

#### 气候科学翻译指令
```text
气候科学专业翻译要求：
1. 物理过程描述要科学准确，避免口语化表达
2. 专业术语使用学术界标准译法
3. 数值和单位要保持原样，只翻译说明文字
4. 公式和符号保持不变，翻译描述部分
5. 保持逻辑推理的严密性
```

#### Fortran代码翻译指令
```text
Fortran代码注释翻译要求：
1. 保持代码格式完全不变，只翻译注释内容
2. 变量名、函数名、模块名保持英文原样
3. 技术术语要与术语词典完全一致
4. 注释格式要保持Fortran语法兼容
5. 确保翻译后的注释不会影响代码编译
```

#### HTML文档翻译指令
```text
HTML文档翻译要求：
1. 保持HTML结构完整，只翻译文本内容
2. 标签、属性、CSS选择器保持不变
3. 链接地址保持原样，只翻译链接文本
4. 图片alt属性可以翻译，但src路径不变
5. 表格结构保持，翻译单元格内容
```

### 术语一致性控制 | Terminology Consistency Control
```yaml
terminology_control:
  dictionary_path: ".claude/terminology-dictionary.md"
  enforcement_level: "strict"  # strict, moderate, flexible
  pre_processing: true
  post_processing: true
  auto_correction: true

  # 术语标记规则
  markup_rules:
    - pattern: "{{TERMINOLOGY}}"
      replacement: "[标准译名]"
      priority: "high"
    - pattern: "\\b(GCM|ESM|NASA|GISS)\\b"
      action: "keep_original"
      priority: "medium"
```

---

## 4. 格式保持算法配置 | Format Preservation Algorithm Configuration

### Fortran注释格式保持 | Fortran Comment Format Preservation
```yaml
fortran_comment_format:
  # 固定格式Fortran (前6列特殊)
  fixed_format:
    comment_indicators:
      - "C"      # 第1列为C表示注释行
      - "c"      # 小写c也表示注释
      - "*"      # 第1列为*也表示注释
    continuation:
      indicator: "      +"  # 第6列为+表示续行
      max_lines: 19       # 最多续行数
    column_rules:
      code_start: 7        # 代码从第7列开始
      comment_column: 73   # 注释区从第73列开始

  # 自由格式Fortran
  free_format:
    comment_indicators:
      - "!"               # !开头表示注释
    line_length_limit: 132  # 行长度限制

  # 格式保持策略
  preservation_strategy:
    preserve_whitespace: true
    preserve_indentation: true
    preserve_line_breaks: true
    preserve_special_characters: true
```

### HTML格式保持 | HTML Format Preservation
```yaml
html_format:
  preserve_structure:
    - "DOCTYPE"
    - "html"
    - "head"
    - "body"
  preserve_attributes:
    - "href"
    - "src"
    - "id"
    - "class"
    - "style"
  translate_content:
    - "title"
    - "alt"
    - "text nodes"

  # 特殊元素处理
  special_elements:
    code_blocks: "keep_original"
    mathematical_expressions: "keep_original"
    references: "translate_with_preservation"
```

---

## 5. 质量检查系统 | Quality Control System

### 自动化质量检查 | Automated Quality Control
```yaml
quality_control:
  # 术语一致性检查
  terminology_check:
    enabled: true
    dictionary_reference: ".claude/terminology-dictionary.md"
    tolerance: "strict"
    auto_correction: true

  # 格式完整性检查
  format_check:
    fortran_syntax: true
    html_validity: true
    link_integrity: true
    encoding_consistency: true

  # 内容完整性检查
  content_check:
    missing_translation_detection: true
    encoding_error_detection: true
    placeholder_detection: true

  # 编译兼容性检查
  compilation_check:
    fortran_compile_test: true
    syntax_validation: true
    dependency_check: true
```

### 人工审查检查点 | Manual Review Checkpoints
```yaml
manual_review:
  high_priority_items:
    - "核心物理过程描述"
    - "关键算法说明"
    - "用户界面文档"

  review_criteria:
    - "技术准确性"
    - "术语一致性"
    - "表达清晰性"
    - "格式兼容性"

  approval_workflow:
    stages: ["translator_review", "expert_review", "final_approval"]
    required_approvals: 2
```

---

## 6. 翻译工作流程 | Translation Workflow

### 标准翻译流程 | Standard Translation Process
```yaml
translation_workflow:
  1_preprocessing:
    - content_analysis
    - terminology_identification
    - format_detection
    - difficulty_assessment

  2_translation:
    - primary_translation
    - terminology_enforcement
    - format_preservation

  3_quality_control:
    - automated_qc
    - format_validation
    - terminology_consistency_check

  4_postprocessing:
    - final_formatting
    - metadata_addition
    - integration_testing
```

### 特殊情况处理 | Special Case Handling
```yaml
special_cases:
  untranslatable_content:
    - "code_snippets"
    - "mathematical_formulas"
    - "file_paths"
    - "url_links"

  ambiguous_terminology:
    action: "flag_for_review"
    auto_suggestion: true
    expert_validation_required: true

  format_conflicts:
    resolution_strategy: "prioritize_compilability"
    fallback_options: ["minimal_translation", "reference_only"]
```

---

## 7. 性能优化配置 | Performance Optimization Configuration

### 批处理设置 | Batch Processing Settings
```yaml
batch_processing:
  batch_size:
    html_documents: 50        # HTML文档批处理大小
    fortran_files: 100        # Fortran文件批处理大小
    small_files: 200          # 小文件批处理大小

  parallel_processing:
    max_concurrent_requests: 5
    request_timeout: 120      # 请求超时时间（秒）
    retry_attempts: 3         # 重试次数

  memory_optimization:
    context_management: "sliding_window"
    cache_frequent_terms: true
    compress_large_files: true
```

### 错误处理和恢复 | Error Handling and Recovery
```yaml
error_handling:
  retry_strategy:
    max_retries: 3
    backoff_factor: 2
    exponential_backoff: true

  error_classification:
    - "network_errors"       # 网络错误
    - "api_errors"          # API错误
    - "format_errors"       # 格式错误
    - "content_errors"      # 内容错误

  recovery_actions:
    network_errors: "retry_with_exponential_backoff"
    api_errors: "switch_to_backup_model"
    format_errors: "manual_intervention"
    content_errors: "flag_for_review"
```

---

## 8. 监控和日志 | Monitoring and Logging

### 翻译进度监控 | Translation Progress Monitoring
```yaml
monitoring:
  progress_tracking:
    file_count: true
    word_count: true
    completion_percentage: true
    estimated_time_remaining: true

  quality_metrics:
    terminology_consistency_score: true
    format_compliance_rate: true
    error_rate: true
    user_satisfaction_score: true

  performance_metrics:
    translation_speed: "words_per_minute"
    api_response_time: "milliseconds"
    error_rate: "percentage"
    cost_tracking: "tokens_used"
```

### 日志配置 | Logging Configuration
```yaml
logging:
  log_level: "INFO"  # DEBUG, INFO, WARNING, ERROR
  log_format: "structured_json"

  log_categories:
    - "translation_requests"
    - "quality_checks"
    - "error_events"
    - "performance_metrics"

  retention_policy:
    max_log_size: "1GB"
    retention_days: 30
    compression: true
```

---

## 9. 配置管理 | Configuration Management

### 版本控制 | Version Control
```yaml
version_control:
  config_version: "v1.0"
  last_updated: "2025-10-28"
  changelog:
    - "v1.0: 初始配置建立，包含完整的翻译工具链设置"

  backup_strategy:
    automatic_backup: true
    backup_frequency: "daily"
    backup_location: ".claude/backup/"
```

### 配置验证 | Configuration Validation
```yaml
validation:
  required_fields:
    - "api_credentials"
    - "dictionary_path"
    - "output_directory"

  validation_tests:
    - "api_connectivity_test"
    - "dictionary_access_test"
    - "format_algorithm_test"
    - "quality_control_test"
```

---

## 10. 使用说明 | Usage Instructions

### 快速开始 | Quick Start
```bash
# 1. 加载翻译配置
source .claude/translation-tools-config.md

# 2. 验证配置
python .claude/scripts/validate-config.py

# 3. 运行翻译
python .claude/scripts/run-translation.py --input=source_file --output=target_file

# 4. 质量检查
python .claude/scripts/quality-check.py --file=translated_file
```

### 高级功能 | Advanced Features
```bash
# 批量翻译
python .claude/scripts/batch-translate.py --directory=input_dir --output_dir=output_dir

# 术语一致性检查
python .claude/scripts/terminology-check.py --file=translated_file --dictionary=dictionary.md

# 格式验证
python .claude/scripts/format-validate.py --file=translated_file --type=fortran
```

---

**配置版本 | Configuration Version**: v1.0
**创建日期 | Creation Date**: 2025-10-28
**最后更新 | Last Updated**: 2025-10-28
**维护者 | Maintainer**: ModelE2.1.2_Lazenca翻译团队

**注意事项 | Important Notes**:
1. 本配置文件包含敏感信息，请妥善保管
2. API密钥需要单独配置在环境变量中
3. 配置更新后需要重新验证
4. 定期备份配置文件防止丢失