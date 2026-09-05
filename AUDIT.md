# 旧路线审计与重构决策

审计对象：重构前 README、LEARNING_STATUS、PROMPT_INDEX、ALL_MODULE_PROMPTS、MODULE_INTERVIEW_RULES，以及 docs/mini_projects 的索引与实际覆盖情况。

## 值得保留

- “运行—观察—修改—故障注入—修复—总结—复述—面试”的实践闭环。
- 第一遍先观察完整链路，再深入 MoveIt/ros2_control 的学习策略。
- 直接调用 FollowJointTrajectory、区分 Plan/Execute、强调 joint name 一致性。
- 每模块面试、错误日志、系统地图和求职项目的证据导向。

## 合并与重画边界

- 原 R0-M0 混合环境验收、参考 Panda 全链路和仓库整理；现拆为 ENV-01 与 SYS-01。
- 原 R1/R2 在基础工程和全链路之间来回跳转；现把 package、C++/Python、launch/YAML/namespace 前置到 Phase 0。
- 原 MP-A/MP-B/MP-C 三个分散项目合并为两个持续演化项目：底层仿真栈与任务执行/恢复。
- MoveIt 架构、Planning Pipeline 与执行链保留知识点，但按“RViz 配置闭环→编程闭环→场景与轨迹质量”重排。

## 前移

- rclcpp、ament_cmake、CMakeLists/package.xml 前移到 ROS-02。
- launch、parameter、YAML、namespace、remap 前移到 ROS-03。
- Gazebo Sim 成为 Phase 1 独立 P0 主线。
- Debugging、测试、软件设计/测试报告成为独立 P0 模块。

## 后移或降级

- joint_trajectory_controller 源码由主线降为 ADV-01/P2。
- 自定义 controller 与 mock hardware 降为 ADV-02/P2。
- 更深入运动学、规划器调参降为 ADV-03/P2。
- DDS 内部、executor/MoveIt 源码、高级动力学与控制等归 P3，不在仓库主线。

## 旧路线缺口

- Gazebo 只有概念位置，没有独立、可验收的模型加载—控制—运动主线。
- C++ ROS 开发过晚，不符合招聘要求。
- 软件测试、launch/integration test、TEST_PLAN/TEST_REPORT 不完整。
- 需求—设计—测试可追踪的软件工程文档训练不足。
- 模块没有全部具备独立文件、统一前置恢复规则和可验证 Exit Criteria。
- mini_projects 多为提示词中的目标，缺少统一演化关系与招聘能力证据矩阵。

## 清除策略

旧工作树由本次课程设计完整替换；旧内容不留在新目录中。Git 历史仍可追溯，但 `LEARNING_STATUS.md` 从未开始状态重新建立，避免把旧 demo 观察误当新版模块验收。
