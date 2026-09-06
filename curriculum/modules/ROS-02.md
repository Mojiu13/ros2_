# ROS-02｜Python 与 C++ ROS 包最小工程

> Phase 0 · P0 · 工作量 L

## 为什么学习

在 APP-01A 前完成 C++/Python 包、custom interface 以及最小 topic/service/action 编程台阶，使 rclcpp_action 不再是首次接触。

## Prerequisites

ROS-01

## 环境要求

默认使用 ENV-01 已构建并验收的完整 `ros2-dev` image；不假定 Host 安装 ROS。正常情况下只启动主 development container、进入容器并确认本模块所需 package 可用，然后直接开始 ROS/机器人软件学习。只有实际缺包、版本冲突或新增项目特定依赖时才修改环境定义、重建并更新 `docs/ENVIRONMENT_MANIFEST.md`。

## 开始时检查

[HOST] 如主环境未运行，启动既有 Compose 项目。[CONTAINER] 确认 workspace/source mount、ROS underlay、workspace overlay和本模块 prerequisite evidence；检查本模块所需 package 可用。环境正常时不重新审计 Docker。

## 核心实践任务

创建 custom interface package。采用跨语言组合完成 publisher/subscriber、service server/client、最小 action server/client，例如 C++ publisher→Python subscriber、C++ service server←Python client、C++ action server←Python action client。Action 只覆盖 goal、goal response、feedback、result、cancel、goal handle 和 CLI 观察；不引入 MoveIt、TaskNode、状态机、retry 或 timeout recovery。

## 最小理论

ament_cmake/ament_python、package.xml、CMakeLists/setup.py、rosidl interface generation；topic/service/action 边界；action server/client 与 goal handle。

## 故障注入

interface 未生成/未 source、C++/Python 类型不一致、action server 缺失、goal 被拒绝、cancel 未处理、构建依赖缺失。

## 输出文件 / Deliverables

custom interface package、C++/Python 通信包、三类通信运行记录、action CLI 证据、构建错误记录。

## Exit Criteria

能独立创建 custom interface package；跨语言 pub/sub、service、action 均可运行；能写最小 Action Server/Client、解释 goal/response/feedback/result/cancel/goal handle，并用 CLI 观察两端；APP-01A 不再首次接触 rclcpp_action。

除非证据、复述和模块面试全部完成，否则不得标记 Completed。

如果实际修改了运行环境，或为诊断在 running container 中临时安装了依赖，必须回写 Dockerfile/Compose/entrypoint、重建验证并更新 `docs/ENVIRONMENT_MANIFEST.md`；否则模块不得 Completed。

## 模块面试范围

跨语言为何能通信；接口生成链；service 与 action；goal handle；cancel 的最小语义；构建成功但 interface 找不到怎么查。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、当前 module、prerequisite reports、Docker architecture、ENVIRONMENT_MANIFEST 和当前项目真实 README/evidence。ENV-01 完成后默认环境稳定；除非出现容器、权限、GUI、缺包、污染或版本冲突，不重新展开 Docker 教学。
