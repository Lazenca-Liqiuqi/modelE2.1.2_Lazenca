#!/usr/bin/env python3
"""
ModelE2.1.2_Lazenca Fortran注释格式保持算法
Fortran Comment Format Preservation Algorithm for ModelE2.1.2_Lazenca

这个模块提供Fortran代码注释翻译时的格式保持功能，确保翻译后的注释格式完全兼容Fortran语法。
This module provides format preservation functionality for Fortran code comment translation, ensuring complete compatibility with Fortran syntax after translation.

作者 | Author: ModelE2.1.2_Lazenca翻译团队
版本 | Version: v1.0
创建日期 | Created: 2025-10-28
"""

import re
import logging
from typing import Dict, List, Tuple, Optional, Union
from dataclasses import dataclass
from enum import Enum

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FortranFormatType(Enum):
    """Fortran格式类型枚举"""
    FIXED_FORMAT = "fixed"      # 固定格式 (传统Fortran)
    FREE_FORMAT = "free"        # 自由格式 (现代Fortran)
    UNKNOWN = "unknown"         # 未知格式

@dataclass
class FortranLine:
    """Fortran代码行数据结构"""
    original: str               # 原始行内容
    line_number: int           # 行号
    format_type: FortranFormatType  # 格式类型
    is_comment: bool           # 是否为注释行
    is_continuation: bool      # 是否为续行
    comment_start: int         # 注释开始位置
    code_part: str             # 代码部分
    comment_part: str          # 注释部分
    indentation: str           # 缩进
    prefix: str               # 行前缀 (C, c, *, !等)
    continuation_marker: str  # 续行标记

class FortranCommentPreserver:
    """Fortran注释格式保持器"""

    def __init__(self):
        """初始化格式保持器"""
        # 固定格式规则
        self.fixed_format_rules = {
            'comment_prefixes': ['C', 'c', '*'],      # 注释行前缀
            'continuation_chars': ['+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
            'code_start_column': 7,                   # 代码开始列
            'comment_column': 73,                     # 注释区开始列
            'line_length': 72,                        # 行长度限制
            'continuation_column': 6                  # 续行列
        }

        # 自由格式规则
        self.free_format_rules = {
            'comment_prefix': '!',                    # 注释前缀
            'line_length': 132,                       # 行长度限制
            'continuation_char': '&'                  # 续行字符
        }

        # 编译指令
        self.compiler_directives = [
            'IFDEF', 'IFNDEF', 'DEFINE', 'UNDEF', 'ELSE', 'ENDIF', 'INCLUDE'
        ]

        # 预处理指令
        self.preprocessor_directives = [
            '#define', '#undef', '#ifdef', '#ifndef', '#else', '#endif', '#include'
        ]

    def detect_format_type(self, lines: List[str]) -> FortranFormatType:
        """
        检测Fortran代码的格式类型

        Args:
            lines: 代码行列表

        Returns:
            FortranFormatType: 检测到的格式类型
        """
        fixed_indicators = 0
        free_indicators = 0

        for line in lines[:100]:  # 检查前100行
            line = line.rstrip('\n\r')

            # 跳过空行
            if not line.strip():
                continue

            # 检查固定格式指示符
            if len(line) >= 6:
                # 第6列有续行标记
                if line[5] in self.fixed_format_rules['continuation_chars']:
                    fixed_indicators += 1
                # 第1列有注释标记
                if line[0] in self.fixed_format_rules['comment_prefixes']:
                    fixed_indicators += 1
                # 第7列前有内容，但不是注释
                if len(line) > 6 and line[:6].strip() and line[6].strip():
                    if line[0] not in self.fixed_format_rules['comment_prefixes']:
                        fixed_indicators += 1

            # 检查自由格式指示符
            if '!' in line:
                # 检查是否是自由格式注释
                comment_pos = line.find('!')
                if comment_pos > 0:  # 不是行首的!
                    free_indicators += 1
            # 检查现代Fortran特性
            if any(keyword in line.upper() for keyword in ['MODULE ', 'USE ', 'CONTAINS', 'END FUNCTION']):
                free_indicators += 2

        # 判断格式类型
        if fixed_indicators > free_indicators * 1.5:
            return FortranFormatType.FIXED_FORMAT
        elif free_indicators > fixed_indicators * 1.5:
            return FortranFormatType.FREE_FORMAT
        else:
            logger.warning(f"无法明确检测Fortran格式类型 (fixed: {fixed_indicators}, free: {free_indicators})")
            return FortranFormatType.UNKNOWN

    def parse_fortran_line(self, line: str, line_number: int, format_type: FortranFormatType) -> FortranLine:
        """
        解析Fortran代码行

        Args:
            line: 代码行
            line_number: 行号
            format_type: 格式类型

        Returns:
            FortranLine: 解析后的行对象
        """
        original_line = line.rstrip('\n\r')

        if format_type == FortranFormatType.FIXED_FORMAT:
            return self._parse_fixed_format_line(original_line, line_number)
        elif format_type == FortranFormatType.FREE_FORMAT:
            return self._parse_free_format_line(original_line, line_number)
        else:
            # 尝试两种格式解析
            try:
                return self._parse_fixed_format_line(original_line, line_number)
            except:
                return self._parse_free_format_line(original_line, line_number)

    def _parse_fixed_format_line(self, line: str, line_number: int) -> FortranLine:
        """解析固定格式Fortran行"""
        is_comment = False
        is_continuation = False
        prefix = ''
        continuation_marker = ''
        comment_start = -1
        code_part = ''
        comment_part = ''
        indentation = ''

        # 检查是否为注释行
        if line and line[0] in self.fixed_format_rules['comment_prefixes']:
            is_comment = True
            prefix = line[0]
            code_part = ''
            comment_part = line[1:] if len(line) > 1 else ''
            comment_start = 0
        else:
            # 检查续行标记
            if len(line) >= 6 and line[5] in self.fixed_format_rules['continuation_chars']:
                is_continuation = True
                continuation_marker = line[5]

            # 提取代码部分 (第7-72列)
            code_start = self.fixed_format_rules['code_start_column'] - 1
            comment_col = self.fixed_format_rules['comment_column'] - 1

            if len(line) > code_start:
                if len(line) <= comment_col:
                    code_part = line[code_start:]
                else:
                    code_part = line[code_start:comment_col]
                    # 检查是否有注释
                    if len(line) > comment_col and line[comment_col:].strip():
                        comment_part = line[comment_col:]
                        comment_start = comment_col

            # 提取缩进 (前6列)
            if len(line) >= 6:
                indentation = line[:6]

        return FortranLine(
            original=line,
            line_number=line_number,
            format_type=FortranFormatType.FIXED_FORMAT,
            is_comment=is_comment,
            is_continuation=is_continuation,
            comment_start=comment_start,
            code_part=code_part,
            comment_part=comment_part,
            indentation=indentation,
            prefix=prefix,
            continuation_marker=continuation_marker
        )

    def _parse_free_format_line(self, line: str, line_number: int) -> FortranLine:
        """解析自由格式Fortran行"""
        is_comment = False
        is_continuation = False
        comment_start = -1
        code_part = ''
        comment_part = ''
        indentation = ''
        prefix = ''
        continuation_marker = ''

        stripped_line = line.lstrip()
        if stripped_line.startswith('!'):
            # 整行都是注释
            is_comment = True
            prefix = '!'
            comment_part = stripped_line[1:]
            comment_start = len(line) - len(stripped_line)
        else:
            # 查找行内注释
            comment_pos = line.find('!')
            if comment_pos >= 0:
                comment_start = comment_pos
                code_part = line[:comment_pos]
                comment_part = line[comment_pos + 1:]
            else:
                code_part = line

            # 提取缩进
            indentation = line[:len(line) - len(stripped_line)]

            # 检查续行标记
            if code_part.rstrip().endswith('&'):
                is_continuation = True
                continuation_marker = '&'

        return FortranLine(
            original=line,
            line_number=line_number,
            format_type=FortranFormatType.FREE_FORMAT,
            is_comment=is_comment,
            is_continuation=is_continuation,
            comment_start=comment_start,
            code_part=code_part,
            comment_part=comment_part,
            indentation=indentation,
            prefix=prefix,
            continuation_marker=continuation_marker
        )

    def translate_comment_part(self, fortran_line: FortranLine, translated_comment: str) -> str:
        """
        翻译注释部分并保持格式

        Args:
            fortran_line: 原始Fortran行对象
            translated_comment: 翻译后的注释内容

        Returns:
            str: 保持格式的翻译后行
        """
        if fortran_line.format_type == FortranFormatType.FIXED_FORMAT:
            return self._reconstruct_fixed_format_line(fortran_line, translated_comment)
        elif fortran_line.format_type == FortranFormatType.FREE_FORMAT:
            return self._reconstruct_free_format_line(fortran_line, translated_comment)
        else:
            # 未知格式，使用自由格式处理
            return self._reconstruct_free_format_line(fortran_line, translated_comment)

    def _reconstruct_fixed_format_line(self, fortran_line: FortranLine, translated_comment: str) -> str:
        """重构固定格式行"""
        if fortran_line.is_comment:
            # 整行注释
            reconstructed = fortran_line.prefix + translated_comment
        else:
            # 代码行可能有注释
            reconstructed_parts = []

            # 前缀/缩进部分 (前6列)
            prefix_part = fortran_line.indentation.ljust(6)
            if fortran_line.is_continuation and fortran_line.continuation_marker:
                prefix_part = prefix_part[:5] + fortran_line.continuation_marker
            reconstructed_parts.append(prefix_part)

            # 代码部分
            if fortran_line.code_part:
                reconstructed_parts.append(fortran_line.code_part)

            # 注释部分
            if translated_comment.strip():
                comment_start = self.fixed_format_rules['comment_column'] - 1
                current_length = len(''.join(reconstructed_parts))

                if current_length < comment_start:
                    # 填充空格到注释列
                    padding = ' ' * (comment_start - current_length)
                    reconstructed_parts.append(padding)
                    reconstructed_parts.append(translated_comment)
                else:
                    # 如果代码太长，在代码后直接加注释
                    reconstructed_parts.append(' ' + translated_comment)

            reconstructed = ''.join(reconstructed_parts)

        # 确保行长度不超过限制
        max_length = self.fixed_format_rules['line_length']
        if len(reconstructed) > max_length:
            logger.warning(f"行 {fortran_line.line_number} 超过长度限制 ({len(reconstructed)} > {max_length})")
            if fortran_line.is_comment:
                # 注释行可以截断，并在下一行继续
                reconstructed = reconstructed[:max_length]
            else:
                # 代码行保持原样，但记录警告
                reconstructed = reconstructed  # 保持代码完整性

        return reconstructed

    def _reconstruct_free_format_line(self, fortran_line: FortranLine, translated_comment: str) -> str:
        """重构自由格式行"""
        if fortran_line.is_comment:
            # 整行注释
            reconstructed = fortran_line.indentation + fortran_line.prefix + translated_comment
        else:
            # 代码行可能有注释
            reconstructed_parts = []

            # 缩进和代码部分
            reconstructed_parts.append(fortran_line.indentation)
            if fortran_line.code_part:
                reconstructed_parts.append(fortran_line.code_part)

            # 注释部分
            if translated_comment.strip():
                reconstructed_parts.append('!' + translated_comment)

            # 续行标记
            if fortran_line.is_continuation and fortran_line.continuation_marker:
                if not reconstructed_parts[-1].endswith('&'):
                    reconstructed_parts.append(' &')

            reconstructed = ''.join(reconstructed_parts)

        # 检查行长度限制
        max_length = self.free_format_rules['line_length']
        if len(reconstructed) > max_length:
            logger.warning(f"行 {fortran_line.line_number} 超过推荐长度 ({len(reconstructed)} > {max_length})")

        return reconstructed

    def process_fortran_file(self, content: str, translation_func) -> str:
        """
        处理完整的Fortran文件

        Args:
            content: 原始文件内容
            translation_func: 翻译函数，接收注释文本，返回翻译结果

        Returns:
            str: 处理后的文件内容
        """
        lines = content.splitlines(keepends=True)

        # 检测格式类型
        format_type = self.detect_format_type(lines)
        logger.info(f"检测到Fortran格式类型: {format_type.value}")

        # 解析每一行
        parsed_lines = []
        for i, line in enumerate(lines):
            parsed_line = self.parse_fortran_line(line, i + 1, format_type)
            parsed_lines.append(parsed_line)

        # 翻译注释
        result_lines = []
        for parsed_line in parsed_lines:
            if parsed_line.comment_part.strip():
                try:
                    # 调用翻译函数
                    translated_comment = translation_func(parsed_line.comment_part.strip())
                    if translated_comment:
                        translated_comment = translated_comment.strip()
                    else:
                        translated_comment = parsed_line.comment_part.strip()
                        logger.warning(f"行 {parsed_line.line_number} 翻译失败，保持原文")
                except Exception as e:
                    logger.error(f"行 {parsed_line.line_number} 翻译出错: {e}")
                    translated_comment = parsed_line.comment_part.strip()

                # 重构行
                reconstructed_line = self.translate_comment_part(parsed_line, translated_comment)
                result_lines.append(reconstructed_line)
            else:
                # 没有注释的行保持原样
                result_lines.append(parsed_line.original)

        return '\n'.join(result_lines)

    def validate_format(self, content: str, original_content: str) -> Dict[str, Union[bool, List[str]]]:
        """
        验证格式保持的正确性

        Args:
            content: 处理后的内容
            original_content: 原始内容

        Returns:
            Dict: 验证结果
        """
        validation_result = {
            'is_valid': True,
            'errors': [],
            'warnings': []
        }

        original_lines = original_content.splitlines()
        processed_lines = content.splitlines()

        if len(original_lines) != len(processed_lines):
            validation_result['is_valid'] = False
            validation_result['errors'].append(
                f"行数不匹配: 原始 {len(original_lines)} 行, 处理后 {len(processed_lines)} 行"
            )

        # 检查每一行的格式
        format_type = self.detect_format_type(original_lines)

        for i, (orig_line, proc_line) in enumerate(zip(original_lines, processed_lines)):
            line_num = i + 1

            if format_type == FortranFormatType.FIXED_FORMAT:
                # 检查固定格式约束
                if len(proc_line) > self.fixed_format_rules['line_length']:
                    validation_result['warnings'].append(
                        f"行 {line_num} 超过固定格式长度限制 ({len(proc_line)} > {self.fixed_format_rules['line_length']})"
                    )

                # 检查续行标记位置
                if len(orig_line) >= 6 and orig_line[5] in self.fixed_format_rules['continuation_chars']:
                    if len(proc_line) < 6 or proc_line[5] != orig_line[5]:
                        validation_result['errors'].append(
                            f"行 {line_num} 续行标记位置或内容改变"
                        )

            elif format_type == FortranFormatType.FREE_FORMAT:
                # 检查自由格式约束
                if len(proc_line) > self.free_format_rules['line_length']:
                    validation_result['warnings'].append(
                        f"行 {line_num} 超过推荐长度 ({len(proc_line)} > {self.free_format_rules['line_length']})"
                    )

        return validation_result

def create_sample_translation_function():
    """创建示例翻译函数用于测试"""
    def sample_translate(text: str) -> str:
        """示例翻译函数，实际使用时替换为真正的翻译函数"""
        # 这里只是简单地在原文前加上"[已翻译]"作为示例
        if text.strip():
            return f"[已翻译] {text}"
        return text
    return sample_translate

def main():
    """主函数，用于测试"""
    # 创建保持器
    preserver = FortranCommentPreserver()

    # 示例Fortran代码
    sample_fortran_code = """C     这是一个示例Fortran程序
C     用于测试注释格式保持功能
      PROGRAM TEST
      IMPLICIT NONE
      INTEGER :: I, J, K  ! 循环计数器

C     主循环开始
      DO I = 1, 100
         J = I * 2       ! 计算J值
         K = J + 1       ! 计算K值
C        这里是循环内部的注释
         PRINT *, I, J, K
      END DO

      END PROGRAM TEST
"""

    print("原始代码:")
    print(sample_fortran_code)
    print("\n" + "="*60 + "\n")

    # 处理代码
    translation_func = create_sample_translation_function()
    processed_code = preserver.process_fortran_file(sample_fortran_code, translation_func)

    print("处理后代码:")
    print(processed_code)
    print("\n" + "="*60 + "\n")

    # 验证格式
    validation_result = preserver.validate_format(processed_code, sample_fortran_code)
    print("验证结果:")
    print(f"格式有效: {validation_result['is_valid']}")
    if validation_result['errors']:
        print("错误:")
        for error in validation_result['errors']:
            print(f"  - {error}")
    if validation_result['warnings']:
        print("警告:")
        for warning in validation_result['warnings']:
            print(f"  - {warning}")

if __name__ == "__main__":
    main()