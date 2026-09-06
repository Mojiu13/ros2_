# DLC INDEX

进入方式：明确说“我要学习 DLC：<DLC_ID>”，并使用 `prompts/DLC_TEACHING_PROMPT_TEMPLATE.md`。

## DLC-A｜高价值扩展

| DLC | 名称 | Trigger 摘要 |
|---|---|---|
| [DLC-CONTROL](modules/DLC-CONTROL.md) | Controller 工程与多执行器 | 目标岗位强调 controller 配置/调参；项目需要 gripper、多 controller、切换或容差优化；CORE controller 已稳定。 |
| [DLC-MOVEIT](modules/DLC-MOVEIT.md) | MoveIt 应用深化 | 项目需要复杂 collision objects、约束、轨迹检查或规划参数调优；面试明确追问 PlanningScene。 |
| [DLC-APP-RECOVERY](modules/DLC-APP-RECOVERY.md) | Retry、Replan 与有限恢复 | CORE 错误传播已经可靠；项目或岗位明确需要自动恢复，而不是只需正确失败。 |
| [DLC-HARDWARE](modules/DLC-HARDWARE.md) | 真实机械臂 Bring-up | 已经获得真机、vendor SDK/driver 或面试岗位明确涉及硬件接入。没有设备或明确岗位需求时不学。 |
| [DLC-TEST](modules/DLC-TEST.md) | 测试自动化与回归工程 | 项目开始频繁回归、团队要求自动化测试/CI，或目标岗位重视测试框架。 |

## DLC-B｜按岗位/项目需要

| DLC | 名称 | Trigger 摘要 |
|---|---|---|
| [DLC-ENV-ADV](modules/DLC-ENV-ADV.md) | Docker、Linux 与设备环境深化 | 稳定 ros2-dev 无法满足 native fallback、USB/serial/device、复杂 GPU 或多 container 需求；出现真实环境阻塞。 |
| [DLC-TOOLS](modules/DLC-TOOLS.md) | Linux、Git 与 CMake 深化 | CORE 实际任务被 shell/process/filesystem、Git 历史操作或 CMake 工程问题阻塞；岗位明确要求更深工具能力。 |
| [DLC-ROS-RUNTIME](modules/DLC-ROS-RUNTIME.md) | QoS、Lifecycle 与 Composition | topic 双方存在但行为异常、系统需要受控启动/停止，或岗位/项目明确使用 lifecycle/composition。 |
| [DLC-ROS-NETWORK](modules/DLC-ROS-NETWORK.md) | ROS 2 Discovery 与容器网络 | 节点跨主机/container 无法发现、ROS_DOMAIN_ID/localhost/network 明显成为真实问题，或部署需要跨机通信。 |
| [DLC-MODEL-ENGINEERING](modules/DLC-MODEL-ENGINEERING.md) | 机器人模型工程化 | 模型开始使用复杂 mesh/mimic、包复用、collision 优化或惯性校验；目标岗位重视 description package。 |
| [DLC-SIM](modules/DLC-SIM.md) | Gazebo 场景、传感器与物理深化 | 项目需要 sensors/world 配置、更多 physics tuning 或仿真诊断；CORE MiniArm 仿真已稳定。 |
| [DLC-SIM-GRAPHICS](modules/DLC-SIM-GRAPHICS.md) | Gazebo / RViz Graphics 排障 | Gazebo/RViz 黑屏、GUI 卡死、software rendering、GPU passthrough 或 OpenGL renderer 实际异常。没有真实 graphics 问题不要学。 |
| [DLC-DOC](modules/DLC-DOC.md) | 工程文档体系 | 团队要求正式追踪/评审/变更流程，或项目规模使简短文档失效。 |
| [DLC-DEBUG](modules/DLC-DEBUG.md) | 复杂与性能故障排查 | 五类 CORE 案例不足以解释真实复合故障、race condition 或性能问题。 |
| [DLC-JOB](modules/DLC-JOB.md) | 求职强化与压力面试 | 已经投递，真实面试反馈显示题库、系统设计、C++/ROS 高频题或压力排障需要强化。 |

## DLC-C｜深度学习

| DLC | 名称 | Trigger 摘要 |
|---|---|---|
| [DLC-CONTROL-LOWLEVEL](modules/DLC-CONTROL-LOWLEVEL.md) | 低层 ros2_control 与 JTC | 目标岗位偏底层控制/ros2_control 框架，或明确要求 JTC 源码、自定义 controller/hardware interface。 |
| [DLC-ROBOT-MATH](modules/DLC-ROBOT-MATH.md) | 机器人运动学与数学 | 岗位笔试/项目明确需要推导、奇异性分析、速度运动学或动力学；CORE 的工程直觉不足以继续。 |
| [DLC-ROS-MIDDLEWARE](modules/DLC-ROS-MIDDLEWARE.md) | DDS、Executor 与 Middleware 内部 | 目标岗位明确要求 middleware/executor/DDS 内部，或真实问题不能在 QoS/network 使用层解决。 |
| [DLC-MOVEIT-INTERNALS](modules/DLC-MOVEIT-INTERNALS.md) | MoveIt 内部机制与规划算法 | 目标岗位偏 MoveIt 平台/规划算法，或明确要求源码、OMPL、trajectory optimization 内部。 |
