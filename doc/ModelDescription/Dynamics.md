# Dynamics / 动力学

The solution of the momentum equations is done within the DYNAM.
动量方程的求解在DYNAM模块内完成。

The scheme is leap frog in time with an initial 2/3 time step every 8 leap-frog steps to prevent solution splitting.
时间积分采用蛙跳格式，每8个蛙跳步执行一次初始2/3时间步，以防止解分裂。

The dynamics are based on the dry physics (no water vapour effects in the pressure gradient calculation) and use potential temperature as the advected variable.
动力学基于干物理过程（压力梯度计算中不包含水汽效应），并使用位温作为平流变量。

Water vapour and tracers are advected outside the dynamics loop (once every source time step).
水汽和示踪物在动力学循环外进行平流（每个源时间步一次）。

All temperature, water and tracer advection is done using the quadratic upstream scheme to minimise numerical diffusion.
所有温度、水和示踪物平流均使用二次迎风格式完成，以最小化数值扩散。
