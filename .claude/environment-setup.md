# ModelE2.1.2_Lazenca 翻译项目环境配置

## 🔧 开发环境要求

### 系统环境
- **操作系统**: Windows 11 + WSL2 / Linux / macOS
- **Python版本**: 3.9+
- **Git**: 版本控制
- **Node.js**: 16+ (用于某些工具脚本)

### Python依赖包
```bash
pip install beautifulsoup4
pip install lxml
pip install requests
pip install markdown
pip install jinja2
pip install pyyaml
pip install click
pip install rich
pip install tqdm
```

### 工具配置
- **文本编辑器**: VS Code + Fortran扩展
- **浏览器**: Chrome/Firefox (用于HTML预览)
- **终端**: Windows Terminal / iTerm2
- **字体**: 支持中英文等宽字体

## 📁 目录结构配置

### 工作目录结构
```
.claude/
├── translation-scope.md          # 翻译范围确认
├── translation-format-standard.md # 格式标准
├── project-workflow.md           # 工作流程
├── environment-setup.md          # 环境配置
├── term-dictionary.md           # 术语词典
├── tools/                       # 工具脚本
│   ├── format-checker.py        # 格式检查工具
│   ├── terminology-checker.py   # 术语一致性检查
│   ├── link-validator.py        # 链接验证工具
│   ├── progress-tracker.py      # 进度追踪工具
│   └── quality-scorer.py        # 质量评分工具
├── templates/                   # 翻译模板
│   ├── html-template.html       # HTML翻译模板
│   ├── fortran-template.f       # Fortran注释模板
│   └── script-template.sh       # 脚本注释模板
├── reports/                     # 报告目录
│   ├── daily-progress/          # 每日进度报告
│   ├── weekly-summary/          # 周度总结
│   └── milestone-review/        # 里程碑评审
└── backup/                      # 备份目录
    └── original-files/          # 原始文件备份
```

## 🛠️ 工具脚本配置

### 1. 格式检查工具 (format-checker.py)
```python
#!/usr/bin/env python3
"""
HTML和Fortran文件格式检查工具
检查翻译格式是否符合标准规范
"""

import re
import os
from pathlib import Path

class FormatChecker:
    def __init__(self, config_file="config/format-rules.json"):
        self.config = self.load_config(config_file)

    def check_html_format(self, file_path):
        """检查HTML文件格式"""
        pass

    def check_fortran_comments(self, file_path):
        """检查Fortran注释格式"""
        pass

    def generate_report(self, results):
        """生成格式检查报告"""
        pass
```

### 2. 术语一致性检查 (terminology-checker.py)
```python
#!/usr/bin/env python3
"""
术语一致性检查工具
确保专业术语翻译的统一性
"""

import json
import re
from collections import defaultdict

class TerminologyChecker:
    def __init__(self, dict_file="term-dictionary.json"):
        self.terminology_dict = self.load_dictionary(dict_file)
        self.inconsistencies = defaultdict(list)

    def check_terminology(self, file_path):
        """检查文件中的术语使用"""
        pass

    def report_inconsistencies(self):
        """报告术语不一致问题"""
        pass
```

### 3. 进度追踪工具 (progress-tracker.py)
```python
#!/usr/bin/env python3
"""
翻译进度追踪工具
实时监控项目完成状态
"""

import json
import datetime
from pathlib import Path

class ProgressTracker:
    def __init__(self, progress_file="progress/translation-progress.json"):
        self.progress_file = progress_file
        self.progress_data = self.load_progress()

    def update_progress(self, file_path, status, notes=""):
        """更新翻译进度"""
        pass

    def generate_daily_report(self):
        """生成每日进度报告"""
        pass

    def calculate_completion_rate(self):
        """计算完成率"""
        pass
```

## 🔍 质量控制配置

### 质量评分标准
```json
{
  "scoring_criteria": {
    "format_compliance": 30,
    "terminology_consistency": 25,
    "technical_accuracy": 25,
    "readability": 20
  },
  "quality_levels": {
    "excellent": 90,
    "good": 75,
    "acceptable": 60,
    "needs_improvement": 40
  }
}
```

### 自动化检查规则
```json
{
  "html_rules": {
    "required_elements": ["h1", "h2", "p", "ul", "li"],
    "translation_markers": ["【中文翻译】"],
    "forbidden_elements": ["machine-translated"],
    "format_requirements": {
      "paragraph_spacing": true,
      "heading_structure": true,
      "list_indentation": true
    }
  },
  "fortran_rules": {
    "comment_format": "^[C!].*",
    "translation_pattern": "^[C!].*【中文翻译】",
    "preserve_indentation": true,
    "preserve_case": true
  }
}
```

## 📊 监控和报告配置

### 每日报告模板
```markdown
# 翻译进度日报 - {日期}

## 📈 今日完成情况
- **完成文件数**: {数量}
- **完成字数**: {字数}
- **质量评分**: {分数}/100

## 📋 具体完成项目
1. {文件1} - 状态: 完成/进行中/遇到问题
2. {文件2} - 状态: 完成/进行中/遇到问题

## ⚠️ 遇到的问题
- {问题描述}
- {解决方案}

## 🎯 明日计划
- {计划任务1}
- {计划任务2}

## 📊 累计进度
- **总体完成率**: {百分比}%
- **阶段完成率**: {百分比}%
```

### 质量评分报告模板
```json
{
  "report_date": "2025-10-28",
  "file_path": "doc/UserGuide/Compiling_the_model.html",
  "scores": {
    "format_compliance": 28,
    "terminology_consistency": 23,
    "technical_accuracy": 24,
    "readability": 18
  },
  "total_score": 93,
  "quality_level": "excellent",
  "issues_found": [],
  "recommendations": []
}
```

## 🔄 自动化工作流程

### Git Hooks配置
```bash
#!/bin/sh
# pre-commit hook - 自动检查翻译质量
python .claude/tools/format-checker.py --staged-files
python .claude/tools/terminology-checker.py --staged-files

# 如果检查失败，阻止提交
if [ $? -ne 0 ]; then
    echo "翻译质量检查失败，请修复问题后重新提交"
    exit 1
fi
```

### CI/CD Pipeline (GitHub Actions)
```yaml
name: Translation Quality Check
on: [push, pull_request]

jobs:
  quality-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run format checks
        run: python .claude/tools/format-checker.py
      - name: Run terminology checks
        run: python .claude/tools/terminology-checker.py
      - name: Generate quality report
        run: python .claude/tools/quality-scorer.py
```

## 🚀 快速启动脚本

### 项目初始化脚本 (setup.sh)
```bash
#!/bin/bash
echo "🚀 初始化ModelE2.1.2_Lazenca翻译项目环境..."

# 创建目录结构
mkdir -p .claude/{tools,templates,reports/{daily-progress,weekly-summary,milestone-review},backup/original-files}

# 安装Python依赖
pip install -r requirements.txt

# 初始化配置文件
cp .claude/config/template.json .claude/config/config.json

# 设置Git hooks
cp .claude/hooks/* .git/hooks/

# 生成初始进度文件
python .claude/tools/progress-tracker.py --init

echo "✅ 环境配置完成！"
echo "📖 请查看 .claude/environment-setup.md 了解详细使用方法"
```

---
*配置版本: v1.0*
*创建时间: 2025-10-28*
*适用项目: ModelE2.1.2_Lazenca翻译项目*