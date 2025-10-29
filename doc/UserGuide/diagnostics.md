# diagnostics / 诊断系统

## Part II: Getting information from the diagnostics / 第二部分：从诊断输出中获取信息

### 1) HOW-TO look at the output / 如何查看输出

**You can look at the output in two distinct ways: using the run-time printout, or using the post-processing program, pdE.**
您可以通过两种不同的方式查看输出：使用运行时打印输出，或使用后处理程序pdE。

**1. The run-time printout.**
**1. 运行时打印输出。**

**If you run the model using 'runE' (as opposed to 'runE -q' which suppresses the printout) the model will produce a $RUNID.PRT file which can contain copious amounts of diagnostic information. It is split into a number of sections: (see next question for a list). This is produced each month (but can be controlled using the KDIAG switches and NMONAV in the NAMELIST).**
如果您使用'runE'运行模型（而不是抑制打印输出的'runE -q'），模型将生成一个$RUNID.PRT文件，该文件可以包含大量的诊断信息。它被分为多个部分：（列表请参见下一个问题）。这是每个月产生的（但可以通过NAMELIST中的KDIAG开关和NMONAV来控制）。

**2. Post-processed output:**
**2. 后处理输出：**

**Each month the program produces an 'acc' accumulated diagnostics file which contains all of the diagnostic information from the previous month. The program 'pdE' (in the exec directory) is an alternate entry point into the model that reads in any number of these files and a) creates a printout (as above) for the time period concerned and b) creates binary output of many more diagnostics. This can be used simply to recreate the monthly printout, but also to create longer term means (annual, seasonal, monthly climatologies etc.).**
程序每个月会产生一个'acc'累积诊断文件，其中包含上个月的所有诊断信息。程序'pdE'（在exec目录中）是模型的另一个入口点，它读取任意数量的这些文件并a)为相关时间段创建打印输出（如上所述）和b)创建更多诊断的二进制输出。这可以简单地用于重新创建月度打印输出，但也可以用于创建更长期平均值（年度、季节、月度气候学等）。

**For example, to recreate the printout in /u/cmrun/$RUNID;**
**例如，要在/u/cmrun/$RUNID中重新创建打印输出；**

```bash
for a single month: pdE $RUNID JAN1987.acc$RUNID
for all Januaries:  pdE $RUNID JAN*.acc$RUNID
for a whole year:   pdE $RUNID *1987.acc$RUNID
```

- **单个月份**：`pdE $RUNID JAN1987.acc$RUNID`
- **所有一月份**：`pdE $RUNID JAN*.acc$RUNID`
- **整年**：`pdE $RUNID *1987.acc$RUNID`

**For pdE to work properly, the directory /u/cmrun/$RUNID has to exist and contain at least ${RUNID}ln  ${RUNID}uln  ${RUNID}.exe . The output files will end up in the PRESENT WORKING DIRECTORY which may be /u/cmrun/$RUNID or any other directory; names and order of the inputfiles are irrelevant (as long as the format of the files is compatible with the model ${RUNID}).**
为了使pdE正常工作，目录/u/cmrun/$RUNID必须存在并且至少包含${RUNID}ln ${RUNID}uln ${RUNID}.exe。输出文件将最终位于当前工作目录中，该目录可以是/u/cmrun/$RUNID或任何其他目录；输入文件的名称和顺序是无关紧要的（只要文件的格式与模型${RUNID}兼容）。

**It is possible to use pdE to average acc-files from several runs, e.g. average over an ensemble of runs. Although the numbers that are produced are fine, subroutine aPERIOD will not be able to create the proper labels: the runID will be taken from the last file that was read in and the number of runs averaged will be interpreted as successive years, so averaging years 1951-1955 of runs runA runB runC runD will produce the label ANN1951-1970.runD rather than ANN1951-1955.runA-D. Some titles will also suffer from that 'bug', but it should be easy to fix it manually afterwards, if anybody cares.**
可以使用pdE来平均来自多次运行的acc文件，例如对集合运行进行平均。虽然产生的数字是正确的，但子程序aPERIOD将无法创建正确的标签：runID将从最后读取的文件中获取，平均的运行次数将被解释为连续的年份，因此平均运行runA runB runC runD的1951-1955年将产生标签ANN1951-1970.runD而不是ANN1951-1955.runA-D。一些标题也会受到这个'bug'的影响，但如果有人在意，应该很容易在之后手动修复。

**Note that the output can be controlled (a little) by the settings in 'Ipd' (which is created if it does not yet exist in the present working directory). A number of files will be created whose names contain the accumulated time period. (monyear[-year] where mon is a 3-letter acronym for a period of 1-12 consecutive months).**
请注意，输出可以通过'Ipd'中的设置来（稍微）控制（如果在当前工作目录中尚不存在，则会创建它）。将创建多个文件，其名称包含累积时间段。（monyear[-year]，其中mon是1-12个连续月份的时间段的3字母缩写）。

```
        monyear.PRT      the printout
        monyear.j$RUNID  zonal budget pages (ASCII Aplot format)
        monyear.jk$RUNID latitude-height binary file
        monyear.il$RUNID longitude-height binary file
        monyear.ij$RUNID lat-lon binary file
        monyear.wp$RUNID Wave power binary file
        monyear.oij$RUNID lat-lon binary file for ocean diagnostics
        monyear.ojl$RUNID lat-depth binary file for ocean diagnostics
        monyear.oht$RUNID lat ASCII file for ocean heat transports
```

**文件说明：**
- **monyear.PRT**：打印输出文件
- **monyear.j$RUNID**：纬向预算页（ASCII Aplot格式）
- **monyear.jk$RUNID**：纬度-高度二进制文件
- **monyear.il$RUNID**：经度-高度二进制文件
- **monyear.ij$RUNID**：纬度-经度二进制文件
- **monyear.wp$RUNID**：波功率二进制文件
- **monyear.oij$RUNID**：海洋诊断的纬度-经度二进制文件
- **monyear.ojl$RUNID**：海洋诊断的纬度-深度二进制文件
- **monyear.oht$RUNID**：海洋热量传输的纬度ASCII文件

**which can be read using the appropriate graphical software.**
**可以使用适当的图形软件读取这些文件。**

### 2) HOW-TO change what is included in the printout / 如何更改打印输出中包含的内容

**The switches KDIAG which are set in the NAMELIST control which subgroups of diagnostics are calculated and output. At present, there is no simple way to pick and choose exactly which diagnostics appear, although we are working on a scheme to do just that. Some of the following options are rarely used, and may soon be made obsolete. These switches can also be used in 'Ipd' input for pdE to control which output to produce. If QDIAG=.true. some binary files are created accompanying the printed output. If QDIAG_ratios=.true. fields which are the products of q1 and q2 and whose titles are of the form "q1 x q2" are replaced by the ratios field/q2, the title being shortened to "q1" (default).**
在NAMELIST中设置的开关KDIAG控制计算和输出哪些诊断子组。目前，没有简单的方法来精确选择哪些诊断出现，尽管我们正在开发一个方案来做到这一点。以下一些选项很少使用，可能很快就会被淘汰。这些开关也可以用于pdE的'Ipd'输入中，以控制产生哪些输出。如果QDIAG=.true.，会创建一些二进制文件伴随打印输出。如果QDIAG_ratios=.true.，那些是q1和q2乘积且标题形式为"q1 x q2"的字段将被替换为比值field/q2，标题缩短为"q1"（默认值）。

**Current options are:**
**当前选项有：**

```
KDIAG(1)  < 9 print Zonal/Regional budget pages
   = 8 only print regional diagnostics
   2-7 only print global zonal means
   = 1 print all zonal diagnostics

KDIAG(2)  = 0 print Latitude-height diagnostics
          = 1 print at most fields listed in file Ijk
              (rearranging the lines of Ijk has no effect)
          = 8 Only print spectral analysis of standing eddies
          = 9 skip all Latitude-height diagnostics
          2-7 same as 1

KDIAG(3)  = 0 standard printout, all binary files if QDIAG=.true.
          = 1 ij-fields as in list Iij, all ijk-fields
          = 2 ij and ijk fields are handled according to list Iij
          = 7 ij-fields as in list Iij, no ijk-fields are produced
          = 8 full list Iij of available fields is produced; this list may
              be edited : don't touch lines starting with 'List' or 'list'
                          you may delete any other lines
                          you may rearrange the remaining ij-fields
                          you may add blank maplets
          = 9 no ij and ijk diagnostics are produced
          3-6 same as 2

KDIAG(4)  < 9 print time history table of energies
KDIAG(5)  < 9 print spectral analysis tables

KDIAG(6)  < 9 print diurnal cycle diagnostics at selected points (up to 4)
          1-4 print out for first 4-KDIAG(6) points (will soon be obsolete)
        -1 - -4 print out for -KDIAG(6) point only.

KDIAG(7)  < 9 print wave power tables

KDIAG(8)  < 9 print tracer diagnostics
          = 0 print all tracer diagnostics
          = 1 skip lat/lon tracer diagnostics
          = 2 skip tracer conservation diagnostics and lat/lon diagnostics

KDIAG(9)  < 9 print out conservation diagnostics
KDIAG(10) < 9 print out Longitude-height diagnostics
KDIAG(11) < 9 print out river runoff diagnostics
KDIAG(12) < 9 print out ocean diagnostics (if there is an ocean)
```

**KDIAG参数说明：**
- **KDIAG(1)**：控制纬向/区域预算页输出
  - `< 9`：打印纬向/区域预算页
  - `= 8`：仅打印区域诊断
  - `2-7`：仅打印全球纬向平均值
  - `= 1`：打印所有纬向诊断

- **KDIAG(2)**：控制纬度-高度诊断输出
  - `= 0`：打印纬度-高度诊断
  - `= 1`：最多打印文件Ijk中列出的字段（重新排列Ijk的行没有影响）
  - `= 8`：仅打印驻涡谱分析
  - `= 9`：跳过所有纬度-高度诊断
  - `2-7`：与1相同

- **KDIAG(3)**：控制ij和ijk字段输出
  - `= 0`：标准打印输出，如果QDIAG=.true.则输出所有二进制文件
  - `= 1`：ij字段如列表Iij所示，所有ijk字段
  - `= 2`：ij和ijk字段根据列表Iij处理
  - `= 7`：ij字段如列表Iij所示，不产生ijk字段
  - `= 8`：产生可用字段的完整列表Iij；此列表可能被编辑：不要触碰以'List'或'list'开头的行，您可以删除任何其他行，您可以重新排列剩余的ij字段，您可以添加空白小地图
  - `= 9`：不产生ij和ijk诊断
  - `3-6`：与2相同

- **KDIAG(4)**：`< 9` 打印能量时间历史表
- **KDIAG(5)**：`< 9` 打印谱分析表

- **KDIAG(6)**：控制日循环诊断输出
  - `< 9`：在选定点（最多4个）打印日循环诊断
  - `1-4`：为前4-KDIAG(6)个点打印输出（将很快过时）
  - `-1 - -4`：仅为-KDIAG(6)个点打印输出

- **KDIAG(7)**：`< 9` 打印波功率表

- **KDIAG(8)**：控制示踪物诊断输出
  - `< 9`：打印示踪物诊断
  - `= 0`：打印所有示踪物诊断
  - `= 1`：跳过纬度/经度示踪物诊断
  - `= 2`：跳过示踪物守恒诊断和纬度/经度诊断

- **KDIAG(9)**：`< 9` 打印守恒诊断
- **KDIAG(10)**：`< 9` 打印经度-高度诊断
- **KDIAG(11)**：`< 9` 打印河流径流诊断
- **KDIAG(12)**：`< 9` 打印海洋诊断（如果存在海洋）

**There is also one section of special lat-lon diagnostics which can be optionally accumulated and output. These are the isccp_diags which calculate some cloud properties as if they were being observed by satellite. This is set as an option in the rundeck (isccp_diags=1) to calculate them. By default these diags are not calculated.**
还有一个特殊的纬度-经度诊断部分，可以选择性累积和输出。这些是isccp_diags，它们计算一些云属性，就好像它们正被卫星观测一样。这在rundeck（运行配置）中设置为一个选项（isccp_diags=1）来计算它们。默认情况下，这些诊断不被计算。

### 3) HOW-TO produce daily/monthly or seasonal diagnostics / 如何产生日/月或季节性诊断

**Controlling the frequency of output of the ACC files is done using the NAMELIST parameter NMONAV. This sets the number of months over which the diagnostics is accumulated. If it is set to 3, seasonal acc files are produced. If set to 12, you will get annual means. Higher numbers could be chosen, but are probably not very useful.**
控制ACC文件的输出频率是使用NAMELIST参数NMONAV完成的。这设置了诊断累积的月数。如果设置为3，则产生季节性acc文件。如果设置为12，您将获得年度平均值。可以选择更高的数字，但可能不是很有用。

**Producing more frequent diagnostics is controlled by the SUBDAILY module. The frequency of saving is controlled by the variable Nsubdd which is the number of internal timesteps between each snapshot (i.e. Nsubdd=1 implies diags every timestep, =24 daily (if dtsrc=3600), =48 is daily for dtsrc=1800). The variables saved are controlled by the strings SUBDD, SUBDD1, which are space seperated lists of names for the required diagnostics. These are currently limited to instantaneous values (with some exceptions as noted below) of some standard fields (SLP, PS, SAT, PREC, QS, LCLD, MCLD, HCLD, PTRO QLAT, QSEN, SWD, SWU, LWD, LWU, LWT, STX, STY, ICEF, SNOWD, TCLD, SST, SIT, US, VS, TMIN, TMAX), the geopotential height, relative and specific humidity and temperature on any (or all) of the following fixed pressure levels (if available): 1000, 850, 700, 500, 300, 100, 30 , 10, 3.4, 0.7, .16, .07, .03, and velocities on any model level. The fixed pressure level diags are set using Z850, R700 and T100, for instance, to request the 850 mb geopotential height, 700 mb relative humidity and 100 mb temperatures, respectively. Requests for ZALL or TALL, will produce individual files of all available levels. The velocities are set using U1, U5, U12, for instance, to get the 1st, 5th and 12th layer U velocities, respectively. If "ALL" levels are requested for a velocity, only one file per variable will be output, containing all requested levels. To limit the number of output levels, set the LmaxSUBDD parameter in the rundeck, and only levels L=1,LmaxSUBDD will be output.**
产生更频繁的诊断由SUBDAILY模块控制。保存频率由变量Nsubdd控制，这是每个快照之间的内部时间步数（即Nsubdd=1表示每个时间步都有诊断，=24表示每日（如果dtsrc=3600），=48表示dtsrc=1800时的每日）。保存的变量由字符串SUBDD, SUBDD1控制，这些是所需诊断名称的空格分隔列表。目前这些仅限于某些标准字段的瞬时值（如下面注意到的一些例外）（SLP, PS, SAT, PREC, QS, LCLD, MCLD, HCLD, PTRO QLAT, QSEN, SWD, SWU, LWD, LWU, LWT, STX, STY, ICEF, SNOWD, TCLD, SST, SIT, US, VS, TMIN, TMAX），在以下固定气压层（如果可用）上的位势高度、相对湿度和比湿度及温度：1000, 850, 700, 500, 300, 100, 30, 10, 3.4, 0.7, .16, .07, .03，以及任何模型层的速度。固定气压层诊断使用Z850, R700和T100设置，例如，分别请求850 mb位势高度、700 mb相对湿度和100 mb温度。对ZALL或TALL的请求将产生所有可用层的单独文件。速度使用U1, U5, U12设置，例如，分别获取第1、第5和第12层的U速度。如果为速度请求"ALL"层，每个变量只会输出一个文件，包含所有请求的层。为了限制输出层的数量，在rundeck（运行配置）中设置LmaxSUBDD参数，只有L=1,LmaxSUBDD的层将被输出。

**More options can be added as cases in subroutine get_subdd in DIAG.f if required. For example, including the following string in the rundeck (i.e. SUBDD="SLP SAT Z500 R850 U5 V5" will produce diags of the sea level pressure, surface air temperature, 500mb geopotential heights, 850 mb level relative humidity and the 5th layer U, and V fields. Each timeseries will be output one month at a time in files named SLPmmmyyyy and SATmmmyyyy (for example) for each month and year. Restarts will find the appropriate file and continue to append records as would be expected.**
如果需要，可以在DIAG.f的子程序get_subdd中添加更多选项作为情况。例如，在rundeck（运行配置）中包含以下字符串（即SUBDD="SLP SAT Z500 R850 U5 V5"将产生海平面气压、表面气温、500mb位势高度、850 mb层相对湿度和第5层U和V场的诊断。每个时间序列将在每个月输出一次，在名为SLPmmmyyyy和SATmmmyyyy（例如）的文件中，对应每个月和年份。重启将找到相应的文件并继续追加记录，正如预期的那样。

**There are three minor special cases to the procedure outlined above. i) PREC will give the accumulated precipitation over the Nsubdd period. ii) TMIN and TMAX are the minimum and maximum daily composite surface air temperatures at each grid point, and therefore can only be output once a day. Note that Nsubdd must divide into the daily number of internal timesteps for this to work properly. i.e. if dtsrc=1800s, there are 48 internal time steps per day. If Nsubdd=6 (denoting 3 hourly output), TMIN and TMAX will be output correctly at midnight UTC once a day. However, if Nsubdd=5 (2.5 hourly output), TMIN and TMAX will only be output every five days as the output hour coincides with midnight UTC.**
上述过程有三个小的特殊情况。i) PREC将给出Nsubdd期间的累积降水量。ii) TMIN和TMAX是每个网格点日合成表面气温的最小值和最大值，因此只能每天输出一次。注意Nsubdd必须能整除每天的内部时间步数才能正常工作。即如果dtsrc=1800s，每天有48个内部时间步。如果Nsubdd=6（表示3小时输出），TMIN和TMAX将在UTC午夜每天正确输出一次。但是，如果Nsubdd=5（2.5小时输出），TMIN和TMAX将每五天才输出一次，因为输出小时与UTC午夜重合。

**You can easily keep track of the running average of all the printout diagnostics using the NIPRNT switch in the parameter database. By setting this to a positive number, the diagnostics will be printed out that number of hours. (i.e. setting NIPRNT=10, will print out the running average of the accumulated diagnostics at the end of each of the next ten hours).**
您可以使用参数数据库中的NIPRNT开关轻松跟踪所有打印诊断的运行平均值。通过将其设置为正数n，诊断将每小时输出一次，持续n小时。（即设置NIPRNT=10，将在接下来十个小时的每个小时结束时打印累积诊断的运行平均值）。

### 4) HOW-TO control the format of the binary output (i.e. GISS/netcdf/hdf etc.) / 如何控制二进制输出的格式（即GISS/netcdf/hdf等）

**The binary output created from 'pdE' can be in a number of formats. Currently there are two options, the traditional GISS formats, and netcdf output. This is set by choosing to compile the model with POUT (for GISS-style output) or POUT_netcdf (for netcdf output). This is set in the rundeck. Note that the choice is made AT THE TIME OF COMPILATION OF THE MODEL EXECTUABLE. If you subsequently change your mind, you must edit the rundeck and recreate the executable (using 'gmake exe RUN=E001xyz').**
从'pdE'创建的二进制输出可以有多种格式。目前有两个选项，传统的GISS格式和netcdf输出。这是通过选择使用POUT（用于GISS风格输出）或POUT_netcdf（用于netcdf输出）编译模型来设置的。这在rundeck（运行配置）中设置。注意，这个选择是在模型可执行文件编译时做出的。如果您随后改变主意，必须编辑rundeck（运行配置）并重新创建可执行文件（使用'gmake exe RUN=E001xyz'）。

**Other formats (HDF?) could be defined as you like with a suitable POUT_xyz.f file.**
**其他格式（HDF？）可以根据您的喜好用适当的POUT_xyz.f文件定义。**

### 5) HOW-TO calculate a model score / 如何计算模型评分

**There is an RMS.f program in the aux/ directory which calculates a 'score' for a model run based on the RMS difference with some selected observations. Additionally, it calculates the Arcsin Mielke score (AMS), which is a non-dimensional statistic (between -1,1 (1 being perfect)) which also includes effects of mean bias and variance. It is compiled whenever the 'gmake aux RUN=....' command is run. Like CMPE001 or qc, it is technically model dependent (since it uses im,jm etc.), but in practice you will not need to recompile it for every version. The executable will be put into the RUNNAME_bin directory (i.e. for gmake aux RUN=E001xyz, the executable will be E001xyz_bin/RMS). Running RMS on its own gives its usage.**
在aux/目录中有一个RMS.f程序，它基于与某些选定观测的RMS差异计算模型运行的'评分'。此外，它计算Arcsin Mielke评分（AMS），这是一个无量纲统计量（在-1,1之间（1为完美）），也包括平均偏差和方差的影响。每当运行'gmake aux RUN=....'命令时它就会被编译。像CMPE001或qc一样，它在技术上依赖于模型（因为它使用im,jm等），但实际上您不需要为每个版本重新编译它。可执行文件将被放入RUNNAME_bin目录中（即对于gmake aux RUN=E001xyz，可执行文件将是E001xyz_bin/RMS）。单独运行RMS会给出其用法。

**You should produce diagnostic files over at least a five year mean. So for a particular run, use pdE to create the JAN and JUL averages**
**您应该产生至少五年平均的诊断文件。因此对于特定运行，使用pdE创建一月和七月的平均值**

```bash
      cd E001xyz
      pdE E001xyz JAN195[1-5].accE001xyz    # => JAN1951-1955.ijE001xyz
      pdE E001xyz JUL195[1-5].accE001xyz    # => JUL1951-1955.ijE001xyz
```

**Make sure that the TOPO file is linked:**
**确保TOPO文件已链接：**

```bash
      E001xyzln
```

**and then run RMS**
**然后运行RMS**

```bash
      ~/modelE/decks/E001xyz_bin/RMS E001xyz JAN1951-1955.ijE001xyz JUL1951-1955.ijE001xyz
```

**This will create files 'E001xyz' in the directories /u/cmrun/modelE/RMS and /u/cmrun/modelE/AMS, which contain the RMS statistics and the Arcsin Mielke score for each selected field,respectively. You can then compare these scores with other existing versions.**
这将在目录/u/cmrun/modelE/RMS和/u/cmrun/modelE/AMS中创建文件'E001xyz'，分别包含每个选定字段的RMS统计和Arcsin Mielke评分。然后您可以将这些评分与其他现有版本进行比较。
