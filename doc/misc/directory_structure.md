# ModelE Source Code Directory Structure

Directory structure of ModelE source tree
===================================================================
**ModelE源代码目录结构**
===================================================================

This document describes the structure and compilation process
for the ModelE source tree
**本文档描述了ModelE源代码树的结构和编译过程**

Directory Structure
================
**目录结构**
================

modelE/
      |
      |- config/          - configuration files for various architectures,
      |                     compilers and libraries
      |                     **各种架构、编译器和库的配置文件**
      |- exec/            - shell and perl scripts
      |                   **shell和perl脚本**
      |
      |- decks/           - working directory: all "make" commands
      |                     should be executed from here
      |                   **工作目录：所有"make"命令都应该从此目录执行**
      |- templates/       - collection of predefined rundecks for
      |                     various model configurations
      |                   **各种模型配置的预定义rundeck集合**
      |- doc/             - documentation files
      |                   **文档文件**
      |
      |- init_cond/       - useful programs for setting initial
      |                     conditions for various simulations
      |                   **用于设置各种模拟的初始条件的实用程序**
      |- aux/             - useful programs for postprocessing
      |                     model output
      |                   **用于模型输出后处理的实用程序**
      |- model/           - main model source code
      |                   **主要模型源代码**
              |
              |- dd2d                 |
              |- Ent                  |
              |- ESMF_Interface        \  ModelE "Components"
              |- giss_LSM              /
              |- shared               |
              |- solvers              |
              |                     **ModelE "组件"**
              |
              |
              | Unsorted files
              | with model source code
              _                     **未排序的模型源代码文件**

Most of the model source code is written in fortran 90/95
in fixed format with small number of files in free format.
**大部分模型源代码使用Fortran 90/95编写，采用固定格式，只有少量文件使用自由格式。**

All the source code needed for compilation of ModelE executable
is located under model/ directory tree. model/ directory consists
of subdirectories (from now called "components"), unsorted
source files and a Makefile.
**编译ModelE可执行文件所需的所有源代码都位于model/目录树下。model/目录由子目录（现在称为"组件"）、未排序的源文件和一个Makefile组成。**

Each "component" conatins source
files collected together according to their functionality.
**每个"组件"包含根据功能收集在一起的源文件。**

They either constitute a certain physics model (Ent, giss_LSM),
provide certain computational functionality (solvers) or serve
for some administrative purposes (shared).
**它们要么构成特定的物理模型（Ent、giss_LSM），要么提供特定的计算功能（solvers），要么用于某些管理目的（shared）。**

Each component has
its own Makefile which typically is trivial: it contains the list
source files in the component and includes a template Makefile
from config/ .
**每个组件都有自己的Makefile，通常很简单：它包含组件中的源文件列表，并包含来自config/的模板Makefile。**

But if necessary a component can provide its
own Makefile which is not related to the rest of the modelE.
**但如果需要，组件可以提供自己的Makefile，与modelE的其他部分无关。**

The only requirement to such Makefile is that it should compile
the code into a library "lib.a" which will then be linked
together with the rest of modelE code.
**对此类Makefile的唯一要求是它应该将代码编译成库"lib.a"，然后将与modelE代码的其余部分链接。**

Though most of the model code now remains unsorted in model/
directory it is anticipated that it will be encapsulated into
"components" with only main drivers remaining in model/
directory.
**虽然大部分模型代码现在仍然在model/目录中未排序，但预计将被封装到"组件"中，只有主要驱动程序保留在model/目录中。**

Compilation
==================
**编译**
==================

The disadvantage of using fortran 90 modules is that files have to
be compiled in certain order, i.e. the file with the module should
be compiled before the file which "uses" this module.
**使用Fortran 90模块的缺点是文件必须按特定顺序编译，即包含模块的文件应该在"使用"此模块的文件之前编译。**

This also
forbids circular dependencies: if file A "uses" module from file B
then file B can't use a module from file A (keep in mind that
such circular dependence may accidentially be created through a third
file).
**这也禁止循环依赖：如果文件A"使用"文件B的模块，那么文件B不能使用文件A的模块（请记住，这种循环依赖可能通过第三个文件意外创建）。**

The same rule applies to modelE "components": they can
depend on other components as long as it doesn't create a dependency
loop between the components.
**同样的规则适用于modelE"组件"：只要不会在组件之间创建依赖循环，它们就可以依赖其他组件。**

Also, files in model/ directory can
depend on "components" but "components" can't depend on files in
model/ directory.
**此外，model/目录中的文件可以依赖"组件"，但"组件"不能依赖model/目录中的文件。**

The compilation of the model is performed in the following order:
**模型的编译按以下顺序执行：**

1. "make" enters each "component" directory and computes dependencies
   there.
   **1. "make"进入每个"组件"目录并计算那里的依赖关系。**

2. Based on dependency lists for each component "make" constructs
   dependency relations between the components.
   **2. 基于每个组件的依赖列表，"make"构建组件之间的依赖关系。**

3. "make" computes dependencies for the main directory.
   **3. "make"计算主目录的依赖关系。**

4. "make" enters each "component" (in appropriate order), compiles
   the code there and combines the object files into a library
   "lib.a". All *.mod files are copied into a global model/mod
   directory.
   **4. "make"进入每个"组件"（按适当顺序），编译那里的代码并将对象文件组合成库"lib.a"。所有*.mod文件都被复制到全局model/mod目录中。**

5. "make" compiles the code in the main model/ directory.
   **5. "make"编译主model/目录中的代码。**

6. All object files in model/ directory are linked together with
   lib.a libraries for each component (listed in appropriate order).
   **6. model/目录中的所有对象文件与每个组件的lib.a库链接（按适当顺序列出）。**

The compilation process is parallel-compatible, so one can request
"make" to use multiple threads for faster compilation
(with -j<num of threads>). Though due to complicated dependencies
between modelE modules one usually doesn't gain much.
**编译过程是并行兼容的，因此可以请求"make"使用多个线程进行更快的编译（使用-j<线程数>）。但由于modelE模块之间复杂的依赖关系，通常收益不大。**