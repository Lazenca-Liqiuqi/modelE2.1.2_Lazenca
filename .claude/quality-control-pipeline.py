#!/usr/bin/env python3
"""
ModelE2.1.2_Lazenca 翻译质量检查流水线
Translation Quality Control Pipeline for ModelE2.1.2_Lazenca

这个模块提供完整的翻译质量检查系统，包括术语一致性检查、格式验证、内容完整性验证等。
This module provides a complete translation quality control system, including terminology consistency checks, format validation, content integrity verification, etc.

作者 | Author: ModelE2.1.2_Lazenca翻译团队
版本 | Version: v1.0
创建日期 | Created: 2025-10-28
"""

import os
import re
import json
import logging
import subprocess
from typing import Dict, List, Tuple, Optional, Union, Any
from dataclasses import dataclass, asdict
from enum import Enum
from pathlib import Path
import yaml

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class QualityLevel(Enum):
    """质量等级"""
    EXCELLENT = "excellent"    # 优秀 (90-100分)
    GOOD = "good"             # 良好 (80-89分)
    ACCEPTABLE = "acceptable"  # 可接受 (70-79分)
    NEEDS_IMPROVEMENT = "needs_improvement"  # 需要改进 (60-69分)
    POOR = "poor"             # 差 (0-59分)

class CheckType(Enum):
    """检查类型"""
    TERMINOLOGY = "terminology"           # 术语一致性
    FORMAT = "format"                     # 格式正确性
    CONTENT = "content"                   # 内容完整性
    COMPILATION = "compilation"           # 编译兼容性
    LINKS = "links"                       # 链接有效性
    ENCODING = "encoding"                 # 编码正确性

@dataclass
class QualityIssue:
    """质量问题"""
    check_type: CheckType
    severity: str  # critical, major, minor, info
    line_number: Optional[int]
    description: str
    suggestion: Optional[str] = None
    auto_fixable: bool = False

@dataclass
class QualityReport:
    """质量报告"""
    file_path: str
    overall_score: float
    quality_level: QualityLevel
    issues: List[QualityIssue]
    metrics: Dict[str, Any]
    summary: str
    recommendations: List[str]

class TerminologyChecker:
    """术语一致性检查器"""

    def __init__(self, dictionary_path: str):
        """
        初始化术语检查器

        Args:
            dictionary_path: 术语词典文件路径
        """
        self.dictionary_path = dictionary_path
        self.terminology_dict = {}
        self.load_dictionary()

    def load_dictionary(self):
        """加载术语词典"""
        try:
            with open(self.dictionary_path, 'r', encoding='utf-8') as f:
                content = f.read()
                self.parse_dictionary(content)
            logger.info(f"成功加载术语词典: {len(self.terminology_dict)} 个术语")
        except Exception as e:
            logger.error(f"加载术语词典失败: {e}")

    def parse_dictionary(self, content: str):
        """解析术语词典内容"""
        current_section = None

        for line in content.split('\n'):
            line = line.strip()

            # 跳过空行和注释
            if not line or line.startswith('#'):
                continue

            # 检测章节
            if line.startswith('##'):
                current_section = line.replace('#', '').strip()
                continue

            # 解析术语条目 (| 分隔格式)
            if '|' in line and current_section:
                parts = [part.strip() for part in line.split('|')]
                if len(parts) >= 2:
                    english_term = parts[0].strip()
                    chinese_term = parts[1].strip()
                    note = parts[2].strip() if len(parts) > 2 else ""

                    self.terminology_dict[english_term.lower()] = {
                        'chinese': chinese_term,
                        'english': english_term,
                        'section': current_section,
                        'note': note
                    }

    def check_terminology_consistency(self, content: str, file_path: str) -> List[QualityIssue]:
        """
        检查术语一致性

        Args:
            content: 文件内容
            file_path: 文件路径

        Returns:
            List[QualityIssue]: 发现的质量问题列表
        """
        issues = []
        lines = content.split('\n')

        # 统计术语使用情况
        term_usage = {}

        for line_num, line in enumerate(lines, 1):
            line_lower = line.lower()

            # 检查每个已知术语
            for english_term, term_info in self.terminology_dict.items():
                if english_term in line_lower:
                    # 检查对应中文翻译是否正确使用
                    chinese_expected = term_info['chinese']

                    if chinese_expected not in line:
                        issues.append(QualityIssue(
                            check_type=CheckType.TERMINOLOGY,
                            severity="major",
                            line_number=line_num,
                            description=f"术语 '{english_term}' 可能未使用标准翻译 '{chinese_expected}'",
                            suggestion=f"建议将 '{english_term}' 的翻译统一为 '{chinese_expected}'",
                            auto_fixable=False
                        ))

                    # 记录术语使用
                    if english_term not in term_usage:
                        term_usage[english_term] = []
                    term_usage[english_term].append({
                        'line': line_num,
                        'context': line.strip()
                    })

        # 检查术语使用一致性
        for term, usage_list in term_usage.items():
            if len(usage_list) > 1:
                # 检查同一术语在不同位置的翻译是否一致
                chinese_translations = set()
                for usage in usage_list:
                    context = usage['context']
                    chinese_term = self.terminology_dict[term]['chinese']
                    if chinese_term in context:
                        chinese_translations.add(chinese_term)

                if len(chinese_translations) > 1:
                    issues.append(QualityIssue(
                        check_type=CheckType.TERMINOLOGY,
                        severity="critical",
                        line_number=None,
                        description=f"术语 '{term}' 在文件中使用了多种翻译: {list(chinese_translations)}",
                        suggestion=f"统一使用标准翻译: {self.terminology_dict[term]['chinese']}",
                        auto_fixable=False
                    ))

        return issues

class FormatChecker:
    """格式检查器"""

    def __init__(self):
        """初始化格式检查器"""
        pass

    def check_fortran_format(self, content: str, file_path: str) -> List[QualityIssue]:
        """
        检查Fortran格式

        Args:
            content: 文件内容
            file_path: 文件路径

        Returns:
            List[QualityIssue]: 发现的质量问题列表
        """
        issues = []
        lines = content.split('\n')

        # 检测文件格式
        is_fixed_format = self._detect_fortran_format(lines)

        for line_num, line in enumerate(lines, 1):
            if is_fixed_format:
                issues.extend(self._check_fixed_format_line(line, line_num))
            else:
                issues.extend(self._check_free_format_line(line, line_num))

        return issues

    def _detect_fortran_format(self, lines: List[str]) -> bool:
        """检测是否为固定格式"""
        fixed_indicators = 0
        free_indicators = 0

        for line in lines[:50]:  # 检查前50行
            line = line.rstrip('\n\r')
            if not line.strip():
                continue

            # 固定格式指示符
            if len(line) >= 6:
                if line[0] in ['C', 'c', '*']:
                    fixed_indicators += 1
                if line[5] in ['+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    fixed_indicators += 1

            # 自由格式指示符
            if '!' in line and not line.startswith(('C', 'c', '*')):
                comment_pos = line.find('!')
                if comment_pos > 0:
                    free_indicators += 1

        return fixed_indicators > free_indicators

    def _check_fixed_format_line(self, line: str, line_num: int) -> List[QualityIssue]:
        """检查固定格式行"""
        issues = []

        # 检查行长度
        if len(line) > 72:
            issues.append(QualityIssue(
                check_type=CheckType.FORMAT,
                severity="minor",
                line_number=line_num,
                description=f"固定格式行长度超过72字符: {len(line)}",
                suggestion="将长行分割为多行",
                auto_fixable=False
            ))

        # 检查续行标记位置
        if len(line) >= 6 and line[5] in ['+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if len(line) < 7 or not line[6].strip():
                issues.append(QualityIssue(
                    check_type=CheckType.FORMAT,
                    severity="major",
                    line_number=line_num,
                    description="续行标记后缺少代码内容",
                    suggestion="在第7列添加续行代码",
                    auto_fixable=False
                ))

        return issues

    def _check_free_format_line(self, line: str, line_num: int) -> List[QualityIssue]:
        """检查自由格式行"""
        issues = []

        # 检查行长度 (推荐不超过132字符)
        if len(line) > 132:
            issues.append(QualityIssue(
                check_type=CheckType.FORMAT,
                severity="minor",
                line_number=line_num,
                description=f"自由格式行长度超过推荐值132字符: {len(line)}",
                suggestion="考虑将长行分割为多行",
                auto_fixable=False
            ))

        return issues

    def check_html_format(self, content: str, file_path: str) -> List[QualityIssue]:
        """
        检查HTML格式

        Args:
            content: 文件内容
            file_path: 文件路径

        Returns:
            List[QualityIssue]: 发现的质量问题列表
        """
        issues = []

        # 检查HTML标签配对
        tag_pattern = re.compile(r'<(/?)(\w+)[^>]*>')
        open_tags = []

        for match in tag_pattern.finditer(content):
            is_closing = match.group(1) == '/'
            tag_name = match.group(2).lower()

            if is_closing:
                if open_tags and open_tags[-1] == tag_name:
                    open_tags.pop()
                else:
                    issues.append(QualityIssue(
                        check_type=CheckType.FORMAT,
                        severity="major",
                        line_number=None,
                        description=f"HTML标签不匹配: </{tag_name}>",
                        suggestion=f"检查标签配对，确保有对应的 <{tag_name}>",
                        auto_fixable=False
                    ))
            elif tag_name not in ['br', 'hr', 'img', 'meta', 'link']:
                open_tags.append(tag_name)

        # 检查未关闭的标签
        for tag in open_tags:
            issues.append(QualityIssue(
                check_type=CheckType.FORMAT,
                severity="major",
                line_number=None,
                description=f"HTML标签未关闭: <{tag}>",
                suggestion=f"在适当位置添加 </{tag}>",
                auto_fixable=False
            ))

        return issues

class ContentChecker:
    """内容完整性检查器"""

    def __init__(self):
        """初始化内容检查器"""
        self.placeholder_patterns = [
            r'\[.*?翻译.*?\]',
            r'\[.*?TODO.*?\]',
            r'\[.*?FIXME.*?\]',
            r'待翻译',
            r'TODO',
            r'FIXME'
        ]

    def check_content_completeness(self, content: str, file_path: str) -> List[QualityIssue]:
        """
        检查内容完整性

        Args:
            content: 文件内容
            file_path: 文件路径

        Returns:
            List[QualityIssue]: 发现的质量问题列表
        """
        issues = []
        lines = content.split('\n')

        # 检查未翻译内容
        for line_num, line in enumerate(lines, 1):
            line_stripped = line.strip()

            # 检查占位符
            for pattern in self.placeholder_patterns:
                matches = re.finditer(pattern, line, re.IGNORECASE)
                for match in matches:
                    issues.append(QualityIssue(
                        check_type=CheckType.CONTENT,
                        severity="critical",
                        line_number=line_num,
                        description=f"发现未翻译的占位符: {match.group()}",
                        suggestion="完成该部分的翻译工作",
                        auto_fixable=False
                    ))

            # 检查中英文混杂（技术术语除外）
            if self._has_mixed_languages(line_stripped):
                issues.append(QualityIssue(
                    check_type=CheckType.CONTENT,
                    severity="minor",
                    line_number=line_num,
                    description="行中存在中英文混杂",
                    suggestion="检查是否为合理的技术术语使用，或统一语言",
                    auto_fixable=False
                ))

        return issues

    def _has_mixed_languages(self, text: str) -> bool:
        """检查文本是否中英文混杂"""
        has_chinese = bool(re.search(r'[\u4e00-\u9fff]', text))
        has_english = bool(re.search(r'[a-zA-Z]{3,}', text))
        return has_chinese and has_english

class CompilationChecker:
    """编译兼容性检查器"""

    def __init__(self, compiler: str = "gfortran"):
        """
        初始化编译检查器

        Args:
            compiler: Fortran编译器名称
        """
        self.compiler = compiler

    def check_fortran_compilation(self, content: str, file_path: str) -> List[QualityIssue]:
        """
        检查Fortran编译兼容性

        Args:
            content: 文件内容
            file_path: 文件路径

        Returns:
            List[QualityIssue]: 发现的质量问题列表
        """
        issues = []

        # 只检查.f, .F90, .f90文件
        if not file_path.lower().endswith(('.f', '.F90', '.f90')):
            return issues

        # 创建临时文件
        temp_file_path = file_path + '.tmp'
        try:
            with open(temp_file_path, 'w', encoding='utf-8') as f:
                f.write(content)

            # 尝试编译检查语法
            result = subprocess.run(
                [self.compiler, '-fsyntax-only', temp_file_path],
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode != 0:
                issues.append(QualityIssue(
                    check_type=CheckType.COMPILATION,
                    severity="critical",
                    line_number=None,
                    description=f"编译检查失败: {result.stderr.strip()}",
                    suggestion="修复编译错误，确保语法正确",
                    auto_fixable=False
                ))

        except subprocess.TimeoutExpired:
            issues.append(QualityIssue(
                check_type=CheckType.COMPILATION,
                severity="major",
                line_number=None,
                description="编译检查超时",
                suggestion="手动检查代码语法",
                auto_fixable=False
            ))
        except FileNotFoundError:
            issues.append(QualityIssue(
                check_type=CheckType.COMPILATION,
                severity="info",
                line_number=None,
                description=f"编译器 {self.compiler} 未找到",
                suggestion="安装Fortran编译器或跳过编译检查",
                auto_fixable=False
            ))
        except Exception as e:
            issues.append(QualityIssue(
                check_type=CheckType.COMPILATION,
                severity="major",
                line_number=None,
                description=f"编译检查出错: {str(e)}",
                suggestion="手动检查代码语法",
                auto_fixable=False
            ))
        finally:
            # 清理临时文件
            if os.path.exists(temp_file_path):
                os.remove(temp_file_path)

        return issues

class QualityControlPipeline:
    """质量检查流水线"""

    def __init__(self, config_path: str = None):
        """
        初始化质量检查流水线

        Args:
            config_path: 配置文件路径
        """
        self.config = self.load_config(config_path)
        self.checkers = self.initialize_checkers()

    def load_config(self, config_path: str) -> Dict:
        """加载配置文件"""
        default_config = {
            'terminology_checker': {
                'enabled': True,
                'dictionary_path': '.claude/terminology-dictionary.md'
            },
            'format_checker': {
                'enabled': True,
                'check_fortran': True,
                'check_html': True
            },
            'content_checker': {
                'enabled': True
            },
            'compilation_checker': {
                'enabled': True,
                'compiler': 'gfortran'
            },
            'scoring_weights': {
                'terminology': 0.3,
                'format': 0.25,
                'content': 0.3,
                'compilation': 0.15
            }
        }

        if config_path and os.path.exists(config_path):
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    user_config = yaml.safe_load(f)
                default_config.update(user_config)
            except Exception as e:
                logger.warning(f"加载配置文件失败: {e}，使用默认配置")

        return default_config

    def initialize_checkers(self) -> Dict[str, Any]:
        """初始化检查器"""
        checkers = {}

        if self.config['terminology_checker']['enabled']:
            dict_path = self.config['terminology_checker']['dictionary_path']
            checkers['terminology'] = TerminologyChecker(dict_path)

        if self.config['format_checker']['enabled']:
            checkers['format'] = FormatChecker()

        if self.config['content_checker']['enabled']:
            checkers['content'] = ContentChecker()

        if self.config['compilation_checker']['enabled']:
            compiler = self.config['compilation_checker']['compiler']
            checkers['compilation'] = CompilationChecker(compiler)

        return checkers

    def check_file(self, file_path: str) -> QualityReport:
        """
        检查单个文件

        Args:
            file_path: 文件路径

        Returns:
            QualityReport: 质量报告
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            logger.error(f"读取文件失败 {file_path}: {e}")
            return self._create_error_report(file_path, str(e))

        all_issues = []
        check_results = {}

        # 执行各项检查
        if 'terminology' in self.checkers:
            issues = self.checkers['terminology'].check_terminology_consistency(content, file_path)
            all_issues.extend(issues)
            check_results['terminology'] = len(issues)

        if 'format' in self.checkers:
            if file_path.lower().endswith(('.f', '.F90', '.f90')):
                issues = self.checkers['format'].check_fortran_format(content, file_path)
            elif file_path.lower().endswith(('.html', '.htm')):
                issues = self.checkers['format'].check_html_format(content, file_path)
            else:
                issues = []
            all_issues.extend(issues)
            check_results['format'] = len(issues)

        if 'content' in self.checkers:
            issues = self.checkers['content'].check_content_completeness(content, file_path)
            all_issues.extend(issues)
            check_results['content'] = len(issues)

        if 'compilation' in self.checkers:
            issues = self.checkers['compilation'].check_fortran_compilation(content, file_path)
            all_issues.extend(issues)
            check_results['compilation'] = len(issues)

        # 计算质量分数
        overall_score = self._calculate_quality_score(check_results)
        quality_level = self._determine_quality_level(overall_score)

        # 生成建议
        recommendations = self._generate_recommendations(all_issues)

        # 生成摘要
        summary = self._generate_summary(all_issues, overall_score, quality_level)

        return QualityReport(
            file_path=file_path,
            overall_score=overall_score,
            quality_level=quality_level,
            issues=all_issues,
            metrics=check_results,
            summary=summary,
            recommendations=recommendations
        )

    def _calculate_quality_score(self, check_results: Dict[str, int]) -> float:
        """计算质量分数"""
        weights = self.config['scoring_weights']
        total_score = 100.0

        for check_type, issue_count in check_results.items():
            if check_type in weights:
                weight = weights[check_type]
                # 根据问题数量扣分
                deduction = min(issue_count * weight * 10, weight * 100)
                total_score -= deduction

        return max(0.0, total_score)

    def _determine_quality_level(self, score: float) -> QualityLevel:
        """确定质量等级"""
        if score >= 90:
            return QualityLevel.EXCELLENT
        elif score >= 80:
            return QualityLevel.GOOD
        elif score >= 70:
            return QualityLevel.ACCEPTABLE
        elif score >= 60:
            return QualityLevel.NEEDS_IMPROVEMENT
        else:
            return QualityLevel.POOR

    def _generate_recommendations(self, issues: List[QualityIssue]) -> List[str]:
        """生成改进建议"""
        recommendations = []

        # 按检查类型统计问题
        issue_counts = {}
        for issue in issues:
            check_type = issue.check_type.value
            if check_type not in issue_counts:
                issue_counts[check_type] = 0
            issue_counts[check_type] += 1

        # 生成针对性建议
        if 'terminology' in issue_counts:
            recommendations.append(f"术语一致性问题 ({issue_counts['terminology']}个): 严格遵循术语词典，确保术语使用统一")

        if 'format' in issue_counts:
            recommendations.append(f"格式问题 ({issue_counts['format']}个): 检查并修正格式错误，确保编译兼容性")

        if 'content' in issue_counts:
            recommendations.append(f"内容完整性问题 ({issue_counts['content']}个): 完成所有未翻译的占位符内容")

        if 'compilation' in issue_counts:
            recommendations.append(f"编译问题 ({issue_counts['compilation']}个): 修复编译错误，确保代码可以正常编译")

        return recommendations

    def _generate_summary(self, issues: List[QualityIssue], score: float, level: QualityLevel) -> str:
        """生成质量摘要"""
        critical_count = sum(1 for issue in issues if issue.severity == 'critical')
        major_count = sum(1 for issue in issues if issue.severity == 'major')
        minor_count = sum(1 for issue in issues if issue.severity == 'minor')

        summary = f"质量评分: {score:.1f}/100 ({level.value})\n"
        summary += f"问题总数: {len(issues)} (严重: {critical_count}, 主要: {major_count}, 次要: {minor_count})"

        return summary

    def _create_error_report(self, file_path: str, error_message: str) -> QualityReport:
        """创建错误报告"""
        return QualityReport(
            file_path=file_path,
            overall_score=0.0,
            quality_level=QualityLevel.POOR,
            issues=[QualityIssue(
                check_type=CheckType.CONTENT,
                severity="critical",
                line_number=None,
                description=f"文件处理错误: {error_message}",
                suggestion="检查文件路径和权限",
                auto_fixable=False
            )],
            metrics={},
            summary=f"文件处理失败: {error_message}",
            recommendations=["检查文件是否存在和可读", "确认文件编码格式正确"]
        )

    def check_directory(self, directory: str, pattern: str = "*") -> List[QualityReport]:
        """
        检查目录中的文件

        Args:
            directory: 目录路径
            pattern: 文件匹配模式

        Returns:
            List[QualityReport]: 质量报告列表
        """
        reports = []
        directory_path = Path(directory)

        if not directory_path.exists():
            logger.error(f"目录不存在: {directory}")
            return reports

        # 查找匹配的文件
        for file_path in directory_path.glob(pattern):
            if file_path.is_file():
                logger.info(f"检查文件: {file_path}")
                report = self.check_file(str(file_path))
                reports.append(report)

        return reports

    def generate_summary_report(self, reports: List[QualityReport]) -> Dict[str, Any]:
        """生成汇总报告"""
        if not reports:
            return {"error": "没有可汇总的报告"}

        total_files = len(reports)
        total_issues = sum(len(report.issues) for report in reports)
        average_score = sum(report.overall_score for report in reports) / total_files

        # 按质量等级统计
        level_counts = {}
        for level in QualityLevel:
            level_counts[level.value] = sum(1 for report in reports if report.quality_level == level)

        # 按问题类型统计
        issue_type_counts = {}
        for report in reports:
            for issue in report.issues:
                issue_type = issue.check_type.value
                if issue_type not in issue_type_counts:
                    issue_type_counts[issue_type] = 0
                issue_type_counts[issue_type] += 1

        return {
            'summary': {
                'total_files': total_files,
                'total_issues': total_issues,
                'average_score': average_score,
                'quality_distribution': level_counts
            },
            'issue_breakdown': issue_type_counts,
            'recommendations': self._generate_overall_recommendations(reports)
        }

    def _generate_overall_recommendations(self, reports: List[QualityReport]) -> List[str]:
        """生成整体改进建议"""
        recommendations = []

        # 统计最常见的问题类型
        all_issues = []
        for report in reports:
            all_issues.extend(report.issues)

        issue_types = {}
        for issue in all_issues:
            issue_type = issue.check_type.value
            if issue_type not in issue_types:
                issue_types[issue_type] = 0
            issue_types[issue_type] += 1

        # 按问题数量排序
        sorted_types = sorted(issue_types.items(), key=lambda x: x[1], reverse=True)

        for issue_type, count in sorted_types[:3]:  # 取前3个最常见问题
            if issue_type == 'terminology':
                recommendations.append("优先解决术语一致性问题：建立术语使用规范，加强翻译过程中的术语检查")
            elif issue_type == 'format':
                recommendations.append("重点修复格式问题：严格执行格式检查，确保编译兼容性")
            elif issue_type == 'content':
                recommendations.append("完善内容完整性：检查并完成所有未翻译的占位符内容")
            elif issue_type == 'compilation':
                recommendations.append("解决编译问题：逐个修复编译错误，确保代码质量")

        return recommendations

def main():
    """主函数，用于测试"""
    # 创建质量检查流水线
    pipeline = QualityControlPipeline()

    # 示例：检查单个文件
    test_content = """C     这是一个测试Fortran程序
C     用于演示质量检查功能
      PROGRAM TEST_PROGRAM
      IMPLICIT NONE
      INTEGER :: I  ! 这是一个计数器变量
C     主循环
      DO I = 1, 10
         PRINT *, 'Value:', I  ! 输出当前值
      END DO
      END PROGRAM TEST_PROGRAM
"""

    # 创建临时测试文件
    test_file = "test_quality.f"
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write(test_content)

    try:
        # 执行质量检查
        report = pipeline.check_file(test_file)

        print("质量检查报告:")
        print(f"文件: {report.file_path}")
        print(f"总分: {report.overall_score:.1f}/100 ({report.quality_level.value})")
        print(f"摘要: {report.summary}")
        print(f"\n发现 {len(report.issues)} 个问题:")

        for issue in report.issues:
            print(f"  [{issue.severity.upper()}] {issue.description}")
            if issue.suggestion:
                print(f"    建议: {issue.suggestion}")

        print(f"\n改进建议:")
        for rec in report.recommendations:
            print(f"  - {rec}")

    finally:
        # 清理测试文件
        if os.path.exists(test_file):
            os.remove(test_file)

if __name__ == "__main__":
    main()