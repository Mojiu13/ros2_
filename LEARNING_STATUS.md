# LEARNING_STATUS

## 当前模块

```text
R0-M0｜环境、仓库、学习记录基线
```

## 当前目标

确认当前 ROS2 + MoveIt2 + ros2_control 环境可复现、可观察、可记录，并整理 GitHub 仓库结构。

## 环境信息

| 项目                | 当前记录                                                                                              | 验证命令                           |
| ----------------- | ------------------------------------------------------------------------------------------------- | ------------------------------ |
| OS                | Ubuntu 24.04.1 LTS noble                                                                          | `lsb_release -a`               |
| ROS2 版本           | jazzy                                                                                             | `printenv ROS_DISTRO`          |
| ROS2 命令路径         | `/opt/ros/jazzy/bin/ros2`                                                                         | `which ros2`                   |
| MoveIt2 是否可用      | 可用，已发现 `moveit_py`、`moveit_ros_move_group`、`moveit_resources_panda_moveit_config` 等包              | `ros2 pkg list \| grep moveit` |
| ros2_control 是否可用 | 可用，`ros2 control` CLI 正常，`controller_manager`、`joint_trajectory_controller`、`ros2_controllers` 存在 | `ros2 control --help`          |
| 工作空间              | `/root/ros_ws`                                                                                    | `pwd`                          |
| GitHub 仓库         | `Mojiu13/ros2_`                                                                                   | `git remote -v`                |

## R0-M0 验收清单

* [x] 能 source ROS2 环境
* [x] 能启动 Panda MoveIt demo
* [x] RViz 能显示 Panda 机器人
* [x] RViz MotionPlanning 插件可用
* [x] Plan 成功
* [x] Execute 成功
* [x] 能列出 ROS2 节点
* [x] 能列出 ROS2 topic
* [x] 能列出 ROS2 action
* [x] 能列出 ros2_control controller
* [x] 能查看 `/move_group` 参数
* [x] 能找到 FollowJointTrajectory action
* [x] 能把观察结果写入文档

## 关键观察结果

### ROS2 Nodes

```bash
ros2 node list
```

实际观察到的关键节点：

```text
/controller_manager
/joint_state_broadcaster
/move_group
/move_group/moveit
/moveit_simple_controller_manager
/panda_arm_controller
/panda_hand_controller
/pandafakesystem
/pandahandfakesystem
/robot_state_publisher
/rviz2
/static_transform_publisher
```

说明：

```text
/controller_manager：ros2_control 的 controller 管理节点。
/move_group：MoveIt2 的核心规划与执行协调节点。
/robot_state_publisher：根据 robot_description 和 joint_states 发布 TF。
/rviz2：可视化界面。
/panda_arm_controller：机械臂轨迹 controller。
/panda_hand_controller：夹爪 controller。
```

### ROS2 Topics

```bash
ros2 topic list | grep -E "joint_states|tf|planning_scene|display_planned_path|robot_description"
```

实际观察到：

```text
/display_planned_path
/dynamic_joint_states
/joint_states
/monitored_planning_scene
/planning_scene
/planning_scene_world
/robot_description
/robot_description_semantic
/tf
/tf_static
```

说明：

```text
/joint_states：机器人关节状态。
/tf 和 /tf_static：机器人坐标变换。
/robot_description：URDF 机器人模型。
/robot_description_semantic：SRDF / MoveIt 语义模型。
/display_planned_path：MoveIt 在 RViz 中显示规划轨迹。
/planning_scene 相关 topic：MoveIt 规划场景。
```

### ROS2 Actions

```bash
ros2 action list | grep -E "trajectory|gripper|move"
```

实际观察到：

```text
/execute_trajectory
/move_action
/panda_arm_controller/follow_joint_trajectory
/panda_hand_controller/gripper_cmd
/sequence_move_group
```

关键 action 详情：

```bash
ros2 action info /panda_arm_controller/follow_joint_trajectory
```

输出：

```text
Action: /panda_arm_controller/follow_joint_trajectory
Action clients: 1
    /moveit_simple_controller_manager
Action servers: 1
    /panda_arm_controller
```

说明：

```text
MoveIt 侧的 /moveit_simple_controller_manager 是 action client。
controller 侧的 /panda_arm_controller 是 action server。
二者通过 /panda_arm_controller/follow_joint_trajectory 对接。
这是 MoveIt 执行机械臂轨迹的关键入口。
```

### Controllers

```bash
ros2 control list_controllers
```

实际观察到：

```text
panda_hand_controller   position_controllers/GripperActionController           active
panda_arm_controller    joint_trajectory_controller/JointTrajectoryController  active
joint_state_broadcaster joint_state_broadcaster/JointStateBroadcaster          active
```

说明：

```text
panda_arm_controller 已 active，可以接收 FollowJointTrajectory 轨迹目标。
panda_hand_controller 已 active，可以接收夹爪控制目标。
joint_state_broadcaster 已 active，可以发布关节状态。
```

### move_group Parameters

```bash
ros2 param get /move_group planning_pipelines
```

实际观察到：

```text
String values are: ['ompl', 'chomp', 'pilz_industrial_motion_planner', 'stomp']
```

说明：

```text
MoveIt2 的 planning pipeline 参数已经加载。
本次 RViz Plan 使用的是 ompl pipeline。
```

## Panda MoveIt Demo 验证结果

启动命令：

```bash
ros2 launch moveit_resources_panda_moveit_config demo.launch.py
```

RViz Plan / Execute 结果：

```text
Plan 成功。
Execute 成功。
RViz 中 Panda 机械臂完成运动。
```

关键日志：

```text
Motion plan was computed successfully.
sending trajectory to panda_arm_controller
[panda_arm_controller]: Received new action goal
[panda_arm_controller]: Accepted new action goal
[panda_arm_controller]: Goal reached, success!
Completed trajectory execution with status SUCCEEDED
Execute request success!
```

对应链路：

```text
RViz MotionPlanning
→ move_group
→ OMPL planning pipeline
→ trajectory
→ moveit_simple_controller_manager
→ /panda_arm_controller/follow_joint_trajectory
→ panda_arm_controller
→ joint_trajectory_controller
→ fake hardware
→ joint_states
→ robot_state_publisher
→ TF / RViz
```

## 关闭验证

关闭方式：

```text
推荐在启动 demo 的 launch 终端中按 Ctrl+C。
```

验证命令：

```bash
ros2 node list
```

结果：

```text
再次执行 ros2 node list 后无节点输出，说明 Panda demo 已干净退出。
```

## 当前发现的问题

### 1. RViz 缺少 rviz_visual_tools 面板插件

现象：

```text
The class required for this panel, 'rviz_visual_tools/RvizVisualToolsGui', could not be loaded.
```

判断：

```text
层级：RViz 插件层。
严重程度：低。
是否影响 R0-M0 主链路：不影响。
Plan / Execute 是否受影响：不受影响。
```

### 2. `ros2 param list /move_group | head -n 40` 出现 BrokenPipeError

现象：

```text
BrokenPipeError: [Errno 32] Broken pipe
```

判断：

```text
层级：命令行管道 / CLI 观察层。
严重程度：低。
原因：head 提前关闭管道，ros2 param list 继续输出时触发 BrokenPipeError。
是否影响 ROS2 / MoveIt：不影响。
```

### 3. `ros2 topic echo /joint_states --once` 出现一次 message lost

现象：

```text
A message was lost!!!
```

判断：

```text
层级：ROS2 通信观察层 / CLI 观察层。
严重程度：低。
是否影响 demo：不影响。
是否影响 Plan / Execute：不影响。
```

## 当前结论

```text
当前 ROS2 Jazzy 环境可用。
MoveIt2 已安装并可运行。
ros2_control 与 ros2_controllers 已安装并可运行。
Panda MoveIt demo 可以启动。
RViz 可以显示 Panda 机器人。
RViz MotionPlanning 可以完成 Plan / Execute。
panda_arm_controller、panda_hand_controller、joint_state_broadcaster 均为 active。
MoveIt 与 controller 通过 /panda_arm_controller/follow_joint_trajectory action 对接。
当前发现的问题均为低严重度观察问题，不影响 R0-M0 主链路。
```

## 下一模块

完成本文件后进入：

```text
R1-M1｜ROS2 最小通信与命令行观察
```
