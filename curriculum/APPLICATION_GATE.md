# APPLICATION_GATE｜最低可投递标准

它不是课程模块，也不是“全部学完”。达到后立即开始投递，同时继续 TEST-01、DOC-01、JOB-01 与 P1，并根据真实面试反馈回补。

## 必须已有

- ENV-01：Dockerized Jazzy 环境可删除 container 后重建，源码仍在，工作区能重编译。
- ROS-01~03：会用 CLI 看计算图，C++/Python 包可构建，launch/YAML/namespace/remap 可解释。
- Project A1：2–3 DOF MiniArm 的模型、TF、Gazebo、ros2_control 学习证据。
- Project A2：成熟 6/7 DOF 机械臂的 Gazebo、controller、直接 trajectory、MoveIt、C++/Python plan→execute 全链路。
- INT-01：干净环境可重复启动，规划、执行和反馈链证据齐全。
- APP-01A/B：真实 REQUIREMENTS、接口、C++ TaskNode、Python client、最小状态机。
- APP-02A：cancel、timeout、planning/execution/controller/action 错误能正确结束并传播。
- DBG-01 核心案例：至少覆盖 Docker/环境、TF/model、controller、MoveIt planning、execution/application 五个故障族。
- Project A/B 各有最小 README：范围、架构、已实现功能、复现入口、真实证据、已知限制。

## Gate 面试检查

能在 3 分钟介绍项目；能画 Docker→ROS→MoveIt→controller→Gazebo 数据链；能解释 Plan failed 与 Execute failed；能给出机械臂不动的分层排查顺序；不得宣称尚未测试或实现的能力。

## Gate 后动作

开始投递；并行完成 TEST-01、DOC-01、JOB-01；再按目标岗位补 P1。面试暴露的问题进入 LEARNING_STATUS，不以新增无关课程替代真实回补。
