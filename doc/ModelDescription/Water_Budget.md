# (Salt) Water Budget in GISS ModelE / GISS ModelE中的（咸）水预算

Variables defined on atmosphere grid are not preceded by 'a'.
定义在大气网格上的变量不带'a'前缀。

Variables defined on ocean grid are preceded by 'o'.
定义在海洋网格上的变量带'o'前缀。

The section "**Without Fluxes**" indicates the prognostic variables that contribute to the salt water mass (kg) for each reservoir.
"**Without Fluxes**"部分表示对每个水库的咸水质量（kg）有贡献的预报变量。

After many subroutines, water mass has been removed from some reservoirs but not yet been added to the next reservoirs; water mass is temporarily stored in a "flux" array.
在许多子程序之后，水质量已从某些水库移除但尚未添加到下一个水库；水质量临时存储在"通量"数组中。

After each subroutine, reservoirs which do not have unadded fluxes are not mentioned; for other reservoirs flux arrays are indicated.
在每个子程序之后，未添加未加通量的水库不会被提及；对于其他水库，指示通量数组。

## Without Fluxes / 无通量状态

```
AtmosQ  = Q*AM*DXYP
Clouds  = WM*AM*DXYP
LandIce = (SNOWLI+ACE1LI+ACE2LI)*FLICE*DXYP
Ground  = GRNDW = see formula below
LakeIce = (SNOWI+ACE1I+MSI)*RSI*FLAKE*DXYP
LiqLake = MWL
SeaIce  = (SNOWI+ACE1I+MSI)*RSI*FOCEAN*DXYP
LiqOcen = oMO*oDXYP + MDWNIMP

NSNB = NSN_IJ(1)
NSNV = NSN_IJ(2)
WIJ  = FB * {Sum[W_IJ(1:NGM,1)] + FR_SNOW_IJ(1) * Sum[WSN_IJ(1:NSNB,1)]} +
     + FV * {Sum[W_IJ(1:NGM,2)] + FR_SNOW_IJ(2) * Sum[WSN_IJ(1:NSNV,2)]}
GRNDW = RHOW * {FEARTH * WIJ + FLAKE * Sum[W_IJ(1:NGM,3)]} * DXYP
```

## After MELT_SI / 在MELT_SI之后

MELTI removed from LakeIce and SeaIce
MELTI从LakeIce和SeaIce中移除

```
LiqLake = MWL + MELTI(non ocean)
LiqOcen = oMO*oDXYP + MDWNIMP + MELTI(ocean)
```

## After CONDSE / 在CONDSE之后

PREC removed from AtmosQ
PREC从AtmosQ中移除

```
LandIce = (SNOWLI+ACE1LI+ACE2LI)*FLICE*DXYP + PREC*FLICE*DXYP
Ground  = GRNDW + PREC*FEARTH*DXYP
LakeIce = (SNOWI+ACE1I+MSI)*RSI*FLAKE*DXYP + PREC*RSI*FLAKE*DXYP
LiqLake = MWL + MELTI(non ocean) + PREC*(1-RSI)*FLAKE*DXYP
SeaIce  = (SNOWI+ACE1I+MSI)*RSI*FOCEAN*DXYP + PREC*RSI*FOCEAN*DXYP
LiqOcen = oMO*oDXYP + MDWNIMP + MELTI(ocean) + PREC*(1-RSI)*FOCEAN*DXYP
```

## After PRECIP_SI / 在PRECIP_SI之后

PREC added to and RUNPSI removed from LakeIce and SeaIce
PREC添加到LakeIce和SeaIce，RUNPSI从LakeIce和SeaIce中移除

```
LandIce = (SNOWLI+ACE1LI+ACE2LI)*FLICE*DXYP + PREC*FLICE*DXYP
Ground  = GRNDW + PREC*FEARTH*DXYP
LiqLake = MWL + MELTI(non ocean) + PREC*(1-RSI)*FLAKE*DXYP + RUNPSI*RSI*FLAKE*DXYP
LiqOcen = oMO*oDXYP + MDWNIMP + MELTI(ocean) + PREC*(1-RSI)*FOCEAN*DXYP + RUNPSI*RSI*FOCEAN*DXYP
```

## After PRECIP_LI / 在PRECIP_LI之后

PREC added to and RUNOLI removed from LandIce
PREC添加到LandIce，RUNOLI从LandIce中移除

```
Ground  = GRNDW + PREC*FEARTH*DXYP
LiqLake = MWL + MELTI(non ocean) + PREC*(1-RSI)*FLAKE*DXYP + RUNPSI*RSI*FLAKE*DXYP + RUNOLI(use 1)*FLICE*DXYP
LiqOcen = oMO*oDXYP + MDWNIMP + MELTI(ocean) + PREC*(1-RSI)*FOCEAN*DXYP + RUNPSI*RSI*FOCEAN*DXYP
```

## After PRECIP_LK / 在PRECIP_LK之后

PREC, RUNPSI and RUNOLI added to LiqLake
PREC、RUNPSI和RUNOLI添加到LiqLake

```
Ground  = GRNDW + PREC*FEARTH*DXYP
LiqOcen = oMO*oDXYP + MDWNIMP + MELTI(ocean) + PREC*(1-RSI)*FOCEAN*DXYP + RUNPSI*RSI*FOCEAN*DXYP
```

## After PRECIP_OC / 在PRECIP_OC之后

PREC and RUNPSI added to LiqOcen
PREC和RUNPSI添加到LiqOcen

```
Ground  = GRNDW + PREC*FEARTH*DXYP
LiqOcen = oMO*oDXYP + MDWNIMP + MELTI(ocean)
```

## After EARTH / 在EARTH之后

EVAPOR(4) added to AtmosQ; PREC added to and RUNOE removed from Ground
EVAPOR(4)添加到AtmosQ；PREC添加到Ground，RUNOE从Ground中移除

```
Ground  = GRNDW + EVAPOR(4)*FEARTH*DXYP
LiqLake = MWL + RUNOE*FEARTH*DXYO
LiqOcen = oMO*oDXYP + MDWNIMP + MELTI(ocean)
```

## After ATM_DIFFUS / 在ATM_DIFFUS之后

EVAPOR(1:3) added to AtmosQ
EVAPOR(1:3)添加到AtmosQ

```
LandIce = (SNOWLI+ACE1LI+ACE2LI)*FLICE*DXYP - EVAPOR(3)*FLICE*DXYP
LakeIce = (SNOWI+ACE1I+MSI)*RSI*FLAKE*DXYP - EVAPOR(2)*RSI*FLAKE*DXYP
LiqLake = MWL + RUNOE*FEARTH*DXYO - EVAPOR(1)*(1-RSI)*FLAKE*DXYP
SeaIce  = (SNOWI+ACE1I+MSI)*RSI*FOCEAN*DXYP - EVAPOR(2)*RSI*FOCEAN*DXYP
LiqOcen = oMO*oDXYP + MDWNIMP + MELTI(ocean) - EVAPOR(1)*(1-RSI)*FOCEAN*DXYP
```

## After SURFCE / 在SURFCE之后

```
LandIce = (SNOWLI+ACE1LI+ACE2LI)*FLICE*DXYP - EVAPOR(3)*FLICE*DXYP
LakeIce = (SNOWI+ACE1I+MSI)*RSI*FLAKE*DXYP - EVAPOR(2)*RSI*FLAKE*DXYP
LiqLake = MWL + RUNOE*FEARTH*DXYO - EVAPOR(1)*(1-RSI)*FLAKE*DXYP
SeaIce  = (SNOWI+ACE1I+MSI)*RSI*FOCEAN*DXYP - EVAPOR(2)*RSI*FOCEAN*DXYP
LiqOcen = oMO*oDXYP + MDWNIMP + MELTI(ocean) - EVAPOR(1)*(1-RSI)*FOCEAN*DXYP
```

## After UNDERICE / 在UNDERICE之后

```
LandIce = (SNOWLI+ACE1LI+ACE2LI)*FLICE*DXYP - EVAPOR(3)*FLICE*DXYP
LakeIce = (SNOWI+ACE1I+MSI)*RSI*FLAKE*DXYP - EVAPOR(2)*RSI*FLAKE*DXYP
LiqLake = MWL + RUNOE*FEARTH*DXYO - EVAPOR(1)*(1-RSI)*FLAKE*DXYP
SeaIce  = (SNOWI+ACE1I+MSI)*RSI*FOCEAN*DXYP - EVAPOR(2)*RSI*FOCEAN*DXYP
LiqOcen = oMO*oDXYP + MDWNIMP + MELTI(ocean) - EVAPOR(1)*(1-RSI)*FOCEAN*DXYP
```

## After GROUND_SI / 在GROUND_SI之后

EVAPOR(2) and RUNOSI removed from LakeIce and SeaIce
EVAPOR(2)和RUNOSI从LakeIce和SeaIce中移除

```
LandIce = (SNOWLI+ACE1LI+ACE2LI)*FLICE*DXYP - EVAPOR(3)*FLICE*DXYP
LiqLake = MWL + RUNOE*FEARTH*DXYO - EVAPOR(1)*(1-RSI)*FLAKE*DXYP + RUNOSI*RSI*FLAKE*DXYP
LiqOcen = oMO*oDXYP + MDWNIMP + MELTI(ocean) - EVAPOR(1)*(1-RSI)*FOCEAN*DXYP + RUNOSI*RSI*FOCEAN*DXYP
```

## After GROUND_LI / 在GROUND_LI之后

EVAPOR(3) and RUNOLI removed from LandIce
EVAPOR(3)和RUNOLI从LandIce中移除

```
LiqLake = MWL + RUNOE*FEARTH*DXYO - EVAPOR(1)*(1-RSI)*FLAKE*DXYP + RUNOSI*RSI*FLAKE*DXYP + RUNOLI*FLICE*DXYP
LiqOcen = oMO*oDXYP + MDWNIMP + MELTI(ocean) - EVAPOR(1)*(1-RSI)*FOCEAN*DXYP + RUNOSI*RSI*FOCEAN*DXYP
```

## After GROUND_LK / 在GROUND_LK之后

EVAPOR(3) and DMSI removed from and RUNOE, RUNOSI and RUNOLI added to LiqLake
EVAPOR(3)和DMSI从LiqLake中移除，RUNOE、RUNOSI和RUNOLI添加到LiqLake

```
LakeIce = (SNOWI+ACE1I+MSI)*RSI*FLAKE*DXYP + DMSI(1)*(1-RSI)*FLAKE*DXYP + DMSI(2)*RSI*FLAKE*DXYP
LiqOcen = oMO*oDXYP + MDWNIMP + MELTI(ocean) - EVAPOR(1)*(1-RSI)*FOCEAN*DXYP + RUNOSI*RSI*FOCEAN*DXYP
```

## After RIVERF / 在RIVERF之后

river flow removed from LiqLake and added to LiqOcen
河流流量从LiqLake移除并添加到LiqOcen

```
LakeIce = (SNOWI+ACE1I+MSI)*RSI*FLAKE*DXYP + DMSI(1)*(1-RSI)*FLAKE*DXYP + DMSI(2)*RSI*FLAKE*DXYP
LiqOcen = oMO*oDXYP + MDWNIMP + MELTI(ocean) - EVAPOR(1)*(1-RSI)*FOCEAN*DXYP + RUNOSI*RSI*FOCEAN*DXYP + FLOWO
```

## After GROUND_E / 在GROUND_E之后

```
LakeIce = (SNOWI+ACE1I+MSI)*RSI*FLAKE*DXYP + DMSI(1)*(1-RSI)*FLAKE*DXYP + DMSI(2)*RSI*FLAKE*DXYP
LiqOcen = oMO*oDXYP + MDWNIMP + MELTI(ocean) - EVAPOR(1)*(1-RSI)*FOCEAN*DXYP + RUNOSI*RSI*FOCEAN*DXYP + FLOWO
```

## After GROUND_OC / 在GROUND_OC之后

MELTI and RUNOSI added to and EVAPOR(1) oDMSI removed from LiqOcen
MELTI和RUNOSI添加到LiqOcen，EVAPOR(1)和oDMSI从LiqOcen中移除

```
LakeIce = (SNOWI+ACE1I+MSI)*RSI*FLAKE*DXYP + DMSI(1)*(1-RSI)*FLAKE*DXYP + DMSI(2)*RSI*FLAKE*DXYP
SeaIce  = (SNOWI+ACE1I+MSI)*RSI*FOCEAN*DXYP + oDMSI(1)*(1-oRSI)*oFOCEAN*oDXYP + oDMSI(2)*oRSI*oFOCEAN*oDXYP
```

## After OCONV / 在OCONV之后

```
LakeIce = (SNOWI+ACE1I+MSI)*RSI*FLAKE*DXYP + DMSI(1)*(1-RSI)*FLAKE*DXYP + DMSI(2)*RSI*FLAKE*DXYP
SeaIce  = (SNOWI+ACE1I+MSI)*RSI*FOCEAN*DXYP + oDMSI(1)*(1-oRSI)*oFOCEAN*oDXYP + oDMSI(2)*oRSI*oFOCEAN*oDXYP
```

## After ODYNAM / 在ODYNAM之后

```
LakeIce = (SNOWI+ACE1I+MSI)*RSI*FLAKE*DXYP + DMSI(1)*(1-RSI)*FLAKE*DXYP + DMSI(2)*RSI*FLAKE*DXYP
SeaIce  = (SNOWI+ACE1I+MSI)*RSI*FOCEAN*DXYP + oDMSI(1)*(1-oRSI)*oFOCEAN*oDXYP + oDMSI(2)*oRSI*oFOCEAN*oDXYP
```

## After OCEANS / 在OCEANS之后

```
LakeIce = (SNOWI+ACE1I+MSI)*RSI*FLAKE*DXYP + DMSI(1)*(1-RSI)*FLAKE*DXYP + DMSI(2)*RSI*FLAKE*DXYP
SeaIce  = (SNOWI+ACE1I+MSI)*RSI*FOCEAN*DXYP + oDMSI(1)*(1-oRSI)*oFOCEAN*oDXYP + oDMSI(2)*oRSI*oFOCEAN*oDXYP
```

## After FORM_SI / 在FORM_SI之后

DMSI added to LakeIce and oDMSI added to SeaIce
DMSI添加到LakeIce，oDMSI添加到SeaIce

## After ADVSI / 在ADVSI之后

## Notes / 说明

EVAPOR is positive for dew and is negative for evaporation.
EVAPOR对于露为正，对于蒸发为负。

RUNOLI array is used twice, to carry flux generated in PRECIP_LI and in GROUND_LI.
RUNOLI数组使用两次，用于携带PRECIP_LI和GROUND_LI中产生的通量。

**Document End / 文档结束**
