# COMMAND_CHEATSHEET

本文件记录 ROS2 + MoveIt2 + ros2_control 学习过程中的常用观察命令。

原则：先观察，再判断，不要盲目改配置。

---

## 0. 环境确认

```bash
printenv ROS_DISTRO
which ros2
ros2 --help
```

```bash
lsb_release -a
uname -a
```

---

## 1. ROS2 节点观察

```bash
ros2 node list
ros2 node info /move_group
```

用途：

```text
确认系统中有哪些节点；
确认某个节点订阅、发布、提供了哪些接口。
```

---

## 2. Topic 观察

```bash
ros2 topic list
ros2 topic info /joint_states
ros2 topic echo /joint_states
```

用途：

```text
确认状态是否在发布；
确认 joint_states 是否存在；
确认 RViz / robot_state_publisher 是否有状态来源。
```

---

## 3. Service 观察

```bash
ros2 service list
ros2 service type /controller_manager/list_controllers
```

用途：

```text
确认 controller_manager 等节点是否提供管理服务。
```

---

## 4. Action 观察

```bash
ros2 action list
ros2 action info /panda_arm_controller/follow_joint_trajectory
```

用途：

```text
确认 FollowJointTrajectory action 是否存在；
确认 MoveIt 执行阶段最终发送轨迹的入口。
```

---

## 5. Parameter 观察

```bash
ros2 param list /move_group
ros2 param get /move_group moveit_controller_manager
ros2 param get /move_group planning_pipelines
```

用途：

```text
确认 MoveIt 配置是否加载；
确认 planning pipeline 和 controller manager 类型。
```

---

## 6. ros2_control 观察

```bash
ros2 control list_controllers
ros2 control list_hardware_interfaces
ros2 control list_controller_types
```

用途：

```text
确认 controller 是否 loaded / active；
确认 joint command interface 和 state interface 是否存在。
```

---

## 7. TF 观察

```bash
ros2 run tf2_tools view_frames
```

生成 `frames.pdf` 后查看 TF tree。

用途：

```text
确认 base_link、world、panda_link 等坐标关系是否存在。
```

---

## 8. R0-M0 必跑命令

```bash
printenv ROS_DISTRO
ros2 node list
ros2 topic list
ros2 action list
ros2 control list_controllers
ros2 param list /move_group
```

---

## 9. 记录格式

每次遇到问题，优先记录：

```text
现象：
命令：
输出：
初步判断：
下一步检查：
最终原因：
修复方式：
```
