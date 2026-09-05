# ROS2 机械臂软件工程师求职课程

面向第一份 ROS2 机械臂应用开发 / 软件工程岗位。默认技术环境为 **Ubuntu 24.04 Host + Docker + ROS2 Jazzy Container**，主线保持 C++/Python、RViz2、URDF/Xacro、Gazebo Sim、ros2_control 与 MoveIt 2。

课程架构已经正式冻结：本次只对既有 Phase / Module 做 Docker-first、项目复杂度、机器人基础、APP 粒度和求职 Gate 的局部修订，未扩大岗位范围。

## 环境原则

- Host 负责 Docker Engine/Compose、Git、编辑器、桌面/GPU driver、硬件访问基础和源码持久化。
- Container 从 ROS2 Jazzy 最小开发环境开始；Gazebo、ros2_control、MoveIt 等按模块 Just-In-Time 写入环境定义并逐步重建。
- 项目源码通过 bind mount 持久化；删除 container 后必须能从 Dockerfile/Compose 重建。
- ENV-01 只记录基本 GPU 信息；RViz GUI 在 SYS-01 按需配置，Gazebo GPU/renderer 在 SIM-01 正式验证。
- 纯仿真默认 Docker；只有记录了实际限制与差异时才允许 Native Fallback。

环境图见 [`curriculum/DOCKER_FIRST_ARCHITECTURE.md`](curriculum/DOCKER_FIRST_ARCHITECTURE.md)。

## 保持不变的课程原则

- 运行 → 观察 → 修改 → 再运行 → 单一故障注入 → 分层定位 → 修复 → 回归 → 总结 → 复述 → 模块面试。
- 先建立完整链路，理论 Just-In-Time；不混用 ROS 1、Gazebo Classic 或旧发行版做法。
- C++ 在 Phase 0 进入，Python 同步保留。
- 源码、自定义 controller 和深入运动学继续是 P2；高级机器人/AI 方向仍为 P3。

## Project A 的两级复杂度

- A1 MiniArm Learning Model：2–3 DOF，只用于真正理解 URDF/Xacro/TF/RViz/Gazebo/ros2_control。
- A2 Full Manipulator Integration：使用教学时确认仍获 Jazzy 良好支持的成熟 6/7 DOF 机械臂；最终求职证据主要来自 A2。

## 路线与投递

- 完整模块顺序：[`curriculum/CURRICULUM_INDEX.md`](curriculum/CURRICULUM_INDEX.md)
- Fast / Standard：[`curriculum/TRACKS.md`](curriculum/TRACKS.md)
- 最低可投递 Gate：[`curriculum/APPLICATION_GATE.md`](curriculum/APPLICATION_GATE.md)
- 岗位映射：[`curriculum/ROLE_COMPETENCY_MATRIX.md`](curriculum/ROLE_COMPETENCY_MATRIX.md)
- 项目边界：[`projects/PROJECTS.md`](projects/PROJECTS.md)

达到 Application Gate 并生成最低简历证据后开始投递，随后继续 TEST-01 → DOC-01 → JOB-01 → P1；不需要等全部课程学完。

## 开始模块

在新对话中复制 [`prompts/MODULE_TEACHING_PROMPT_TEMPLATE.md`](prompts/MODULE_TEACHING_PROMPT_TEMPLATE.md)，替换 `<MODULE_ID>`。新版状态见 [`LEARNING_STATUS.md`](LEARNING_STATUS.md)。
