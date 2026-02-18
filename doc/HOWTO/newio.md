# NEW_IO / NEW_IO系统指南

M. Kelley, November 2010
M. Kelley，2010年11月

## Table of Contents / 目录

- [HOW-TO configure your rundeck and set up your environment](#rundeck) - 如何配置运行配置和设置环境
- [HOW-TO examine a quantity in the restart file](#model_state) - 如何检查重启文件中的量
- [HOW-TO compare restart files](#diffreport) - 如何比较重启文件
- [HOW-TO save a quantity in the restart file](#defvar) - 如何在重启文件中保存量
- [HOW-TO obtain scaled diagnostics (short version)](#pdE) - 如何获取缩放诊断输出（简版）
- [HOW-TO obtain scaled diagnostics](#scaleacc) - 如何获取缩放诊断输出
- [HOW-TO do time averages](#sumfiles) - 如何进行时间平均
- [HOW-TO obtain lat-lon outputs from a cubed-sphere run](#remap) - 如何从立方体球面运行获取经纬度输出
- [HOW-TO print the diagnostics tables](#tables) - 如何打印诊断表
- [HOW-TO convert netcdf to GISS-binary format](#gissbin) - 如何将netcdf转换为GISS二进制格式
- [HOW-TO print a netcdf variable in ASCII format](#ncksprt) - 如何以ASCII格式打印netcdf变量
- [HOW-TO extract hemispheric/global means](#hemis) - 如何提取半球/全球平均值
- [HOW-TO write "subdaily" diagnostics in netcdf format](#subdd) - 如何以netcdf格式写入"亚日"诊断
- [HOW-TO add a new diagnostic to an existing category](#add_diag) - 如何向现有类别添加新诊断
- [HOW-TO add a new category of diagnostic](#add_diag_cat) - 如何添加新的诊断类别
- [Special diagnostic calculations](#special_cat) - 特殊诊断计算
- [Troubleshooting](#probs) - 故障排除
- [Plotting options](#plotting) - 绘图选项
- [How it works](#rules) - 工作原理
- [Local information](#local_info) - 本地信息

<a id="rundeck"></a>

## HOW-TO configure your rundeck and set up your environment / 如何配置运行配置和设置环境

Cubed-sphere rundecks function in NEW_IO mode only and no changes are necessary.
立方体球面运行配置仅在NEW_IO模式下运行，无需任何更改。

To reconfigure a rundeck for NEW_IO, change the following:
要为NEW_IO重新配置运行配置，请进行以下更改：

- `#define NEW_IO` in the `Preprocessor Options` section
  
  - 在`预处理器选项`部分添加`#define NEW_IO`
  
- in the `Object Modules:` section, replace `IORSF` by `IO_DRV`. If doing a tracer run, add `TRDIAG` somewhere.
  - 在`对象模块：`部分，用`IO_DRV`替换`IORSF`。如果进行示踪物运行，在某处添加`TRDIAG`。

- in the `Components:` section, add `dd2d`
  - 在`组件：`部分，添加`dd2d`

- If you wish to use parallel-netcdf, add a line `OPTS_dd2d = NC_IO=PNETCDF` in the `Component Options:` section of the rundeck, and check that PNETCDFHOME is set in your .modelErc (see [Local information](#local_info) for installation locations). If your run writes restart files larger than 1-2 GB, this option is highly recommended.
  - 如果您希望使用parallel-netcdf，在运行配置的`组件选项：`部分添加一行`OPTS_dd2d = NC_IO=PNETCDF`，并检查PNETCDFHOME是否在您的.modelErc中设置（参见[本地信息](#local_info)了解安装位置）。如果您的运行写入的重启文件大于1-2 GB，强烈建议使用此选项。

- If ISTART=2: in the `Data input files:` section, set `GIC=name_of_a_netcdf_gic.nc`
  - 如果ISTART=2：在`数据输入文件：`部分，设置`GIC=name_of_a_netcdf_gic.nc`

  (The [Local information](#local_info) section will point you to some existing netcdf GIC files)
  - （[本地信息](#local_info)部分将为您指出一些现有的netcdf GIC文件）

Most systems running modelE have a netcdf installation which is probably already specified in your .modelErc file.
大多数运行modelE的系统都已安装netcdf，可能已在您的.modelErc文件中指定。

However, your PATH environment variable may not include the location of two important helper programs: `ncdump` and `ncgen`.
然而，您的PATH环境变量可能未包含两个重要辅助程序的位置：`ncdump`和`ncgen`。

If it doesn't, add `NETCDFHOME/bin` to your PATH (`NETCDFHOME` denoting whatever is present in your .modelErc).
如果不包含，请将`NETCDFHOME/bin`添加到您的PATH中（`NETCDFHOME`表示.modelErc中存在的任何内容）。

Unless indicated otherwise, standalone programs/scripts referenced below are installed in a location noted in the [Local information](#local_info) section.
除非另有说明，下面引用的独立程序/脚本安装在[本地信息](#local_info)部分注明的位置。

Most are built from the code in the `model/mk_diags` directory.
大多数是从`model/mk_diags`目录中的代码构建的。

Though not necessary to run the model, the NCO package is a prerequisite for the `ncksprt` script.
虽然运行模型不是必需的，但NCO包是`ncksprt`脚本的先决条件。

Again, see [Local information](#local_info)
再次，参见[本地信息](#local_info)

<a id="model_state"></a>

## HOW-TO examine a quantity in the restart file / 如何检查重启文件中的量

To view a plot of the instantaneous state of particular model variables, one can open a restart file using a [netcdf-aware](#plotting) plotting package.
要查看特定模型变量瞬时状态的图，可以使用[支持netcdf的](#plotting)绘图包打开重启文件。

However, note that restart files are not currently written with coordinate data and other metadata, which causes some packages to throw up their hands and refuse to plot anything, period.
然而，请注意，重启文件当前未写入坐标数据和其他元数据，这导致某些包束手无策并拒绝绘制任何内容，完全无法绘图。

Thankfully there exist packages like the CDAT GUI `vcdat` that accept just about any input and plot it in gridpoint space.
幸运的是，存在像CDAT GUI `vcdat`这样的包，它几乎接受任何输入并在网格点空间中绘制。

To simply print the (local) values of one or model variables to the screen, use the `ncksprt` utility described [here:](#ncksprt)
要简单地将一个或模型变量的（本地）值打印到屏幕，请使用[这里描述的](#ncksprt)`ncksprt`工具

<a id="diffreport"></a>

## HOW-TO compare restart files / 如何比较重启文件

Say you have two restart files `fort.2.8proc.nc` and `fort.2.1proc.nc` whose comparison will tell you whether the model produced the same result on 8 processors versus 1.
假设您有两个重启文件`fort.2.8proc.nc`和`fort.2.1proc.nc`，它们的比较将告诉您模型在8个处理器上是否产生与1个处理器相同的结果。

To print a report of which variables differ, and their maximum absolute and relative differences, use the `diffreport` utility (which can be applied to any two netcdf files from any source, actually):
要打印哪些变量不同的报告，以及它们的最大绝对和相对差异，请使用`diffreport`工具（实际上可以应用于来自任何源的任何两个netcdf文件）：

```bash
diffreport fort.2.8proc.nc fort.2.1proc.nc
```

To suppress reports for certain variables, an optional third command-line argument can be passed to `diffreport` specifying a dummy netcdf variable whose attributes contain a list of on/off switches.
要禁止某些变量的报告，可以向`diffreport`传递可选的第三个命令行参数，指定一个虚拟netcdf变量，其属性包含开关列表。

One use of this feature in the modelE example above would be:
在上述modelE示例中，此功能的一个用途是：

```bash
diffreport fort.2.8proc.nc fort.2.1proc.nc is_npes_reproducible
```

Here, the `is_npes_reproducible` variable is defined by modelE to contain a list of (diagnostic) arrays known to have roundoff differences on different processor counts.
在这里，`is_npes_reproducible`变量由modelE定义，包含已知在不同处理器数上具有舍入差异的（诊断）数组列表。

For a broader look at a potential problem, the NCO utility `ncdiff` can be used to generate a file containing the differences which can then be viewed (or printed with `ncksprt`):
要更广泛地查看潜在问题，可以使用NCO工具`ncdiff`生成包含差异的文件，然后可以查看（或使用`ncksprt`打印）：

```bash
ncdiff fort.2.8proc.nc fort.2.1proc.nc diff.nc
```

<a id="defvar"></a>

## HOW-TO save a quantity in the restart file / 如何在重启文件中保存量

As of March 2010, NEW_IO versions of existing model input/output routines exist alongside the default `io_XYZ` versions, but with a `new_` prefix.
截至2010年3月，现有模型输入/输出例程的NEW_IO版本与默认的`io_XYZ`版本并存，但带有`new_`前缀。

With a few exceptions described below, these function analogously to the `io_XYZ` versions, but call special routines which handle the netcdf and parallelization details.
除了下面描述的几个例外，这些例程的功能类似于`io_XYZ`版本，但调用处理netcdf和并行化细节的特殊例程。

A single call to one of these routines reads/writes a single model variable, which is associated with the corresponding variable in the file using its netcdf name.
对这些例程之一的单次调用读/写单个模型变量，该变量使用其netcdf名称与文件中的相应变量关联。

There is no requirement that the Fortran name in the code match the netcdf name in the file.
不要求代码中的Fortran名称与文件中的netcdf名称匹配。

The ordering of variables in a netcdf file is arbitrary since they are always read/written using their netcdf names.
netcdf文件中变量的顺序是任意的，因为它们总是使用其netcdf名称进行读/写。

```fortran
! write distributed array u to the netcdf variable 'u':
    call write_dist_data(grid,fid,'u',u) ! grid is a dist_grid object, fid is file ID

! read distributed array t from the netcdf variable 't':
    call read_dist_data(grid,fid,'t',t)

! root processor writes its copy of non-distributed array idacc to the netcdf variable 'idacc'
    call write_data(grid,fid,'idacc',idacc)

! read non-distributed variable s0 from netcdf variable s0, and broadcast to all processors
    call read_data(grid,fid,'s0',s0,bcast_all=.true.) ! bcast_all is an optional argument
```

Subroutines `write_dist_data,read_dist_data` take an optional argument `jdim` which specifies which dimension is the LAST horizontal dimension;
子程序`write_dist_data,read_dist_data`采用可选参数`jdim`，它指定哪个维度是最后一个水平维度；

if `jdim` is not specified it is assumed to be 2, which is the case for model arrays like temperature T(I,J,L).
如果未指定`jdim`，则假定为2，这对于像温度T(I,J,L)这样的模型数组就是这种情况。

To write an array dimensioned L,I,J, set `jdim=3`
要写入维度为L,I,J的数组，请设置`jdim=3`

Before calling one of these I/O routines, the shapes of model variables and their netcdf names must have been declared already, via a call to `defvar` in one of the `def_rsf_XYZ` subroutines.
在调用这些I/O例程之一之前，必须已经通过在`def_rsf_XYZ`子程序之一中调用`defvar`来声明模型变量的形状及其netcdf名称。

The sizes of dimensions are inferred from those of Fortran arrays passed to `defvar`, and the netcdf names of variables and their dimensions are taken from string arguments.
维度的大小从传递给`defvar`的Fortran数组推断，变量及其维度的netcdf名称取自字符串参数。

```fortran
! declare a scalar 's0'
    call defvar(grid,fid,s0,'s0')
! declare a 1-D array 'idacc' and a dimension 'nsampl'
    call defvar(grid,fid,idacc,'idacc(nsampl)')
```

For distributed arrays, a prefix `dist_` must be added to dimension names.
对于分布式数组，必须向维度名称添加前缀`dist_`。

The sizes of distributed dimensions are taken from the `grid` object.
分布式维度的大小取自`grid`对象。

```fortran
! declare a 3-D array 't' whose first two dimensions are distributed
    call defvar(grid,fid,t,'t(dist_im,dist_jm,lm)')  ! grid is a dist_grid object, fid is file ID
```

Obviously many model variables share dimensions; it is not necessary to declare separate dimension names for each variable.
显然，许多模型变量共享维度；不必为每个变量声明单独的维度名称。

If a dimension is ever redeclared with a different size than previously, `defvar` will abort.
如果维度以前后不同的大小重新声明，`defvar`将中止。

If a call to one of the write routines is made for a variable that does not exist in the output file, they will abort.
如果为输出文件中不存在的变量调用写入例程之一，它们将中止。

If a read routine is called for a nonexistent variable, a warning message is printed but execution will continue; this behavior is useful when restarting from older model versions for example.
如果为不存在的变量调用读取例程，将打印警告消息但执行将继续；例如，当从较旧的模型版本重启时，此行为很有用。

<a id="scaleacc"></a>

## HOW-TO obtain scaled diagnostics / 如何获取缩放诊断输出

```bash
scaleacc acc-file acc-array-name[,name2,name3...]

# Examples:
# scale the JAN1901 "aj" and "aij" accumulations of run E001xyz:
   scaleacc JAN1901.accE001xyz.nc aj,aij # output files will be JAN1901.{aj,aij}E001xyz.nc
# scale all available accumulations using the "all" request
   scaleacc JAN1901.accE001xyz.nc all
```

The standalone (i.e. run-independent) `scaleacc` utility converts the contents of an accumulation array to final scaled form in much the same way as the `pdE` command.
独立（即与运行无关的）`scaleacc`工具以与`pdE`命令非常相似的方式将累加数组的内容转换为最终缩放形式。

Accumulations are divided by the number of times they were accumulated, scale factors are applied, ratios are calculated, and so forth.
累加结果除以累加次数，应用缩放因子，计算比率，等等。

The name of the output file produced is the name of the accumulation file with the "acc" substring replaced by the name of the accumulation array (this differs from the filename choices of `pdE`).
生成的输出文件的名称是累加文件的名称，其中"acc"子字符串被累加数组的名称替换（这与`pdE`的文件名选择不同）。

From the end user's point of view, there are a few other minor procedural differences compared to "standard" `pdE`:
从最终用户的角度来看，与"标准"`pdE`相比，还有一些其他次要的程序差异：

- Final scaled outputs are written in netcdf format, but these are easily convertible to GISS-binary using one of the utilities documented [here.](#gissbin)
  - 最终缩放输出以netcdf格式写入，但这些可以使用[这里记录的](#gissbin)工具之一轻松转换为GISS二进制格式。

- Individual diagnostics categories are requested by name rather than via the KDIAG namelist array. Several categories can be specfied with a comma-separated list, or this collection can be built up one category at a time. For simplicity, [remapped output](#remap) must be generated using the latter approach.
  - 各个诊断类别按名称请求，而不是通过KDIAG namelist数组。可以用逗号分隔的列表指定多个类别，或者可以一次构建一个类别的集合。为简单起见，[重映射输出](#remap)必须使用后一种方法生成。

- `scaleacc` does NOT perform time averaging - time averages are constructed by first applying the `sumfiles` utility to the set of acc-files constituting a particular time period (see [the next section](#sumfiles)), and then applying `scaleacc` to the resulting "sum of files".
  - `scaleacc`不执行时间平均——时间平均是通过首先将`sumfiles`工具应用于构成特定时间段的acc文件集（参见[下一节](#sumfiles)），然后将`scaleacc`应用于结果中的"文件总和"来构建的。

- `scaleacc` does not calculate diagnostics defined using nontrivial operations on time-mean output; [special standalone programs](#special_cat) have been created for this purpose.
  - `scaleacc`不计算使用对时间平均输出的非平凡操作定义的诊断；[特殊独立程序](#special_cat)已为此目的创建。

Model E diagnostics categories configured for `scaleacc` include:
为`scaleacc`配置的模型E诊断类别包括：

- `aj`: atmospheric model, budget page (budget latitude bands)
  - `aj`：大气模型，预算页（预算纬度带）

- `areg`: atmospheric model, aj diagnostics for predefined regions
  - `areg`：大气模型，预定义区域的aj诊断

- `ajl`: atmospheric model, latitude-height (budget latitude bands)
  - `ajl`：大气模型，纬度-高度（预算纬度带）

- `aij`: atmospheric model, longitude-latitude (or on the cubed-sphere grid if applicable)
  - `aij`：大气模型，经度-纬度（或在立方体球面网格上，如适用）

- `aijl`: atmospheric model, longitude-latitude-height (or on the cubed-sphere grid if applicable)
  - `aijl`：大气模型，经度-纬度-高度（或在立方体球面网格上，如适用）

- `consrv`: atmospheric model, conservation quantities on the budget grid
  - `consrv`：大气模型，预算网格上的守恒量

- `agc`: atmospheric model, latitude-height general circulation diagnostics on constant-pressure levels (winds, temperature, eddy fluxes etc.)
  - `agc`：大气模型，等压面上的纬度-高度大气环流诊断（风、温度、涡度通量等）

- `aijk`: atmospheric model, longitude-latitude-height general circulation diagnostics on constant-pressure levels (winds, temperature, eddy fluxes etc.)
  - `aijk`：大气模型，等压面上的经度-纬度-高度大气环流诊断（风、温度、涡度通量等）

- `tconsrv`: atmospheric model, tracer conservation quantities on the budget grid
  - `tconsrv`：大气模型，预算网格上的示踪物守恒量

- `tajl`: atmospheric model, latitude-height tracer fields (budget latitude bands)
  - `tajl`：大气模型，纬度-高度示踪物场（预算纬度带）

- `taij`: atmospheric model, longitude-latitude tracer fields (or on the cubed-sphere grid if applicable)
  - `taij`：大气模型，经度-纬度示踪物场（或在立方体球面网格上，如适用）

- `taijl`: atmospheric model, longitude-latitude-height tracer fields (or on the cubed-sphere grid if applicable)
  - `taijl`：大气模型，经度-纬度-高度示踪物场（或在立方体球面网格上，如适用）

- `adiurn`: atmospheric model, diurnal cycles at selected gridpoints
  - `adiurn`：大气模型，选定网格点处的日循环

- `hdiurn`: atmospheric model, hourly timeseries at selected gridpoints
  - `hdiurn`：大气模型，选定网格点处的小时时间序列

- `otj`: Ocean R, northward transports
  - `otj`：海洋R，向北输送

- `ojl`: Ocean R, latitude-depth
  - `ojl`：海洋R，纬度-深度

- `oij`: Ocean R, longitude-latitude
  - `oij`：海洋R，经度-纬度

- `oijl`: Ocean R, longitude-latitude-depth
  - `oijl`：海洋R，经度-纬度-深度

- `olnst`: Ocean R, straits
  - `olnst`：海洋R，海峡

- `toijl`: Ocean R, longitude-latitude-depth tracer fields
  - `toijl`：海洋R，经度-纬度-深度示踪物场

- `icij`: Viscous-plastic ice dynamics, longitude-latitude fields
  - `icij`：粘-塑性冰动力学，经度-纬度场

<a id="sumfiles"></a>

## HOW-TO do time averages / 如何进行时间平均

```bash
sumfiles acc-files-to-be-summed

# Example: produce the JJA1901 accumulations of run E001xyz:
   sumfiles {JUN,JUL,AUG}1901.accE001xyz.nc
```

The scaled diagnostics for a multi-month averaging period are generated by applying `scaleacc` to an acc-file generated by `sumfiles` which contains sums over the months in this averaging period.
多月平均周期的缩放诊断是通过将`scaleacc`应用于由`sumfiles`生成的acc文件生成的，该文件包含此平均周期中月份的总和。

`sumfiles` attempts to guess an appropriate name for the file it produces, but is not foolproof.
`sumfiles`试图为其生成的文件猜测一个合适的名称，但并非万无一失。

Caution should be used when applying regular expressions like `*1901.accE001xyz.nc` ; this will cause problems if one has already created seasonal sums like `JJA1901.accE001xyz.nc` for example.
应用正则表达式如`*1901.accE001xyz.nc`时应谨慎；例如，如果已经创建了像`JJA1901.accE001xyz.nc`这样的季节总和，这将导致问题。

Multi-year sums can be calculated by applying `sumfiles` to single-year sums.
可以通过将`sumfiles`应用于单年总和来计算多年总和。

The `sumfiles` program can do more than the computation of the sums used to define time averages.
`sumfiles`程序可以做的不仅仅是计算用于定义时间平均的总和。

In fact, the only accumulation arrays it sums are those having a netcdf attribute `reduction = "sum"`.
事实上，它求和的唯一累加数组是那些具有netcdf属性`reduction = "sum"`的数组。

In addition to "sum", it currently understands "min" and "max"; other operations can easily be added.
除了"sum"之外，它目前理解"min"和"max"；可以轻松添加其他操作。

<a id="remap"></a>

## HOW-TO obtain lat-lon outputs from a cubed-sphere run / 如何从立方体球面运行获取经纬度输出

For a cubed-sphere run whose so-called "native grid" is not a latitude-longitude mesh, scaled diagnostics from accumulation arrays such as `aij` can be output on the native grid or remapped to a user-specified latitude-longitude grid.
对于所谓的"原生网格"不是经纬度网格的立方体球面运行，来自累加数组（如`aij`）的缩放诊断可以在原生网格上输出，或重新映射到用户指定的经纬度网格。

Native-grid accumulation arrays remain native in acc-files; remapping to a different grid is requested during the `scaleacc` step by adding the name of a "remap" file to the command line:
原生网格累加数组在acc文件中保持原生；在`scaleacc`步骤期间，通过将"重映射"文件的名称添加到命令行来请求重映射到不同的网格：

```bash
# Example: scale the JAN1901 "aij" accumulations of run E001xyz whose native
# grid is C90, and output them on a 288x180 latitude-longitude grid defined
# in the file remap_C90_288x180.nc
   scaleacc JAN1901.accE001xyz.nc aij remap_C90_288x180.nc
```

The name of the remap file is arbitrary since the resolutions of the cubed-sphere and latitude-longitude grids are taken from its contents.
重映射文件的名称是任意的，因为立方体球面和经纬度网格的分辨率取自其内容。

If no remap file is specified, `scaleacc` outputs quantities on their native grids.
如果未指定重映射文件，`scaleacc`在其原生网格上输出量。

Outputs which are ratios are defined as the ratio of remapped numerators and denominators.
作为比率的输出定义为重映射的分子和分母的比率。

At some point the calculation of remapping information may be moved into the `scaleacc` process, but most users will find it convenient to use one of several precalculated files available on systems where modelE runs or acc-files are archived (see [Local information](#local_info) concerning locations of remap files).
在某个时候，重映射信息的计算可能会移入`scaleacc`过程中，但大多数用户会发现使用在运行modelE或存档acc文件的系统上可用的几个预计算文件之一很方便（参见[本地信息](#local_info)关于重映射文件位置）。

The choice of remapping method for a particular diagnostic (first- versus second-order accuracy, area-weighted versus interpolation) is made during the declaration of the metadata for that diagnostic (conventions for this are currently being decided).
特定诊断的重映射方法选择（一阶与二阶精度、面积加权与插值）是在该诊断的元数据声明期间进行的（此约定目前正在确定中）。

For more information, contact the author.
有关更多信息，请联系作者。

<a id="tables"></a>

## HOW-TO print the diagnostics tables / 如何打印诊断表

To allow a large amount of output to be perused quickly, modelE provides routines which print certain categories of results in tabular form (e.g. zonal means).
为了允许快速浏览大量输出，modelE提供了以表格形式打印某些类别结果的例程（例如纬向平均）。

Most of these routines have been transplanted to standalone programs and modified to read the files produced by `scaleacc`.
这些例程中的大多数已被移植到独立程序，并修改为读取由`scaleacc`生成的文件。

Fortran format statements, powers of 10, and other information needed to replicate the look and feel of existing output are retrieved from the metadata for each quantity.
复制现有输出的外观和感觉所需的Fortran格式语句、10的幂以及其他信息从每个量的元数据中检索。

Each standalone program is designed to print one and only one category of output (although tracer quantities can be printed using the same programs as non-tracer quantities).
每个独立程序设计为仅打印一个类别的输出（尽管示踪物量可以使用与非示踪物量相同的程序打印）。

Tables are printed to standard output which can be redirected to user-specified output files.
表打印到标准输出，可以重定向到用户指定的输出文件。

Currently available print programs and their syntax for January 1901 of a run E001xyz are:
当前可用的打印程序及其语法（运行E001xyz的1901年1月）如下：

```bash
#  program          input file or argument
   prtaj            JAN1901.ajE001xyz.nc
   prtareg          JAN1901.aregE001xyz.nc
   prtconsrv        JAN1901.consrvE001xyz.nc
   prtconsrv_tracer JAN1901.tconsrvE001xyz.nc
   prtajl           JAN1901.ajlE001xyz.nc     # also works for tajl
   prtadiurn        JAN1901.adiurnE001xyz.nc
   prtrvr           JAN1901.accE001xyz.nc     # river flow; acc file is read
   prtisccp         JAN1901.accE001xyz.nc     # ISCCP clouds; acc file is read
   prtotj           JAN1901.otjE001xyz.nc
   prtolnst         JAN1901.olnstE001xyz.nc
   prtostat E001xyz JAN1901                   # reads ojl and oij output files
```

<a id="gissbin"></a>

## HOW-TO convert netcdf to GISS-binary format / 如何将netcdf转换为GISS二进制格式

GISS-binary files can be created from netcdf files using one of these programs:
可以使用以下程序之一从netcdf文件创建GISS二进制文件：

```bash
write_giss2d       infile.nc outfile [ varname OR dimname1 dimname2 ]
write_2d_as_giss4d infile.nc outfile [ varname OR dimname1 dimname2 ]
```

which behave identically save for the coordinate information written to "GISS 4D" files.
它们的行为完全相同，除了写入"GISS 4D"文件的坐标信息。

If the optional argument `varname` is specified, only that netcdf variable is written to the GISS-binary file; otherwise all dimension-matched variables are written.
如果指定了可选参数`varname`，则只有该netcdf变量被写入GISS二进制文件；否则，写入所有维度匹配的变量。

If the optional arguments `dimname1` and `dimname2` are specified, dimension-matched variables are defined as those whose dimensions include `dimname1` and `dimname2`; otherwise all variables having two or more dimensions are written.
如果指定了可选参数`dimname1`和`dimname2`，则维度匹配的变量定义为其维度包括`dimname1`和`dimname2`的变量；否则，写入所有具有两个或更多维度的变量。

If `dimname1` and `dimname2` are not specified, they are assumed to correspond to the first two dimensions of 3D+ variables.
如果未指定`dimname1`和`dimname2`，则假定它们对应于3D+变量的前两个维度。

A two-dimensional variable is written as a single fortran record, and each record of a 3D+ variable contains a two-dimensional "slab" of data spanning the two dimensions `dimname1` and `dimname2`.
二维变量作为单个fortran记录写入，3D+变量的每个记录包含跨越两个维度`dimname1`和`dimname2`的二维"数据板"。

The 80-byte title of each record is created from the `long_name` and `units` attributes of the variable being written, and contains the index information along the dimensions other than the slab dimensions `dimname1 dimname2`.
每个记录的80字节标题从正在写入的变量的`long_name`和`units`属性创建，并包含除数据板维度`dimname1 dimname2`之外的维度的索引信息。

The slab dimensions need not be the first two of a given variable, nor consecutive.
数据板维度不需要是给定变量的前两个维度，也不需要是连续的。

If `long_name` is absent, the netcdf variable name is used in the title.
如果缺少`long_name`，则在标题中使用netcdf变量名称。

Examples:
示例：

```bash
write_giss2d JAN1901.aijE001xyz.nc JAN1901.aijE001xyz.giss2d            # convert all variables in the input file
write_giss2d JAN1901.aijE001xyz.nc JAN1901.aijE001xyz.giss2d lon lat    # extract only the aij variables dimensioned by lon and lat
write_giss2d JAN1901.aijE001xyz.nc JAN1901.tsurfE001xyz.giss2d tsurf    # extract only the "tsurf" variable
write_giss2d JAN1901.aijlE001xyz.nc JAN1901.aijlE001xyz.giss2d lon plm  # aijl variables split along the lat dimension to make "IL" records
write_giss2d JAN1901.aijlE001xyz.nc JAN1901.aijlE001xyz.giss2d          # all aijl variables will be split along their 3rd dimension
write_2d_as_giss4d JAN1901.ajlE001xyz.nc JAN1901.ajlE001xyz.giss4d      # extract all AJL fields
```

<a id="pdE"></a>

## HOW-TO obtain scaled diagnostics (short version) / 如何获取缩放诊断输出（简版）

R. Ruedy has created a NEW_IO version of the `pdE` script which executes the commands described in the previous sections.
R. Ruedy创建了`pdE`脚本的NEW_IO版本，该脚本执行前面章节中描述的命令。

It collects the printed tables for all diagnostics categories into a single text file, and offers the option to convert netcdf to GISS-format files.
它将所有诊断类别的打印表收集到一个文本文件中，并提供将netcdf转换为GISS格式文件的选项。

Execute `pdE` without arguments to see the syntax of its usage.
执行不带参数的`pdE`以查看其使用语法。

<a id="ncksprt"></a>

## HOW-TO print a netcdf variable in ASCII format / 如何以ASCII格式打印netcdf变量

The script `ncksprt` employs the NCO utility `ncks` to print the values of variables in ASCII format, with further formatting of the output done by UNIX `sed`, `awk`, and `paste`.
脚本`ncksprt`使用NCO工具`ncks`以ASCII格式打印变量的值，输出的进一步格式化由UNIX `sed`、`awk`和`paste`完成。

Coordinate values are printed along with the requested variables, and multiple variables can be printed simultaneously (in column format).
坐标值与请求的变量一起打印，可以同时打印多个变量（以列格式）。

The syntax for specifying dimension bounds is that of NCO: integers correspond to (1-based) dimension indices, while floating-point numbers correspond to coordinate values.
指定维度边界的语法是NCO的语法：整数对应于（从1开始）维度索引，而浮点数对应于坐标值。

Although it can be used to print multidimensional hyperslabs of data, this tool was intended for point or one-dimensional reports.
虽然它可以用于打印多维数据超板，但此工具旨在用于点或一维报告。

Examples:
示例：

```bash
# surface air temperature and wind speed as a function of longitude, at the latitude closest to 30 degrees north
   ncksprt -v tsurf,wsurf -d lat,30. JAN1901.aijE001xyz.nc

# model variables t(i,j,l),q(i,j,l) at i=20 and j=10 for l=1 to l=5
   ncksprt -v t,q -d im,10 -d jm,10 -d lm,1,5 fort.2.nc  # netcdf dimension names are im,jm,lm in the restart file
```

<a id="hemis"></a>

## HOW-TO extract hemispheric/global means / 如何提取半球/全球平均值

To avoid making standalone programs understand the details of horizontal grids and area weightings, the model computes hemispheric and global means of accumulation quantities, saves these means in auxiliary arrays in acc-files, and defines auxiliary scaled output quantities having the suffix `_hemis`.
为了避免让独立程序理解水平网格和面积加权的细节，模型计算累加量的半球和全球平均值，将这些平均值保存在acc文件中的辅助数组中，并定义具有后缀`_hemis`的辅助缩放输出量。

These auxiliary outputs have a dimension name `shnhgm` of size 3 in addition to whatever other relevant dimensions they may possess.
这些辅助输出除了可能具有的其他相关维度外，还有一个大小为3的维度名称`shnhgm`。

The first position in the `shnhgm` dimension contains the southern hemisphere mean, the second the northern hemisphere, and the third the global mean.
`shnhgm`维度中的第一个位置包含南半球平均值，第二个包含北半球平均值，第三个包含全球平均值。

From an aij output file for example, the hemispheric and/or global means of surface air temperature can be printed using `ncksprt`
例如，从aij输出文件，可以使用`ncksprt`打印地表气温的半球和/或全球平均值

```bash
ncksprt -v tsurf_hemis JAN1901.aijE001xyz.nc
ncksprt -v tsurf_hemis -d shnhgm,3 JAN1901.aijE001xyz.nc # print global mean only
```

The `scaleacc` program defines the means of diagnostics which are ratios using the ratio of the means of the respective accumulations.
`scaleacc`程序使用各自累加平均值的比率来定义作为比率的诊断的平均值。

<a id="subdd"></a>

## HOW-TO write "subdaily" diagnostics in netcdf format / 如何以netcdf格式写入"亚日"诊断

(The reader is assumed to be familiar with the workings of the subdaily diagnostics code.)
（假定读者熟悉亚日诊断代码的工作原理。）

A line `#define NEW_IO_SUBDD` in the `Preprocessor Options` section of a rundeck is currently required to override the default output format for these diagnostics (one lat-lon slice per Fortran binary sequential-access record).
运行配置的`预处理器选项`部分中的一行`#define NEW_IO_SUBDD`当前是覆盖这些诊断的默认输出格式（每个Fortran二进制顺序访问记录一个经纬度切片）所必需的。

Note that this option currently requires that the model be built with parallel netcdf.
请注意，此选项当前要求使用parallel netcdf构建模型。

The default routine `write_data` outputs only one lat-lon slice per call; for simplicity/efficiency, an alternate interface `write_subdd` was introduced to allow output of 3- and higher-dimensional arrays in one call.
默认例程`write_data`每次调用仅输出一个经纬度切片；为了简单/效率，引入了备用接口`write_subdd`以允许在一次调用中输出3维及更高维度的数组。

The coding for the default format will soon be changed to use this interface.
默认格式的编码将很快更改为使用此接口。

<a id="add_diag"></a>

## HOW-TO add a new diagnostic to an existing category / 如何向现有类别添加新诊断

For the most part, postprocessing by standalone programs does not change the procedure.
在大多数情况下，通过独立程序进行后处理不会更改程序。

However, it does require attention to a few details that are sometimes overlooked.
然而，它确实需要注意有时被忽略的一些细节。

Firstly, the short names of output quantities must be accepted by the netcdf library: they must begin with an alphabetic character followed by zero or more alphanumeric characters (including underscores).
首先，输出量的短名称必须被netcdf库接受：它们必须以字母字符开头，后跟零个或多个字母数字字符（包括下划线）。

Secondly, for outputs that are ratios, a denominator must be stored somewhere in the accumulation array since it cannot be computed "on the fly" during postprocessing.
其次，对于作为比率的输出，必须在累加数组中的某处存储分母，因为它无法在后处理期间"即时"计算。

The metadata for the numerator should contain the index of the denominator.
分子的元数据应包含分母的索引。

Some categories of diagnostics in modelE (e.g. `aij,ajl`) are already scaled online using this denominator system, so there are examples to follow.
modelE中的某些诊断类别（例如`aij,ajl`）已经使用此分母系统进行在线缩放，因此有示例可循。

More challenging for standalone postprocessing are diagnostics that are declared locally within modelE print programs, or those having some meta-metadata not registered anywhere (e.g. which tracer outputs need division by gridcell area when most others don't, or vice versa).
对于独立后处理来说，更具挑战性的是在modelE打印程序中本地声明的诊断，或那些在任何地方都未注册某些元元数据的诊断（例如，哪些示踪物输出需要除以网格单元面积，而大多数不需要，反之亦然）。

The number of such special cases has declined recently and hopefully the trend will continue.
此类特殊情况的数量最近有所下降，希望这一趋势将继续。

Finally, for outputs that are simple functions of already-existing outputs, it may be more expedient to calculate/extract them using generic tools rather than adding new code to modelE.
最后，对于作为现有输出的简单函数的输出，使用通用工具计算/提取它们可能比向modelE添加新代码更高效便捷。

<a id="special_cat"></a>

## Special diagnostic calculations / 特殊诊断计算

Special-purpose programs for outputs not fitting the generic-postprocessing mold include:
不适合通用后处理模式的输出的专用程序包括：

- `agcstat`: calculates standing-eddy statistics, refractive indices, etc. from time-mean output, and places the results into the `agc` output file
  - `agcstat`：从时间平均输出计算驻波涡度统计、折射指数等，并将结果放入`agc`输出文件

- `prtostat`: prints selected ocean circulation statistics from time-mean output
  - `prtostat`：从时间平均输出打印选定的海洋环流统计

<a id="add_diag_cat"></a>

## HOW-TO add a new category of diagnostic / 如何添加新的诊断类别

Recipe to be written.
配方待写。

<a id="probs"></a>

## Troubleshooting / 故障排除

Known causes of aberrant behavior:
异常行为的已知原因：

- Application of `sumfiles/scaleacc` to acc-files residing in a mass-storage facility. Some facilities have commands to create temporary copies of slow-media (tape) files on higher-performance media. The coding of `sumfiles/scaleacc` assumes that once a file has been successfully opened, its contents will remain available during execution. Unfortunately, files can sometimes "disappear" before execution completes.
  - 将`sumfiles/scaleacc`应用于驻留在大容量存储设施中的acc文件。某些设施有命令在更高性能的媒体上创建慢速介质（磁带）文件的临时副本。`sumfiles/scaleacc`的编码假设一旦文件成功打开，其内容将在执行期间保持可用。不幸的是，文件有时会在执行完成前"消失"。

<a id="plotting"></a>

## Plotting options / 绘图选项

To be written.
待写。

<a id="rules"></a>

## How it works / 工作原理

Move mk_diags/conventions.txt here.
将mk_diags/conventions.txt移至此处。

<a id="local_info"></a>

## Local information / 本地信息

```
                       On Discover:
                       ------------

modelE standalone programs: /discover/nobackup/projects/giss/exec

netcdf GIC files in /discover/nobackup/projects/giss/prod_input_files:
                     GIC.E046D3M20A.1DEC1955.ext.nc  for 4x5    lat-lon resolution
                     GIC.144X90.DEC01.1.ext.nc           2x2.5  lat-lon resolution
                     GIC.288X180.DEC01.1.ext.nc          1x1.25 lat-lon resolution

PNETCDFHOME=/discover/nobackup/mkelley5/pnetcdf-1.2.0  (ifort 10.1.017, impi 3.2.011)

remap files: /discover/nobackup/mkelley5/remap_files

NCO programs: /usr/local/other/NCO/3.9.9_gcc/bin
```

**Document End / 文档结束**
