# Creating a rundeck / 创建运行配置

**Creating a rundeck**
**创建运行配置**

Each modelE run is completely described by a configuration file which we call a "rundeck".
每个ModelE运行都由一个配置文件完全描述，我们称之为"运行配置"（rundeck）。

A rundeck can be created by copying an existing rundeck to a file with a different name and then modifying it. One can also create a typical rundeck for a particular configuration from one of the provided templates (files modelE/templates/*.R). To create a rundeck from a template just execute:
可以通过复制现有运行配置到一个不同名称的文件然后修改它来创建新的运行配置。也可以从提供的模板之一（文件modelE/templates/*.R）为特定配置创建典型的运行配置。要从模板创建运行配置，只需执行：

```bash
    make rundeck RUN=<RunID> RUNSRC=<Template>
```

where `<RunID>` is the name of the new rundeck and `<Template>` is the name of a template (both without `.R`).
其中`<RunID>`是新运行配置的名称，`<Template>`是模板的名称（两者都不包括`.R`）。

When rundeck is created a copy of it is saved for permanent storage in "decks repository" under ModelE_Support. This is done so that one could always find the rundeck used for a particular production simulation even long time after this simulation was done. As a result the system will not allow you to create a rundeck with the name which is already present in the repository. If you don't need this stored rundeck and want to overwrite it with a new one just specify OVERWRITE=YES on command line, i.e.
当创建运行配置时，它的副本会保存在ModelE_Support下的"decks repository"中进行永久存储。这样做是为了即使在模拟完成很久之后，也能够始终找到用于特定生产模拟的运行配置。因此，系统不允许您创建与存储库中已有名称相同的运行配置。如果您不需要这个存储的运行配置并想用新的覆盖它，只需在命令行上指定OVERWRITE=YES，即：

```bash
    make rundeck RUN=<RunID> RUNSRC=<Template> OVERWRITE=YES
```

See next chapter for a detailed description of modelE rundeck.
请参阅下一章了解ModelE运行配置的详细描述。

---

## Rundeck Creation Guide / 运行配置创建指南

### What is a Rundeck? / 什么是运行配置？

**Definition / 定义**:
- Rundeck（运行配置）是描述ModelE运行的完整配置文件
- 包含所有模型参数、物理选项、输出设置等
- 是模型运行的基础和核心控制文件

**Purpose / 用途**:
- 确保模型运行的可重现性
- 保存实验配置的完整记录
- 便于不同实验之间的比较和管理

### Creating Methods / 创建方法

#### Method 1: Copy Existing Rundeck / 方法1：复制现有运行配置
```bash
# 复制现有运行配置
cp existing_rundeck.R new_rundeck.R
# 然后编辑 new_rundeck.R
```

#### Method 2: Use Template / 方法2：使用模板
```bash
# 从模板创建新的运行配置
make rundeck RUN=<RunID> RUNSRC=<Template>
```

### Command Parameters / 命令参数说明

**Required Parameters / 必需参数**:
- `RUN=<RunID>`: 新运行配置的名称
- `RUNSRC=<Template>`: 模板名称（不包含.R扩展名）

**Optional Parameters / 可选参数**:
- `OVERWRITE=YES`: 覆盖同名现有运行配置

### Template Location / 模板位置

**Template Directory / 模板目录**:
- 路径：`modelE/templates/*.R`
- 包含各种预定义的配置模板
- 适用于不同类型的模拟实验

### Repository Management / 存储库管理

**Decks Repository / 运行配置存储库**:
- 位置：`ModelE_Support/decks/`
- 自动保存每个创建的运行配置副本
- 提供永久存储和版本追踪

**Name Conflict Handling / 名称冲突处理**:
- 默认不允许创建同名运行配置
- 使用`OVERWRITE=YES`参数覆盖现有配置
- 确保每个运行配置的唯一性

### Best Practices / 最佳实践

**Naming Conventions / 命名约定**:
- 使用描述性名称反映实验内容
- 包含日期、版本号或其他标识信息
- 避免使用特殊字符和空格

**Example Names / 示例名称**:
- `control_run_2025`
- `sensitivity_test_co2`
- `historical_simulation_v2`

**Version Control / 版本控制**:
- 为重要实验创建多个版本
- 保留原始模板作为备份
- 记录每次修改的内容和原因

### Usage Examples / 使用示例

**Basic Creation / 基本创建**:
```bash
# 从默认模板创建
make rundeck RUN=my_experiment RUNSRC=template_name
```

**Overwrite Existing / 覆盖现有**:
```bash
# 覆盖同名运行配置
make rundeck RUN=my_experiment RUNSRC=template_name OVERWRITE=YES
```

### Next Steps / 后续步骤

1. **Edit the rundeck / 编辑运行配置**: 根据实验需求修改参数
2. **Validate configuration / 验证配置**: 检查参数设置的正确性
3. **Test run / 测试运行**: 进行短期测试运行
4. **Production run / 生产运行**: 开始正式模拟实验

### Troubleshooting / 故障排除

**Common Issues / 常见问题**:
1. **Template not found / 找不到模板**: 检查模板名称和路径
2. **Permission denied / 权限被拒绝**: 确保对目录有写权限
3. **Name already exists / 名称已存在**: 使用OVERWRITE=YES或选择新名称

**Verification Steps / 验证步骤**:
- 检查运行配置文件是否创建成功
- 验证文件格式和内容完整性
- 确认参数设置符合预期

---

**Note / 注意**:
- 运行配置文件是ModelE的核心控制文件，创建后请仔细检查所有参数设置
- 建议在修改前备份原始模板文件
- 详细的运行配置参数说明请参阅下一章节