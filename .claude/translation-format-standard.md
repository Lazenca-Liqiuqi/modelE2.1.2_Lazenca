# ModelE2.1.2_Lazenca 翻译格式标准

## 🎯 翻译原则

### 1. 中英对照叠放模式
- **原文在上**: 保持英文原文不变
- **译文在下**: 中文翻译紧接原文
- **段落对应**: 一个原文段落对应一个译文段落
- **格式保持**: 完全保留原文档格式结构

### 2. 文档类型分类处理

#### 📄 HTML文档（UserGuide/ModelDescription）
```html
<!-- 原文段落 -->
<p>Original English paragraph content here.</p>
<!-- 译文段落 -->
<p>【中文翻译】对应的中文翻译内容。</p>

<!-- 标题处理 -->
<h2>Original Title</h2>
<h2>【中文翻译】原标题</h2>

<!-- 代码块保持不变 -->
<pre><code>Original Code</code></pre>
```

#### 💻 Fortran源代码注释
```fortran
! Original English comment
!【中文翻译】对应的中文注释说明
```

#### 🔧 脚本文件注释
```bash
# Original English comment
#【中文翻译】对应的中文注释说明
```

## 📋 具体格式规范

### 1. HTML文档格式
- **段落级对照**: 每个p标签都添加中文版本
- **标题处理**: h1-h6标题全部翻译
- **列表处理**: li项目添加中文翻译
- **表格内容**: th和td内容翻译
- **代码保留**: code和pre标签内容保持英文

### 2. Fortran代码注释格式
- **行注释**: 在每行注释后添加中文翻译
- **块注释**: 保持注释块结构，添加中文版本
- **函数头注释**: 确保参数说明完整翻译
- **重要算法注释**: 重点翻译算法逻辑说明

### 3. 标记规范
- **翻译标记**: 使用【中文翻译】标识翻译开始
- **保留标记**: 原文标记全部保留
- **空行处理**: 保持原文档空行结构
- **缩进保持**: 完全保持原文档缩进格式

## 🔍 质量控制标准

### 1. 术语一致性
- 使用统一的术语词典
- 相同概念使用相同翻译
- 新术语需要记录并审核

### 2. 技术准确性
- 专业概念翻译准确
- 数值和单位保持不变
- 技术参数保留原文

### 3. 可读性要求
- 中文表达自然流畅
- 避免直译生硬表达
- 保持技术文档的专业性

### 4. 格式完整性
- 所有格式标记正确
- 超链接保持有效
- 图片说明完整翻译

## 📝 示例格式

### HTML文档示例
```html
<div class="section">
  <h2>Model Configuration</h2>
  <h2>【中文翻译】模型配置</h2>

  <p>The model configuration is specified in the rundeck file.</p>
  <p>【中文翻译】模型配置在rundeck文件中指定。</p>

  <ul>
    <li>Grid resolution: 2°×2.5°</li>
    <li>【中文翻译】网格分辨率：2°×2.5°</li>
    <li>Time step: 30 minutes</li>
    <li>【中文翻译】时间步长：30分钟</li>
  </ul>
</div>
```

### Fortran代码示例
```fortran
C***********************************************************************
      SUBROUTINE ATM_DRV (Itime,DT)
C
C     Driver for atmospheric model calculations
C     【中文翻译】大气模型计算驱动程序
C
C     Input:   Itime  - current time step
C              DT     - time step length (hours)
C     【中文翻译】输入:   Itime  - 当前时间步
C              DT     - 时间步长（小时）
C
      IMPLICIT NONE
      INTEGER Itime
      REAL*8 DT
C
C     Initialize atmospheric variables
C     【中文翻译】初始化大气变量
      CALL INIT_ATM ()
```

## 🛠️ 工具支持

### 1. 自动化检查
- 格式验证脚本
- 术语一致性检查
- 链接有效性验证

### 2. 质量评估
- 翻译完整性检查
- 格式正确性验证
- 专业术语审核

### 3. 版本控制
- 翻译进度追踪
- 变更历史记录
- 协作工作流程

---
*版本: v1.0*
*制定时间: 2025-10-28*
*适用范围: ModelE2.1.2_Lazenca全项目翻译*