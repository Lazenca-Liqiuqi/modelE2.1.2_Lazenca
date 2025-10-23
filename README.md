# ModelE2.1.2_Lazenca - NASA GISS Earth System Model (Lazenca Fork)

NOTE: The full documentation on how to run the model is in
**注意：** 关于如何运行模型的完整文档位于

doc/UserGuide/index.html

or you can read it online at
**或者你可以在线阅读：**

http://simplex.giss.nasa.gov/gcm/doc/UserGuide/index.html

This summary is not complete, and not necessarily up-to-date either.
**本摘要并不完整，也不一定是最新的。**

PLEASE READ THE FULL DOCUMENTATION - IT REALLY WILL MAKE YOUR LIFE EASIER!
**请阅读完整文档 - 它真的会让你的生活更轻松！**

The directory tree of the modelE2.1.2_Lazenca has the following structure:
**ModelE2.1.2_Lazenca的目录树结构如下：**

modelE2.1.2_Lazenca
      |
      |-/model   (the source code for GCM model)
      |            **模型源代码目录**
      |
      |-/aux     (auxiliary programs such as pre- and post-processing)
      |           **辅助程序目录，如预处理和后处理**
      |
      |-/exec    (various scripts needed to compile and setup the model)
      |           **编译和设置模型所需的各种脚本**
      |
      |-/doc     (directory for documentation)
      |           **文档目录**
      |
      |-/decks   (directory for rundecks)
      |           **rundeck目录**
              |
              |-<run_name_1>.R     (rundeck for the run <run_name_1>)
              |                     **运行<run_name_1>的rundeck**
              |
              |-/<run_name_1>_bin  (directory for binaries for <run_name_1>)
              |                     **<run_name_1>的二进制文件目录**
              |
              |-/<run_name_1>      (link to directory where you setup
              |                     and run <run_name_1>)
              |                     **设置和运行<run_name_1>的目录链接**
              |-<run_name_2>.R
              ........................

   Configuring the model on your local system
   **在本地系统上配置模型**

Intended working directory is directory modelE/decks. The following
command will configure your system to be used with modelE (assuming
you are going to use "gfortran" fortran compiler):
**预期的工作目录是modelE/decks。以下命令将配置你的系统以使用modelE（假设你将使用"gfortran" Fortran编译器）：**

make config COMPILER=gfortran ModelE_Support=$HOME/ModelE_Support

This will create a default ~/.modelErcfile in your home directory.
**这将在你的主目录中创建一个默认的~/.modelErc文件。**

This should be edited so that run output, rundeck libraries etc. can
be properly directed, and so that the compile options (multiple
processing, compiler name , NetCDF libraries etc.)  can be set
appropriately. This command also creates ModelE_Support directory
for modelE support files.
**你应该编辑这个文件，以便正确定向运行输出、rundeck库等，并且可以适当设置编译选项（多处理、编译器名称、NetCDF库等）。此命令还会创建ModelE_Support目录用于存储modelE支持文件。**

               Compiling and running the model.
               **编译和运行模型。**

All rundecks should be created inside this directory and all "make"
commands should be run from there. The following is a typical example
of how to compile and setup a run with the name "my_run":
**所有rundeck都应该在此目录内创建，所有"make"命令都应该从此目录运行。以下是一个典型的例子，说明如何编译和设置名为"my_run"的运行：**

     cd decks                      # go to directory decks
     **cd decks                      # 进入decks目录**

     gmake rundeck RUN=my_run      # create rundeck for "my_run"
     **gmake rundeck RUN=my_run      # 为"my_run"创建rundeck**

You will need to edit the rundeck in order to choose a configuration
that is appropriate. Once that is done...
**你需要编辑rundeck以选择适当的配置。完成后...**

     gmake setup RUN=my_run        # compile the model and set up
                                   # a run directory for "my_run"
     **gmake setup RUN=my_run        # 编译模型并为"my_run"设置运行目录**

     ../exec/runE my_run -cold-restart   # Start model run from the
                                         # initial conditions
     **../exec/runE my_run -cold-restart   # 从初始条件开始模型运行**

     ../exec/runE my_run                 # Continue model run from
                                         # a saved checkpoint
     **../exec/runE my_run                 # 从保存的检查点继续模型运行**

Make sure that you create the rundeck with "gmake rundeck ..." before
running any other commands for this run, otherwise the Makefile will
not understand you.  All the binaries created by "make" are stored in
 /decks/my_run.bin .
**确保在运行此运行的任何其他命令之前，使用"gmake rundeck ..."创建rundeck，否则Makefile将无法理解你。"make"创建的所有二进制文件都存储在/decks/my_run.bin中。**

The following is a list of targets currently supported by Makefile:
**以下是Makefile当前支持的目标列表：**

config  - copy the default .modelErc setup to your home directory.
**config  - 将默认.modelErc设置复制到你的主目录。**

rundeck - create new rundeck
**rundeck - 创建新的rundeck**

depend  - create dependencies for specified rundeck
**depend  - 为指定rundeck创建依赖关系**

gcm     - compile object files and build executable for specified rundeck
**gcm     - 编译对象文件并为指定rundeck构建可执行文件**

aux     - compile standard auxiliary programs
**aux     - 编译标准辅助程序**

auxqflux- compile auxiliary programs for computing qflux
**auxqflux- 编译用于计算qflux的辅助程序**

auxdeep - compile auxiliary programs for setting deep ocean
**auxdeep - 编译用于设置深海的辅助程序**

setup   - compile executable and prepare run directory for specified rundeck
**setup   - 编译可执行文件并为指定rundeck准备运行目录**

clean   - remove object files, .mod files and dependencies
**clean   - 删除对象文件、.mod文件和依赖关系**

newstart- remove all files in the run directory
**newstart- 删除运行目录中的所有文件**

exe     - compile gcm and put executable into RUN directory
**exe     - 编译gcm并将可执行文件放入RUN目录**

htmldoc - create web-based documentation for this RUN
**htmldoc - 为此运行创建基于Web的文档**

If you run "gmake" without arguments it will print a short help.
**如果你运行不带参数的"gmake"，它将打印简短的帮助信息。**

## 项目文档系统 | Project Documentation System

### 文档结构 | Documentation Structure
本项目已建立完整的现代化文档系统，采用中英对照段落格式：
**This project has established a complete modernized documentation system using paragraph-level bilingual format:**

- **CLAUDE.md** - AI可读的项目技术概览和架构说明
**CLAUDE.md** - AI-readable project technical overview and architecture description
- **README.md** - 人类友好的项目使用指南（本文档）
**README.md** - Human-friendly project usage guide (this document)
- **CHANGELOG.md** - 完整版本变更记录
**CHANGELOG.md** - Complete version change history

### 技术文档 | Technical Documents
- **doc/ARCHITECTURE_ANALYSIS.md** - 详细的ModelE架构分析和模块依赖关系
**doc/ARCHITECTURE_ANALYSIS.md** - Detailed ModelE architecture analysis and module dependencies
- **doc/PROJECT_ANALYSIS_REPORT.md** - 全面项目分析报告和现代化路线图
**doc/PROJECT_ANALYSIS_REPORT.md** - Comprehensive project analysis report and modernization roadmap
- **doc/PROJECT_MEMORY_INDEX.md** - 项目记忆系统索引和使用指南
**doc/PROJECT_MEMORY_INDEX.md** - Project memory system index and usage guide

### 当前状态 | Current Status
- **版本 | Version**: ModelE Fork v0.0.2 (基于 modelE-3-0 v2.1.2)
- **文档更新 | Documentation Update**: 2025-10-23
- **文档格式 | Documentation Format**: 段落级中英对照 | Paragraph-level bilingual format
- **维护状态 | Maintenance Status**: 活跃维护，持续改进 | Active maintenance, continuous improvement

############# end of README file ################################
############# README文件结束 ################################