# 岗位能力矩阵

| 岗位要求 | 对应能力 | 课程模块 | 优先级 | 最终证据 |
|---|---|---|---:|---|
| 可复现 ROS 开发环境 | 最小 Dockerfile/Compose、non-root UID/GID、持久化 workspace、环境逐步演化、重建 | ENV-01, ROS-01, SIM-01 | P0 | docker/ 定义、ENVIRONMENT_MANIFEST、ownership 与重建记录 |
| ROS 机械手需求/方案/开发 | 需求、接口、节点架构、Task action、状态机、C++/Python | ROS-01~03（含最小 Action）, APP-01A/B | P0 | REQUIREMENTS、INTERFACE_DESIGN、TaskNode、Python client |
| 多自由度机械手集成 | 成熟 6/7 DOF 模型上的 MoveIt/controller/Gazebo 集成 | SYS-01, MOVEIT-01/02, INT-01 | P0 | Project A2 全链路与集成报告 |
| 自建模型与仿真理解 | 2–3 DOF MiniArm、URDF/Xacro/TF、碰撞/惯性、Gazebo | MODEL-01, SIM-01, CTRL-01 | P0 | Project A1 参数实验和模型证据 |
| 最低机器人学理解 | DOF、joint/task space、pose/frame/transform、FK/IK/工作空间/奇异直觉 | MODEL-01, MOVEIT-01/02 | P0 | 模型实验、pose goal 与失败解释 |
| ros2_control 执行 | interfaces、lifecycle、controller、FollowJointTrajectory | CTRL-01~03 | P0/P1 | 直接轨迹、状态/接口图、参数实验 |
| 可控失败的应用 | cancel、timeout、错误传播、有限 retry/replan | APP-02A/B | P0/P1 | Project B 错误语义与恢复策略 |
| 跨层调试 | Host→Docker→ROS→model→controller→MoveIt→application | DBG-01 | P0 | 决策树与可复现 ERROR_LOG |
| 软件功能测试 | Requirement→Test Case、pytest/gtest、launch/integration、回归 | TEST-01 | P0 | TEST_PLAN、自动化测试、TEST_REPORT |
| 设计与测试报告 | 需求追踪、架构、时序、配置、调试、测试文档 | APP-01A, DOC-01 | P0 | 软件设计与测试文档包 |
| 最低求职表达 | 项目事实、故障案例、白板链路、简历证据 | APPLICATION_GATE, JOB-01 | P0 | Project README、Pitch、问答与简历条目 |
| 底层/规划加分 | 源码、自定义 controller、深入运动学/规划参数 | ADV-01~03 | P2 | 可选实验，不阻塞投递 |
