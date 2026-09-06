# CORE 求职项目

## Project A｜Manipulator Simulation & Integration

### A1 MiniArm Learning Model

MODEL-01 → SIM-01 → CTRL-01 → CTRL-02 Stage A。2–3 DOF 自建模型用于理解 URDF/TF/Gazebo/ros2_control/FJT 原理。

### A2 Full Manipulator Integration

SYS-01 选择成熟 6/7 DOF → CTRL-02 Stage B 独立 controller baseline → MOVEIT-01 → MOVEIT-02 → INT-01。最终求职集成证据主要来自 A2，不要求从零手搓复杂工业模型。

## Project B｜TaskNode Application

APP-01A 小规模需求/接口 → APP-01B TaskNode/状态机 → APP-02A cancel/timeout/error → DBG-01 高频故障 → DELIVERY-01 最低测试/文档。

CORE 明确停止在“可靠成功或明确失败”。Retry/replan/recovery 属于 `DLC-APP-RECOVERY`。

## 最低交付

两个项目均需真实 README、架构/执行图、运行证据、已知限制和简历 bullet。复杂调参、真机、完整自动化测试或大规模文档均非 Gate 前提。
