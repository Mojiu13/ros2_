# SYSTEM_MAP

本文件用于记录 ROS2 + MoveIt2 + ros2_control 的系统地图。

当前阶段是：

```text
R0-M0｜环境、仓库、学习记录基线
```

本阶段目标不是深入源码，而是确认当前系统链路能跑通、能观察、能记录。

---

## 1. 总链路

### 1.1 机器人显示链路

```text
URDF / Xacro
    ↓
robot_description
    ↓
robot_state_publisher
    ↓
TF / TF_STATIC
    ↓
RViz RobotModel
```

含义：

```text
URDF / Xacro：描述机器人结构。
robot_description：ROS2 参数或 topic 中的机器人模型描述。
robot_state_publisher：根据 robot_description 和 joint_states 发布 TF。
TF / TF_STATIC：机器人各 link 之间的坐标关系。
RViz RobotModel：根据模型和 TF 显示机器人。
```

---

### 1.2 MoveIt 规划执行链路

```text
RViz MotionPlanning
    ↓
move_group
    ↓
Planning Pipeline
    ↓
RobotTrajectory / JointTrajectory
    ↓
moveit_simple_controller_manager
    ↓
/panda_arm_controller/follow_joint_trajectory
    ↓
panda_arm_controller
    ↓
joint_trajectory_controller
    ↓
fake hardware
    ↓
joint_states
    ↓
robot_state_publisher
    ↓
TF / RViz
```

本次 R0-M0 实际验证结果：

```text
RViz 中点击 Plan。
MoveIt 使用 ompl planning pipeline 生成运动规划。
RViz 中点击 Execute。
MoveIt 将轨迹发送给 panda_arm_controller。
panda_arm_controller 接收并执行 FollowJointTrajectory action goal。
最终日志显示 Goal reached, success。
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

---

## 2. MoveIt 与 ros2_control 的边界

```text
MoveIt：负责规划 trajectory。
ros2_control：负责通过 controller 执行 trajectory。
trajectory：规划层和执行层之间的接口。
```

本次实际观察到的边界是：

```text
MoveIt 侧 action client：
/moveit_simple_controller_manager

controller 侧 action server：
/panda_arm_controller

二者之间的 action：
/panda_arm_controller/follow_joint_trajectory
```

这说明：

```text
MoveIt 本身不直接“驱动关节”。
MoveIt 把规划结果变成 trajectory。
trajectory 通过 FollowJointTrajectory action 交给 controller。
controller 执行轨迹并更新 joint_states。
RViz 再根据 joint_states 和 TF 显示机器人运动。
```

---

## 3. R0-M0 当前确认对象

### 3.1 关键节点

命令：

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

节点含义：

```text
/controller_manager
ros2_control 的 controller 管理节点，负责加载、配置、激活 controller。

/move_group
MoveIt2 的核心节点，负责接收规划请求、调用规划管线、协调执行。

/moveit_simple_controller_manager
MoveIt 侧的 controller manager 插件节点/接口，用于把 trajectory 发送给实际 controller。

/panda_arm_controller
Panda 机械臂的 joint_trajectory_controller，负责接收 FollowJointTrajectory goal。

/panda_hand_controller
Panda 手爪 controller，负责夹爪动作。

/joint_state_broadcaster
负责发布 joint_states。

/robot_state_publisher
根据 robot_description 和 joint_states 发布 TF。

/rviz2
可视化界面，用于显示机器人和操作 MotionPlanning 插件。

/pandafakesystem、/pandahandfakesystem
Panda demo 中的 fake hardware。
```

---

### 3.2 关键 topic

命令：

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

topic 含义：

```text
/joint_states
机器人当前关节状态。

/dynamic_joint_states
更详细的动态关节状态。

/tf
运行时动态坐标变换。

/tf_static
静态坐标变换。

/robot_description
URDF 机器人模型。

/robot_description_semantic
SRDF / MoveIt 语义模型。

/display_planned_path
MoveIt 在 RViz 中显示规划轨迹。

/planning_scene、/monitored_planning_scene、/planning_scene_world
MoveIt 规划场景相关 topic。
```

---

### 3.3 关键 action

命令：

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

最关键 action：

```text
/panda_arm_controller/follow_joint_trajectory
```

详情命令：

```bash
ros2 action info /panda_arm_controller/follow_joint_trajectory
```

实际输出：

```text
Action: /panda_arm_controller/follow_joint_trajectory
Action clients: 1
    /moveit_simple_controller_manager
Action servers: 1
    /panda_arm_controller
```

解释：

```text
/moveit_simple_controller_manager 是 action client。
/panda_arm_controller 是 action server。
MoveIt 执行阶段通过 /panda_arm_controller/follow_joint_trajectory 把轨迹交给 controller。
```

---

### 3.4 关键 controller

命令：

```bash
ros2 control list_controllers
```

实际观察到：

```text
panda_hand_controller   position_controllers/GripperActionController           active
panda_arm_controller    joint_trajectory_controller/JointTrajectoryController  active
joint_state_broadcaster joint_state_broadcaster/JointStateBroadcaster          active
```

controller 含义：

```text
panda_arm_controller
机械臂轨迹 controller，类型是 joint_trajectory_controller/JointTrajectoryController。
它接收 FollowJointTrajectory action goal。

panda_hand_controller
手爪 controller，类型是 position_controllers/GripperActionController。
它接收 gripper_cmd action goal。

joint_state_broadcaster
关节状态广播器。
它让系统中其他节点能看到 /joint_states。
```

关键结论：

```text
三个 controller 均为 active。
因此 controller 层在 R0-M0 中验证通过。
```

---

### 3.5 关键 parameter

命令：

```bash
ros2 param get /move_group planning_pipelines
```

实际观察到：

```text
String values are: ['ompl', 'chomp', 'pilz_industrial_motion_planner', 'stomp']
```

说明：

```text
MoveIt 已加载多个 planning pipeline。
本次 RViz Plan 日志中实际使用的是 ompl。
```

---

## 4. R0-M0 形成的最小系统地图

```text
用户在 RViz 点击 Plan / Execute
        ↓
RViz MotionPlanning 插件发送请求给 move_group
        ↓
move_group 调用 planning pipeline
        ↓
ompl 生成规划路径
        ↓
MoveIt 对轨迹做时间参数化
        ↓
生成可执行 trajectory
        ↓
moveit_simple_controller_manager 选择 controller
        ↓
trajectory 发送到 /panda_arm_controller/follow_joint_trajectory
        ↓
panda_arm_controller 接收 action goal
        ↓
joint_trajectory_controller 执行轨迹
        ↓
fake hardware 更新状态
        ↓
joint_state_broadcaster 发布 /joint_states
        ↓
robot_state_publisher 发布 TF
        ↓
RViz 显示机器人运动
```

---

## 5. 当前已验证结论

```text
ROS2 Jazzy 环境可用。
MoveIt2 可用。
moveit_py 已安装。
Panda MoveIt demo 资源已安装。
ros2_control 可用。
ros2_controllers 可用。
Panda demo 可启动。
RViz 可显示机器人。
RViz MotionPlanning 插件可进行 Plan / Execute。
panda_arm_controller 可接收并执行 FollowJointTrajectory goal。
/joint_states、/tf、/tf_static、/robot_description 等关键 topic 存在。
关闭 launch 后再次 ros2 node list 无输出，说明 demo 最终退出干净。
```

---

## 6. 当前发现但不影响主链路的问题

### 6.1 RViz 缺少 rviz_visual_tools 面板插件

```text
The class required for this panel, 'rviz_visual_tools/RvizVisualToolsGui', could not be loaded.
```

判断：

```text
层级：RViz 插件层。
严重程度：低。
是否影响 Plan / Execute：不影响。
```

### 6.2 ros2 param list 管道触发 BrokenPipeError

```text
ros2 param list /move_group | head -n 40
```

出现：

```text
BrokenPipeError: [Errno 32] Broken pipe
```

判断：

```text
层级：命令行管道 / CLI 观察层。
严重程度：低。
是否影响 ROS2 / MoveIt：不影响。
```

### 6.3 joint_states echo 出现一次 message lost

```text
A message was lost!!!
```

判断：

```text
层级：ROS2 通信观察层 / CLI 观察层。
严重程度：低。
是否影响 Plan / Execute：不影响。
```

---

## 7. 后续要补的图

* [x] MoveIt plan + execute 数据流图
* [x] MoveIt → controller → hardware 执行链路图
* [ ] ROS2 node / topic / action 通信图
* [ ] URDF / TF / RViz 显示链路图
* [ ] 故障定位决策树
