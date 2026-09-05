# Fast / Standard / Advanced 路线

路线按技能依赖定义，不按固定日历。模块保持 S/M/L 粒度；没有 XL 模块。

## Fast Track：求职优先

ENV-01 → ROS-01 → ROS-02 → ROS-03 → SYS-01 → MODEL-01 → SIM-01 → CTRL-01 → CTRL-02 → MOVEIT-01 → MOVEIT-02 → INT-01 → APP-01A → APP-01B → APP-02A → DBG-01 → **APPLICATION_GATE** → TEST-01 → DOC-01 → JOB-01。

Fast Track 仍必须最终完成 TEST-01、DOC-01、JOB-01；但达到 Application Gate 后立即开始投递，并边投边完成它们。

## Application Gate

Gate 不是课程结束。它要求 Docker 可复现环境、6/7 DOF 全链路、C++/Python 编程闭环、TaskNode v1、取消/超时/错误传播、核心跨层故障案例和最小项目 README。详见 `APPLICATION_GATE.md`。

## Standard Track：基本独立工作

完成 Fast 主干并开始投递后，加入 MODEL-02、ROS-04、CTRL-03、MOVEIT-03、APP-02B；随后用新增证据更新 TEST/DOC/JOB 材料。

目标从“达到面试与投递门槛”升级为“进入团队后能基本独立修改模型/配置、开发应用、处理常见故障、测试并交付文档”。

## Advanced Optional

- ADV-01：joint_trajectory_controller 源码，P2。
- ADV-02：自定义 ros2_control controller，P2。
- ADV-03：更深入运动学与 MoveIt 参数实验，P2。

## P3 暂不学习

DDS 内部实现、executor/MoveIt 全源码、高级动力学/控制、强化学习、Isaac Lab、灵巧手、视觉伺服、触觉、CUDA/TensorRT、具身智能。
