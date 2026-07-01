# ERROR_LOG

本文件记录 ROS2 + MoveIt2 + ros2_control 学习过程中的错误。

不要只记录“怎么修好”，要记录“为什么会坏”。

---

## 错误记录模板

```text
## 编号：ERR-YYYYMMDD-001

模块：
日期：
环境：

### 现象

### 触发命令

### 关键日志

### 初步层级判断

### 实际原因

### 定位过程

### 修复方法

### 本质理解

### 以后如何避免
```

---

# R0-M0 错误记录

## ERR-20260701-001｜RViz 缺少 rviz_visual_tools 面板插件

模块：R0-M0｜环境、仓库、学习记录基线
日期：2026-07-01
环境：Ubuntu 24.04.1 LTS noble / ROS2 Jazzy / Docker 容器 / Panda MoveIt demo

### 现象

启动 Panda MoveIt demo 后，RViz GUI 中出现面板插件加载错误。

### 触发命令

```bash
ros2 launch moveit_resources_panda_moveit_config demo.launch.py
```

### 关键日志

```text
The class required for this panel, 'rviz_visual_tools/RvizVisualToolsGui', could not be loaded.

PluginlibFactory: The plugin for class 'rviz_visual_tools/RvizVisualToolsGui' failed to load.
Error: According to the loaded plugin descriptions the class rviz_visual_tools/RvizVisualToolsGui with base class type rviz_common::Panel does not exist.
```

### 初步层级判断

```text
RViz 层 / RViz 插件层
```

不是：

```text
MoveIt 核心层
ros2_control 层
controller 层
URDF / TF 层
```

### 实际原因

当前环境缺少 RViz 配置文件中引用的 `rviz_visual_tools/RvizVisualToolsGui` panel 插件，或者该插件在当前 ROS2 Jazzy 环境中的类名 / 插件描述未正确提供。

### 定位过程

1. Panda demo 可以继续启动。
2. RViz 可以显示 Panda 机器人。
3. MotionPlanning 插件可以连接 `panda_arm` planning group。
4. RViz 中 Plan 成功。
5. RViz 中 Execute 成功。
6. 终端日志显示轨迹成功发送到 `panda_arm_controller` 并执行完成。

关键成功日志：

```text
Motion plan was computed successfully.
sending trajectory to panda_arm_controller
[panda_arm_controller]: Received new action goal
[panda_arm_controller]: Accepted new action goal
[panda_arm_controller]: Goal reached, success!
Completed trajectory execution with status SUCCEEDED
Execute request success!
```

因此该错误不影响 R0-M0 的主链路。

### 修复方法

R0-M0 阶段暂不修复，只记录。

后续如果需要修复，可以检查是否安装 RViz visual tools 相关包，例如：

```bash
ros2 pkg list | grep rviz_visual_tools
```

如果缺失，再考虑安装对应 ROS2 Jazzy 包。

### 本质理解

RViz 是可视化层。
RViz 中某个 panel 插件加载失败，不等于 MoveIt 规划失败，也不等于 controller 执行失败。

判断错误时要先分层：

```text
RViz 插件错误
≠ MoveIt 核心错误
≠ ros2_control 错误
≠ controller 执行错误
```

### 以后如何避免

不要看到 RViz 报错就立刻重装环境。
先检查主链路是否正常：

```bash
ros2 node list
ros2 action list
ros2 control list_controllers
```

再用 RViz 做 Plan / Execute 验证是否真正影响功能。

---

## ERR-20260701-002｜ros2 param list 管道触发 BrokenPipeError

模块：R0-M0｜环境、仓库、学习记录基线
日期：2026-07-01
环境：Ubuntu 24.04.1 LTS noble / ROS2 Jazzy / Docker 容器 / Panda MoveIt demo

### 现象

查看 `/move_group` 参数时，命令输出前 40 行后出现 Python `BrokenPipeError`。

### 触发命令

```bash
ros2 param list /move_group | head -n 40
```

### 关键日志

```text
BrokenPipeError: [Errno 32] Broken pipe
Exception ignored in: <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>
BrokenPipeError: [Errno 32] Broken pipe
```

### 初步层级判断

```text
命令行管道层 / CLI 观察层
```

如果必须归入固定分层，最接近：

```text
环境层
```

但它不是 ROS2 环境损坏。

### 实际原因

`head -n 40` 读取前 40 行后会提前关闭管道。
上游的 `ros2 param list /move_group` 仍试图继续向 stdout 写入内容，于是 Python 进程遇到已经关闭的管道，触发 `BrokenPipeError`。

### 定位过程

1. `/move_group` 参数可以正常读取。
2. `ros2 param get /move_group planning_pipelines` 成功返回：

```text
String values are: ['ompl', 'chomp', 'pilz_industrial_motion_planner', 'stomp']
```

3. Panda demo 的 Plan / Execute 均成功。
4. 因此该问题只出现在 CLI 输出管道，不是 MoveIt 参数损坏。

### 修复方法

R0-M0 阶段不需要修复。

如果想避免该现象，可以不用 `head` 截断：

```bash
ros2 param list /move_group
```

或者直接用 `grep` 过滤目标参数：

```bash
ros2 param list /move_group | grep planning
```

也可以直接读取具体参数：

```bash
ros2 param get /move_group planning_pipelines
```

### 本质理解

这是 Linux 管道和 Python stdout 的交互问题，不是 ROS2 通信问题。

```text
head 提前退出
→ 管道关闭
→ 上游 ros2 命令继续写 stdout
→ BrokenPipeError
```

### 以后如何避免

查看大量 ROS2 参数时，优先使用：

```bash
ros2 param get /node_name parameter_name
```

而不是先完整 list 再用 `head` 截断。

---

## ERR-20260701-003｜joint_states echo 出现一次 message lost

模块：R0-M0｜环境、仓库、学习记录基线
日期：2026-07-01
环境：Ubuntu 24.04.1 LTS noble / ROS2 Jazzy / Docker 容器 / Panda MoveIt demo

### 现象

使用 `ros2 topic echo /joint_states --once` 查看一次关节状态时，终端提示丢失一条消息。

### 触发命令

```bash
ros2 topic echo /joint_states --once
```

### 关键日志

```text
A message was lost!!!
        total count change:1
        total count: 1
```

随后仍然成功读取到了 `/joint_states`：

```text
name:
- panda_finger_joint1
- panda_finger_joint2
- panda_joint1
- panda_joint2
- panda_joint3
- panda_joint4
- panda_joint5
- panda_joint6
- panda_joint7
```

### 初步层级判断

```text
ROS2 通信观察层 / CLI 观察层
```

不是：

```text
MoveIt 层
controller 层
ros2_control 层
URDF / TF 层
```

### 实际原因

`ros2 topic echo --once` 是临时启动一个订阅器，只接收一次消息后退出。
订阅器刚建立连接时，可能因为 QoS、缓冲、发布频率或启动瞬间时序，出现一次 message lost 提示。

但随后命令成功接收到了完整的 `/joint_states` 消息，因此这不是主链路故障。

### 定位过程

1. `/joint_states` topic 存在。
2. 输出中包含 Panda 手爪关节和 7 个机械臂关节。
3. controller 均为 active。
4. RViz Plan / Execute 成功。
5. 因此该提示不影响 demo。

### 修复方法

R0-M0 阶段不需要修复。

如果后续想更稳定观察，可以不加 `--once`：

```bash
ros2 topic echo /joint_states
```

或者只看 topic 信息：

```bash
ros2 topic info /joint_states
```

### 本质理解

一次 CLI 观察丢消息，不等于系统状态发布失败。
真正关键的是：

```text
/joint_states 是否存在
是否能持续发布
是否包含正确 joint name
robot_state_publisher 是否能用它发布 TF
RViz 是否能显示机器人运动
```

### 以后如何避免

遇到 message lost，不要立刻判断系统坏了。
先执行：

```bash
ros2 topic list | grep joint_states
ros2 topic info /joint_states
ros2 topic echo /joint_states
```

看是否持续有消息。

---

# R0-M0 错误总结

本模块发现的 3 个问题均不影响主链路：

```text
ERR-20260701-001：RViz visual tools 面板插件缺失，属于 RViz 插件层。
ERR-20260701-002：BrokenPipeError，属于命令行管道 / CLI 观察层。
ERR-20260701-003：message lost，属于 ROS2 通信观察层 / CLI 观察层。
```

R0-M0 主链路结论：

```text
ROS2 Jazzy 可用。
MoveIt2 可用。
ros2_control 可用。
Panda demo 可启动。
RViz 可显示机器人。
Plan 成功。
Execute 成功。
FollowJointTrajectory action 可用。
controller 均 active。
```
