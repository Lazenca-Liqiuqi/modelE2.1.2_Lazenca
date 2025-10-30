# Description of Tracer Rundeck Parameters | 示踪物Rundeck参数说明

 Many settings for Tracer-related code can be set from parameters in the rundeck. Below is a list of some of these parameters and their settings and sometimes conflicts. Note however that an exhaustive desciption of all combinations and potential conflicts is probably not possible. So it is always a good idea to check from the model output whether what you think should be happening is indeed happening (or seek help from GISS). Below the list is a section describing how to use rundeck parameters to perturb tracer emissions by sector and region.
 示踪物相关代码的许多设置可以通过rundeck中的参数设置。下面是这些参数及其设置和有时冲突的列表。但请注意，对所有组合和潜在冲突的详尽描述可能是不可能的。因此从模型输出检查您认为应该发生的事情是否确实发生总是一个好主意（或寻求GISS的帮助）。列表下方有一个部分描述如何使用rundeck参数按部门和区域扰动示踪物排放。

#### General or Multi-group Tracer Parameters | 通用或多组示踪物参数 
 - `*_nBBsources` : Where '*' is the tracer name. Say `CO_nBBsources=2` is set in the rundeck: This tells the model that the final 2 sources listed for tracer CO (if its emission files are listed in the standard way like `CO_01, CO_02...`) are to be treated as biomass burning sources and emitted mixed throughout the PBL rather than strictly as a surface flux. This could be used for any type of emission you would liked treated that way.
 - `*_nBBsources` : 其中'*'是示踪物名称。例如在rundeck中设置`CO_nBBsources=2`：这告诉模型示踪物CO列出的最后2个源（如果其排放文件以标准方式列出如`CO_01, CO_02...`）将被视为生物质燃烧源，并在整个PBL中混合排放，而不仅仅是地表通量。这可以用于您希望以这种方式处理的任何类型的排放。
 - `*_##_sect, REG_{N,S,E,W}, REGIONS_ARE, SECT_##, SECTORS_ARE` : These are related to tagging of emission source files as belonging to a sector and then scaling sector emissions within rectangular (including global) geographic regions. Please see the special section below.
 - `*_##_sect, REG_{N,S,E,W}, REGIONS_ARE, SECT_##, SECTORS_ARE` : 这些与将排放源文件标记为属于某个部门然后在矩形（包括全球）地理区域内缩放部门排放有关。请参见下面的特殊部分。
 - `COUPLED_CHEM` : if set to 1, couples Shindell chemistry tracers to aerosol tracers (for example aerosols make use of oxidants and gasses make use of sulfate). Setting to 0 decouples, and then some file input is needed.
 - `COUPLED_CHEM` : 如果设置为1，将Shindell化学示踪物与气溶胶示踪物耦合（例如气溶胶利用氧化剂，气体利用硫酸盐）。设置为0则解耦，然后需要一些文件输入。
 - `no_emis_over_ice` : If this is greater than 0, surface tracer emissions are set to 0 for grid boxes greater than 90% covered by ice. This is rarely used, so please confirm it is working for you.
 - `no_emis_over_ice` : 如果此值大于0，对于冰覆盖超过90%的网格盒，地表示踪物排放设置为0。这很少使用，所以请确认它对您有效。

#### Mostly Shindell Chemistry-Related Tracer Parameters | 主要Shindell化学相关示踪物参数 
 - `initial_GHG_setup` : Some (GHG chemistry) tracers may have their mixing ratios tied to values prescribed by the radiation code. (See `use_rad_*` parameters below). Due to the order of the main model loop, the best way to initialize such tracers is to run the model setup and save the needed information to files for the current year and then start the model again, reading from those files to initialize the tracers. To do so, one sets `initial_GHG_setup=1` for the first set up, then changes to `initial_GHG_setup=0` for the second (and the rest of the run). This is not generally needed if starting one run from another with tracer continuity (simply keep `initial_GHG_setup=0`). Since the double-setup is tedious, there is also the option of setting up only once with `initial_GHG_setup=1`. In this case, the first time tracers are used (including the chemistry) tracer mass will use tracer defaults which may not be appropriate to your current simulation conditions. But then the appropriate tracers are overwritten with desired values later in the time step. Thus, the initial diagnostics (including therefore the first month's acc file) will be contaminated by a potentially strange chemistry term and a large overwrite term, but this should smooth out quickly and so in many cases one could appropriately do this single setup method and just ignore the spin-up.
因此，初始诊断（因此包括第一个月的acc文件）将被一个可能奇怪的化学项和一个大覆盖项污染，但这应该很快平滑，所以在许多情况下可以适当地进行这种单设置方法并忽略自旋期（spin-up）。注意：如果您的年龄年龄计算跨越多个模拟，请检查初始条件确实从1 ppbv开始（如果是新模拟）或从父模拟继续其值（如果需要跨越模拟）。这通常可以通过在rundeck中正确设置`itime_tr0( )`参数或通过修改代码来实现。
 - `o3_yr` : This parameter belongs to the radiation code and is used to choose the climatological ozone input (set to a desired year or to 0 to follow the model date). But it is also used to choose the date of trace-gas emissions, if transient emissions files were provided in the rundeck. A linear interpolation between available time slices is done. If the setting is outside the range of those transient files, the emissions repeat either the first or final time slices available. Note that this does NOT control the aerosol emissions, nor does the `aero_yr` radiation code parameter. You want `aer_int_yr` for that.
 - `o3_yr` : 此参数属于辐射代码，用于选择气候学臭氧输入（设置为所需年份或设置为0以跟随模型日期）。但如果在rundeck中提供了瞬态排放文件，它也用于选择痕量气体排放的日期。在可用时间片之间进行线性插值。如果设置超出那些瞬态文件的范围，排放重复第一个或最后一个可用时间片。注意这不控制气溶胶排放，`aero_yr`辐射代码参数也不控制。您需要`aer_int_yr`来控制气溶胶排放。
 - `aircraft_Tyr1, aircraft_Tyr2` : While the code can generally recognize transient files for 2D surface emissions, as these have a header record of meta-data, this is not the case for a few remaining 3D sources. For example the NOx from aircraft. One can list a multi-time slice file, but the parameters `aircraft_Tyr1` (the year of the first time slice) and `aircraft_Tyr2` (the year of the last time slice) must be defined. For non-transient aircraft source, omit these two parameters or set them equal to each other.
 - `aircraft_Tyr1, aircraft_Tyr2` : 虽然代码通常可以识别2D地表排放的瞬态文件，因为这些具有元数据的头记录，但对于少数剩余的3D源情况并非如此。例如来自飞机的NOx。可以列出多时间片文件，但必须定义参数`aircraft_Tyr1`（第一时间片的年份）和`aircraft_Tyr2`（最后时间片的年份）。对于非瞬态飞机源，省略这两个参数或将它们设置为相等。
 - `biomass_Tyr1, biomass_Tyr2` : analagous to `aircraft_Tyr1, aircraft_Tyr2` above but for the case where transient `GFED_3D_BIOMASS` (preprocessor option) sources are used. (It is now perhaps easier though to use standard 2D input sources and set `*_nBBsources` parameters, as described above).
 - `biomass_Tyr1, biomass_Tyr2` : 类似于上面的`aircraft_Tyr1, aircraft_Tyr2`，但用于使用瞬态`GFED_3D_BIOMASS`（预处理器选项）源的情况。（不过现在使用标准2D输入源并设置`*_nBBsources`参数可能更容易，如上所述）。
 - `clim_interact_chem` : If set to 1, this allows the chemistry tracers to affect climate via ozone and CH4 in the radiation calculation and via water chemistry altering the model humidity. Note that if this is turned on we tend to set the radiation code parameter `H2ObyCH4` to 0, and when `clim_interact_chem=0`, we tend to set `H2ObyCH4=1`. There are ways to have finer control over this setting. For example, if you want the humidity feedback on but the radiation feedback off, you could set: `clim_interact_chem=1, Lmax_rad_{O3,CH4}=0`.
 - `clim_interact_chem` : 如果设置为1，这允许化学示踪物通过辐射计算中的臭氧和CH4以及通过水化学改变模型湿度来影响气候。注意如果开启此选项，我们倾向于将辐射代码参数`H2ObyCH4`设置为0，而当`clim_interact_chem=0`时，我们倾向于设置`H2ObyCH4=1`。有方法可以更精细地控制此设置。例如，如果您希望湿度反馈开启但辐射反馈关闭，可以设置：`clim_interact_chem=1, Lmax_rad_{O3,CH4}=0`。
 - `Lmax_rad_O3` : To use less than all levels of ozone tracer in the radiation code's calculation, one could set this to less than `LM` and it will use levels 1 to `Lmax_rad_O3`.
 - `Lmax_rad_O3` : 要在辐射代码计算中使用少于所有层的臭氧示踪物，可以将其设置为小于`LM`，它将使用层1到`Lmax_rad_O3`。
 - `Lmax_rad_CH4` : To use less than all levels of methane tracer in the radiation code's calculation, one could set this to less than `LM` and it will use levels 1 to `Lmax_rad_CH4`.
 - `Lmax_rad_CH4` : 要在辐射代码计算中使用少于所有层的甲烷示踪物，可以将其设置为小于`LM`，它将使用层1到`Lmax_rad_CH4`。
 - `use_rad_n2o` : 1 means have tracer N2O follow the mixing ratios in the radiation code's GHG file by using a L=1 overwrite of the tracer each time step. 0 means to use a default general present-day mixing ratio to do the same.
 - `use_rad_n2o` : 1表示通过在每个时间步使用L=1覆盖来让示踪物N2O跟随辐射代码GHG文件中的混合比。0表示使用默认的一般现代混合比来做同样的事情。
 - `use_rad_cfc` : 1 means have tracer CFC follow the mixing ratios in the radiation code's GHG file (mixture of cfc11 and cfc12) by using a L=1 overwrite of the tracer each time step. 0 means to use a default general present-day mixing ratio to do the same.
 - `use_rad_cfc` : 1表示通过在每个时间步使用L=1覆盖来让示踪物CFC跟随辐射代码GHG文件（cfc11和cfc12的混合物）中的混合比。0表示使用默认的一般现代混合比来做同样的事情。
 - `use_rad_ch4` : 1 means have tracer CH4 follow the mixing ratios in the radiation code's GHG file by using a L=1 overwrite of the tracer each time step. 0 means to use a default general present-day mixing ratio to do the same. Therefore, remember to unlist CH4 emissions files from the rundeck when using the `use_rad_ch4=1` method.
 - `use_rad_ch4` : 1表示通过在每个时间步使用L=1覆盖来让示踪物CH4跟随辐射代码GHG文件中的混合比。0表示使用默认的一般现代混合比来做同样的事情。因此，记得在使用`use_rad_ch4=1`方法时从rundeck中取消列出CH4排放文件。
 - `tune_lt_land` : linear tuning factor for lightning flash rate over land
 - `tune_lt_land` : 陆地闪电闪率的线性调节因子
 - `tune_lt_sea` : linear tuning factor for lightning flash rate over ocean
 - `tune_lt_sea` : 海洋闪电闪率的线性调节因子
 - `PltOx` : the pressure (hPa) above which Ox, NOx, BrOx, and ClOx will be overwritten with climatology. Code default of 0.1 is based on the 23-layer model so won't choose any 40-layer model levels. Recommended setting for 40-layer model is 0.2.
 - `PltOx` : 在此压力（hPa）以上，Ox、NOx、BrOx和ClOx将被气候学值覆盖。代码默认值0.1基于23层模型，因此不会选择任何40层模型层。40层模型的推荐设置是0.2。
 - `Tpsc_offset_N` : can be used to offset the temperature at which polar stratospheric clouds form in the Northern Hemisphere
 - `Tpsc_offset_N` : 可用于偏移北半球极地平流层云形成的温度
 - `Tpsc_offset_S` : can be used to offset the temperature at which polar stratospheric clouds form in the Southern Hemisphere
 - `Tpsc_offset_S` : 可用于偏移南半球极地平流层云形成的温度
 - `use_sol_Ox_cycle` : This is not strictly a tracer code parameter: it can be used to allow the radiation code to alter its file-read ozone based on current year's position in the solar cycle and a parameterization based on tracer ozone simulations. Note that this is not yet available in the case of preprocessor option `RAD_O3_GCM_HRES`.
 - `use_sol_Ox_cycle` : 这不严格是一个示踪物代码参数：它可以用于允许辐射代码根据当前年份在太阳周期中的位置和基于示踪物臭氧模拟的参数化来改变其文件读取的臭氧。注意在预处理器选项`RAD_O3_GCM_HRES`的情况下这还不可用。
 - `rad_FL` : 1 means to use the radiation code's fluxes (rebinned) as the photon flux for the fastj2 photolysis code. 0 means the chemistry will use an offline file's photon flux.
 - `rad_FL` : 1表示使用辐射代码的通量（重新分箱）作为fastj2光解代码的光子通量。0表示化学将使用离线文件的光子通量。
 - `allowSomeChemReinit` : If set to 0 this disallows certain sections of chemistry code from reinitializing (including stratospheric model humidity variable altering!) This is helpful when attempting to initialize tracers/chemistry from the state saved from another run. Note you may still have to set `itime_tr0( )` parameters properly for smooth tracer transitions.
 - `allowSomeChemReinit` : 如果设置为0，这不允许某些化学代码段重新初始化（包括平流层模型湿度变量改变！）当尝试从另一个运行保存的状态初始化示踪物/化学时这很有帮助。注意您可能仍需要正确设置`itime_tr0( )`参数以实现平滑的示踪物转换。
 - `which_trop` : For the non-recommended case where `TRACERS_SPECIAL_Shindell` preprocessor directive is on but `SHINDELL_STRAT_CHEM` is off, this parameter controls what is used as the tropopause for chemistry purposes. 0 means the model calculated meteorological tropopause (`LTROPO(I,J)`) and 1 means a flat level demarcation (`LS1` is the first stratospheric layer).
 - `which_trop` : 对于不推荐的情况，当`TRACERS_SPECIAL_Shindell`预处理器指令开启但`SHINDELL_STRAT_CHEM`关闭时，此参数控制化学用途使用的对流层顶。0表示模型计算的气象对流层顶（`LTROPO(I,J)`），1表示平坦层分界（`LS1`是第一个平流层）。
 - `nn_or_zon` : for INTERACTIVE_WETLANDS_CH4 preprocessor option on: nn_or_zon=0 searches for neareast-neighbor wetlands emissions when expanding wetlands to a new gridbox; nn_or_zon=1 instead uses the local zonal average of wetland emissions.
 - `nn_or_zon` : 对于INTERACTIVE_WETLANDS_CH4预处理器选项开启：nn_or_zon=0在将湿地扩展到新网格盒时搜索最近邻湿地排放；nn_or_zon=1则使用湿地排放的局部纬向平均。
 - `int_wet_dist` : for `INTERACTIVE_WETLANDS_CH4` preprocessor option on: `int_wet_dist=1` allows wetlands to change spatially in addition to magnitude of emissions. `int_wet_dist=0` for magnitude-only.
 - `int_wet_dist` : 对于`INTERACTIVE_WETLANDS_CH4`预处理器选项开启：`int_wet_dist=1`允许湿地在空间上变化以及排放量。`int_wet_dist=0`仅为量级变化。
 - `ice_age` : for `INTERACTIVE_WETLANDS_CH4` preprocessor option on: if this is set to non-zero, no wetlands emissions are allowed for latitudes poleward of this setting (in degrees)
 - `ice_age` : 对于`INTERACTIVE_WETLANDS_CH4`预处理器选项开启：如果设置为非零，此设置（度数）极向纬度不允许湿地排放。
 - `ns_wet` : for `INTERACTIVE_WETLANDS_CH4` preprocessor option on: IMPORTANT: this is how the model knows which methane source to adjust based on the interactive wetlands scheme. For example, if file `CH4_13` is linked to your base CH4 from wetlands, set `ns_wet=13`.
 - `ns_wet` : 对于`INTERACTIVE_WETLANDS_CH4`预处理器选项开启：重要：这是模型知道根据交互式湿地方案调整哪个甲烷源的方式。例如，如果文件`CH4_13`链接到您来自湿地的基础CH4，设置`ns_wet=13`。
 - `exclude_us_eu` : for `INTERACTIVE_WETLANDS_CH4` preprocessor option on: `exclude_us_eu=1` excludes the region that is very roughly the United States and Europe from spatially-changing wetlands. `exclude_us_eu=0` allows.
 - `exclude_us_eu` : 对于`INTERACTIVE_WETLANDS_CH4`预处理器选项开启：`exclude_us_eu=1`将非常粗略的美国和欧洲区域从空间变化的湿地中排除。`exclude_us_eu=0`允许。
 - `topo_lim` : for `INTERACTIVE_WETLANDS_CH4` preprocessor option on: upper limit of topographic variation for new wetlands formation
 - `topo_lim` : 对于`INTERACTIVE_WETLANDS_CH4`预处理器选项开启：新湿地形成的地形变化上限
 - `sat_lim` : for `INTERACTIVE_WETLANDS_CH4` preprocessor option on: lower limit on surface air temperature for new wetlands formation
 - `sat_lim` : 对于`INTERACTIVE_WETLANDS_CH4`预处理器选项开启：新湿地形成的地表气温下限
 - `gw_ulim` : for `INTERACTIVE_WETLANDS_CH4` preprocessor option on: upper limit on ground wetness for new wetlands formation
 - `gw_ulim` : 对于`INTERACTIVE_WETLANDS_CH4`预处理器选项开启：新湿地形成的地面湿度上限
 - `gw_llim` : for `INTERACTIVE_WETLANDS_CH4` preprocessor option on: lower limit on ground wetness for new wetlands formation
 - `gw_llim` : 对于`INTERACTIVE_WETLANDS_CH4`预处理器选项开启：新湿地形成的地面湿度下限
 - `SW_lim` : for `INTERACTIVE_WETLANDS_CH4` preprocessor option on: lower limit on short-wave downward flux for new wetlands formation
 - `SW_lim` : 对于`INTERACTIVE_WETLANDS_CH4`预处理器选项开启：新湿地形成所需的短波向下通量下限
 - `fix_CH4_chemistry` :  this is no longer is active use (preferred method is to set `use_rad_ch4=1` to keep methane close to radiation code GHG file values). But one can set `fix_CH4_chemistry=1` and the CH4 tracer should be overwritten each time step to its initial conditions, allowing the chemistry to experience the same methane field each time. An even rarer option is to set this to -1 in which case one should be able to read CH4 initial conditions from file `CH4_IC`.
 - `fix_CH4_chemistry` : 这不再是活跃使用（首选方法是设置`use_rad_ch4=1`以保持甲烷接近辐射代码GHG文件值）。但可以设置`fix_CH4_chemistry=1`，CH4示踪物应在每个时间步被覆盖到其初始条件，允许化学每次经历相同的甲烷场。一个更罕见的选项是将其设置为-1，在这种情况下应该能够从文件`CH4_IC`读取CH4初始条件。
 - `scale_ch4_IC_file` :  in the rare case of reading CH4 initial conditions from file `CH4_IC` (when `fix_CH4_chemistry=-1`) this `scale_ch4_IC_file` parameter can be used to uniformly scale those initial conditions.
 - `scale_ch4_IC_file` : 在从文件`CH4_IC`读取CH4初始条件的罕见情况下（当`fix_CH4_chemistry=-1`时），此`scale_ch4_IC_file`参数可用于均匀缩放这些初始条件。
 - `ch4_init_sh, ch4_init_nh` : when not using the preferred method of initial conditions (set `use_rad_ch4=1` to initialize methane close to radiation code GHG file values), one can use these two parameters to set a Northern hemisphere (`ch4_init_nh`) and Southern hemisphere (`ch4_init_sh`) value to initialize CH4. Vertically some variation is applied using HALOE observations.
 - `ch4_init_sh, ch4_init_nh` : 当不使用初始条件的首选方法（设置`use_rad_ch4=1`将甲烷初始化为接近辐射代码GHG文件值）时，可以使用这两个参数设置北半球（`ch4_init_nh`）和南半球（`ch4_init_sh`）值来初始化CH4。垂直方向使用HALOE观测应用一些变化。
 - `PI_run` : long ago, this was used to switch the whole chemistry code to preindustrial condition runs. Its last bit of usefulness is to put into effect the `PIratio_*` parameters (see below)
 - `PI_run` : 很久以前，这用于将整个化学代码切换到前工业条件运行。其最后的用处是实施`PIratio_*`参数（见下文）
 - `PIratio_*` : where '*' is {N,CO_T,CO_S,other,N2O,CFC} These parameters can be used to scale the initial conditions of trace gases and any overwriting they may experience during the run. They are for: N = {NOx, HNO3, N2O5, HO2NO2}, CO_T = CO in the troposphere, CO_S = CO in the stratosphere, other = {PAN, Isoprene, AlkyNit, Alkenes, Paraffin}, N2O = N2O, and CFC = CFC. Note that for N2O and CFC if these are being set by the radiation code's GHG file (recommended) one should set these factors to 1.0 (for `PI_run=1`). These used to be used for scaling trace gas emissions, but this is now done separately (see special section below).
 - `PIratio_*` : 其中'*'是{N,CO_T,CO_S,other,N2O,CFC}这些参数可用于缩放痕量气体的初始条件以及它们在运行期间可能经历的任何覆盖。它们用于：N = {NOx, HNO3, N2O5, HO2NO2}, CO_T = 对流层中的CO, CO_S = 平流层中的CO, other = {PAN, 异戊二烯, 烷基硝酸盐, 烯烃, 石蜡烃}, N2O = N2O, CFC = CFC。注意对于N2O和CFC，如果这些是由辐射代码的GHG文件设置的（推荐），应将这些因子设置为1.0（对于`PI_run=1`）。这些过去用于缩放痕量气体排放，但现在单独完成（参见下面的特殊部分）。

#### Mostly Aerosol Tracer Parameters | 主要气溶胶示踪物参数 
 - `rad_forc_lev` : controls location of aerosol radiative forcing diagnostics (0 for TOA, 1 for tropopause. If preprocessor option `ACCMIP_LIKE_DIAGS` is used, you must have `rad_forc_lev=0`. There is a online check for this.)
 - `rad_forc_lev` : 控制气溶胶辐射强迫诊断的位置（0为TOA，1为对流层顶。如果使用预处理器选项`ACCMIP_LIKE_DIAGS`，您必须有`rad_forc_lev=0`。对此有在线检查。）
 - `rad_interact_aer` : if equals to 1, aerosols affect radiation. If equals to 0, aerosols are independent of the radiation code. Radiation uses some default aerosol fields.
 - `rad_interact_aer` : 如果等于1，气溶胶影响辐射。如果等于0，气溶胶独立于辐射代码。辐射使用一些默认气溶胶场。
 - `BBinc` : enhancement factor for carbonaceous aerosols' biomass burning sources (to match GISS AR5 simulations, 1.4 should be used). 1.0 is the default.
 - `BBinc` : 碳质气溶胶生物质燃烧源的增强因子（为了匹配GISS AR5模拟，应使用1.4）。默认为1.0。
 - `aer_int_yr` : select year of aerosol emissions. If set to zero, the actual simulated year will be used.
 - `aer_int_yr` : 选择气溶胶排放年份。如果设置为零，将使用实际模拟年份。
 - `tune_ss1` : factor to multiply seasalt1 emissions with. Equals to 1.0 if ommitted.
 - `tune_ss1` : 海盐1排放的乘法因子。如果省略则等于1.0。
 - `tune_ss2` : factor to multiply seasalt2 emissions with. Equals to 1.0 if ommitted.
 - `tune_ss2` : 海盐2排放的乘法因子。如果省略则等于1.0。
 - `OFFLINE_DMS_SS` : If equals to 1, DMS and seasalt emissions are not interactive. Input files are also needed as rundeck parameters: `DMS_SEA`, `SALT1`, `SALT2`
 - `OFFLINE_DMS_SS` : 如果等于1，DMS和海盐排放不是交互式的。还需要作为rundeck参数的输入文件：`DMS_SEA`、`SALT1`、`SALT2`
 - `OFFLINE_SS` : If equals to 1, seasalt emissions are not interactive. Input files are also needed as rundeck parameters: `SALT1`, `SALT2`
 - `OFFLINE_SS` : 如果等于1，海盐排放不是交互式的。还需要作为rundeck参数的输入文件：`SALT1`、`SALT2`
 - `DMS_SEA` : Input file for DMS emissions when `OFFLINE_DMS_SS` equals to 1.
 - `DMS_SEA` : 当`OFFLINE_DMS_SS`等于1时的DMS排放输入文件。
 - `SALT1` : Input file for seasalt1 emissions when either `OFFLINE_DMS_SS` or `OFFLINE_SS` equal to 1.
 - `SALT1` : 当`OFFLINE_DMS_SS`或`OFFLINE_SS`等于1时的海盐1排放输入文件。
 - `SALT2` : Input file for seasalt2 emissions when either `OFFLINE_DMS_SS` or `OFFLINE_SS` equal to 1.
 - `SALT2` : 当`OFFLINE_DMS_SS`或`OFFLINE_SS`等于1时的海盐2排放输入文件。
 - `*_om2oc`, where '*' is the tracer name : modify the default organic matter-to-organic carbon (OM/OC) ratio for the specific tracer. Default is 1.4.
 - `*_om2oc`，其中'*'是示踪物名称：修改特定示踪物的默认有机物-有机碳（OM/OC）比率。默认为1.4。

#### Mostly Dust Tracer Parameters | 主要尘土示踪物参数 
 - `imDust` : (0: PDF emission scheme, 1: AEROCOM)
- `imDust` : (0表示PDF排放方案，1表示AEROCOM方案)

- `adiurn_dust` : (1: daily dust diagnostics at certain grid points)
- `adiurn_dust` : (1表示在特定网格点的每日尘土诊断)

- `prefDustSources` : (0: Ginoux 2001 w/ vegetation mask ! 1: Ginoux 2009 w/ vegetation mask (current default) ! 2: Ginoux 2009 w/o vegetation, 3: Grini/Zender sources ! 4: Tegen sources, >4: Free choice of emis. parameters)
- `prefDustSources` : (0: Ginoux 2001年带植被掩膜；1: Ginoux 2009年带植被掩膜（当前默认）；2: Ginoux 2009年不带植被，3: Grini/Zender源；4: Tegen源，>4: 排放参数自由选择)

- `fracClayPDFscheme` : (Frac. clay emis, only effective for prefDustSources > 4)
- `fracClayPDFscheme` : (粘土排放分数，仅对prefDustSources > 4有效)

#### 附加参数说明 | Additional Parameters Description

- `prather_limits` : (1: to avoid some negative tracers in sub-gridscale)
- `prather_limits` : (1: 避免子网格中的一些负示踪物)

- `diag_rad` : (1: additional radiation diagnostics)
- `diag_rad` : (1: 附加辐射诊断)

- `diag_wetdep` : (1: additional wet deposition diagnostics)
- `diag_wetdep` : (1: 附加湿沉降诊断)

- `itime_tr0` : (time index parameter: set time reference point for tracers, used for smooth startup and transition)
- `itime_tr0` : (时间索引参数：设置示踪物的时间基准点，用于平滑启动和转换)

- `to_per_mil` : (per mil parameter: control tracer concentration scaling)
- `to_per_mil` : (每百万分率参数：控制示踪物浓度缩放)

- `supsatfac` : (supersaturation factor: adjust water vapor supersaturation calculation)
- `supsatfac` : (饱和度调节因子：调整水汽饱和度计算)

- `water_tracer_ic` : (water tracer initial condition file: specify initial conditions for water tracers)
- `water_tracer_ic` : (水示踪物初始条件文件：指定水示踪物的初始条件)

- `TESObsDiagnosticsOn` : (TES observation diagnostics switch: enable TES satellite observation data diagnostic output)
- `TESObsDiagnosticsOn` : (TES观测诊断开关：启用TES卫星观测数据的诊断输出)

- `TESObsMinDegFr` : (TES minimum degree fraction: set minimum degree fraction for TES observations)
- `TESObsMinDegFr` : (TES最小度数限制：设置TES观测的最小度数)

- `TESObsDataDir` : (TES observation data directory: specify TES data file storage directory)
- `TESObsDataDir` : (TES观测数据目录：指定TES数据文件存储目录)

- `TESCatDiagnosticsOn` : (TES category diagnostics switch: enable TES category analysis diagnostic output)
- `TESCatDiagnosticsOn` : (TES类别诊断开关：启用TES类别分析的诊断输出)

- `TESCatMinQuality` : (TES minimum quality threshold: set minimum quality threshold for TES data)
- `TESCatMinQuality` : (TES最小质量阈值：设置TES数据的最小质量阈值)

- `TESCatUseColloc` : (TES collocation correction switch: enable data collocation correction function)
- `TESCatUseColloc` : (TES并置校正开关：启用数据并置校正功能)

- `TESCatVariableHDOAKOnly` : (TES HDOAK specific variable switch: enable only HDOAK related variables)
- `TESCatVariableHDOAKOnly` : (TES HDOAK专用变量开关：仅启用HDOAK相关变量)

- `checktracer_on` : (tracer check switch: enable tracer runtime checking)
- `checktracer_on` : (示踪物检查开关：启用示踪物运行检查)

- `base_isopreneX` : (isoprene baseline value: set baseline concentration for isoprene)
- `base_isopreneX` : (异戊二烯基线值：设置异戊二烯的基线浓度)

- `AMP_DIAG_FC` : (AMP diagnostic function control: enable aerosol model diagnostic functions)
- `AMP_DIAG_FC` : (AMP诊断功能控制：启用气溶胶模式诊断功能)

- `AMP_RAD_KEY` : (AMP radiation key: specify aerosol radiation calculation key)
- `AMP_RAD_KEY` : (AMP辐射密钥：指定气溶胶辐射计算密钥)

- `FreeFe` : (free iron parameter: set free iron related parameters)
- `FreeFe` : (自由铁参数：设置自由铁相关参数)

- `frHemaInQuarAggr` : (hematite fraction in aggregate: proportion of hematite in aggregates)
- `frHemaInQuarAggr` : (聚合体中赤铁矿含量比例)

- `pureByTotalHematite` : (total hematite purity: set total hematite purity)
- `pureByTotalHematite` : (总赤铁矿纯度：设置总赤铁矿纯度)

- `be7_src_param` : (beryllium-7 source parameter: configure beryllium-7 isotope source parameters)
- `be7_src_param` : (铍7源参数：配置铍7同位素源参数)

#### Using Rundeck Parameters to Perturb Tracer Emissions by Sector and Region | 使用Rundeck参数按部门和区域扰动示踪物排放 
 For tracers that have emissions files listed in the standard way of `tracerName_01, tracerName_02, ... tracerName_NN`, one can tag emission files as belonging to an emission sector. Then, one can define rectangular regions (including global) and how each sector should be linearly scaled over each region. All this can be done from rundeck parameters, with no code recompilation. It is easiest demonstrated by an example: Say a rundeck has the following files listed:
 对于以`tracerName_01, tracerName_02, ... tracerName_NN`标准方式列出排放文件的示踪物，可以将排放文件标记为属于某个排放部门。然后，可以定义矩形区域（包括全球）以及每个部门在每个区域应如何线性缩放。所有这些都可以从rundeck参数完成，无需代码重新编译。通过示例最容易演示：假设rundeck列出了以下文件：
```


CO_01=/path/to/file/CO_biomassBurning.dat
CO_02=/path/to/file/fossilFuelCO.dat
CO_03=/path/to/file/OceanCO_2.dat
CH4_01=/path/to/file/wetlandsCH4.dat
CH4_02=/path/to/file/CH4_biomassBurning.dat
CH4_03=/path/to/file/termintes.dat
```
Then, let's say we want to cut European CO emissions to 50% and then increase global (multi-species) biomass burning emissions by 20%. One would set that run up with the following parameters:
然后，假设我们希望将欧洲CO排放削减到50%，然后将全球（多物种）生物质燃烧排放增加20%。可以使用以下参数设置该运行：
```

! First, tag the emissions files as belonging to sectors, by defining parameters based on their file numbers:
CO_01_sect='CO BBURN'
CO_02_sect='CO'
CO_03_sect='CO'
CH4_02_sect='BBURN'
!
! Next, make a table of regions by defining their North/South/East/West edges in degrees.
! Careful: they are allowed to overlap. Note that 3 extra regions are defined here, not
! strictly needed in this example:
!
REGIONS_ARE='global S_Asia E_Asia Europe N_America'
REG_S=        -90.,    5.,   15.,   25.,      15.
REG_N=         90.,   35.,   50.,   65.,      55.
REG_W=       -180.,   50.,   95.,  -10.,    -125.
REG_E=        180.,   95.,  160.,   50.,     -60.
!
! Now, define an order for the sectors, giving them the same names you used to tag source files:
SECTORS_ARE='CO BBURN'
!
! And, in that order, define the scaling factors to use per sector, per region:
!        global S_Asia E_Asia Europe N_America
SECT_01= 1.000, 1.000, 1.000, 0.500,     1.000 ! this is CO sector
SECT_02= 1.200, 1.000, 1.000, 1.000,     1.000 ! this is the BBURN sector
!
! Remember to check your model output diagnostics, to make sure everything worked as planned.
```