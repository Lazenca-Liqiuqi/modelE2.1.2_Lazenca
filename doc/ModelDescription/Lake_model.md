# Lake model / 湖泊模型

The lakes are modelled using a two layer code.
湖泊使用二层模式进行建模。

The first layer has a minimum depth of 1m, while the second layer is unlimited.
第一层具有1米的最小深度，而第二层深度无限制。

Lake mass is effected by precipitation, evaporation and lake ice melt and freeze.
湖泊水量受降水、蒸发以及湖冰融化和冻结的影响。

In addition, river inflow from upstream boxes and outflow to the downstream box modify the first layer properties.
此外，来自上游网格的河流入流和流向下游网格的出流会改变第一层的属性。

There is a small amount of heat diffusion at the interface, and convective overturning occurs if the temperature stratification is unstable.
界面处存在少量热扩散，若温度层结不稳定，则发生对流翻转。
