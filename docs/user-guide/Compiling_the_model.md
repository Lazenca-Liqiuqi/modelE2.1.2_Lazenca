# Compiling the model / 编译模型

## Compiling the model and setting up a directory for model run / 编译模型并设置模型运行目录

**Compilation of the model and preparation of a directory for the model run is performed by combination of make and perl scripts. They are designed to automatically detect model configuration and resolve dependencies between Fortran modules. Typical user would never need to modify any of these scripts.**
模型的编译和运行目录准备是通过make和perl脚本的组合来执行的。这些脚本被设计为自动检测模型配置并解决Fortran模块之间的依赖关系。普通用户通常永远不需要修改这些脚本。

**Typical command for compiling the model and setting up a directory for model run is**
编译模型和设置模型运行目录的典型命令是：

```bash
     make setup RUN=<RunID>
```

**This command will read model configuration from `<RunID>.R` rundeck and compile the corresponding executable. It will also create a directory for the run and link it to the current directory with the name `<RunID>`. The executable will be put into this run directory together with all the scripts which are needed to run the model.**
此命令将从`<RunID>.R`运行配置中读取模型配置并编译相应的可执行文件。它还将为运行创建一个目录，并将其以名称`<RunID>`链接到当前目录。可执行文件将与运行模型所需的所有脚本一起放入此运行目录中。

**This command compiles the model for serial run. If one wants to compile the model for parallel run (using MPI) one has to append a flag `MPI=YES` on the command line, i.e.**
此命令编译模型用于串行运行。如果想为并行运行（使用MPI）编译模型，必须在命令行中添加标志`MPI=YES`，即：

```bash
     make setup RUN=<RunID> MPI=YES
```

**Normally, once the model is compiled and before you start a long run, you want to perform a "cold start", i.e. you want to start your simulations from initial conditions, run the model for 1 hour of model time and save its state into a checkpoint file (restart file). This can be done with a command**
通常，一旦模型编译完成，在开始长时间运行之前，您需要执行"冷启动"，即您想从初始条件开始模拟，运行模型1小时的模型时间，并将其状态保存到检查点文件（重启文件）中。这可以通过以下命令完成：

```bash
    ../exec/runE <RunID> -np <NP> -cold-restart
```

**where `<NP>` is the number of MPI threads you want to use (typically the number of available cpu cores). Keep in mind that on big computers you may not be allowed to run MPI jobs interactively. In this case you have to set a variable QSUB_STRING in your ~/.modelErc file to a command which would submit your task as a batch job (see next section). Once first-hour run finishes successfully your model is ready for longer runs.**
其中`<NP>`是您想要使用的MPI进程数（通常是可用CPU核心数）。请记住，在大型计算机上，您可能不允许交互式运行MPI作业。在这种情况下，您必须在~/.modelErc文件中设置变量QSUB_STRING为将您的任务提交为批处理作业的命令（参见下一节）。一旦第一小时运行成功完成，您的模型就准备好进行更长时间的运行。

**If you really want to, you can request `make` to automatically run the model for the first hour after it finishes the setup. To do this use the target "setup-run" instead of "setup", i.e.**
如果您真的想要，可以请求`make`在完成设置后自动运行模型第一小时。为此，请使用目标"setup-run"而不是"setup"，即：

```bash
    make setup-run RUN=<RunID> MPI=YES NPES=<NP>
```

**where `<NP>` is the number of MPI threads for the first hour run.**
其中`<NP>`是第一小时运行的MPI进程数。

**Typically `make` resolves dependencies well when code changes and recompiles only those files which have to be recompiled. But when one switches to a completely different rundeck or checks out a different branch from the git repository, it may be safer to delete all precompiled object files and start a fresh compilation. To do it just execute**
通常，当代码更改时，`make`能够很好地解决依赖关系，只重新编译那些必须重新编译的文件。但是当切换到完全不同的运行配置或从git仓库检出到不同分支时，删除所有预编译的目标文件并开始新的编译可能更安全。为此，只需执行：

```bash
    make clean
```

**before starting a new compilation.**
在开始新编译之前。

**If for some reason you want to compile the model, but don't want to set up a run directory you can do it by using a target "gcm" instead of "setup".**
如果出于某种原因您想要编译模型，但不想设置运行目录，可以通过使用目标"gcm"而不是"setup"来实现。