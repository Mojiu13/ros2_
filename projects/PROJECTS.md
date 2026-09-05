# 两个持续演化的求职项目

## Project A｜Manipulator Simulation & Integration

### A1｜MiniArm Learning Model

使用 2–3 DOF 自建机械臂，服务于 MODEL-01 → SIM-01 → CTRL-01/02。亲手理解 URDF、Xacro、TF、RViz、collision、inertial、Gazebo Sim、ros2_control 和直接 trajectory。它是学习模型，不承担最终工业复杂度证明。

### A2｜Full Manipulator Integration

从 MOVEIT-01 起迁移到教学时根据 Jazzy 当前支持状态确认的成熟 6 DOF 或 7 DOF 机械臂（例如维护良好的 UR/Panda 类方案）。不为“原创”从零手搓复杂工业模型。

完成 MoveIt 配置与 RViz、C++/Python plan→execute、controller mapping、FollowJointTrajectory、Gazebo 仿真、反馈链和 INT-01 集成验收。最终 Project A 求职证据主要来自 A2；A1 用来证明基本原理不是黑盒。

Project A 的 Docker README 最终给出：clone → build image → start container → build workspace → launch project。镜像/版本在教学时按 Jazzy、Gazebo、MoveIt 官方当前文档确认。

## Project B｜Task Execution & Recovery

APP-01A：先写 REQUIREMENTS（FR/NFR/Acceptance Criteria）、INTERFACE_DESIGN、Task.action、C++ server 骨架和 Python client。

APP-01B：接入 MoveIt，完成 named/joint/pose、plan/execution 错误分离、feedback/result 与最小状态机，形成 Project B v1。

APP-02A：实现 cancel、timeout、客户端中断与下游不可用的确定结束和错误传播；这是 Fast/P0。

APP-02B：在 Standard/P1 中增加受限 retry/replan、readiness 和 recovery budget；禁止无限重试或用恢复掩盖根因。

TEST-01 建立 Requirement→Test Case 追踪；DOC-01 只整理真实使用的需求和设计，不事后虚构。

## 项目环境证据

`docker/` 逐渐形成 Dockerfile、compose.yaml、entrypoint.sh、README；源码由宿主 Git 仓库 bind mount，删除 container 后仍在。Project A/B README 都引用同一可重建环境定义，并记录必要的差异。
