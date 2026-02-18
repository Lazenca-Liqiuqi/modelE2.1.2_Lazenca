# Initialisation / 初始化

Initialisation is handled almost exclusively by the call to subroutine <TT>INPUT</TT>.
初始化几乎完全通过调用子程序 <TT>INPUT</TT> 来处理。

This routine will initialise all prognostic variables depending on the value of <TT>ISTART</TT>.
该例程将根据 <TT>ISTART</TT> 的值初始化所有预报变量。

Submodules (for instance, ocean, ice, radiation etc.) are initialised through calls to various <TT>init_XYZ</TT> routines.
子模块（例如海洋、海冰、辐射等）通过调用各种 <TT>init_XYZ</TT> 例程进行初始化。

Most input files will be opened and read at this point.
大多数输入文件将在此时被打开并读取。

**Document End / 文档结束**
