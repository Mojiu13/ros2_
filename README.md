# ROS2 机械臂软件工程师求职课程

面向 Ubuntu 24.04、ROS 2 Jazzy、C++/Python、RViz2、URDF/Xacro、Gazebo Sim、ros2_control 与 MoveIt 2 的工程训练路线。目标是第一份 ROS 机械臂应用开发工作，不是高级机器人算法研究。

本仓库当前只定义课程体系、学习顺序、模块边界、验收证据和教学规则；尚未开始任何模块教学。

## 课程原则

- 实践闭环：运行 → 观察 → 修改 → 再运行 → 单一故障注入 → 分层定位 → 修复 → 回归 → 总结 → 复述 → 模块面试。
- 先建立完整链路，再按岗位价值深化；理论 Just-In-Time。
- C++ 在 Phase 0 进入，Python 同步保留；应用项目以 C++ 核心节点 + Python 调用/测试为默认组合。
- 现代 Jazzy 实践：Gazebo Sim 与对应 ROS 集成；不混用 ROS 1、Gazebo Classic 或旧发行版命令。
- 每个模块可在全新 ChatGPT 对话独立启动，完成状态只以 GitHub 证据为准。
- 不把源码阅读、自定义 controller、高级运动学或规划算法放入主线。

## 学习顺序

1. Phase 0：环境、计算图、双语言包、launch/config。
2. Phase 1：参考全链路 → 自建模型 → Gazebo → ros2_control → 直接轨迹 → MoveIt → 编程闭环 → 集成验收。
3. Phase 2：模型、ROS 工程、controller、PlanningScene 与轨迹质量深化。
4. Phase 3：TaskNode、故障恢复、独立 Debugging 主线、测试与工程文档。
5. Phase 4：求职证据与综合模拟面试。
6. Advanced Optional：按岗位需要选择源码、自定义 controller、规划参数深化。

## 三条路线

- Fast Track：只取首份工作面试与最小可展示项目不可缺的 P0 模块。
- Standard Track：P0 + P1，目标是进入团队后能承担基本独立开发、调试、测试和文档工作。
- Advanced Optional：P2，不阻塞求职主线。

具体范围见 [`curriculum/TRACKS.md`](curriculum/TRACKS.md)，完整顺序见 [`curriculum/CURRICULUM_INDEX.md`](curriculum/CURRICULUM_INDEX.md)。

## 两个演化项目

- Project A：MiniArm Simulation Stack。证明模型、Gazebo、ros2_control、MoveIt 与完整执行链能力。
- Project B：Task Execution & Recovery。证明 C++/Python 应用开发、action 接口、取消/超时/恢复、测试和文档能力。

项目边界与证据见 [`projects/PROJECTS.md`](projects/PROJECTS.md)。仓库的当前设计区与未来学习产物区见 [`REPOSITORY_STRUCTURE.md`](REPOSITORY_STRUCTURE.md)。

## 从新对话开始模块

复制 [`prompts/MODULE_TEACHING_PROMPT_TEMPLATE.md`](prompts/MODULE_TEACHING_PROMPT_TEMPLATE.md)，只替换 `<MODULE_ID>`。教学者必须读取对应独立模块定义和前置模块产物，不能依赖聊天记忆。

## 完成定义

“运行成功”不是完成。模块同时需要：可运行证据、CLI/日志观察、至少一个受控故障、修复与回归、模块产物、口头复述、5–8 题模块面试及标准问答。状态见 [`LEARNING_STATUS.md`](LEARNING_STATUS.md)。

## 范围外

强化学习、Isaac Lab、灵巧手、视觉伺服、触觉、CUDA/TensorRT、具身大模型、高级控制算法均为 P3，本路线不安排；只有目标岗位改变时才重新评估。
