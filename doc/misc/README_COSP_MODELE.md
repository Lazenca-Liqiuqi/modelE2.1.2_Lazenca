# COSP (CFMIP Observation Simulator Package) - ModelE Integration Guide

###############################################################################
                    COSP (CFMIP Observation Simulator Package)

Home Page: http://cfmip.metoffice.com/COSP.html
**主页: http://cfmip.metoffice.com/COSP.html**

Code Base: http://code.google.com/p/cfmip-obs-sim/
**代码库: http://code.google.com/p/cfmip-obs-sim/**

COSP Documentation:
**COSP文档:**
    http://code.google.com/p/cfmip-obs-sim/downloads/detail?name=COSP_user_manual.v1.3.1.pdf

Current Version 1.3.2 (April 2011)
**当前版本 1.3.2 (2011年4月)**

Overview: Bodas-Salcedo, A., and Coauthors, 2011: COSP: Satellite simulation
    software for model assessment. Bull. Amer. Meteor. Soc., 92, 1023-1043.
    doi: 10.1175/2011BAMS2856.1
**概述: Bodas-Salcedo, A., 及合著者, 2011: COSP: 模型评估的卫星模拟
    软件. 美国气象学会通报, 92, 1023-1043.
    doi: 10.1175/2011BAMS2856.1**

    From Bodas-Salcede et al. 2011
    **根据Bodas-Salcede等人2011年研究**

        COSP is a flexible software tool that enables the simulation from model
        variables of data from several satelliteborne active and passive sensors.
        **COSP是一个灵活的软件工具，能够从模型变量模拟多个星载主动和被动传感器的数据。**

        It facilitates the use of satellite data to evaluate models in a
        consistent way.
        **它促进了使用卫星数据以一致方式评估模型。**

        The flexibility of COSP makes it suitable for use in many
        types of numerical models, from high-resolution models (~1-km
        resolution) to coarse-resolution models, such as the GCMs used in climate
        modeling, and the scales in be- tween used in weather forecast and
        regional models.
        **COSP的灵活性使其适用于多种类型的数值模型，从高分辨率模型（~1公里分辨率）到粗分辨率模型，如气候建模中使用的GCM，以及天气预报和区域模型中使用的介于两者之间的尺度。**

        The fact that COSP includes several simulators under the
        same interface facilitates the implementation of a range of simulators in
        models.
        **COSP在同一接口下包含多个模拟器的事实，便于在模型中实现一系列模拟器。**

        Another advantage of COSP-and in general, the simulator
        approach--is that it facilitates model intercomparison, not only
        model-satellite comparison (e.g., comparisons of cloud properties
        simulated by GCMs and CRMs).
        **COSP的另一个优势——一般来说，模拟器方法——是它促进了模型间比较，不仅是模型-卫星比较（例如，GCM和CRM模拟的云属性比较）。**

Key Features:
**主要特性:**

- Satellite data simulation from model variables
**从模型变量模拟卫星数据**

- Multiple sensor support under unified interface
**统一接口下的多传感器支持**

- Consistent model evaluation framework
**一致的模型评估框架**

- Cross-resolution compatibility
**跨分辨率兼容性**

Usage in ModelE:
**在ModelE中的使用:**

COSP is integrated into ModelE to provide satellite-like output
that can be directly compared with observational data. This integration
helps validate cloud parameterizations and radiation schemes
in the model.
**COSP已集成到ModelE中，提供可与观测数据直接比较的卫星类输出。这种集成有助于验证模型中的云参数化和辐射方案。**

The COSP output includes:
**COSP输出包括:**

- Cloud optical depth and height distributions
**云光学厚度和高度分布**

- Cloud fraction statistics
**云比例统计**

- Radar reflectivity profiles
**雷达反射率剖面**

- Lidar backscatter profiles
**激光雷达后向散射剖面**

Installation:
**安装:**

COSP is typically enabled during the ModelE compilation process
by setting appropriate compiler flags in the rundeck configuration.
**COSP通常在ModelE编译过程中通过在rundeck配置中设置适当的编译器标志来启用。**

For more information, see the complete COSP user manual at the URL
provided above.
**更多信息，请参阅上面URL提供的完整COSP用户手册。**

---
*Document updated: October 23, 2025*