# ModelE Coding Conventions / ModelE 编程规范

**Author / 作者**: Tom Clune
**Affiliation / 所属机构**: NASA Goddard Space Flight Center
**Email / 邮箱**: thomas.l.clune@nasa.gov
**Date / 日期**: January 2010

---

## Table of Contents / 目录

- [Introduction / 介绍](#introduction)
  - [Mandatory vs. Voluntary / 强制性与自愿性](#mandatory-vs-voluntary)
- [Naming conventions / 命名约定](#naming-conventions)
  - [General Guidelines / 通用指南](#general-guidelines)
    - [Communicate intention / 传达意图](#communicate-intention)
    - [Consistency, predictability, and ambiguity / 一致性、可预测性和歧义](#consistency-predictability-and-ambiguity)
    - [Generic terminology / 通用术语](#generic-terminology)
    - [Name length / 名称长度](#name-length)
  - [Specific conventions / 具体约定](#specific-conventions)
    - [Multi-word Names / 多词名称](#multi-word-names)
    - [File names / 文件名](#file-names)
    - [Derived type names / 派生类型名称](#derived-type-names)
    - [Module names / 模块名称](#module-names)
    - [Procedure names / 过程名称](#procedure-names)
    - [Variable names / 变量名称](#variable-names)
- [Fortran language constructs / Fortran语言构造](#fortran-language-constructs)
  - [Which Fortran version / Fortran版本选择](#which-fortran-version)
  - [Obsolete and discouraged features / 过时和不建议使用的特性](#obsolete-and-discouraged-features)
  - [Required and encouraged features / 必需和鼓励使用的特性](#required-and-encouraged-features)
- [Formatting conventions / 格式约定](#formatting-conventions)
  - [Free format / 自由格式](#free-format)
  - [Indentation / 缩进](#indentation)
    - [Indentation of documentation / 文档缩进](#indentation-of-documentation)
  - [Spacing / 空格](#spacing)
    - [Two word Fortran keywords / 双词Fortran关键字](#two-word-fortran-keywords)
    - [Operators / 运算符](#operators)
  - [Capitalization / 大小写](#capitalization)
- [Documentation / 文档](#documentation)
  - [Documentation of Fortran modules / Fortran模块文档](#documentation-of-fortran-modules)
  - [Documentation of Fortran procedures / Fortran过程文档](#documentation-of-fortran-procedures)
  - [Documentation of rundeck parameters / rundeck参数文档](#documentation-of-rundeck-parameters)
- [Miscellaneous / 杂项](#miscellaneous)
  - [Free format templates / 自由格式模板](#free-format-templates)
  - [Emacs settings / Emacs设置](#emacs-settings)

---

<a id="introduction"></a>
## Introduction / 介绍

This document establishes certain common coding conventions within `ModelE` software.
本文确立了`ModelE`软件中的某些通用编程约定。

With the overarching goal of improving science productivity, these coding conventions are intended to:
以提升科学生产力为总体目标，这些编程约定旨在：

- reduce common causes of bugs and/or inscrutible software,
  减少常见错误和/或难以理解的软件的成因，
- improve overall software quality,
  提高整体软件质量，
- reduce differences in coding styles that limit legibility, and
  减少限制可读性的编码风格差异，并
- enable the use of automatic sofware development tools (e.g. Photran).
  支持使用自动软件开发工具（如Photran）。

Documents analogous to this are an increasingly common practice among commercial software development organizations and are widely believed to improve productivity through a number of direct and indirect impacts.
类似文档在商业软件开发组织中越来越常见，并被普遍认为通过多种直接和间接影响提高生产力。

No doubt the balance of these drivers are somewhat different in research organizations, and the set of conventions below are intended to be a compromise among conflicting ideals of best practices, existing coding conventions, and other unique requirements of `ModelE`.
毫无疑问，这些驱动因素在研究组织中的平衡略有不同，以下约定旨在最佳实践、现有编码约定和`ModelE`的其他独特要求之间取得折衷。

Where possible, each requirement and/or recommendation is provided with rationale in the hopes of providing a compelling motivation.
在可能的情况下，每个要求和/或建议都提供了基本原理，以提供令人信服的动机。

The conventions in this document will be periodically reviewed, updated, and extended to ensure maximum benefit.
本文档中的约定将定期审查、更新和扩展，以确保最大效益。

<a id="mandatory-vs-voluntary"></a>
### Mandatory vs. Voluntary / 强制性与自愿性

For the most part the establishment of these conventions these conventions is *not intended to be disruptive* to ongoing work, but rather to guide a gradual transformation as the community becomes more comfortable with the various elements.
在很大程度上，建立这些约定并不旨在干扰正在进行的工作，而是在社区更加熟悉各种元素时引导渐进式转变。

In that spirit, please note that *most* conventions in this document are *not* considered to be mandatory for `ModelE` developers.
本着这种精神，请注意，本文档中的*大多数*约定对`ModelE`开发者来说不是强制性的。

Developers who find themselves uncomfortable with any items should continue with their existing coding style and/or discuss their concerns with any member of the core software engineering team.
对任何项目感到不适的开发者应继续使用其现有的编码风格，或与核心软件工程团队的任何成员讨论他们的关切。

---

<a id="naming-conventions"></a>
## Naming conventions / 命名约定

Named software entities (variables, procedures, etc) are perhaps the most important mechanism by which one communicates and understands the intent an implementation.
命名软件实体（变量、过程等）可能是传达和理解实现意图的最重要机制。

The choice of a good name can be challenging in many instances, but is also often a rewarding opportunity for creativity.
在许多情况下，选择一个好的名称可能具有挑战性，但也常常是一个富有创意的机会。

<a id="general-guidelines"></a>
### General Guidelines / 通用指南

Explicit absolute naming rules would be difficult to produce and most likely counter-productive in practice.
明确的绝对命名规则很难制定，在实践中很可能适得其反。

Instead `ModelE` developers should focus on general principles for good names and use their own experience and judgment in the final selection.
相反，`ModelE`开发者应专注于好名称的一般原则，并在最终选择时使用他们自己的经验和判断。

The importance of name selection generally increases with the scope for an entity.
名称选择的重要性通常随实体范围的增大而增加。

Thus, names for input parameters are the most critical followed by names for public module variables, subroutines, and functions.
因此，输入参数的名称最关键，其次是公共模块变量、子例程和函数的名称。

Next lower in priority would be names of dummy arguments.
优先级再低一些是虚拟参数的名称。

And lowest in priority would be names of local variables and private module variables.
优先级最低的是局部变量和私有模块变量的名称。

Names that are used more frequently are worth greater investment than names that are used very infrequently.
更频繁使用的名称值得投入更多精力，而不常使用的名称则投入较少。

<a id="communicate-intention"></a>
#### Communicate intention / 传达意图

Good names should communicate the intention of a given software entity unambiguously to other developers.
好的名称应该向其他开发者明确传达给定软件实体的意图。

The name should give a useful indication of the role that the entity serves in the software using terminology that is understandable by other developers.
该名称应使用其他开发者可理解的术语，为实体在软件中的作用提供有用的指示。

Generally this guideline implies a preference for full English words and phrases, with the understanding that numerous caveats and exceptions exist.
一般来说，本指南倾向于使用完整的英语单词和短语，但存在许多注意事项和例外。

As an example consider the choice for naming a variable which contains the heat flux at the bottom of a grid-cell.
例如，考虑为包含网格单元底部热通量的变量命名。

The variable names `f` or `Q` are common in this situation, but within a large routine do not generally provide much insight to other developers.
变量名`f`或`Q`在这种情况下很常见，但在大型例程中通常不会为其他开发者提供太多见解。

The name `flux` is better, but still lacks a certain degree of specificity.
名称`flux`更好，但仍缺乏一定的特异性。

The name `heatFlux` or `heatFluxQ` or `lowerFlux` are better and depending on context might be sufficient.
名称`heatFlux`或`heatFluxQ`或`lowerFlux`更好，并且根据上下文可能就足够了。

In a large routine with multiple types of fluxes at various boundaries, a better name would be `lowerHeatFlux` or `heatFluxAtBottom`.
在具有各种边界多种通量类型的大型例程中，更好的名称是`lowerHeatFlux`或`heatFluxAtBottom`。

Perhaps the worst offense against the guideline here would be reusing a variable with a perfectly fine name for a second very different purpose.
对此指南最严重的违反可能是将一个具有完美名称的变量重用于第二个非常不同的目的。

E.g. reusing `heatFlux` at a later point to represent something like the total mass.
例如，在后面重用`heatFlux`来表示总质量之类的东西。

<a id="consistency-predictability-and-ambiguity"></a>
#### Consistency, predictability, and ambiguity / 一致性、可预测性和歧义

Developers should not need to unnecessarily spend time determining the correct spelling of a given name.
开发者不应不必要地花费时间确定给定名称的正确拼写。

Abbreviations of long words are perfectly natural so long as they are *consistently applied and predictable*.
长单词的缩写是很自然的，只要它们*一致应用且可预测*。

When multiple abbreviations or alternate spellings (or even misspellings!) are in common use, developers *must* frequently check other pieces of code to ensure they are using the correct spelling.
当多种缩写或替代拼写（甚至拼写错误！）普遍使用时，开发者*必须*经常检查其他代码片段以确保他们使用正确的拼写。

For example the name `trop` is probably poor for indicating a tropospheric quantity if `tropo` and `troposph` are also used.
例如，如果同时使用`tropo`和`troposph`，那么名称`trop``对于表示对流层量可能不太合适。

At some point in the future, a table of abbreviations will be added to this document.
在将来的某个时候，本文档将添加缩写表。

> **📘 Encouraged / 鼓励**
>
> Avoid abbreviations in names unless consistent throughout `ModelE`.
> 除非在`ModelE`中保持一致，否则避免在名称中使用缩写。

> **📘 Encouraged / 鼓励**
>
> Use correct spelling. Where English and American spellings differ, the American spelling should be preferred.
> 使用正确的拼写。当英语和美式拼写不同时，应优先使用美式拼写。

<a id="generic-terminology"></a>
#### Generic terminology / 通用术语

Although very tempting, certain common words are too generic to confer any useful information to other developers and are generally poor candidates for parts of a variable name.
虽然很诱人，但某些常用词过于通用，无法向其他开发者传达任何有用信息，通常不适合作为变量名的一部分。

Examples of such bland terms include:
此类平淡术语的示例包括：

- variable
  变量
- parameter
  参数
- buffer
  缓冲区
- string
  字符串
- array
  数组
- table
  表格

When tempted to use such terms in a name, consider other aspects of the functionality to come up with alternatives.
当想要在名称中使用此类术语时，请考虑功能的其他方面以提出替代方案。

> **📘 Encouraged / 鼓励**
>
> Avoid bland or generic terms in names of variables.
> 避免在变量名中使用平淡或通用的术语。

<a id="name-length"></a>
#### Name length / 名称长度

The guidelines given above generally drive selection toward longer names which convey more information.
上面给出的指南通常倾向于选择能传达更多信息的长名称。

Clearly there are advantages to shorter names as well, and a good compromise is a bit of an art form.
显然，短名称也有优势，而好的折衷是一门艺术。

Note that concern about time spent (wasted) typing longer names is generally misplaced, as numerous studies have shown that source code is read many more times than than it is written.
请注意，对输入长名称所花费（浪费）的时间的担忧通常是 misplaced 的，因为大量研究表明源代码被阅读的次数远多于被编写的次数。

Further, many modern software editors provide means to "auto-complete" names, which further reduces concerns over typing long names.
此外，许多现代软件编辑器提供"自动完成"名称的方法，这进一步减少了对输入长名称的担忧。

Names which are *too* long can reduce clarity, especially in long expressions.
*太*长的名称会降低清晰度，尤其是在长表达式中。

When the discrepancy is severe, there are several alternatives:
当差异严重时，有几种替代方案：

1. Split the long expression into multiple statements by introducing intermediate variables for subexpressions. This often improves the clarity in a number of ways with the intermediate names providing new avenues for communication.
   通过为子表达式引入中间变量，将长表达式拆分为多个语句。这通常可以通过中间名称提供新的交流途径，从而在多方面提高清晰度。

2. Introduce a local variable with a shorter name to be used as an alias. Because the new name has a smaller scope and is directly associated with the original variable, a very short string is very sensible.
   引入一个较短名称的局部变量作为别名。由于新名称的作用域较小，并且与原始变量直接关联，因此非常短的字符串是非常合理的。

3. In the near future the F2003 `associate` construct will provide a formal mechanism for using a short name (alias) to represent repeated subexpressions within a longer expression.
   在不久的将来，F2003 `associate`构造将提供一种正式机制，使用短名称（别名）来表示长表达式中的重复子表达式。

> **🔴 Mandatory / 强制**
>
> In no event shall a name exceed 31 characters which is the maximum under the F2003 standard.
> 在任何情况下，名称都不得超过31个字符，这是F2003标准下的最大值。

The F2008 standard will extend this to 63 characters, but this is motivated by the need to support automatically generated source code, and should *not* be seen as guidance for human-generated software.
F2008标准将此扩展到63个字符，但这源于支持自动生成的源代码的需要，不应被视为人工生成软件的指导。

<a id="specific-conventions"></a>
### Specific conventions / 具体约定

<a id="multi-word-names"></a>
#### Multi-word Names / 多词名称

> **📘 Encouraged / 鼓励**
>
> `ModelE` will use the common so-called mixed-case convention for concatenating multiple words in a variable name.
> `ModelE`将使用通用的所谓大小写混合约定来连接变量名中的多个单词。

In this convention the beginnings of words are indicated by starting them with capital letters, e.g. `potentialTemperature` and `numTracers`.
在此约定中，单词的开头用大写字母表示，例如`potentialTemperature`和`numTracers`。

Capitalization of the first word is context dependent and discussed in more detail below.
第一个单词的大小写取决于上下文，下面将详细讨论。

Although this convention is somewhat arbitrary, many groups have adjusted to this convention and grow to prefer it.
虽然此约定有些武断，但许多团体已经适应并喜欢这种约定。

It is important that a single convention be established as it eliminates time spent determining whether a given variable uses some other mechanism to append words.
重要的是建立单一约定，因为它消除了花费在确定给定变量是否使用其他机制来附加单词的时间。

Also, although Fortran is case-insensitive, consistent capitalization aids in reading code and finding other instances of the same variable. (Not to mention simply eliminating debate about which capitalization to use in the first place.)
此外，虽然Fortran不区分大小写，但一致的大小写有助于阅读代码和查找同一变量的其他实例。（更不用说简单地消除了首先使用哪种大小写的争论。）

<a id="file-names"></a>
#### File names / 文件名

As with variable names, file names should communicate their intent which should be their contents.
与变量名一样，文件名应传达其意图，即其内容。

In this sense, files should ideally contain only one entity which will either be a program, a subroutine, a function or a module.
从这个意义上说，文件理想情况下应只包含一个实体，可以是程序、子例程、函数或模块。

The current implementation of `ModelE` is far from this ideal, and adoption is expected to be very gradual.
`ModelE`的当前实现远未达到此理想，采用预计将非常渐进。

> **📘 Encouraged / 鼓励**
>
> Choose file names to coincide with its contents.
> 选择与内容一致的文件名。

The suffix of a file name is to be used to indicate whether the overall format is *fixed* or *free*.
文件名后缀用于指示整体格式是*固定格式*还是*自由格式*。

> **🔴 Mandatory / 强制**
>
> Fixed format files *must* end with the `.f` or `.F` suffix, while free format files *must* end with `.F90`.
> 固定格式文件*必须*以`.f`或`.F`后缀结尾，而自由格式文件*必须*以`.F90`结尾。

For example, given a software entity named `foo`, the corresponding free-format file name should be `foo.F90`.
例如，给定名为`foo`的软件实体，相应的自由格式文件名应为`foo.F90`。

<a id="derived-type-names"></a>
#### Derived type names / 派生类型名称

Derived type names should end with the `_type` suffix to indicate their role.
派生类型名称应以`_type`后缀结尾以指示其作用。

This convention might change once F2003 becomes more widespread and other object-orient conventions will be more appropriate.
一旦F2003变得更加普及，此约定可能会改变，其他面向对象约定将更合适。

Fortran 95 did not permit module procedures to have the same name as derived types which is a natural situation for constructor methods.
Fortran 95不允许模块过程与派生类型同名，这对于构造函数方法来说是自然情况。

F2003 relaxes this restriction.
F2003放宽了此限制。

> **📘 Encouraged / 鼓励**
>
> Use the `_type` suffix for names of Fortran derived types.
> 对Fortran派生类型名称使用`_type`后缀。

In analogy with object-oriented languages where developers typically capitalize class names, derived type names should be capitalized.
与开发者通常将类名大写的面向对象语言类似，派生类型名称应大写。

The issue is less important in Fortran since the `type` keyword is always present for derived types.
这个问题在Fortran中不太重要，因为派生类型始终存在`type`关键字。

<a id="module-names"></a>
#### Module names / 模块名称

Modules are sufficiently fundamental that reserving a special suffix to indicate their names is a sensible and common convention.
模块足够基础，保留特殊后缀以指示其名称是合理且常见的约定。

Most communities have opted to use `Mod` suffix for this purpose.
大多数社区选择使用`Mod`后缀用于此目的。

This is also the recommendation for `ModelE`, but with special exemptions related to existing conventions for physical components within the model.
这也是`ModelE`的建议，但针对模型内物理组件的现有约定有特殊豁免。

Files containing a module should also follow the convention of dropping the `Mod` suffix in the file name.
包含模块的文件也应遵循在文件名中省略`Mod`后缀的约定。

In that context the suffix is somewhat redundant, and dropping the suffix is more consistent with the style of other community software.
在那种情况下，后缀有点多余，省略后缀与其他社区软件的风格更一致。

As with derived type names, it is generally appropriate to capitalize module names.
与派生类型名称一样，模块名称通常应该大写。

> **📘 Encouraged / 鼓励**
>
> Most module names should use the `Mod` suffix.
> 大多数模块名称应使用`Mod`后缀。

> **📘 Encouraged / 鼓励**
>
> The `Mod` suffix should be omitted from the name of a file containing a module.
> 包含模块的文件的名称应省略`Mod`后缀。

> **📘 Encouraged / 鼓励**
>
> Capitalize module names.
> 模块名称应大写。

**Subsystem global entities module `_COM` / 子系统全局实体模块`_COM`**

A consistent existing convention within `ModelE` is for modules which provide the various global variables associated with a given physical component.
`ModelE`内部一个一致的现有约定是针对提供与给定物理组件相关的各种全局变量的模块。

The modules are currently named with the `_COM` suffix, and warrant an exception from the usual naming convention for modules.
这些模块目前以`_COM`后缀命名，值得作为模块常规命名约定的例外。

In most instances this convention is already consistent with the corresponding file name, but will eventually require a fix for th exceptions.
在大多数情况下，此约定已经与相应的文件名一致，但最终需要修复例外。

**Subsystem driver module `_DRV` / 子系统驱动模块`_DRV`**

In `ModelE` a consistent existing convention for most physical components is to have a top level file containing the suffix `_DRV`.
在`ModelE`中，大多数物理组件的一个一致的现有约定是具有包含`_DRV`后缀的顶级文件。

This convention is also to be continued, but the corresponding procedure names are generally quite inconsistent with this convention.
此约定也将继续，但相应的过程名称通常与此约定非常不一致。

E.g. the file `RAD_DRV.f` contains the top-level procedure `RADIA()`
例如，文件`RAD_DRV.f`包含顶级过程`RADIA()`

Both of the preceeding two exceptions are likely to be revisited if and when these physical components are re-implemented as ESMF components.
如果这些物理组件作为ESMF组件重新实现，前述两个例外都可能会重新审视。

<a id="procedure-names"></a>
#### Procedure names / 过程名称

Subroutines and functions perform actions and are generally best expressed with names corresponding to English verbs.
子例程和函数执行操作，通常最好用与英语动词对应的名称表示。

E.g. `print()` or `accumulate()`.
例如`print()`或`accumulate()`。

Many routines are intended to put or retrieve information from some sort of data structure, possibly indirectly.
许多例程旨在从某种数据结构中放入或检索信息，可能是间接的。

The words `put` and `get` are useful modifiers in such instances.
在这些情况下，`put`和`get`是有用的修饰词。

E.g. `putLatitude` or `getSurfaceAlbedo()`.
例如`putLatitude`或`getSurfaceAlbedo()`。

Although these conventions are fairly natural, actual awareness of them of can be beneficial when creating names.
虽然这些约定相当自然，但在创建名称时实际意识到它们可能是有益的。

<a id="variable-names"></a>
#### Variable names / 变量名称

Variable names represent objects and as such are generally best represented with names corresponding to English nouns.
变量名代表对象，因此通常最好用与英语名词对应的名称表示。

A good rule-of-thumb is to use singular nouns for scalars and plurals for lists/arrays.
一个好的经验法则是标量使用单数名词，列表/数组使用复数名词。

Note, however, that this rule-of-thumb has a very important exception for arrays which represent spatially distributed quantities such as `temperature(i,j,k)` which are referred to in the singular by common convention.
但是请注意，此经验法则对于表示空间分布量（如`temperature(i,j,k)`）的数组有一个非常重要的例外，按照通用惯例，这些量用单数表示。

---

<a id="fortran-language-constructs"></a>
## Fortran language constructs / Fortran语言构造

<a id="which-fortran-version"></a>
### Which Fortran version / Fortran版本选择

In an ideal world, `ModelE` would to be implemented in strict compliance with the Fortran standard.
在理想世界中，`ModelE`将严格按照Fortran标准实现。

However, allowance *must* be given to the evolution of the Fortran standard itself as well as to a very small number of nonstandard, yet highly portable extension to the Fortran language.
然而，必须考虑到Fortran标准本身的演变，以及非常少量的非标准但高度可移植的Fortran语言扩展。

At the time of this writing (January 2010), the current standard is Fortran 2003 (F2003) and the Fortran 2008 (F2008) standard is expected to be fully ratified later this year.
在撰写本文时（2010年1月），当前标准是Fortran 2003 (F2003)，Fortran 2008 (F2008)标准预计将在今年晚些时候完全批准。

In reality, few Fortran compilers have implemented the full F2003 standard and the interests of `ModelE` portability require that source code be restricted to a more portable subset of F2003 defined as that which is supported by current version of both GFortran *and* Intel Fortran compilers.
实际上，很少有Fortran编译器实现了完整的F2003标准，而`ModelE`可移植性的利益要求源代码限制为更可移植的F2003子集，定义为当前版本的GFortran*和*Intel Fortran编译器支持的子集。

`ModelE` execution under GFortran guarantees a strong degree of portability, while Intel guarantees continuity and high performance for GISS's primary computing environments.
在GFortran下执行`ModelE`可保证高度的可移植性，而Intel为GISS的主要计算环境保证连续性和高性能。

Note that some other compilers most likely also support this subset of F2003 (and beyond), so this constraint is not as severe as it might first appear.
请注意，其他一些编译器很可能也支持F2003的子集（及更高版本），因此此约束并不像看起来那么严重。

> **🔴 Mandatory / 强制**
>
> `ModelE` is implemented in the subset of Fortran 2003 that is robustly implemented by both current Intel and GFortran compilers.
> `ModelE`使用当前Intel和GFortran编译器稳健实现的Fortran 2003子集实现。

#### Non standard extensions in ModelE / ModelE中的非标准扩展

**CPP**
The build process of `ModelE` relies upon the C preprocessor (CPP), which is technically not part of the Fortran standard.
`ModelE`的构建过程依赖于C预处理器(CPP)，从技术上讲，它不是Fortran标准的一部分。

This capability is essential for enabling multiple configurations of the model.
此功能对于启用模型的多种配置至关重要。

**real\*8**
Although the Fortran 90 standard introduced portable syntax for controlling the precision of floating point quantities, the widespread extension (`real*8, real*4`) is portable on virtually all Fortran compilers and deeply embedded in `ModelE`.
虽然Fortran 90标准引入了用于控制浮点量精度的可移植语法，但广泛使用的扩展(`real*8, real*4`)几乎在所有Fortran编译器上都是可移植的，并深深嵌入在`ModelE`中。

The Fortran `KIND=` mechanism is of course permitted and encouraged in software sections where support of multiple precisions is required.
在需要支持多种精度的软件部分中，Fortran `KIND=`机制当然是允许和鼓励的。

<a id="obsolete-and-discouraged-features"></a>
### Obsolete and discouraged features / 过时和不建议使用的特性

Due to the desire to support legacy software, the Fortran standard rarely actually removes language features even when superior mechanisms have been introduced.
由于希望支持遗留软件，Fortran标准很少实际删除语言特性，即使已经引入了更优越的机制。

`ModelE` developers are strongly encouraged to avoid the following language features:
强烈鼓励`ModelE`开发者避免以下语言特性：

**`entry` statement**
At best this mechanism has always been confusing, and far better mechanisms now exist to share functionality across multiple interfaces.
这种机制充其量一直令人困惑，现在存在更好的机制来在多个接口之间共享功能。

This feature is strictly forbidden from being added to `ModelE`, and all existing uses will soon be eliminated.
此功能严格禁止添加到`ModelE`，所有现有用途将很快被消除。

This change is further motivated by some software tools which do not support this language "feature".
某些不支持此语言"功能"的软件工具进一步推动了这一变化。

> **🔴 Mandatory / 强制**
>
> The `entry` statement should not be used in `ModelE`.
> `ModelE`中不应使用`entry`语句。

**arithmetic `if`**
Although compact, this construct generally obfuscates code.
虽然紧凑，但这种构造通常会使代码晦涩难懂。

> **🔴 Mandatory / 强制**
>
> The arithmetic `if` construct should not be used in `ModelE`.
> `ModelE`中不应使用算术`if`构造。

**computed `goto`**
This feature is generally inferior to the newer `select case` construct which shows the conditions for execution at the top of each case.
此功能通常不如较新的`select case`构造，后者在每个case的顶部显示执行条件。

> **🔴 Mandatory / 强制**
>
> The computed `goto` construct should not be used in `ModelE`.
> `ModelE`中不应使用计算`goto`构造。

**`goto` statement**
Although there are still certain situations where the use of `goto` is the clearest expression of an algorithm, such situations are vanishingly rare in practice.
虽然仍有某些情况下使用`goto`是算法的最清晰表达，但这种情况在实践中非常罕见。

The `cycle` and `exit` statements generally communicate intent in a superior manner within loops, and `select case` and plain old `if` statements cover most other cases.
`cycle`和`exit`语句通常在循环中以更优越的方式传达意图，而`select case`和普通的旧`if`语句覆盖大多数其他情况。

> **📘 Encouraged / 鼓励**
>
> Alternatives to the `goto` statement should be be used.
> 应使用`goto`语句的替代方案。

**`continue` statement**
`END DO` is generally the preferred mechanism to close loops.
`END DO`通常是关闭循环的首选机制。

For longer loops where the loss of a statement label might complicate finding the corresponding beginning of a loop, developers should use the F90 mechanism for labeling blocks.
对于较长的循环，丢失语句标签可能会使查找循环的相应开头变得复杂，开发者应使用F90机制来标记块。

```fortran
outerLoop: do i = 1, 10
...
end do outerLoop
```

> **📘 Encouraged / 鼓励**
>
> Avoid the use of the `continue` statement.
> 避免使用`continue`语句。

**statement labels**
Although these are still necessary for `goto` statements which cannot yet be removed, other uses should rely on the F90 mechanism for labeling blocks.
虽然这些对于尚未删除的`goto`语句仍然是必要的，但其他用途应依赖F90机制来标记块。

> **📘 Encouraged / 鼓励**
>
> Use F90 statement labels for long nested loops that extend more than one screen.
> 对跨越多个屏幕的长嵌套循环使用F90语句标签。

<a id="required-and-encouraged-features"></a>
### Required and encouraged features / 必需和鼓励使用的特性

Accidental misspelling of variables was once a common source of errors in Fortran programs.
变量的意外拼写错误曾经是Fortran程序中常见的错误来源。

The introduction of `implicit none` has alleviated many such errors and fortunately has become widely used.
`implicit none`的引入缓解了许多此类错误，幸运的是它已被广泛使用。

> **🔴 Mandatory / 强制**
>
> The `implicit none` statement *must* be used in all modules and all non-module subroutines and functions.
> `implicit none`语句*必须*在所有模块和所有非模块子例程和函数中使用。

By default all Fortran module entities are "public" which can lead to problems with multiple paths by which those entities are accessed by higher level program units.
默认情况下，所有Fortran模块实体都是"公共的"，这可能导致高级程序单元访问这些实体的多个路径出现问题。

The cascade of possible host association can lead to long and/or aborted compilation.
可能的宿主关联级联可能导致编译时间过长和/或编译中止。

Aside from these technical issues, one of the intents of the Fortran module construct is to encapsulate (i.e. hide) details of implementation from external program units.
除这些技术问题外，Fortran模块构造的意图之一是从外部程序单元封装（即隐藏）实现细节。

Fortunately, Fortran has the `private` statement which toggles this default.
幸运的是，Fortran有`private`语句来切换此默认值。

> **📘 Encouraged / 鼓励**
>
> Modules should use the `private` statement. Entities which should be accessible by other program units should be declared with the `public` attribute.
> 模块应使用`private`语句。其他程序单元应可访问的实体应使用`public`属性声明。

Even more than Fortran modules, derived types should hide the details of their internal implementation.
甚至比Fortran模块更重要的是，派生类型应隐藏其内部实现的细节。

Unfortunately, as with modules, the default public access leads to over-reliance on access to internal details.
不幸的是，与模块一样，默认的公共访问导致过度依赖对内部细节的访问。

With F95 such structures must be entirely public or entirely private, but F2003 introduces finer control.
在F95中，此类结构必须完全是公共的或完全是私有的，但F2003引入了更精细的控制。

> **📘 Encouraged / 鼓励**
>
> Fortran derived types should use the `private` statement where possible.
> Fortran派生类型应尽可能使用`private`语句。

---

<a id="formatting-conventions"></a>
## Formatting conventions / 格式约定

Formatting issues are far less substantive than the software elements that are discussed earlier in this document.
格式问题远不如本文档前面讨论的软件要素重要。

However, a consistent "look-and-feel" can be a powerful aid to the readability of `ModelE` as well as preventing needless thrashing in CVS as one developer after another imposes their personal preference.
然而，一致的"外观和感觉"可以极大地提高`ModelE`的可读性，并防止在CVS中不必要的混乱，因为一个接一个的开发者强加他们的个人偏好。

Nonetheless, this section is intentionally minimalist and as much as possible reflects existing style within `ModelE`.
尽管如此，本节有意采用极简主义，并尽可能反映`ModelE`中的现有风格。

<a id="free-format"></a>
### Free format / 自由格式

Although `ModelE` is at the time of this writing almost exclusively implemented in the older fixed-format Fortran convention, the new default format is exclusively free-format.
虽然`ModelE`在撰写本文时几乎完全以旧的固定格式Fortran约定实现，但新的默认格式完全是自由格式。

Further, the existing code base will soon be thoroughly converted to free-format.
此外，现有代码库将很快彻底转换为自由格式。

While there are several minor advantages to free-format, the rationale for the wholesale conversion is to leverage a new generation of powerful software tools that do not support the older format.
虽然自由格式有几个小优势，但批量转换的基本原理是利用新一代不支持旧格式的强大软件工具。

Although, free-format permits source code to extend up to column 132, practical readability requires that source code be limited to column 80.
虽然自由格式允许源代码扩展到第132列，但实际可读性要求源代码限制在第80列。

Exceptional cases where the code marginally exceeds this threshold may be acceptable if additional line-splits have comparable consequences on appearance.
如果额外的行分割对外观有相当影响，则代码略微超过此阈值的特殊情况可能是可以接受的。

<a id="indentation"></a>
### Indentation / 缩进

The interior of each of the following categories of Fortran code blocks shall be indented in a consistent manner:
以下各类Fortran代码块的内部应以一致的方式缩进：

- module / 模块
- subroutine / 子例程
- function / 函数
- program / 程序
- type / 类型
- interface / 接口
- if ... then / if ... then
- select case / select case
- do / do

At this time precisely 2 spaces shall be used for each level of indentation.
此时每个缩进级别应准确使用2个空格。

Although a larger indentation is generally preferable for readability, existing reliance on very deep nesting is a dominant concern.
虽然较大的缩进通常更适合可读性，但对非常深层嵌套的现有依赖是一个主要问题。

If at some later time, deep nests have been eliminated from `ModelE`, the level of indentation will be raised.
如果在以后的某个时候，`ModelE`中消除了深层嵌套，缩进级别将会提高。

Indentation should always be implemented with spaces, as the `<TAB>` character is not legal in Fortran source code.
缩进应始终使用空格实现，因为`<TAB>`字符在Fortran源代码中是非法的。

Unfortunately, some common editors will permit the insertion of `<TAB>` characters, so some caution is appropriate.
不幸的是，一些常见的编辑器允许插入`<TAB>`字符，因此需要适当注意。

Note to Emacs users: Although the `<TAB>` key is used to auto-indent lines of source code in Fortran mode, the editor actually only inserts (or removes) spaces to achieve indentation.
Emacs用户注意：虽然`<TAB>`键用于在Fortran模式下自动缩进源代码行，但编辑器实际上只插入（或删除）空格来实现缩进。

<a id="indentation-of-documentation"></a>
#### Indentation of documentation / 文档缩进

Documentation in the header of procedures and modules should not be indented, while documentation lines in executable sections should be indented at the same level as the surrounding code.
过程和模块头部的文档不应缩进，而可执行部分中的文档行应与周围代码处于同一缩进级别。

End-of-line not extend beyond column 80.
行尾不超过第80列。

<a id="spacing"></a>
### Spacing / 空格

<a id="two-word-fortran-keywords"></a>
#### Two word Fortran keywords / 双词Fortran关键字

Although spaces are generally significant under the free-format convention, for most (possibly all?) compound keywords (e.g. `end do` and `go to`) the intervening space is optional.
虽然空格在自由格式约定中通常很重要，但对于大多数（可能是全部？）复合关键字（例如`end do`和`go to`），中间的空格是可选的。

For `ModelE` the convention is to require the intervening space for all such constructs except for `goto`:
对于`ModelE`，约定是要求所有此类构造的中间空格，除了`goto`：

**推荐使用**:
- goto
- end do
- end if
- end select
- end subroutine
- end function

**不推荐使用**:
- ~~go to~~
- ~~enddo~~
- ~~endif~~
- ~~endselect~~
- ~~endsubroutine~~
- ~~endfunction~~
- ~~endsubroutine~~

> **🔴 Mandatory / 强制**
>
> Use a space between compound keywords except for the `goto` statement.
> 在复合关键字之间使用空格，但`goto`语句除外。

<a id="operators"></a>
#### Operators / 运算符

> **📘 Encouraged / 鼓励**
>
> To improve legibility, expressions should attempt to use the space character in a judicious manner.
> 为了提高可读性，表达式应明智地使用空格字符。

The rules here are not absolute, but guidelines that should be followed unless other legibility issues are more important.
这里的规则不是绝对的，而是应遵循的指南，除非其他可读性问题更重要。

In order of decreasing priority one should:
按优先级递减的顺序，应该：

- Use at least one space should be left on each side of the assignment (`=`) operator.
  在赋值(`=`)运算符的每一侧至少留一个空格。
- Use at least one space on each side of `+` and `-` operators to both emphasize grouping as well as order of precedence among operators.
  在`+`和`-`运算符的每一侧至少留一个空格，以强调分组以及运算符之间的优先级顺序。
- *Not* use space around `*` and `**` operators.
  *不*在`*`和`**`运算符周围使用空格。
- Use one space after `,` in arguments to procedures and functions.
  在过程和函数的参数中的`,`之后使用一个空格。
- *Not* use space between array indices.
  *不*在数组索引之间使用空格。

<a id="capitalization"></a>
### Capitalization / 大小写

Although Fortran is case insensitive, capitalization can be useful to convey additional information to readers.
虽然Fortran不区分大小写，但大小写可以向读者传达额外的信息。

Because modern editors can generally highlight language keywords, capitalization is generally only to be applied to user-defined entities.
由于现代编辑器通常可以突出显示语言关键字，因此大小写通常仅应用于用户定义的实体。

As mentioned above, capitalization should be used to separate words within multi-word names, as well as for derived type and module names.
如上所述，大小写应用于分隔多词名称中的单词，以及派生类型和模块名称。

> **📘 Encouraged / 鼓励**
>
> Use lower case for Fortran keywords.
> Fortran关键字使用小写。

> **📘 Encouraged / 鼓励**
>
> Use mixed case for multiword names.
> 多词名称使用混合大小写。

> **📘 Encouraged / 鼓励**
>
> Start names with lower case except for derived types and modules.
> 名称以小写开头，派生类型和模块除外。

---

<a id="documentation"></a>
## Documentation / 文档

`ModelE` uses scripts to dynamically assemble certain documentation from source code in an automated manner based upon special identification tags.
`ModelE`使用脚本基于特殊标识标签以自动化方式从源代码动态组装某些文档。

<a id="documentation-of-fortran-modules"></a>
### Documentation of Fortran modules / Fortran模块文档

Each module *must* have a top-level summary indicated with the comment tag: `!@sum`.
每个模块*必须*具有用注释标签`!@sum`指示的顶级摘要。

This summary should explain the nature of the modules contents and the role of the module within the context of the overall model.
此摘要应解释模块内容的性质以及模块在整个模型上下文中的作用。

All global (i.e. `public` module entities *must* be documented with the comment tag: `!@var`.
所有全局（即`public`）模块实体*必须*用注释标签`!@var`记录文档。

This documentation should emphasize the purpose of the entity, and for physical quantities the documentation should specify the physical units (e.g. `m/s`).
此文档应强调实体的用途，对于物理量，文档应指定物理单位（例如`m/s`）。

Where appropriate each module should specify the primary author(s) or point(s)-of-contact with the comment tag: `!@auth`.
在适当的情况下，每个模块应使用注释标签`!@auth`指定主要作者或联系人。

For more complex situations, the repository is a better mechanism for determining which developers are responsible for any bit of code.
对于更复杂的情况，存储库是确定哪些开发者负责任何代码位的更好机制。

<a id="documentation-of-fortran-procedures"></a>
### Documentation of Fortran procedures / Fortran过程文档

> **🔴 Mandatory / 强制**
>
> Each public procedure (subroutine or function) *must* have a top-level summary indicated with the comment tag: `!@sum`.
> 每个公共过程（子例程或函数）*必须*具有用注释标签`!@sum`指示的顶级摘要。

This summary should explain the nature of the modules contents and the role of the module within the context of the overall model.
此摘要应解释模块内容的性质以及模块在整个模型上下文中的作用。

> **🔴 Mandatory / 强制**
>
> Each procedure dummy variable *must* be documented with the comment tag: `!@var`.
> 每个过程虚拟变量*必须*用注释标签`!@var`记录文档。

This documentation should emphasize the purpose of the entity, and for physical quantities the documentation should specify the physical units (e.g. `m/s`).
此文档应强调实体的用途，对于物理量，文档应指定物理单位（例如`m/s`）。

> **📘 Encouraged / 鼓励**
>
> Important/nontrivial local variables should be also be documented with the `!@var` tag.
> 重要的/非平凡的局部变量也应使用`!@var`标签记录文档。

> **📘 Encouraged / 鼓励**
>
> Where appropriate and/or different than for the surrounding module, each procedure should specify the primary author or point-of-contact with the comment tag: `!@auth`.
> 在适当的情况下和/或与周围模块不同，每个过程应使用注释标签`!@auth`指定主要作者或联系人。

For more complex situations, the repository is a better mechanism for determining which developers are responsible for any bit of code.
对于更复杂的情况，存储库是确定哪些开发者负责任何代码位的更好机制。

<a id="documentation-of-rundeck-parameters"></a>
### Documentation of rundeck parameters / rundeck参数文档

Rundeck parameters are among the most important quantities from the point-of-view of other users of the software, and strong documentation for those parameters is a very high priority.
从软件其他用户的角度来看，rundeck参数是最重要的量之一，这些参数的强有力文档是非常高优先级的。

> **🔴 Mandatory / 强制**
>
> All rundeck parameters *must* be documented using the comment tag `!@dbparam`.
> 所有rundeck参数*必须*使用注释标签`!@dbparam`记录文档。

---

<a id="miscellaneous"></a>
## Miscellaneous / 杂项

<a id="free-format-templates"></a>
### Free format templates / 自由格式模板

Some users may find it convenient to begin new modules and/or procedures with a skeleton implementation that indicates such things as proper indentation and other conventions.
一些用户可能会发现，以骨架实现开始新模块和/或过程很方便，该实现指示诸如正确缩进和其他约定之类的内容。

Figure 1 provides a template for Fortran modules that conforms to the conventions established in this document.
图1提供了符合本文档中建立的约定的Fortran模块模板。

Figure 2 provides an analogous template for Fortran subroutines, and Figure 3 provides a template for Fortran functions.
图2提供了Fortran子例程的类似模板，图3提供了Fortran函数的模板。

#### Figure 1: Template for Fortran module in free-format / 图1：自由格式Fortran模块模板

```fortran
module <module-name>Mod
!@sum <summary>
!@auth <principle author>
  use <use-module>, only: <item>
  ...
  implicit none
  private

  ! list public entities
  public :: <item>
  ...

  ! declare any public derived types
  type <name>_type
    private
    <declare components of derived type>
  end type <name>_type
  ...

  ! declare public variables
  !@var <var1> <description> <units>
  real*8, allocatable :: <var1>(:,:,:)
  ...

contains

  <procedure 1>

  <procedure 2>

end module <module-name>Mod
```

#### Figure 2: Template for Fortran subroutine in free-format / 图2：自由格式Fortran子例程模板

```fortran
subroutine <routine-name>(<arg1>[, <arg2>, ...])
!@sum <summary>
!@auth <principle author>
  use <use-module>, only: <item>
  ...
  implicit none ! not required for module subroutine

  ! declare dummy arguments
  !@var <arg1> <description> <units>
  real*8, allocatable, intent(...) :: <arg1>(:,:)

  ! declare local variables
  real*8, allocatable :: <var1>(:,:)


  <executable statement>
  ...

end subroutine <routine-name>
```

#### Figure 3: Template for Fortran function in free-format / 图3：自由格式Fortran函数模板

```fortran
function <routine-name>(<arg1>[, <arg2>, ...])
!@sum <summary>
!@auth <principle author>
  use <use-module>, only: <item>
  ...
  implicit none ! not required for module subroutine

  ! declare dummy arguments
  !@var <arg1> <description> <units>
  real*8, allocatable, intent(...) :: <arg1>(:,:)

  ! declare return type
  real*8 :: <routine-name>

  ! declare local variables
  real*8, allocatable :: <var1>(:,:)


  <executable statement>
  ...

end function <routine-name>
```

<a id="emacs-settings"></a>
### Emacs settings / Emacs设置

The Emacs editor has a number of useful features for editing free-format Fortran files.
Emacs编辑器有许多用于编辑自由格式Fortran文件的有用功能。

However, the default settings (e.g. indentation) do not correspond to the conventions established in this document.
然而，默认设置（例如缩进）与本文档中建立的约定不对应。

The elisp code in Figure 4, when inserted into a users `.emacs` file, will cause Emacs to automatically recognize files ending in `.F90` or `.f90` as free-format and set the default indentation to be 2 characters.
当将图4中的elisp代码插入用户的`.emacs`文件时，将使Emacs自动识别以`.F90`或`.f90`结尾的文件为自由格式，并将默认缩进设置为2个字符。

#### Figure 4: Elisp code to customize Emacs environment for ModelE conventions / 图4：为ModelE约定自定义Emacs环境的Elisp代码

```elisp
; Ensure that F90 is the default mode for F90 files
(setq auto-mode-alist (append auto-mode-alist
                        (list '("\\.f90$" . f90-mode)
                              '("\\.F90$" . f90-mode))))
; ModelE F90 indentation rules
(setq  f90-directive-comment-re "!@")
(setq  f90-do-indent 2)
(setq  f90-if-indent 2)
(setq  f90-program-indent 2)
(setq  f90-type-indent 2)
(setq  fortran-do-indent 2)
(setq  fortran-if-indent 2)
(setq  fortran-structure-indent 2)
```

---

**Document End / 文档结束**

