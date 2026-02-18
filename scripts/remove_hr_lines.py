#!/usr/bin/env python3
"""
去除Markdown文档中多余的分割线（---）
Remove unnecessary horizontal rules (---) from Markdown documents
"""

import re
import os

# 要处理的文件列表（不包含archive-old-doc归档文件）
FILES_TO_PROCESS = [
    "doc/README.md",
    "doc/HOWTO/git_howto.md",
    "doc/HOWTO/newio.md",
    "doc/HOWTO/SCM.md",
    "doc/HOWTO/time_management.md",
    "doc/misc/CHANGES.md",
    "doc/misc/rundeck.md",
    "doc/ModelDescription/Ground_Hydrology.md",
]

def remove_hr_lines(content: str) -> str:
    """
    去除独立成行的分割线（---）
    保留代码块内的内容
    """
    lines = content.split('\n')
    result = []
    in_code_block = False

    for line in lines:
        # 检测代码块开始/结束
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            continue

        # 在代码块内，保留所有内容
        if in_code_block:
            result.append(line)
            continue

        # 检测并去除分割线（独立成行的 ---）
        if re.match(r'^-{3,}\s*$', line):
            continue  # 跳过分割线

        result.append(line)

    return '\n'.join(result)


def main():
    # 获取项目根目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    total_removed = 0

    for rel_path in FILES_TO_PROCESS:
        file_path = os.path.join(project_root, rel_path)

        if not os.path.exists(file_path):
            print(f"[SKIP] File not found: {rel_path}")
            continue

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 统计原始分割线数量
        original_count = len(re.findall(r'^-{3,}\s*$', content, re.MULTILINE))

        # 去除分割线
        new_content = remove_hr_lines(content)

        # 统计新分割线数量
        new_count = len(re.findall(r'^-{3,}\s*$', new_content, re.MULTILINE))
        removed = original_count - new_count

        if removed > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"[OK] {rel_path}: removed {removed} hr lines")
            total_removed += removed
        else:
            print(f"[SKIP] {rel_path}: no hr lines found")

    print(f"\nTotal removed: {total_removed} horizontal rule lines")


if __name__ == '__main__':
    main()
