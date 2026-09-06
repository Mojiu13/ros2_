# Embedded Skills｜CORE Supporting Knowledge

这些能力不单独扩张为长期课程，但也不是“看到就跳过、以后学 DLC”。它们在首次服务于当前 CORE 时，必须解释、亲手使用并按 Minimum Sufficient Depth 验收。

## Must Learn Along CORE

### Linux basic

- 路径/文件：`pwd`、`ls`、`cd`、`mkdir`、`cp`、`mv`、`rm`。
- 阅读/检索：`cat`、`less`、`head`、`tail`、`grep`、`find`。
- 环境/命令：`env`、`export`、`which`、`echo`。
- 进程：`ps`、`pgrep`、`kill`。
- 权限/安装：`ls -l`、`chmod`、`chown`、`apt`。

ENV-01 负责文件、环境、权限和安装的起点；ROS-01/DBG-01 继续用进程、日志和证据排错。首次出现必须解释命令的观察目标与风险。

### Git basic

CORE 内自然使用 `status`、`diff`、`add`、`commit`、`log`、`branch`、`switch`、`restore`、`.gitignore`。每个完成的 CORE 模块应形成一次范围合理、信息可解释的 commit；提交前检查 diff，不提交伪造证据或构建产物。

### CMake / ament basic

随 ROS-02 和后续包修改理解：

- `package.xml` 与 `CMakeLists.txt` 的职责；
- `find_package`、`add_executable` 与依赖声明；
- `ament_target_dependencies`；
- executable、launch、config 的 install rules；
- `rosidl` interface generation；
- build → source overlay → run/inspect 的关系。

只解释当前实际变化，但不得只让学习者复制模板。

### YAML、CLI / log inspection、basic debugging method

ROS-03 首次系统掌握 YAML 的配置角色、缩进/类型/作用域和生效验证。所有模块都使用 CLI、log、graph、TF、controller state 或运行输出作为证据，并采用 baseline → symptom → observation → layer → hypothesis → verification → root cause → fix → regression。

## DLC

- advanced Linux：复杂 shell、systemd、网络管理、系统调优；
- advanced Git：rebase、cherry-pick、bisect、reflog、submodule、复杂分支策略；
- advanced CMake：大型工程抽象、toolchain、复杂导出/安装；
- networking internals、DDS/RTPS 内部；
- performance profiling 与复杂竞态工具。

上述进入 `DLC-TOOLS`、`DLC-ROS-NETWORK`、`DLC-ROS-MIDDLEWARE` 或 `DLC-DEBUG`。但若某个基础点是当前 CORE 的 Required Supporting Knowledge，DLC LOCK 不得阻止讲解。
