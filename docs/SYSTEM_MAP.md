# SYSTEM_MAP

本文件用于记录 ROS2 + MoveIt2 + ros2_control 的系统地图。

当前阶段先写粗图，后续每个模块逐步补细。

---

## 1. 总链路

```text
Robot Model
URDF / Xacro
    ↓
robot_description
    ↓
robot_state_publisher
    ↓
TF
    ↓
RViz / MoveIt
```

```text
Python / C++ Task Node
    ↓
MoveItPy / MoveGroupInterface
    ↓
move_group
    ↓
Planning Pipeline
    ↓
RobotTrajectory / JointTrajectory
    ↓
FollowJointTrajectory Action
    ↓
joint_trajectory_controller
    ↓
command interface
    ↓
robot / fake hardware
    ↓
state interface
    ↓
joint_states
    ↓
robot_state_publisher
    ↓
TF / RViz
```

---

## 2. MoveIt 与 ros2_control 的边界

```text
MoveIt：负责规划 trajectory。
ros2_control：负责通过 controller 执行 trajectory。
trajectory：规划层和执行层之间的接口。
```

---

## 3. R0-M0 当前需要确认的对象

### 关键节点

```text
/move_group
/robot_state_publisher
/rviz2
/controller_manager
```

实际结果待填写。

### 关键 topic

```text
/joint_states
/tf
/tf_static
```

实际结果待填写。

### 关键 action

```text
/panda_arm_controller/follow_joint_trajectory
```

实际结果待填写。

### 关键 controller

```text
joint_state_broadcaster
panda_arm_controller
panda_hand_controller
```

实际结果待填写。

---

## 4. 后续要补的图

- [ ] ROS2 node / topic / action 通信图
- [ ] URDF / TF / RViz 显示链路图
- [ ] MoveIt plan + execute 数据流图
- [ ] MoveIt → controller → hardware 执行链路图
- [ ] 故障定位决策树
