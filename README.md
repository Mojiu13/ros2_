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

MP-A   MoveItPy TaskNode 任务节点项目
MP-B   arm + gripper 顺序执行项目
MP-C   故障注入与自动恢复项目
MP-D   自定义 controller 项目，可选

JOB-M1 README / 架构图 / 调试文档
JOB-M2 简历项目描述
JOB-M3 面试问答库
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
│   ├── PROMPT_INDEX.md
│   ├── ALL_MODULE_PROMPTS.md
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

## 后续对话通用调用方式

在新的 ChatGPT 对话框里，可以直接说：

```text
请连接并读取我的 GitHub 仓库：Mojiu13/ros2_

请优先读取以下文件：
1. README.md
2. LEARNING_STATUS.md
3. docs/COMMAND_CHEATSHEET.md
4. docs/ERROR_LOG.md
5. docs/SYSTEM_MAP.md
6. prompts/PROMPT_INDEX.md
7. prompts/ALL_MODULE_PROMPTS.md

我要学习的模块是：<MODULE_ID>

请在 prompts/ALL_MODULE_PROMPTS.md 中找到该模块对应的提示词，并严格按该模块提示词带我学习。

要求：
- 把我当作真正的新手；
- 不要百科式堆知识点；
- 先跑最小例子，再观察，再修改，再故障注入，再总结；
- 每次只给我少量命令，等我贴输出后再判断；
- 如果报错，先判断错误属于哪一层；
- 每完成一个阶段，告诉我应该更新仓库里的哪个文件；
- 本模块结束时，帮我生成可提交到 GitHub 的总结文档。

现在请从该模块的第一步开始带我做。
```

把 `<MODULE_ID>` 换成：`R0-M0`、`R1-M1`、`R2-M6`、`MP-A`、`JOB-M3` 等即可。
