# Installing NetCDF library in your computer / 在您的计算机上安装NetCDF库

**Installing NetCDF library in your computer**
**在您的计算机上安装NetCDF库**

On Linux and Mac OS X machines typically you can install NetCDF from the main software repositories (with "yum" or similar package manage on Linux or MacPorts on Mac). You can try it, but we don't recommend this approach. The problem is that for a library to be compatible with your Fortran compiler it has to be compiled with the same compiler and with the same flags you will be using and that may be not the case when you get a precompiled library from a repository. If you install NetCDF with MacPorts, at least make sure that you have installed the Fortran compiler before you start the installation of NetCDF and that MacPorts recognizes it as a default compiler.
在Linux和Mac OS X机器上，通常您可以从主软件仓库安装NetCDF（在Linux上使用"yum"或类似的包管理器，在Mac上使用MacPorts）。您可以尝试这种方法，但我们不推荐这种方式。问题是，为了使库与您的Fortran编译器兼容，必须使用您将要使用的相同编译器和相同标志来编译它，而当您从仓库获取预编译库时可能不是这种情况。如果您使用MacPorts安装NetCDF，至少请确保在开始安装NetCDF之前已经安装了Fortran编译器，并且MacPorts将其识别为默认编译器。

The safer way, though, is to install NetCDF from the source code. You can download the gzipped tar file with the source code from:
然而，更安全的方法是从源代码安装NetCDF。您可以从以下网址下载包含源代码的gzip压缩tar文件：

```
http://www.unidata.ucar.edu/downloads/netcdf/index.jsp
```

To install it do the following. Untar the downloaded file and enter the directory with downloaded code:
安装步骤如下。解压下载的文件并进入包含下载代码的目录：

```bash
tar -xzf netcdf-3.6.3.tar.gz
cd netcdf-3.6.3
```

Choose a directory where you want to install NetCDF, say "/opt/netcdf/3.6.3" (make sure that directory above it exists and is writable to you). Make sure that Fortran compiler is installed and is functional. Now, start the installation process.
选择您想要安装NetCDF的目录，比如"/opt/netcdf/3.6.3"（确保其上层的目录存在并且您有写权限）。确保Fortran编译器已安装且功能正常。现在，开始安装过程。

**Inform the system which Fortran compiler you are going to use**
**告知系统您将要使用的Fortran编译器**

```bash
export FC=gfortran
```

**Configure the package giving it the desired location for installation**
**配置软件包，指定所需的安装位置**

```bash
./configure --prefix=/opt/netcdf/3.6.3
```

**Compile and install the package**
**编译并安装软件包**

```bash
make
make install
```

Netcdf library should now be functional on your system. To inform modelE about its location you need to add the following line to your `~/.modelErc` file:
现在NetCDF库应该在您的系统上正常工作了。要告知ModelE其位置，您需要在您的`~/.modelErc`文件中添加以下行：

```bash
NETCDFHOME=/opt/netcdf/3.6.3
```

---

## Installation Notes / 安装说明

**Platform Compatibility / 平台兼容性**:
- Linux: 推荐使用源码编译以确保与Fortran编译器的兼容性
- Mac OS X: 如果使用MacPorts，请确保先安装Fortran编译器
- 其他Unix系统: 建议使用源码编译方式

**Compiler Requirements / 编译器要求**:
- 支持的编译器: gfortran, Intel ifort
- 编译器版本: gfortran 4.9+, ifort 12.0+
- 必须在安装NetCDF之前确认编译器正常工作

**Directory Permissions / 目录权限**:
- 安装目录: `/opt/netcdf/3.6.3` (可自定义)
- 权限要求: 对安装目录有写权限
- 建议创建专门的软件安装目录

**Configuration Tips / 配置提示**:
- `FC`环境变量指定Fortran编译器
- `--prefix`参数指定安装路径
- 确保路径正确且可访问

**Troubleshooting / 故障排除**:
- 如果编译失败，检查编译器版本和权限设置
- 确保网络连接正常，能够下载源代码
- 验证`~/.modelErc`文件路径和格式正确

**Version Note / 版本说明**:
- 本文档基于NetCDF 3.6.3版本
- 推荐使用NetCDF 4.x系列以获得更好的功能和性能
- 如果使用新版本，请相应调整版本号