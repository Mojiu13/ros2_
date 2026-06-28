# ROS2 + MoveIt2 + ros2_control 学习仓库

这是一个面向机械臂软件工程方向的 ROS2 + MoveIt2 + ros2_control 学习仓库。

当前主线不是百科式学习，而是工程训练：

```text
运行 → 观察 → 修改 → 破坏 → 修复 → 总结 → 复述
```

## 当前学习路线

```text
R0-M0  环境、仓库、学习记录基线

R1-M1  ROS2 最小通信与命令行观察
R1-M2  URDF / Xacro / TF 最小机器人模型
R1-M3  ros2_control 最小执行链路
R1-M4  MoveIt2 RViz 规划执行流程
R1-M5  MoveItPy Python 代码闭环
R1-M6  全链路串联与最小故障定位
R1-M7  第一遍整合小项目

R2-M1  ROS2 工程组织：package / launch / parameter / YAML
R2-M2  机器人模型工程：URDF / Xacro / SRDF / TF / MoveIt config
R2-M3  ros2_control 配置深化：controller / interface / lifecycle
R2-M4  MoveIt 架构深化：RobotModel / RobotState / PlanningScene
R2-M5  MoveIt Planning Pipeline 与 trajectory 生成
R2-M6  MoveIt Execution 与 controller 对接
R2-M7  ROS2 Action 与 C++ 工程基础
R2-M8  joint_trajectory_controller 源码主线
R2-M9  自定义 controller 与 mock hardware，可选进阶
```

## 当前阶段

当前从 `R0-M0` 开始：环境、仓库、学习记录基线。

本阶段不追求写复杂代码，只确认：

- ROS2 Jazzy 环境是否可用
- MoveIt2 是否可用
- ros2_control 是否可用
- Panda MoveIt demo 是否能启动
- RViz 是否能显示机器人
- Plan / Execute 是否成功
- 关键节点、topic、action、controller、parameter 能否被观察

## 推荐仓库结构

```text
ros2_/
├── README.md
├── LEARNING_STATUS.md
├── docs/
│   ├── COMMAND_CHEATSHEET.md
│   ├── ERROR_LOG.md
│   ├── SYSTEM_MAP.md
│   └── INTERVIEW_QA.md
├── prompts/
│   └── R0-M0.md
├── scripts/
│   └── collect_r0_m0_baseline.sh
├── round1_fast_flow/
├── round2_work_depth/
└── mini_projects/
```

## R0-M0 验收命令

```bash
ros2 node list
ros2 topic list
ros2 action list
ros2 control list_controllers
ros2 param list /move_group
```

## 学习原则

不要只看教程。每个模块必须留下：

1. 可运行结果
2. 观察命令
3. 系统链路图
4. 故障记录
5. README 总结
6. 面试问答

## 后续对话使用方式

在新的 ChatGPT 对话框里，可以直接说：

```text
我正在学习 Mojiu13/ros2_ 仓库中的 R0-M0 模块。请读取仓库 README、LEARNING_STATUS、docs/COMMAND_CHEATSHEET.md、docs/ERROR_LOG.md 和 prompts/R0-M0.md，然后带我完成本模块。
```
