# Imposed Sea surface conditions / 强迫海面条件

The simplest ocean model is one where the sea surface temperature is read in from a file, either a fixed (annually repeating) climatology, or a transient (monthly varying) realisation based on observations or previous simulations.
最简单的海洋模型是从文件中读取海表温度的模型，可以是固定的（年度循环）气候态，或基于观测或先前模拟的瞬变（月变化）实现。

Monthly means and end of month values are read in and a quadratic approximation used to interpolate to the (fixed) daily value at every grid point.
读取月均值和月末值，并使用二次近似插值到每个网格点的（固定）日值。

This is constructed to ensure that the monthly mean of the daily interpolated values is equal to the specified mean.
这样构造以确保日插值值的月平均值等于指定的平均值。

Along with SST, the sea ice concentration is also a required field.
与SST一起，海冰密集度也是一个必需字段。

This is interpolated similarly but is constructed so that the minimum and maximum values are respected.
这以类似方式插值，但构造时确保最小值和最大值得到保持。

Sea ice thickness is also fixed in these cases, but given the lack of reliable global observations, we set this based on a local scaling to the sea ice concentration.
在这些情况下，海冰厚度也是固定的，但由于缺乏可靠的全球观测，我们基于对海冰密集度的局地缩放来设置它。

However, if the sea surface conditions come from the output of a coupled model simulation, sea ice thickness can be provided as an input, by using the ZSI file, which is interpolated similarly.
然而，如果海面条件来自耦合模型模拟的输出，则可以通过使用ZSI文件提供海冰厚度作为输入，该文件以类似方式插值。
