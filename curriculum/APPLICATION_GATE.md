# APPLICATION_GATE｜最低可投递标准

它不是课程模块，也不是全部学完。达到后立即开始投递，然后依次继续 TEST-01 → DOC-01 → JOB-01 → P1，并按真实面试反馈回补。

## 技术证据

- ENV-01：non-root/UID/GID 正确，完整 Dockerized Jazzy 机械臂开发环境可删除重建，源码不丢失，最小节点再次成功。
- ROS-01~03：计算图、容器 discovery、C++/Python、custom interface、最小 Action、launch/config 均有证据。
- A1：2–3 DOF MiniArm 完成建模、Gazebo、ros2_control、direct trajectory 原理学习。
- A2：CTRL-02 Stage B 已证明成熟 6/7 DOF 的 Gazebo/simulated hardware→ros2_control→JTC→FJT→motion；MOVEIT/编程/INT 全链路完成。
- APP-01A/B：真实 REQUIREMENTS、接口、C++ TaskNode、Python client、状态机。
- APP-02A：cancel、timeout、planning/execution/controller/action 错误正确终止并传播。
- DBG-01：至少覆盖 Docker user/mount/network、TF/model、controller、MoveIt planning、execution/application 五个故障族。
- Project A/B 各有最小 README：范围、技术栈、架构、复现入口、真实证据、已知限制。

## 最低简历材料

必须生成 `docs/MINIMUM_RESUME_EVIDENCE.md`，Project A 和 B 各包含：项目名称、技术栈、2–3 条真实 bullet、GitHub 项目入口。使用模板 `docs/templates/MINIMUM_RESUME_EVIDENCE.md`。

禁止虚构真机经验、性能指标、工业落地、未实现 recovery 或未经测试的功能。完整 pitch、简历优化和模拟面试仍由 JOB-01 完成。

## Gate 面试检查

能三分钟介绍项目；能画 Docker→ROS→MoveIt→controller→Gazebo 链路；能解释 A1/A2 分工、Plan/Execute、Action 生命周期及分层排障。
