# Rundeck / Rundeck运行配置

A rundeck (a file with an extension .R) is a file which contains a complete description of a particular model run, including the description of model code used and run-time parameters.
rundeck（扩展名为.R的文件）是一个包含特定模型运行的完整描述的文件，包括所使用的模型代码描述和运行时参数。

Directory modelE/templates contains typical rundecks which can be used as examples.
目录modelE/templates包含典型的rundeck，可用作示例。

## Rundeck structure / Rundeck结构

Rundeck consists of a number of sections describing different aspects of the run.
rundeck由多个部分组成，描述运行的不同方面。

Each section starts with certain keywords (like "Object modules:") and terminates either with "End ..." statement or with the start of a new section.
每个部分以特定关键字开头（如"Object modules:"），并以"End ..."语句或新部分的开始结束。

The sections are supposed to follow in a pre-defined order and can't be interchanged, though some unneeded sections can be skipped.
这些部分应按预定义顺序排列，不可互换，但可以跳过某些不需要的部分。

The character `!` starts a comment.
字符`!`开始注释。

Everything to the right of `!` until the end of the line is ignored.
`!`右侧到行尾的所有内容都将被忽略。

Here is the list of rundeck sections in proper order:
以下是按正确顺序排列的rundeck部分列表：

* Run name and comment
  运行名称和注释
* Preprocessor Options
  预处理器选项
* Run Options
  运行选项
* Object modules
  对象模块
* Components
  组件
* Component Options
  组件选项
* Data input files
  数据输入文件
* Label and Namelist
  标签和Fortran名录
* Run-time parameters
  运行时参数
* Restart and timing parameters
  重启和计时参数

Any text after the last section is considered a comment and is ignored.
最后一部分之后的任何文本都被视为注释并被忽略。

## Run name and comment / 运行名称和注释

The first line of this section should start from the name of this rundeck (including .R) and contain short information on the run (no more than 80 characters).
此部分的第一行应以此rundeck的名称开头（包括.R），并包含关于运行的简短信息（不超过80个字符）。

The rest of this section is a comment.
此部分的其余内容是注释。

## Preprocessor Options / 预处理器选项

Starts with the line
以以下行开始

```
Preprocessor Options
```

and ends with the line
并以以下行结束

```
End Preprocessor Options
```

This section should contain all preprocessing definitions you want to be set in the code.
此部分应包含您想在代码中设置的所有预处理器定义。

Keep in mind that these preprocessing options are passed by means of creating a file rundeck_opts.h which is included from the source files.
请记住，这些预处理器选项是通过创建文件rundeck_opts.h来传递的，该文件从源文件中包含进来。

When adding preprocessing instructions to a source file one should make sure that rundeck_opts.h is included at the start of this file.
在向源文件添加预处理器指令时，应确保在此文件开头包含rundeck_opts.h。

## Run Options / 运行选项

Starts with the line
以以下行开始

```
Run Options
```

This section contains options for setting a proper environment before startting a model run.
此部分包含在启动模型运行之前设置适当环境的选项。

Only one option is currently supported:
目前仅支持一个选项：

```
STACKSIZE=<stack size in KB>
```

which sets a corresponding stack size.
它设置相应的堆栈大小。

Currenlty if the default stack size is bigger than the one requested this option is ignored.
当前，如果默认堆栈大小大于请求的大小，则忽略此选项。

## Object modules / 对象模块

Starts with a line
以以下行开始

```
Object modules:
```

This section lists all the source files from modelE/model which have to be compiled with current executable.
此部分列出了modelE/model中必须与当前可执行文件一起编译的所有源文件。

Only basename of these files should be given (no suffix).
应仅提供这些文件的基本名称（无后缀）。

If more than one source file with the same basename is present in modelE/model directory the search is done in the following order: `*.f`, `*.F90`, `*.c`.
如果在modelE/model目录中存在多个具有相同基本名称的源文件，则按以下顺序搜索：`*.f`、`*.F90`、`*.c`。

For each source file one can specify individual compilation options which will be appended to the compilation command.
对于每个源文件，可以指定单独的编译选项，这些选项将附加到编译命令中。

These options are specified between "||" after the file name, for example " MODELE |-O0 -g| ".
这些选项在文件名后的"||"之间指定，例如" MODELE |-O0 -g| "。

The files located inside "Components" should not be listed in this section.
位于"Components"内的文件不应在此部分列出。

## Components / 组件

Starts with a line
以以下行开始

```
Components:
```

This section lists all "Components" (the subdirectories of modelE/model) which have to be compiled with the executable.
此部分列出了必须与可执行文件一起编译的所有"组件"（modelE/model的子目录）。

Keep in mind that each Component will be compiled into a library which will be then linked with the main executable.
请记住，每个组件将被编译到一个库中，然后与主可执行文件链接。

As a result in a case of a name conflict (more than one subroutine with the same name is present) the preference will be given to the one located in modelE/model directory.
因此，在名称冲突的情况下（存在多个同名的子例程），将优先选择位于modelE/model目录中的那个。

## Component Options / 组件选项

Starts with a line
以以下行开始

```
Component Options:
```

This section lists specific options which have to be passed to certain components.
此部分列出了必须传递给某些组件的特定选项。

For each Component the options are listed on a single line as follows
对于每个组件，选项列在一行上，格式如下

```
OPTS_<ComponentName> = <Opt1>=<X> <Opt2>=<Y>
```

where Opt1, Opt2 are variabes to be set and X, Y are corresponding values.
其中Opt1、Opt2是要设置的变量，X、Y是对应的值。

The instruction above is equivalent to setting Opt1=X, Opt2=Y at the start of <ComponentName> Makefile.
上述指令等同于在<ComponentName> Makefile开头设置Opt1=X、Opt2=Y。

There is a special debugging option OVERWRITE_FSRCS which can be passed to any component (which uses base.mk).
有一个特殊的调试选项OVERWRITE_FSRCS，可以传递给任何组件（使用base.mk的组件）。

If this option is set to a list of source files, these files will be used when compiling the component (instead of the ones specified inside the component Makefile).
如果此选项设置为源文件列表，则在编译组件时将使用这些文件（而不是组件Makefile中指定的文件）。

The use of this option is discouraged for the production runs though (which should use the source files specified by the component itself).
不鼓励在生产运行中使用此选项（生产运行应使用组件本身指定的源文件）。

Similar option OVERWRITE_F90SRCS can be used to specify F90 files.
类似的选项OVERWRITE_F90SRCS可用于指定F90文件。

## Data input files / 数据输入文件

Starts with a line
以以下行开始

```
Data input files:
```

This section lists all the input files used by the current executable.
此部分列出了当前可执行文件使用的所有输入文件。

The files are listed in the form
文件以以下形式列出

```
<short_name>=<path to the actual file>
```

where <short_name> is the name of the file used in the code and <path to the actual file> is the path to the actual input file.
其中<short_name>是代码中使用的文件名，<path to the actual file>是实际输入文件的路径。

The pass is specified with respect to GCMSEARCHPATH directory, unless it starts with "/" in which case it is an absolute path.
路径是相对于GCMSEARCHPATH目录指定的，除非它以"/"开头，在这种情况下它是绝对路径。

## Label and Namelist / 标签和Fortran名录

Starts with a line
以以下行开始

```
Label and Namelist:
```

And consists of a single line which starts with the name of the run which is followed by a short description.
它由一行组成，以运行名称开头，后跟简短描述。

This section may follow by (now obsolete) instruction
此部分后面可以跟（现已过时的）指令

```
DTFIX=<time_step>
```

where <time_step> is a fall-back time step (s) which the model should use if it discovers internal instability.
其中<time_step>是回退时间步长（秒），如果模型发现内部不稳定，应使用该步长。

## Run-time parameters / 运行时参数

Starts with a line
以以下行开始

```
&&PARAMETERS
```

and ends with a line
并以以下行结束

```
&&END_PARAMETERS
```

This section contains all run-time parameters which have to be passed to the model.
此部分包含必须传递给模型的所有运行时参数。

Parameters shoud be listed one per line in the form
参数应每行一个，以以下形式列出

```
<param_name>=<param_value>
```

where <param_name> is the name of the parameter as it is used in the model code.
其中<param_name>是参数在模型代码中使用的名称。

<param_value> is its numerical value.
<param_value>是其数值。

In case of an array <param_value> is a coma-separated list of values.
对于数组，<param_value>是逗号分隔的值列表。

Values should be of the same type as the parameter they are assigned to (as it is declared in the model code).
值应与分配给的参数类型相同（如在模型代码中声明的）。

## Restart and timing parameters / 重启和计时参数

Starts with a line
以以下行开始

```
&INPUTZ
```

This section contains the fortran namelist for the timing and restart parameters.
此部分包含计时和重启参数的Fortran名录（namelist）。

By default these should be set to start the model from some kind of initial conditions and run it for one hour of model time (for "make setup ...").
默认情况下，这些应设置为从某种初始条件启动模型，并运行一小时模型时间（用于"make setup ..."）。

**Document End / 文档结束**
