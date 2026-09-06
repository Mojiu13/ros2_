# APPLICATION GATE｜最低可投递标准

Gate 只判断能否证明已走通一个可信 ROS2 机械臂应用项目，不判断是否完成全部机器人知识。DLC 完全不是 Gate prerequisite。

## 通过位置

`DELIVERY-01` 完成后执行检查；通过即开始投递。

## 必须证据

- 17 个 Gate 前 CORE 均满足 practice + real evidence + module report + interview；报告位于 `docs/modules/<MODULE_ID>/MODULE_REPORT.md`。
- ENV-01：完整 ros2-dev 可重建，源码持久化、non-root 权限正常。
- ROS-01~03：能观察 graph，C++/Python/custom interface、topic/service/action、launch/YAML/parameter/remap 有运行证据。
- Project A1：MiniArm 的 URDF/TF/RViz、Gazebo、ros2_control 和 direct trajectory。
- Project A2：成熟 6/7 DOF 的独立 controller baseline、MoveIt RViz、C++/Python plan→execute 和干净启动集成。
- Project B：小规模需求、Task.action、TaskNode、三类目标、feedback/result、planning/execution error distinction。
- APP-02A：invalid/cancel/timeout/controller/action unavailable 均有明确终态和错误传播。
- DBG-01：五类高频故障各至少一个代表案例。
- DELIVERY-01：6–10 个 meaningful test cases、1–3 个 automated smoke tests、最小 README/design/diagram/interface/TEST_REPORT/limitations。
- `docs/MINIMUM_RESUME_EVIDENCE.md`：Project A/B 各 2–3 条真实 bullet 和 GitHub 入口。

## 明确不要求

DLC（但不包括 CORE Required Supporting Knowledge）、完整测试工程、完整文档体系、QoS/Lifecycle、advanced controller、retry/recovery、deep Docker、advanced robotics math、大型面试题库。

## Gate 后

立即投递；完成 JOB-01；根据真实岗位和面试反馈选择 DLC。不得把“DLC 还没学”当作停止投递的理由。
