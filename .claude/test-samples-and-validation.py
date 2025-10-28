#!/usr/bin/env python3
"""
ModelE2.1.2_Lazenca 翻译工具链测试和验证
Translation Toolchain Testing and Validation for ModelE2.1.2_Lazenca

这个模块提供翻译工具链的测试样本和验证功能，确保所有组件正常工作。
This module provides test samples and validation functionality for the translation toolchain, ensuring all components work correctly.

作者 | Author: ModelE2.1.2_Lazenca翻译团队
版本 | Version: v1.0
创建日期 | Created: 2025-10-28
"""

import os
import sys
import json
import logging
from typing import Dict, List, Tuple, Optional
from pathlib import Path

# 导入自定义模块
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# 动态导入模块
fortran_preserver_file = os.path.join(current_dir, 'fortran-comment-format-preservation.py')
quality_control_file = os.path.join(current_dir, 'quality-control-pipeline.py')

if os.path.exists(fortran_preserver_file):
    import importlib.util
    spec = importlib.util.spec_from_file_location("fortran_preserver", fortran_preserver_file)
    fortran_preserver = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fortran_preserver)
    FortranCommentPreserver = fortran_preserver.FortranCommentPreserver
else:
    raise FileNotFoundError(f"Fortran format preserver file not found: {fortran_preserver_file}")

if os.path.exists(quality_control_file):
    import importlib.util
    spec = importlib.util.spec_from_file_location("quality_control", quality_control_file)
    quality_control = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(quality_control)
    QualityControlPipeline = quality_control.QualityControlPipeline
else:
    raise FileNotFoundError(f"Quality control file not found: {quality_control_file}")

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TranslationToolchainTester:
    """翻译工具链测试器"""

    def __init__(self):
        """初始化测试器"""
        self.test_samples = self.create_test_samples()
        self.format_preserver = FortranCommentPreserver()
        self.quality_pipeline = QualityControlPipeline()

    def create_test_samples(self) -> Dict[str, str]:
        """创建测试样本"""
        samples = {
            'fortran_fixed_format': '''C     这是一个测试用的固定格式Fortran程序
C     用于测试注释格式保持功能
C     作者: ModelE翻译团队
C     版本: v1.0
      PROGRAM ATM_TEST_DRV
      IMPLICIT NONE
C
C     程序参数定义
C
      INTEGER :: IM, JM, LM  ! 网格维度参数
      PARAMETER (IM=72, JM=46, LM=20)

      REAL*8 :: DT            ! 时间步长 (秒)
      REAL*8 :: TIME          ! 当前时间 (秒)

C     变量声明
      REAL*8, DIMENSION(IM,JM,LM) :: T  ! 温度场 (K)
      REAL*8, DIMENSION(IM,JM,LM) :: Q  ! 湿度场 (kg/kg)
      REAL*8, DIMENSION(IM,JM) :: PS   ! 地面气压 (Pa)

C     初始化变量
      PRINT *, '初始化大气驱动程序...'
      DT = 1800.0D0  ! 30分钟时间步长
      TIME = 0.0D0

C     调用初始化子程序
      CALL INIT_ATMOS(IM, JM, LM, T, Q, PS)

C     主时间循环
      DO WHILE (TIME .LT. 86400.0D0)  ! 运行24小时
C        更新时间
         TIME = TIME + DT

C        调用物理过程
         CALL PHYSICS_DRV(IM, JM, LM, T, Q, PS, DT)

C        输出诊断信息
         IF (MOD(INT(TIME/DT), 4) .EQ. 0) THEN
            PRINT *, '时间步:', INT(TIME/DT), ' 时间:', TIME/3600.0, '小时'
         END IF
      END DO

      PRINT *, '模拟完成!'

      END PROGRAM ATM_TEST_DRV

C-----------------------------------------------------------------------
C     大气初始化子程序
C     功能: 初始化大气温度、湿度和气压场
C     输入: IM, JM, LM - 网格维度
C     输出: T, Q, PS - 初始化的气象场
C-----------------------------------------------------------------------
      SUBROUTINE INIT_ATMOS(IM, JM, LM, T, Q, PS)
      IMPLICIT NONE
      INTEGER IM, JM, LM
      REAL*8 T(IM,JM,LM), Q(IM,JM,LM), PS(IM,JM)

C     局部变量
      INTEGER I, J, L
      REAL*8 T0, Q0, P0

C     标准大气参数
      T0 = 288.15D0  ! 标准温度 (K)
      Q0 = 0.001D0   ! 标准湿度 (kg/kg)
      P0 = 101325.0D0 ! 标准气压 (Pa)

C     初始化温度场 (等温大气)
      DO L = 1, LM
         DO J = 1, JM
            DO I = 1, IM
               T(I,J,L) = T0
               Q(I,J,L) = Q0
            END DO
         END DO
      END DO

C     初始化地面气压 (均一气压)
      DO J = 1, JM
         DO I = 1, IM
            PS(I,J) = P0
         END DO
      END DO

      PRINT *, '大气初始化完成'

      RETURN
      END
''',

            'fortran_free_format': '''! 这是一个测试用的自由格式Fortran程序
! 用于测试现代Fortran格式保持功能
! 作者: ModelE翻译团队
! 版本: v1.0

program radiation_test
  use iso_fortran_env, only: real64
  implicit none

  ! 程序参数
  integer, parameter :: nx = 144        ! 经度格点数
  integer, parameter :: ny = 90         ! 纬度格点数
  integer, parameter :: nz = 20         ! 垂直层次数
  integer, parameter :: nb = 2          ! 光谱波段数 (短波、长波)

  real(real64), parameter :: pi = 3.14159265358979323846_real64
  real(real64), parameter :: solar_constant = 1361.0_real64  ! 太阳常数 (W/m²)
  real(real64), parameter :: stefan_boltzmann = 5.67e-8_real64  ! 斯特藩-玻尔兹曼常数

  ! 变量声明
  real(real64) :: time                   ! 模拟时间 (秒)
  real(real64) :: dt                     ! 时间步长 (秒)
  real(real64) :: solar_declination      ! 太阳赤纬 (弧度)
  real(real64) :: hour_angle             ! 时角 (弧度)

  ! 辐射场变量
  real(real64), dimension(nx, ny, nz) :: temperature    ! 温度场 (K)
  real(real64), dimension(nx, ny, nz) :: humidity       ! 湿度场 (kg/kg)
  real(real64), dimension(nx, ny, nz) :: pressure       ! 气压场 (Pa)
  real(real64), dimension(nx, ny, nb) :: radiative_flux ! 辐射通量 (W/m²)

  ! 光学性质
  real(real64), dimension(nx, ny, nz) :: optical_depth   ! 光学厚度
  real(real64), dimension(nx, ny, nz) :: single_scatter  ! 单次散射反照率
  real(real64), dimension(nx, ny, nz) :: asymmetry_param  ! 不对称因子

  print *, "初始化辐射传输模块..."

  ! 设置初始条件
  call initialize_fields(nx, ny, nz, temperature, humidity, pressure, &
                       optical_depth, single_scatter, asymmetry_param)

  ! 主时间循环
  time = 0.0_real64
  dt = 3600.0_real64  ! 1小时时间步长

  do while (time < 86400.0_real64)  ! 运行24小时

    ! 计算太阳几何参数
    solar_declination = calculate_solar_declination(time)
    hour_angle = calculate_hour_angle(time)

    ! 计算短波辐射
    call calculate_shortwave_radiation(nx, ny, nz, nb, &
        temperature, humidity, pressure, &
        optical_depth, single_scatter, asymmetry_param, &
        solar_declination, hour_angle, solar_constant, &
        radiative_flux(:,:,1))

    ! 计算长波辐射
    call calculate_longwave_radiation(nx, ny, nz, nb, &
        temperature, humidity, pressure, &
        optical_depth, single_scatter, &
        stefan_boltzmann, &
        radiative_flux(:,:,2))

    ! 更新时间
    time = time + dt

    ! 输出进度
    if (mod(int(time/dt), 6) == 0) then
      print *, "模拟时间:", time/3600.0_real64, "小时"
    end if

  end do

  print *, "辐射传输模拟完成!"

contains

  ! 初始化场变量
  subroutine initialize_fields(nx, ny, nz, T, Q, P, tau, omega, g)
    integer, intent(in) :: nx, ny, nz
    real(real64), intent(out) :: T(nx, ny, nz), Q(nx, ny, nz), P(nx, ny, nz)
    real(real64), intent(out) :: tau(nx, ny, nz), omega(nx, ny, nz), g(nx, ny, nz)

    integer :: i, j, k
    real(real64) :: p0, t0, scale_height

    ! 标准大气参数
    p0 = 101325.0_real64    ! 海平面气压 (Pa)
    t0 = 288.15_real64      ! 海平面温度 (K)
    scale_height = 8500.0_real64  ! 标高 (m)

    ! 初始化温度和湿度
    do k = 1, nz
      do j = 1, ny
        do i = 1, nx
          ! 温度随高度递减
          T(i,j,k) = t0 - 6.5e-3_real64 * (k-1) * scale_height/nz

          ! 相对湿度设为常数
          Q(i,j,k) = 0.5e-3_real64

          ! 气压随高度指数递减
          P(i,j,k) = p0 * exp(-(k-1) * scale_height/nz / scale_height)

          ! 简单的光学性质
          tau(i,j,k) = 0.1_real64
          omega(i,j,k) = 0.9_real64
          g(i,j,k) = 0.85_real64
        end do
      end do
    end do

    print *, "场变量初始化完成"

  end subroutine initialize_fields

end program radiation_test
''',

            'html_document': '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ModelE2.1.2_Lazenca 用户指南 - 大气驱动程序</title>
    <link rel="stylesheet" href="../styles/main.css">
</head>
<body>
    <header>
        <h1>ModelE2.1.2_Lazenca 用户指南</h1>
        <nav>
            <ul>
                <li><a href="index.html">首页</a></li>
                <li><a href="compiling.html">编译指南</a></li>
                <li><a href="running.html">运行指南</a></li>
                <li><a href="atmosphere.html">大气模块</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="atmospheric-driver">
            <h2>大气驱动程序 (ATM_DRV.f)</h2>

            <p>
                <strong>ATM_DRV.f</strong> 是ModelE2.1.2_Lazenca中大气过程的核心驱动程序，
                负责协调所有大气物理过程的执行，包括动力学、辐射、云微物理、
                边界层过程等。该模块是整个大气模拟系统的中枢控制器。
            </p>

            <h3>主要功能</h3>
            <ul>
                <li><strong>过程协调</strong>: 管理各个物理过程模块的调用顺序和数据传递</li>
                <li><strong>时间步进</strong>: 控制模型的时间积分和子循环</li>
                <li><strong>诊断输出</strong>: 收集和输出各种大气诊断变量</li>
                <li><strong>边界条件</strong>: 处理海表温度、海冰等边界条件数据</li>
            </ul>

            <h3>关键子程序</h3>
            <dl>
                <dt><code>ATM_DRV</code></dt>
                <dd>主驱动子程序，控制整个大气模拟的时间循环</dd>

                <dt><code>INIT_ATM</code></dt>
                <dd>大气初始化子程序，设置初始场和模型参数</dd>

                <dt><code>PHYSICS_DRV</code></dt>
                <dd>物理过程驱动，协调辐射、对流、边界层等过程</dd>

                <dt><code>DYNAMICS_DRV</code></dt>
                <dd>动力学驱动，处理风场和温度场的动力学演化</dd>
            </dl>

            <h3>数值方法</h3>
            <p>
                大气驱动程序采用<strong>算子分裂方法</strong>将不同的物理过程分离处理，
                每个时间步内按照以下顺序执行：
            </p>

            <ol>
                <li><strong>动力学过程</strong>: 求解原始方程组，更新风场、温度场</li>
                <li><strong>辐射过程</strong>: 计算短波和长波辐射加热率</li>
                <li><strong>云微物理</strong>: 处理云的形成、消散和降水过程</li>
                <li><strong>边界层过程</strong>: 计算湍流混合和地表通量</li>
                <li><strong>对流过程</strong>: 参数化积云对流效应</li>
            </ol>

            <h3>重要参数</h3>
            <table class="parameter-table">
                <thead>
                    <tr>
                        <th>参数名</th>
                        <th>描述</th>
                        <th>典型值</th>
                        <th>单位</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><code>DT_ATM</code></td>
                        <td>大气时间步长</td>
                        <td>1800</td>
                        <td>秒</td>
                    </tr>
                    <tr>
                        <td><code>NSW</code></td>
                        <td>短波辐射波段数</td>
                        <td>11</td>
                        <td>-</td>
                    </tr>
                    <tr>
                        <td><code>NLW</code></td>
                        <td>长波辐射波段数</td>
                        <td>16</td>
                        <td>-</td>
                    </tr>
                </tbody>
            </table>

            <div class="note-box">
                <h4>注意</h4>
                <p>
                    大气时间步长的选择需要在计算效率和数值稳定性之间平衡。
                    典型的取值范围为10-30分钟，具体取决于分辨率和物理过程复杂性。
                </p>
            </div>

            <h3>性能优化</h3>
            <p>
                为了提高计算效率，大气驱动程序实现了以下优化策略：
            </p>
            <ul>
                <li><strong>并行计算</strong>: 使用OpenMP和MPI混合并行</li>
                <li><strong>负载均衡</strong>: 动态调整各处理器的计算任务</li>
                <li><strong>内存优化</strong>: 减少不必要的数组分配和拷贝</li>
                <li><strong>I/O优化</strong>: 批量输出诊断数据</li>
            </ul>
        </section>

        <section id="troubleshooting">
            <h2>常见问题排查</h2>

            <h4>Q: 模拟发散怎么办？</h4>
            <p>
                A: 首先检查时间步长是否过大，可以尝试减小DT_ATM。
                同时检查初始条件是否合理，特别是温度场的极值。
            </p>

            <h4>Q: 辐射计算很慢如何优化？</h4>
            <p>
                A: 可以减少辐射计算频率（例如每N个动力学步计算一次辐射），
                或者使用更简化的辐射方案进行初步测试。
            </p>
        </section>
    </main>

    <footer>
        <p>
            &copy; 2025 ModelE2.1.2_Lazenca翻译团队 |
            基于 <a href="https://www.giss.nasa.gov/tools/modelE/">NASA GISS ModelE</a>
        </p>
    </footer>

    <script src="../scripts/main.js"></script>
</body>
</html>
''',

            'markdown_document': '''# ModelE2.1.2_Lazenca 云微物理模块技术文档

## 概述

**CLOUDS2.F90** 是ModelE2.1.2_Lazenca中的云微物理过程模块，负责处理云的形成、发展、消散以及相关的降水过程。该模块采用了体积水方案，是现代气候模型中重要的物理过程参数化模块。

## 主要功能

### 1. 云水含量计算
- 计算网格平均的云水混合比
- 考虑凝结、蒸发、碰并等过程
- 区分液态水和冰相水

### 2. 云覆盖率参数化
- 基于相对湿度和云水含量计算云覆盖率
- 考虑大尺度稳定性和湍流混合的影响
- 支持部分云覆盖的情况

### 3. 降水过程
- 自动转换过程：云水向雨水的转换
- 碰并增长过程：云滴碰并增长形成降水
- 蒸发过程：降水在下落过程中的蒸发

## 数值方法

### 时间积分方案
采用显式-隐式混合的时间积分方案：
```fortran
! 云水含量的时间积分
qc_new = qc_old + dt * (condensation - autoconversion - collection)
```

### 空间离散化
使用上游差分方案确保数值稳定性：
```fortran
! 平流计算
flux_upwind = max(qc(i), qc(i-1)) * u(i)
```

## 关键参数

| 参数 | 描述 | 典型值 | 单位 |
|------|------|--------|------|
| `qc_crit` | 临界云水混合比 | 5e-4 | kg/kg |
| `k_auto` | 自动转换率系数 | 1e-3 | 1/s |
| `k_coll` | 碰并系数 | 2.0 | m³/kg |
| `evp_rate` | 蒸发率系数 | 1e-5 | 1/s |

## 算法流程

1. **初始化阶段**
   - 读取云微物理参数
   - 初始化云场变量
   - 设置诊断变量

2. **主循环**
   ```fortran
   do while (time < end_time)
     ! 计算凝结过程
     call condensation_process(qv, t, qc, qi)

     ! 计算自动转换
     call auto_conversion(qc, qr)

     ! 计算碰并过程
     call collection_process(qc, qr)

     ! 计算蒸发过程
     call evaporation_process(qr, qv, t)
   end do
   ```

3. **诊断输出**
   - 云水路径积分
   - 降水率
   - 云覆盖率统计

## 性能考虑

### 计算复杂度
- 时间复杂度: O(N³) 其中N为网格点数
- 内存需求: 约占总内存的8-12%

### 优化策略
1. **向量化优化**: 利用SIMD指令加速循环计算
2. **缓存优化**: 合理安排数组访问模式
3. **并行化**: OpenMP并行处理垂直层次

## 验证和测试

### 标准测试用例
1. **单点云滴增长测试**: 验证微物理过程的正确性
2. **理想化对流测试**: 检查云系统的发展过程
3. **气候平均态测试**: 确保长期积分的稳定性

### 对比验证
- 与观测数据对比：卫星云产品和地面观测
- 与其他模式对比：CMIP6模式间比较
- 敏感性测试：参数扰动对结果的影响

## 未来改进方向

1. **物理过程改进**
   - 引入更详细的冰相过程
   - 考虑气溶胶-云相互作用
   - 改进深对流参数化

2. **数值方法优化**
   - 采用更高精度的数值格式
   - 实现自适应时间步长
   - 优化并行计算效率

3. **诊断功能增强**
   - 增加更多云微物理诊断量
   - 改进输出格式和频率
   - 支持实时可视化

## 参考资料

1. Del Genio, A.D., et al. (1996): "A prognostic cloud water parameterization for global climate models", *Journal of Climate*, 9, 270-304.

2. Yao, M.-S., and A.D. Del Genio (1999): "Effects of cloud microphysics on the radiative properties of tropical deep convective systems", *Journal of the Atmospheric Sciences*, 56, 3766-3787.

3. Schmidt, G.A., et al. (2006): "Present day atmospheric simulations using GISS ModelE: Comparison to in-situ, satellite and reanalysis data", *Journal of Climate*, 19, 153-192.
'''
        }

        return samples

    def test_format_preservation(self) -> Dict[str, any]:
        """测试格式保持功能"""
        logger.info("开始测试格式保持功能...")
        results = {}

        # 测试固定格式Fortran
        logger.info("测试固定格式Fortran...")
        fixed_sample = self.test_samples['fortran_fixed_format']

        def mock_translate(text: str) -> str:
            """模拟翻译函数"""
            return f"[翻译] {text}" if text.strip() else text

        try:
            preserved = self.format_preserver.process_fortran_file(fixed_sample, mock_translate)

            # 验证结果
            validation_result = self.format_preserver.validate_format(preserved, fixed_sample)

            results['fortran_fixed'] = {
                'success': True,
                'validation_result': validation_result,
                'sample_lines': len(fixed_sample.split('\n')),
                'preserved_lines': len(preserved.split('\n'))
            }

            logger.info(f"固定格式测试完成: {validation_result['is_valid']}")

        except Exception as e:
            results['fortran_fixed'] = {
                'success': False,
                'error': str(e)
            }
            logger.error(f"固定格式测试失败: {e}")

        # 测试自由格式Fortran
        logger.info("测试自由格式Fortran...")
        free_sample = self.test_samples['fortran_free_format']

        try:
            preserved = self.format_preserver.process_fortran_file(free_sample, mock_translate)

            validation_result = self.format_preserver.validate_format(preserved, free_sample)

            results['fortran_free'] = {
                'success': True,
                'validation_result': validation_result,
                'sample_lines': len(free_sample.split('\n')),
                'preserved_lines': len(preserved.split('\n'))
            }

            logger.info(f"自由格式测试完成: {validation_result['is_valid']}")

        except Exception as e:
            results['fortran_free'] = {
                'success': False,
                'error': str(e)
            }
            logger.error(f"自由格式测试失败: {e}")

        return results

    def test_quality_control(self) -> Dict[str, any]:
        """测试质量控制功能"""
        logger.info("开始测试质量控制功能...")
        results = {}

        # 创建临时测试文件
        test_files = {}

        try:
            # 测试Fortran文件
            fortran_file = "test_fortran.f"
            with open(fortran_file, 'w', encoding='utf-8') as f:
                f.write(self.test_samples['fortran_fixed_format'])
            test_files['fortran'] = fortran_file

            # 测试HTML文件
            html_file = "test_html.html"
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(self.test_samples['html_document'])
            test_files['html'] = html_file

            # 测试Markdown文件
            md_file = "test_markdown.md"
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(self.test_samples['markdown_document'])
            test_files['markdown'] = md_file

            # 运行质量检查
            for file_type, file_path in test_files.items():
                logger.info(f"检查 {file_type} 文件...")
                try:
                    report = self.quality_pipeline.check_file(file_path)

                    results[file_type] = {
                        'success': True,
                        'score': report.overall_score,
                        'quality_level': report.quality_level.value,
                        'issues_count': len(report.issues),
                        'critical_issues': sum(1 for issue in report.issues if issue.severity == 'critical'),
                        'major_issues': sum(1 for issue in report.issues if issue.severity == 'major'),
                        'minor_issues': sum(1 for issue in report.issues if issue.severity == 'minor'),
                        'recommendations_count': len(report.recommendations)
                    }

                    logger.info(f"{file_type} 质量检查完成: {report.overall_score:.1f}/100")

                except Exception as e:
                    results[file_type] = {
                        'success': False,
                        'error': str(e)
                    }
                    logger.error(f"{file_type} 质量检查失败: {e}")

        except Exception as e:
            logger.error(f"质量测试文件创建失败: {e}")

        finally:
            # 清理测试文件
            for file_path in test_files.values():
                if os.path.exists(file_path):
                    os.remove(file_path)

        return results

    def test_terminology_consistency(self) -> Dict[str, any]:
        """测试术语一致性检查"""
        logger.info("开始测试术语一致性检查...")
        results = {}

        try:
            # 检查术语词典是否可用
            if hasattr(self.quality_pipeline.checkers.get('terminology'), 'terminology_dict'):
                terminology_checker = self.quality_pipeline.checkers['terminology']

                if terminology_checker.terminology_dict:
                    results['dictionary_loaded'] = {
                        'success': True,
                        'terms_count': len(terminology_checker.terminology_dict)
                    }
                    logger.info(f"术语词典加载成功: {len(terminology_checker.terminology_dict)} 个术语")

                    # 测试术语检查功能
                    test_text = """
                    这是一个测试文本，包含大气环流模型(GCM)和地球系统模型(ESM)的术语。
                    辐射传输是一个重要的物理过程。
                    云微物理过程影响降水形成。
                    """

                    issues = terminology_checker.check_terminology_consistency(test_text, "test.txt")

                    results['terminology_check'] = {
                        'success': True,
                        'issues_found': len(issues),
                        'sample_issues': [
                            {
                                'type': issue.check_type.value,
                                'severity': issue.severity,
                                'description': issue.description
                            } for issue in issues[:3]  # 只显示前3个问题
                        ]
                    }

                else:
                    results['dictionary_loaded'] = {
                        'success': False,
                        'error': "术语词典为空"
                    }
            else:
                results['dictionary_loaded'] = {
                    'success': False,
                    'error': "术语检查器未初始化"
                }

        except Exception as e:
            results['terminology_check'] = {
                'success': False,
                'error': str(e)
            }
            logger.error(f"术语一致性测试失败: {e}")

        return results

    def run_comprehensive_test(self) -> Dict[str, any]:
        """运行综合测试"""
        logger.info("开始运行综合测试...")

        test_results = {
            'timestamp': '2025-10-28',
            'test_environment': {
                'python_version': sys.version,
                'working_directory': os.getcwd()
            },
            'tests': {}
        }

        # 运行各项测试
        test_results['tests']['format_preservation'] = self.test_format_preservation()
        test_results['tests']['quality_control'] = self.test_quality_control()
        test_results['tests']['terminology_consistency'] = self.test_terminology_consistency()

        # 计算总体结果
        total_tests = 0
        successful_tests = 0

        for test_category, test_results_list in test_results['tests'].items():
            if isinstance(test_results_list, dict):
                for test_name, result in test_results_list.items():
                    total_tests += 1
                    if result.get('success', False):
                        successful_tests += 1

        test_results['summary'] = {
            'total_tests': total_tests,
            'successful_tests': successful_tests,
            'success_rate': (successful_tests / total_tests * 100) if total_tests > 0 else 0,
            'overall_status': 'PASSED' if successful_tests == total_tests else 'FAILED'
        }

        logger.info(f"综合测试完成: {successful_tests}/{total_tests} 通过 ({successful_tests/total_tests*100:.1f}%)")

        return test_results

    def generate_test_report(self, results: Dict[str, any]) -> str:
        """生成测试报告"""
        report_lines = [
            "# ModelE2.1.2_Lazenca 翻译工具链测试报告",
            f"测试时间: {results['timestamp']}",
            f"测试环境: Python {results['test_environment']['python_version'].split()[0]}",
            "",
            "## 测试概览",
            f"- 总测试数: {results['summary']['total_tests']}",
            f"- 成功测试数: {results['summary']['successful_tests']}",
            f"- 成功率: {results['summary']['success_rate']:.1f}%",
            f"- 总体状态: {results['summary']['overall_status']}",
            "",
            "## 详细测试结果"
        ]

        for test_category, test_results_list in results['tests'].items():
            report_lines.append(f"\n### {test_category.replace('_', ' ').title()}")

            if isinstance(test_results_list, dict):
                for test_name, result in test_results_list.items():
                    status = "✅ 通过" if result.get('success', False) else "❌ 失败"
                    report_lines.append(f"\n**{test_name}**: {status}")

                    if result.get('success', False):
                        # 显示成功的关键指标
                        if 'score' in result:
                            report_lines.append(f"- 质量评分: {result['score']:.1f}/100")
                        if 'terms_count' in result:
                            report_lines.append(f"- 术语数量: {result['terms_count']}")
                        if 'issues_count' in result:
                            report_lines.append(f"- 问题数量: {result['issues_count']}")
                    else:
                        # 显示错误信息
                        if 'error' in result:
                            report_lines.append(f"- 错误: {result['error']}")

        # 添加结论和建议
        report_lines.extend([
            "",
            "## 结论和建议",
            ""
        ])

        if results['summary']['overall_status'] == 'PASSED':
            report_lines.extend([
                "✅ **所有测试通过**",
                "",
                "翻译工具链已准备就绪，可以开始正式的翻译工作。建议：",
                "1. 在正式使用前，先在小规模样本上进行验证",
                "2. 建立定期的质量检查机制",
                "3. 持续更新和完善术语词典"
            ])
        else:
            failed_tests = results['summary']['total_tests'] - results['summary']['successful_tests']
            report_lines.extend([
                f"❌ **{failed_tests}个测试失败**",
                "",
                "翻译工具链需要进一步调试和完善。建议：",
                "1. 检查失败的测试项并修复相关问题",
                "2. 验证依赖项和环境配置",
                "3. 确保所有组件正常工作后再进行正式翻译"
            ])

        return "\n".join(report_lines)

def main():
    """主函数"""
    print("🚀 开始ModelE2.1.2_Lazenca翻译工具链测试...")

    # 创建测试器
    tester = TranslationToolchainTester()

    # 运行综合测试
    results = tester.run_comprehensive_test()

    # 生成报告
    report = tester.generate_test_report(results)

    # 保存报告
    report_file = os.path.join(current_dir, "test-report.md")
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"\n📊 测试完成！报告已保存到: {report_file}")
    print("\n" + "="*60)
    print(report)
    print("="*60)

if __name__ == "__main__":
    main()