# Embedded Skills｜CORE Supporting Knowledge

Must Learn Along CORE 表示这些辅助能力要在整条 CORE 路线中逐步掌握，不是 ENV-01 的一次性 prerequisite checklist，也不是“看到就跳过、以后学 DLC”。

这些能力按第一次真实服务某个 CORE module 的位置 Just-In-Time 教学：当前实践马上需要、缺少理解会导致纯复制，且存在可验证实践时，才解释、亲手使用并按 Minimum Sufficient Depth 验收。未在当前模块使用的 Embedded Skill，不得仅因为最终属于 CORE 就提前强制学习。

## Must Learn Along CORE

### Linux basic

- 路径/文件：`pwd`、`ls`、`cd`、`mkdir`、`cp`、`mv`、`rm`。
- 阅读/检索：`cat`、`less`、`head`、`tail`、`grep`、`find`。
- 环境/命令：`env`、`export`、`which`、`echo`。
- 进程：`ps`、`pgrep`、`kill`。
- 权限/安装：`ls -l`、`chmod`、`chown`、`apt`。

ENV-01 只学习搭建环境当下真实使用的路径、环境、权限和安装命令；`cat/grep/find` 也只在当前任务实际需要时加入。`less/head/tail` 与 `ps/pgrep/kill` 留在本清单中，分别在首次查看较长日志、观察或终止真实进程的 CORE 模块教学。首次出现必须解释命令的观察目标与风险。

### Git basic

CORE 内逐步掌握 `status`、`diff`、`add`、`commit`、`log`、`branch`、`switch`、`restore`、`.gitignore`。ENV-01 只要求当前提交闭环所需的 status/diff/add/commit/.gitignore；log、branch/switch、restore 等在真实查看历史、使用分支或恢复文件时再教学。每个完成的 CORE 模块仍应形成一次范围合理、信息可解释的 commit；提交前检查 diff，不提交伪造证据或构建产物。

### CMake / ament basic

随 ROS-02 和后续包修改理解：

- `package.xml` 与 `CMakeLists.txt` 的职责；
- `find_package`、`add_executable` 与依赖声明；
- `ament_target_dependencies`；
- ROS-02：executable 的 install rule；
- ROS-02：`rosidl` interface generation；
- ROS-02：build → source overlay → run/inspect 的关系；
- ROS-03：首次创建 launch/config 时再学习 directory install rules。

只解释当前实际变化，但不得只让学习者复制模板。

### YAML、CLI / log inspection、basic debugging method

ROS-03 首次系统掌握 YAML 的配置角色、缩进/类型/作用域和生效验证。CLI/log inspection 与 basic debugging method 同样按首次真实使用的位置教学；每个模块只使用当前问题需要的 graph、TF、controller state 或运行输出作为证据，并逐步形成 baseline → symptom → observation → layer → hypothesis → verification → root cause → fix → regression。

## DLC

- advanced Linux：复杂 shell、systemd、网络管理、系统调优；
- advanced Git：rebase、cherry-pick、bisect、reflog、submodule、复杂分支策略；
- advanced CMake：大型工程抽象、toolchain、复杂导出/安装；
- networking internals、DDS/RTPS 内部；
- performance profiling 与复杂竞态工具。

上述进入 `DLC-TOOLS`、`DLC-ROS-NETWORK`、`DLC-ROS-MIDDLEWARE` 或 `DLC-DEBUG`。但若某个基础点是当前 CORE 的 Required Supporting Knowledge，DLC LOCK 不得阻止讲解。
