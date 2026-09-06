# 两个持续演化的求职项目

## Project A｜Manipulator Simulation & Integration

### A1｜MiniArm Learning Model

使用 2–3 DOF 自建机械臂，从零完成 URDF/Xacro/TF/RViz、collision/inertial、Gazebo、ros2_control 和 direct trajectory。A1 用于理解原理，不作为最终工业复杂度证明。

### A2｜Full Manipulator Integration

实际型号在 SYS-01 根据 ROS2 Jazzy、Gazebo Sim、ros2_control、MoveIt 与 Docker 当前支持状态选择，可优先评估维护良好的 UR/Panda 类模型，但不提前固定。

~~~text
SYS-01
参考 6/7 DOF 基线观察与型号/版本记录
    ↓
CTRL-02 Stage B
A2 Gazebo/simulated hardware + ros2_control + direct trajectory baseline
    ↓
MOVEIT-01
A2 SRDF / kinematics / MoveIt config / RViz plan-execute
    ↓
MOVEIT-02
A2 C++/Python planning and execution
    ↓
INT-01
A2 Dockerized full integration
~~~

成熟模型若已有 controller/config，重点是读懂、验证、修改、故障注入与排查，不重复发明。最终 Project A 求职证据主要来自 A2。

## Project B｜Task Execution & Recovery

APP-01A 在编码前创建 REQUIREMENTS、INTERFACE_DESIGN、Task.action、C++ server skeleton 和 Python client；此时 ROS-02 已提供最小 Action 编程经验。

APP-01B 接入 MoveIt 与最小状态机；APP-02A 完成 cancel/timeout/error propagation；APP-02B 在 P1 增加有限 retry/replan。TEST-01 建立 Requirement→Test Case，DOC-01 只整理真实需求与证据。

## 环境与求职证据

Project A/B 使用 ENV-01 一次构建的同一个稳定主 `ros2-dev` container，不强制拆成微服务。README 最终给出 clone→build image→start container→build workspace→launch。Application Gate 生成 `docs/MINIMUM_RESUME_EVIDENCE.md`；不得虚构真机、性能、工业落地、未实现 recovery 或未经测试的功能。
