### Downloading necessary input files
### 下载所需输入文件

We store all input files used in our modelE simulations on a server at GSFC. One can browse (and manually download) them here:

我们将所有 ModelE 模拟使用的输入文件存储在 GSFC 的服务器上。您可以在此处浏览（并手动下载）它们：

[http://portal.nccs.nasa.gov/GISS_modelE](http://portal.nccs.nasa.gov/GISS_modelE)

But typically it is much more convenient to use a script which automatically downloads all necessary input files for a particular rundeck. The command (executed from `modelE/decks`)

但通常使用脚本自动下载特定运行配置（Rundeck）所需的所有输入文件会更加方便。该命令（从 `modelE/decks` 目录执行）：

```
../exec/get_input_data -w <RunID>
```

will download all input files needed for the run described by `<RunID>.R` and will store them in a subdirectory `<RunID>_data`. Actually, if you have write access to the directory which stores modelE input files on your computer, it is even more convenient to provide this directory to `get_input_data` script. In this case it will automatically update input files in this directory as necessary for `<RunID>.R` Rundeck. If you used the default location for ModelE_Support directory, then modelE input files are stored in the directory `$HOME/ModelE_Support/prod_input_files/` on your computer. So, to update it for `<RunID>.R` Rundeck you have to execute

将下载由 `<RunID>.R` 描述的运行所需的所有输入文件，并将它们存储在子目录 `<RunID>_data` 中。实际上，如果您对计算机上存储 ModelE 输入文件的目录有写入权限，那么将此目录提供给 `get_input_data` 脚本会更加方便。在这种情况下，它将根据 `<RunID>.R` 运行配置（Rundeck）的需要自动更新此目录中的输入文件。如果您使用了 ModelE_Support 目录的默认位置，那么 ModelE 输入文件存储在您计算机的 `$HOME/ModelE_Support/prod_input_files/` 目录中。因此，要为 `<RunID>.R` 运行配置（Rundeck）更新它，您必须执行：

```
../exec/get_input_data -w <RunID> $HOME/ModelE_Support/prod_input_files
```

This will download only the files which are missing in `prod_input_files` directory. If you want to overwrite some of the existing files, you have to delete them first.

这将仅下载 `prod_input_files` 目录中缺失的文件。如果您想覆盖某些现有文件，必须先删除它们。