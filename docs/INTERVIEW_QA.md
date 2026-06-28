# INTERVIEW_QA

本文件用于积累 ROS2 + MoveIt2 + ros2_control 面试问答。

原则：每个模块结束后，至少新增 3～5 个问题。

---

## R0-M0｜环境、仓库、学习记录基线

### Q1：当前 ROS2 版本如何确认？

```bash
printenv ROS_DISTRO
```

回答模板：

```text
可以通过环境变量 ROS_DISTRO 确认当前 source 的 ROS2 发行版。
如果输出是 jazzy，说明当前 shell 已经 source 到 ROS2 Jazzy 环境。
```

---

### Q2：为什么要先确认 Panda MoveIt demo 能启动？

回答模板：

```text
因为 Panda MoveIt demo 是一条现成的完整链路，包含机器人模型、MoveIt 配置、move_group、ros2_control controller、RViz 可视化和规划执行流程。
如果 demo 能跑通，说明基础环境、MoveIt、controller 和 RViz 大体可用。
```

---

### Q3：R0-M0 为什么不急着写代码？

回答模板：

```text
因为本阶段的目标是建立可复现环境和观察基线。
如果连节点、topic、action、controller、parameter 都不能稳定观察，过早写代码只会把问题混在一起。
```

---

### Q4：MoveIt 和 ros2_control 的基本边界是什么？

回答模板：

```text
MoveIt 主要负责规划轨迹，ros2_control 通过 controller 执行轨迹。
二者之间常见接口是 FollowJointTrajectory Action。
```

---

### Q5：如果 Plan 成功但 Execute 失败，可能是哪几层问题？

回答模板：

```text
Plan 成功说明规划层至少生成了轨迹。
Execute 失败可能发生在 MoveIt execution 配置、controller action namespace、controller active 状态、joint name 匹配、trajectory tolerance 或底层 hardware interface。
```

---

## 待补充模块

- [ ] R1-M1｜ROS2 最小通信与命令行观察
- [ ] R1-M2｜URDF / Xacro / TF 最小机器人模型
- [ ] R1-M3｜ros2_control 最小执行链路
- [ ] R1-M4｜MoveIt2 RViz 规划执行流程
- [ ] R1-M5｜MoveItPy Python 代码闭环
- [ ] R1-M6｜全链路串联与最小故障定位
- [ ] R1-M7｜第一遍整合小项目
