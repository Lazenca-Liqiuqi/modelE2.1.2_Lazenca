# Aerosol Tracers / 气溶胶示踪物

TwO-Moment Aerosol Sectional (TOMAS) microphysics model uses a sectional approach that represents the aerosol size distribution by predicting the amount of aerosol in several size sections or "bins" (Adams and Seinfeld, 2002; Lee and Adams, 2011).
二矩气溶胶分档（TOMAS）微物理模型使用分档方法，通过预测几个尺寸分段或"档"中的气溶胶量来表示气溶胶尺寸分布（Adams和Seinfeld，2002；Lee和Adams，2011）。

TOMAS uses a moving sectional approach to treat water uptake; changes in water mass do not move particles between sections.
TOMAS使用移动分档方法来处理水分吸收；水质量的变化不会在分段之间移动颗粒。

TOMAS tracks two moments of the aerosol size distribution in each size bin: total aerosol number and mass.
TOMAS在每个尺寸档中跟踪气溶胶尺寸分布的两个矩：气溶胶总数和质量。

Total mass is decomposed into several aerosol species, allowing prediction of the size-resolved aerosol composition.
总质量分解为几种气溶胶物种，允许预测尺寸分辨的气溶胶组成。

The TOMAS model tracks ten quantities for each size bin: sulfate mass, sea-salt mass, mass of externally mixed elemental carbon (EC), mass of internally mixed EC (mixed with all other species), mass of hydrophobic organic matter (OM), mass of hydrophilic OM, mass of mineral dust, mass of ammonium, and mass of aerosol-water and the number of aerosol particles in that size section.
TOMAS模型为每个尺寸档跟踪十个量：硫酸盐质量、海盐质量、外混元素碳（EC）质量、内混EC质量（与所有其他物种混合）、疏水有机物（OM）质量、亲水OM质量、矿物尘埃质量、铵质量、气溶胶水质量以及该尺寸分段中的气溶胶颗粒数。

In addition, the model tracks two bulk aerosol-phase species, methanesulfonic acid (MSA) and Ammonium(NH4), and six bulk gas-phase species: H2O2, SO2, dimethylsulfide (DMS), H2SO4, ammonia (NH3), and a lumped gas-phase tracer representing oxidized organic vapors that can form secondary organic aerosol (SOA).
此外，模型跟踪两个总体气溶胶相物种、甲烷磺酸（MSA）和铵（NH4），以及六个总体气相物种：H2O2、SO2、二甲基硫醚（DMS）、H2SO4、氨（NH3）和总体气相示踪物，代表可形成二次有机气溶胶（SOA）的氧化有机蒸气。

Gas-phase H2SO4 is assumed to be in pseudo-steady state equilibrium between chemical production and condensational/nucleation losses (Pierce and Adams, 2009).
气相H2SO4被假设为在化学产生与凝结/成核损失之间处于伪稳态平衡（Pierce和Adams，2009）。

TOMAS model simulates coagulation, condensation, and nucleation processes.
TOMAS模型模拟碰并、凝结和成核过程。

For in-cloud scavenging, modified Köhler theory is applied for the large-scale and convective clouds that are assumed to have supersaturations of 0.2% and 1.0%, respectively.
对于云内清除，改进的Köhler理论应用于大尺度云和对流云，假设其过饱和度分别为0.2%和1.0%。

Dry deposition uses the series resistance approach that treats sizedependent gravitational settling of particles and a size-dependent resistance in the quasilaminar sublayer.
干沉降使用串联阻力方法，处理依赖尺寸的颗粒重力沉降和准层流子层中依赖尺寸的阻力。

## TOMAS models by size resolution / 按尺寸分辨率的TOMAS模型

TOMAS-12: This is the default configuration in ModelE, which as 12 bins for each species.
TOMAS-12：这是ModelE中的默认配置，每个物种有12个档。

Size resolution from 10 nm to 10 micron - 10 logarithmically spaced bins covering from 10 nm to 1 micron and 2 logarithmically spaced bins covering from 1 microns to 10 micro.
尺寸分辨率从10 nm到10 μm——10个对数间隔的档覆盖10 nm到1 μm，2个对数间隔的档覆盖1 μm到10 μm。

Coarser bin spacing than TOMAS-30.
档间距比TOMAS-30粗。

Improved computation time.
改善计算时间。

TOMAS-12-3NM: Available in ModelE.
TOMAS-12-3NM：在ModelE中可用。

It is same as TOMAS-12 but has extra 3 bins extending the lowest size boundary to 3nm.
它与TOMAS-12相同，但有额外的3个档将最小尺寸边界扩展到3 nm。

Size resolution from 3 nm to 10 micron - 13 logarithmically spaced bins covering from 3 nm to 1 micron and 2 logarithmically spaced bins covering from 1 microns to 10 micro.
尺寸分辨率从3 nm到10 μm——13个对数间隔的档覆盖3 nm到1 μm，2个对数间隔的档覆盖1 μm到10 μm。

TOMAS-15: Same as TOMAS-12 but no lumping super-micron size.
TOMAS-15：与TOMAS-12相同但没有超微米尺寸的合并。

Size resolution ranging from 10 nm to 10 micron, spanned by 15 logarithmically spaced bins.
尺寸分辨率从10 nm到10 μm，由15个对数间隔的档跨越。

Not available in ModelE yet.
在ModelE中尚不可用。

TOMAS-30: All size-resolved aerosol species have size resolution ranging from 10 nm to 10 micron, spanned by 30 logarithmically spaced bins.
TOMAS-30：所有尺寸分辨的气溶胶物种的尺寸分辨率从10 nm到10 μm，由30个对数间隔的档跨越。

Not available in ModelE yet.
在ModelE中尚不可用。

TOMAS-40: Size resolution from 1 nm to 10 micron, again spanned by 40 logarithmically spaced bins.
TOMAS-40：尺寸分辨率从1 nm到10 μm，同样由40个对数间隔的档跨越。

Not available in ModelE yet.
在ModelE中尚不可用。

TOMAS-36: Size resolution from 3 nm to 10 micron, 36 logarithmically spaced bins.
TOMAS-36：尺寸分辨率从3 nm到10 μm，36个对数间隔的档。

Not available in ModelE yet.
在ModelE中尚不可用。

Note that TOMAS-12 and TOMAS-12-3NM are available in the developing branch, AR5_v2_branch, and AR5_aer - NOT IN AR5_branch.
请注意，TOMAS-12和TOMAS-12-3NM在开发分支AR5_v2_branch和AR5_aer中可用——不在AR5_branch中。

## Aerosol species properties table / 气溶胶物种性质表

| | SO4 | Sea salt | BC | OA | Dust | NH4 | Aerosol-water | Aerosol number |
|---|-----|----------|----|----|----|-----|---------------|----------------|
| Molecular weight (g/mol) | 96 | 75 | 12 | 200 | 1 | 18 | 18 | n/a |
| Density (kg/m³) | 1780 | 2165 | 1800 | 1400 | Dp<2μm: 2500; Dp>2μm: 2650 | 1700 | 1000 | n/a |

## Aerosol tracers / 气溶胶示踪物

### Sulfate / 硫酸盐
12 tracers (i.e. ASO4__01 to ASO4__12) for TOMAS-12 ; 15 tracers (i.e. ASO4__01 to ASO4__15) for TOMAS-12-3NM
TOMAS-12为12个示踪物（即ASO4__01到ASO4__12）；TOMAS-12-3NM为15个示踪物（即ASO4__01到ASO4__15）

- **Direct emissions**: 2.5% by mass of anthropogenic SO2 emissions in the model are assumed to be emitted as SO4.
  **直接排放**：模型中人为SO2排放的2.5%（质量）被假设为以SO4形式排放。
- **Gas-phase chemistry**: The gaseous oxidation of SO2 by OH (Koch et al., 1999; 2006). The SO4 produced from the gas-phase chemistry is condensed on SO4 tracers.
  **气相化学**：SO2被OH气相氧化（Koch等，1999；2006）。气相化学产生的SO4凝结在SO4示踪物上。
- **Aqueous-phase chemistry**: in-cloud oxidation of SO2 by H2O2 (Koch et al., 1999; 2006). The SO4 produced from the aqueous-phase chemistry is condensed on SO4 tracers.
  **液相化学**：SO2被H2O2云内氧化（Koch等，1999；2006）。液相化学产生的SO4凝结在SO4示踪物上。

### Sea salt / 海盐
12 tracers (ANACL_01 to ANACL_12) for TOMAS-12 ; 15 tracers for TOMAS-12-3NM.
TOMAS-12为12个示踪物（ANACL_01到ANACL_12）；TOMAS-12-3NM为15个示踪物。

Sea salt particles are being emitted as a function of 10-m wind speed, based on Gong et al. (2003).
海盐颗粒作为10米风速的函数排放，基于Gong等（2003）。

### Organic aerosols (OA) / 有机气溶胶
OA is distinguished into two types: hydrophobic (AOCOB) and hydrophilic (AOCIL).
OA分为两种类型：疏水性（AOCOB）和亲水性（AOCIL）。

Each type has 12 tracers for TOMAS-12 (or 15 tracers for TOMAS-12-3NM).
每种类型在TOMAS-12中有12个示踪物（或在TOMAS-12-3NM中有15个示踪物）。

TOMAS has one tracer for SOA precursor gas (SOAgas) and no tracer for a separate SOA - the SOAgas condenses on hydrophilic OA tracers directly.
TOMAS有一个SOA前体气体示踪物（SOAgas），没有单独的SOA示踪物——SOAgas直接凝结在亲水OA示踪物上。

- **POA**: 50% of fossil fuel and biofuel emissions are assumed to be hydrophobic, which are being converted to hydrophilic with an e-folding time of 1.5 days. The ratio of organic matter-to-organic carbon is OM/OC=1.4.
  **POA**：50%的化石燃料和生物燃料排放被假设为疏水性，以1.5天的e-fold时间转换为亲水性。有机物与有机碳的比率为OM/OC=1.4。
- **SOA**: SOA emission is simply assumed to be 10% of terpene emissions.
  **SOA**：SOA排放简单地假设为萜烯排放的10%。

### Elemental Carbon (EC) / 元素碳
EC is distinguished into two types: externally mixed EC (AECOB) and internally mixed EC (AECIL).
EC分为两种类型：外混EC（AECOB）和内混EC（AECIL）。

Each type has 12 tracers for TOMAS-12 (or 15 tracers for TOMAS-12-3NM).
每种类型在TOMAS-12中有12个示踪物（或在TOMAS-12-3NM中有15个示踪物）。

80% of fossil fuel and biofuel emissions are considered to produce externally mixed BC, which are being converted to internally mixed BC with an e-folding time of 1.5 days.
80%的化石燃料和生物燃料排放被认为产生外混BC，以1.5天的e-fold时间转换为内混BC。

### Dust / 尘埃
12 tracers (ADUST_01 to ADUST_12) for TOMAS-12; 15 tracers (ADUST_01 to ADUST_15) for TOMAS-12-3NM
TOMAS-12为12个示踪物（ADUST_01到ADUST_12）；TOMAS-12-3NM为15个示踪物（ADUST_01到ADUST_15）

### Ammonium (NH4) / 铵
12 tracers in TOMAS model but lumped into one tracer when exit the TOMAS model.
TOMAS模型中有12个示踪物，但在离开TOMAS模型时合并为一个示踪物。

Produced from NH3 uptake, simply based on the neutralization with SO4 tracers (i.e. 2 moles of ammonium per 1 mole of sulfate and the remainder of ammonia is left in the gas phase)
由NH3吸收产生，简单地基于与SO4示踪物的中和（即每1摩尔硫酸盐对应2摩尔铵，剩余的氨留在气相中）

### Aerosol-water / 气溶胶水
12 tracers (i.e. AH2O__01 to AH2O__12) for TOMAS-12 ; 15 tracers (i.e. AH2O__01 to AH2O__15) for TOMAS-12-3NM.
TOMAS-12为12个示踪物（即AH2O__01到AH2O__12）；TOMAS-12-3NM为15个示踪物（即AH2O__01到AH2O__15）。

Water update by sulfate, sea-salt, and hydrophilic OA.
水由硫酸盐、海盐和亲水OA更新。

### Aerosol number / 气溶胶数
12 tracers (i.e. ANUM__01 to ANUM__12) for TOMAS-12 ; 15 tracers (i.e. ANUM__01 to ANUM__15) for TOMAS-12-3NM.
TOMAS-12为12个示踪物（即ANUM__01到ANUM__12）；TOMAS-12-3NM为15个示踪物（即ANUM__01到ANUM__15）。

## References / 参考文献

Adams, P. J., and Seinfeld, J. H.: Predicting global aerosol size distributions in general circulation models, Journal of Geophysical Research-Atmospheres, 107, doi:10.1029/2001JD001010, 2002.

Lee, Y. H. and Adams, P. J.: A fast and efficient version of the TwO-Moment Aerosol Sectional (TOMAS) global aerosol microphysics model, Aerosol Sci. Tech., 46, 678–689, doi:10.1080/02786826.2011.643259, 2011.

Pierce, J. R., and Adams, P. J.: A Computationally Efficient Aerosol Nucleation/Condensation Method: Pseudo-Steady-State Sulfuric Acid, Aerosol Science and Technology, 43, 216-226, 2009.

**Document End / 文档结束**
