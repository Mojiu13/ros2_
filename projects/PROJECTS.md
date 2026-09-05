# 两个持续演化的求职项目

## Project A｜MiniArm Simulation Stack

演化：MODEL-01 最小模型 → SIM-01 Gazebo 物理模型 → CTRL-01 控制接入 → CTRL-02 直接轨迹 → MOVEIT-01 配置 → MOVEIT-02 编程规划执行 → INT-01 集成验收。

最终范围：2–3+ DOF 自建机械臂；单一描述源；Gazebo Sim；ros2_control；joint_trajectory_controller；FollowJointTrajectory；MoveIt 规划执行；C++/Python 示例；分层启动和验收。

证明：URDF/Xacro/TF、仿真、controller 配置、MoveIt 对接、Linux/ROS 工程、C++/Python、全链路调试。

明确不做：高级动力学控制、真实硬件安全认证、视觉抓取、复杂规划算法。

## Project B｜Task Execution & Recovery

演化：APP-01 TaskNode action server → DBG-01 故障分类 → TEST-01 自动化测试 → APP-02 取消/超时/重试/恢复 → DOC-01 文档 → JOB-01 答辩。

功能边界：named/joint/pose 目标；真实 feedback/result；输入校验；规划与执行错误分离；timeout/cancel；有限 retry/replan；controller/action readiness；最终失败原因。

默认架构：C++ TaskNode 为核心；Python 客户端与测试工具；MoveIt 负责规划/执行协调；ros2_control controller 负责按时轨迹；Gazebo Sim 提供仿真机器人。

证明：需求与方案、ROS action 应用、状态机、故障恢复、测试、软件设计文档、测试报告、项目表达。

## 仓库目标结构

未来教学产物写入 `projects/project_a_sim_stack/` 与 `projects/project_b_task_executor/`。当前仅保留本设计文件和模板；不得预生成虚假的运行证据。
