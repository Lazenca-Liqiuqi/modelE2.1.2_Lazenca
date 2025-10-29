# Running the model / 运行模型

**The standard way to run modelE is to start it first from the initial conditions, run it for one hour of model time, let it write the checkpoint file and stop. After this one is supposed to check the log file to make sure that the model behaves properly and then one can restart it for a longer run. While running, the model periodically writes a checkpoint file, so that if it is stopped or killed by a system, it can be restarted from this checkpoint to continue the execution. Both ending times (for initial short run and for a longer run) are specified in the rundeck in the section with `INPUTZ` namelist parameters. The ending time for a short run is specified on a line which starts with `ISTART=`, the ending time for a longer run is specified on the line above it.**

运行modelE的标准方式是首先从初始条件启动，运行一个小时的模型时间，让其写入检查点文件（用于重启）然后停止。之后应该检查日志文件以确保模型行为正常，然后可以重启动进行更长时间的运行。在运行过程中，模型会定期写入检查点文件，因此如果模型被停止或被系统终止，可以从这个检查点重启动继续执行。结束时间（初始短运行和长时间运行）都在rundeck中`INPUTZ` 参数名录节（Namelist）中指定。短运行的结束时间在以`ISTART=`开头的行上指定，长时间运行的结束时间在紧邻上一行指定。

**ModelE source repository provides a simple script for starting the model runs: `modelE/exec/runE`. This script provides enough functionality to run the model on personal computes (desktops and laptops), but when working on a supercomputer one typically has to submit the runs as batch jobs (since MPI jobs are not allowed to run interactively). This functionality depends on a particular architecture and a special script has to be written for each such computer. You have to check local information for a particular computer to see which scripts are available there.**

ModelE源代码库提供了一个启动模型运行的简单脚本：`modelE/exec/runE`。这个脚本提供了足够的功能来在个人计算机（台式机和笔记本电脑）上运行模型，但在超级计算机上工作时，通常必须将运行作为批处理作业提交（因为不允许交互式运行MPI作业）。这个功能取决于特定的架构，必须为每台这样的计算机编写专门的脚本。请参考所用计算机的本地使用说明，以了解有哪些可用脚本。

## Using `runE` script / 使用 `runE` 脚本

**The command to start a model run**

```bash
runE <RunID> [-np NP] [-t time] [-cold-restart] [-d] [-q] [-l logfile] [-s tag]
```

**启动模型运行的命令**

```bash
runE <RunID> [-np NP] [-t time] [-cold-restart] [-d] [-q] [-l logfile] [-s tag]
```

**Here `<RunID>` is the name of your run (rundeck name without `.R`). The script accepts the following options:**

这里`<RunID>`是您的运行名称（不带`.R`的rundeck名称）。该脚本接受以下选项：

**`-np NP`**: Run the model in parallel with `NP` MPI threads.

使用`NP`个MPI进程并行运行模型。

**`-t time`**: Specify the execution time `time` to be used in `QSUB_STRING` (see below). Otherwise does not take effect.

指定要在`QSUB_STRING`中使用的执行时间`time`（见下文）。否则不生效。

**`-cold-restart`**: Start the run from the initial conditions. If not specified the run will be restarted from the latest checkpoint.

从初始条件开始运行。如果未指定，将从最新的检查点重启动运行。

**`-d`**: Start the run in debugger. (You should compile the code with `-g` flag). By default `gdb` is used starting each MPI thread in a separate `xterm` window. If you want to use a different debugger you can specify your own debugger command by assigning it to an environment variable `DEBUG_COMMAND`.

在调试器中启动运行。（您应该使用`-g`标志编译代码）。默认使用`gdb`，在单独的`xterm`窗口中启动每个MPI进程。如果您想使用不同的调试器，可以通过将其赋给环境变量`DEBUG_COMMAND`来指定自己的调试器命令。

**`-q`**: Do not write output to the log file. By default all standard output is written to `<RunID>.PRT` file.

不将输出写入日志文件。默认情况下，所有标准输出都写入`<RunID>.PRT`文件。

**`-l logfile`**: Instead of `<RunID>.PRT` use `logfile` as a log file.

使用`logfile`作为日志文件，而不是`<RunID>.PRT`。

**`-s tag`**: Instead of default `QSUB_STRING` use `QSUB_STRING_tag` (see below).

使用`QSUB_STRING_tag`而不是默认的`QSUB_STRING`（见下文）。

## Batch job submission / 批处理作业提交

**If you want to use this script to start model runs as batch jobs on a supercomputer, you can do it in most cases. You just have to add a variable `QSUB_STRING` to your `~/.modelErc` file and set it to a command which would start an appropriate batch job. One can set several such strings (with different settings) giving each one a "tag" and choose which string to use by specifying the tag with `-s` flag. For example, for Slurm resource manager you could use**

```bash
QSUB_STRING="sbatch -A account_name -n %np -t %t"
QSUB_STRING_debug="sbatch --qos=debug -A account_name -n %np -t %t"
```

**Here `%np` and `%t` are the number of MPI threads and execution time passed from the command line.**

如果您想使用此脚本在超级计算机上作为批处理作业启动模型运行，在大多数情况下您都可以做到。您只需要在`~/.modelErc`文件中添加一个变量`QSUB_STRING`，并将其设置为启动适当批处理作业的命令。可以设置多个这样的字符串（具有不同的设置），为每个字符串分配一个"标记"，并通过`-s`标志指定标记来选择使用哪个字符串。例如，对于Slurm资源管理器，您可以使用

```bash
QSUB_STRING="sbatch -A account_name -n %np -t %t"
QSUB_STRING_debug="sbatch --qos=debug -A account_name -n %np -t %t"
```

这里`%np`和`%t`是从命令行传递的MPI进程数和执行时间。

**To start a run which was set up in the previous section, you can just execute**

```bash
../exec/runE <RunID> -np <NP>
```

**Actually, this command will always restart your `<RunID>` run from the latest saved checkpoint file.**

要启动上一节中设置的运行，您只需执行

```bash
../exec/runE <RunID> -np <NP>
```

实际上，此命令将始终从最新保存的检查点文件重启动您的`<RunID>`运行。

## Stopping the model / 停止模型

**The standard way to stop the model is to use a command `sswE` (also located in `modelE/exec`). To stop the run `<RunID>` just execute the command**

```bash
sswE <RunID>
```

**This will let the model know that you want to interrupt the execution. The model will finish the current time step, write the checkpoint file and then it will stop.**

停止模型的标准方法是使用命令`sswE`（也位于`modelE/exec`中）。要停止运行`<RunID>`，只需执行命令

```bash
sswE <RunID>
```

这将让模型知道您想要中断执行。模型将完成当前时间步，写入检查点文件，然后停止。