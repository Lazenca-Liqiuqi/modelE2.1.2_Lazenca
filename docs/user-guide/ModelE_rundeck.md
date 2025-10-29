# ModelE rundeck / ModelE运行配置

**A rundeck (a file with an extension .R) is a file which contains a complete description of a particular model run, including the description of model code used and run-time parameters. Directory modelE/templates contains typical rundecks which can be used as examples.**

rundeck（扩展名为.R的文件）是包含特定模型运行完整描述的文件，包括所用模型代码的描述和运行时参数。modelE/templates目录包含可用作示例的典型rundeck。

## Rundeck structure / Rundeck结构

**Rundeck consists of a number of sections describing different aspects of the run. Each section starts with certain keywords (like "Object modules:") and terminates either with "End ..." statement or with the start of a new section. The sections are supposed to follow in a pre-defined order and can't be interchanged, though some unneeded sections can be skipped. The character ! starts a comment. Everything to the right of ! until the end of the line is ignored. Here is the list of rundeck sections in proper order:**

rundeck由多个描述运行不同方面的部分组成。每个部分以特定关键字开始（如"Object modules:"），并以"End ..."语句或新部分的开始终止。这些部分应按预定义顺序排列，不能互换，但可以跳过一些不需要的部分。字符!开始注释。!右侧直到行尾的所有内容都被忽略。以下是rundeck部分的正确顺序列表：

- **Run name and comment** / 运行名称和注释
- **Preprocessor Options** / 预处理选项
- **Run Options** / 运行选项
- **Object modules** / 对象模块
- **Components** / 组件
- **Component Options** / 组件选项
- **Data input files** / 数据输入文件
- **Label and Namelist** / 标签和Namelist
- **Run-time parameters** / 运行时参数
- **Restart and timing parameters** / 重启和时间参数

**Any text after the last section is considered a comment and is ignored.**

最后一个部分之后的任何文本都被视为注释并被忽略。

## Run name and comment / 运行名称和注释

**The first line of this section should start from the name of this rundeck (including .R) and contain short information on the run (no more than 80 characters). The rest of this section is a comment.**

此部分的第一行应从此rundeck的名称开始（包括.R），并包含关于运行的简短信息（不超过80个字符）。此部分的其余部分是注释。

## Preprocessor Options / 预处理选项

**Starts with the line**

```bash
Preprocessor Options
```

**and ends with the line**

```bash
End Preprocessor Options
```

**This section should contain all preprocessing definitions you want to be set in the code. Keep in mind that these preprocessing options are passed by means of creating a file rundeck_opts.h which is included from the source files. When adding preprocessing instructions to a source file one should make sure that rundeck_opts.h is included at the start of this file.**

此部分应包含要在代码中设置的所有预处理定义。请记住，这些预处理选项通过创建包含在源文件中的rundeck_opts.h文件来传递。在向源文件添加预处理指令时，应确保在此文件开头包含rundeck_opts.h。

## Run Options / 运行选项

**Starts with the line**

```bash
Run Options
```

**This section contains options for setting a proper environment before starting a model run. Only one option is currently supported:**

```bash
STACKSIZE=<stack size in KB>
```

**which sets a corresponding stack size. Currently if the default stack size is bigger than the one requested this option is ignored.**

此部分包含在启动模型运行之前设置适当环境的选项。目前只支持一个选项：

```bash
STACKSIZE=<栈大小（KB）>
```

用于设置相应的栈大小。如果默认栈大小大于请求的大小，则当前此选项被忽略。

## Object modules / 对象模块

**Starts with a line**

```bash
Object modules:
```

**This section lists all the source files from modelE/model which have to be compiled with current executable. Only basename of these files should be given (no suffix). If more than one source file with the same basename is present in modelE/model directory the search is done in the following order: *.f, *.F90, *.c. For each source file one can specify individual compilation options which will be appended to the compilation command. These options are specified between "||" after the file name, for example " MODELE |-O0 -g| ". The files located inside "Components" should not be listed in this section.**

此部分列出了必须与当前可执行文件一起编译的modelE/model的所有源文件。应只给出这些文件的基本名称（无后缀）。如果modelE/model目录中存在多个具有相同基本名的源文件，搜索按以下顺序进行：*.f、*.F90、*.c。对于每个源文件，可以指定将附加到编译命令的单独编译选项。这些选项在文件名后的"||"之间指定，例如" MODELE |-O0 -g| "。位于"Components"内的文件不应在此部分列出。

## Components / 组件

**Starts with a line**

```bash
Components:
```

**This section lists all "Components" (the subdirectories of modelE/model) which have to be compiled with the executable. Keep in mind that each Component will be compiled into a library which will then be linked with the main executable. As a result in a case of a name conflict (more than one subroutine with the same name is present) the preference will be given to the one located in modelE/model directory.**

此部分列出了必须与可执行文件一起编译的所有"Components"（modelE/model的子目录）。请记住，每个组件将被编译成一个库，然后与主可执行文件链接。在名称冲突的情况下（存在多个同名的子例程），优先选择位于modelE/model目录中的那个。

## Component Options / 组件选项

**Starts with a line**

```bash
Component Options:
```

**This section lists specific options which have to be passed to certain components. For each Component the options are listed on a single line as follows**

```bash
OPTS_<ComponentName> = <Opt1>=<X> <Opt2>=<Y>
```

**where Opt1, Opt2 are variables to be set and X, Y are corresponding values. The instruction above is equivalent to setting Opt1=X, Opt2=Y at the start of `<ComponentName>` Makefile.**

此部分列出了必须传递给特定组件的特定选项。对于每个组件，选项在单行上列出，格式如下：

```bash
OPTS_<组件名> = <选项1>=<值X> <选项2>=<值Y>
```

其中Opt1、Opt2是要设置的变量，X、Y是对应的值。上述指令等同于在`<组件名>`Makefile开头设置Opt1=X、Opt2=Y。

**There is a special debugging option OVERWRITE_FSRCS which can be passed to any component (which uses base.mk). If this option is set to a list of source files, these files will be used when compiling the component (instead of the ones specified inside the component Makefile). The use of this option is discouraged for the production runs though (which should use the source files specified by the component itself). Similar option OVERWRITE_F90SRCS can be used to specify F90 files.**

有一个特殊的调试选项OVERWRITE_FSRCS可以传递给任何使用base.mk的组件。如果此选项设置为源文件列表，则在编译组件时将使用这些文件（而不是组件Makefile中指定的文件）。不过，不鼓励在生产运行中使用此选项（应使用组件本身指定的源文件）。可以使用类似的选项OVERWRITE_F90SRCS来指定F90文件。

## Data input files / 数据输入文件

**Starts with a line**

```bash
Data input files:
```

**This section lists all the input files used by the current executable. The files are listed in the form**

```bash
<short_name>=<path to the actual file>
```

**where `<short_name>` is the name of the file used in the code and `<path to the actual file>` is the path to the actual input file. The path is specified with respect to GCMSEARCHPATH directory, unless it starts with "/" in which case it is an absolute path.**

此部分列出了当前可执行文件使用的所有输入文件。文件以以下形式列出：

```bash
<短名称>=<实际文件路径>
```

其中`<短名称>`是代码中使用的文件名，`<实际文件路径>`是实际输入文件的路径。路径是相对于GCMSEARCHPATH目录指定的，除非以"/"开头，在这种情况下它是绝对路径。

## Label and Namelist / 标签和Namelist

**Starts with a line**

```bash
Label and Namelist:
```

**And consists of a single line which starts with the name of the run which is followed by a short description.**

由单行组成，以运行名称开始，后跟简短描述。

**This section may follow by (now obsolete) instruction**

```bash
DTFIX=<time_step>
```

**where `<time_step>` is a fall-back time step (s) which the model should use if it discovers internal instability.**

此部分后面可以跟（现已过时的）指令：

```bash
DTFIX=<时间步>
```

其中`<时间步>`是模型在发现内部不稳定性时应使用的回退时间步（秒）。

## Run-time parameters / 运行时参数

**Starts with a line**

```bash
&&PARAMETERS
```

**and ends with a line**

```bash
&&END_PARAMETERS
```

**This section contains all run-time parameters which have to be passed to the model. Parameters should be listed one per line in the form**

```bash
<param_name>=<param_value>
```

**where `<param_name>` is the name of the parameter as it is used in the model code. `<param_value>` is its numerical value. In case of an array `<param_value>` is a comma-separated list of values. Values should be of the same type as the parameter they are assigned to (as it is declared in the model code).**

此部分包含必须传递给模型的所有运行时参数。参数应每行列出一个，格式为：

```bash
<参数名>=<参数值>
```

其中`<参数名>`是模型代码中使用的参数名称。`<参数值>`是其数值。如果是数组，`<参数值>`是逗号分隔的值列表。值的类型应与分配给的参数类型相同（如在模型代码中声明的）。

## Restart and timing parameters / 重启和时间参数

**Starts with a line**

```bash
&INPUTZ
```

**This section contains the fortran namelist for the timing and restart parameters. By default these should be set to start the model from some kind of initial conditions and run it for one hour of model time (for "make setup ...").**

此部分包含时间和重启参数的fortran namelist。默认情况下，这些应设置为从某种初始条件启动模型，并运行一个小时的模型时间（用于"make setup ..."）。