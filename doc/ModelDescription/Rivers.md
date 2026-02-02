# Rivers / 河流

Rivers exist in all land grid boxes and collect runoff from the soil and land ice models.
河流存在于所有陆地网格中，并收集土壤模型和陆地冰模型产生的径流。

Where there is a lake fraction, the water is considered a lake (as above).
在有湖泊比例的地方，水体被视为湖泊（如上所述）。

Where there is not, there is no interaction with the atmosphere.
在没有湖泊比例的地方，水体与大气不发生交互。（原文拼写：intereaction）

Transport of river water depends on the (fixed) downstream direction file and mean slope, and the depth of the upstream river/lake above a predefined sill depth.
河流水的输送取决于（固定的）下游方向文件和平均坡度，以及上游河流/湖泊超过预定义门槛深度的那部分水深。（原文拼写：Tranpsort）

Some boxes do not contain an outlet, and so can accumulate water indefinitely.
某些网格不包含出口，因此可以无限期地积水。

As the river water reaches an ocean box, the water is deposited uniformly within that box.
当河水到达海洋网格时，水量在该网格内均匀分配。
