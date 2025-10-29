# System requirements / 系统要求

**System requirements**
**系统要求**

The ModelE source code is quite portable and can be installed and used basically on any Unix machine with enough CPU power and memory (from Linux clusters to Linux and Mac OS X desktops). Though one can run the basic serial version of the model with prescribed ocean on a single core with as little as 2 GB of memory, to do any useful simulations in reasonable time one would need a computer with at least 16 cores (Sandy Bridge or faster) with at least 1 GB of memory per core. To do dynamic ocean simulations with full atmospheric chemistry one typically would need 88 cores with at least 1 GB of memory per core.
ModelE源代码具有很好的可移植性，基本上可以在任何具有足够CPU和内存的Unix机器上安装和使用（从Linux集群到Linux和Mac OS X桌面）。虽然可以在单核上运行指定海洋的基本串行版本模型，最少只需要2GB内存，但要在合理时间内进行任何有用的模拟，需要一台至少具有16个核心（Sandy Bridge或更快）的计算机，每个核心至少1GB内存。要进行带有完整大气化学的动态海洋模拟，通常需要88个核心，每个核心至少1GB内存。

The source code is written mostly in Fortran 90 language with some elements of Fortran 2003 and can be compiled either with Intel `ifort` compiler (version 12.0) or with GNU `gfortran` (version 4.9 or later).
源代码主要使用Fortran 90语言编写，包含一些Fortran 2003元素，可以使用Intel `ifort`编译器（12.0版本）或GNU `gfortran`（4.9版本或更高版本）进行编译。

For input/output we use a NetCDF library, so it has to be installed (version 3.6 or later).
对于输入/输出，我们使用NetCDF库，因此需要安装NetCDF库（3.6版本或更高版本）。

For parallel simulations on multiple cores the model needs to be compiled with MPI support, so an MPI library needs to be installed on your computer. The following MPI distributions are currently supported by the model:
对于多核上的并行模拟，模型需要使用MPI支持进行编译，因此需要在您的计算机上安装MPI库。模型目前支持以下MPI发行版：

- OpenMPI - 开源MPI实现，推荐用于桌面系统
- Intel - Intel MPI，商业实现，性能优异
- MPICH2 - MPI的标准实现之一
- MVAPICH2 - 基于InfiniBand的高性能MPI实现
- SCALI - 并行计算通信库
- mpt - MPI并行传输工具

For desktops or small servers we would recommend OpenMPI, since it is the easiest one to install and configure, though MPICH2 also works without problems. On a cluster, typically it would be up to support group to make a decision on which MPI distribution is more suitable for a particular platform. Over the last few years we were using Intel MPI with great success.
对于桌面计算机或小型服务器，我们推荐使用OpenMPI，因为它是最容易安装和配置的，尽管MPICH2也能正常工作。在集群上，通常由支持团队决定哪种MPI发行版更适合特定平台。在过去几年中，我们使用Intel MPI取得了很大成功。

The compilation process is based on GNU `make` command and uses `perl` scripting language and `m4` preprocessor (GNU version). Typically these are present by default on any Linux or Mac OS X system, but if you are using other type on Unix you may need to install them.
编译过程基于GNU `make`命令，使用`perl`脚本语言和`m4`预处理器（GNU版本）。通常这些工具在Linux或Mac OS X系统上默认存在，但如果您使用其他类型的Unix系统，可能需要安装它们。

If instead of latitude-longitude version of the model you want to work with cubed sphere version, then in addition to the requirements mentioned above you will need to install a compatible ESMF library. You will also need to obtain the source code for the cubed sphere dynamical core from the developers since it is not included in the standard modelE distribution.
如果您想要使用立方体球面版本的模型而不是经纬度版本，那么除了上述要求外，您还需要安装兼容的ESMF库。您还需要从开发者那里获取立方体球面动力学核心的源代码，因为它不包含在标准的ModelE发行版中。

---

**Platform note / 平台说明**:
- 本文档中的硬件配置建议基于当前的气候模拟需求，实际需求可能因具体实验配置而异
- MPI发行版的选择建议：桌面用户首选OpenMPI，集群用户请咨询系统管理员
- 编译器版本要求为最低版本，使用更新版本通常能获得更好的性能

**Version note / 版本说明**:
- NetCDF 3.6为最低版本要求，推荐使用4.x系列以获得更好的性能和功能支持
- gfortran 4.9为最低版本，推荐使用5.0或更高版本
- Intel MPI 12.0为最低版本，推荐使用更新版本