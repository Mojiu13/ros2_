# ROS-02｜Python 与 C++ ROS 包最小工程

> Phase 0 · P0 · 工作量 L

## 为什么学习

在 APP-01A 前完成 C++/Python 包、custom interface 以及最小 topic/service/action 编程台阶，使 rclcpp_action 不再是首次接触。

## Prerequisites

ROS-01

## 环境要求

使用 ENV-01 验收通过的 Dockerized ROS2 Jazzy 基础环境；不假定 Host 安装 ROS。此时 Just-In-Time 加入 ROS package/interface 开发依赖，并写入版本化环境定义、重建、验证和记录版本。

## 开始时检查

先确认 Docker Engine、目标 image/container、source mount、ROS underlay、workspace overlay、ROS-01 证据；检查自定义 interface 所需生成器是否已版本化。

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

如果为了本模块在 running container 中临时安装或修改依赖，但没有回写 Dockerfile/Compose/entrypoint 等版本化环境定义并重建验证，则模块不得 Completed。

## 模块面试范围

跨语言为何能通信；接口生成链；service 与 action；goal handle；cancel 的最小语义；构建成功但 interface 找不到怎么查。

## 新对话上下文恢复

读取 `README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、当前 module、prerequisite reports、`curriculum/DOCKER_FIRST_ARCHITECTURE.md`、`docs/ENVIRONMENT_MANIFEST.md`，以及当前项目真实 README/evidence。不得依赖上一聊天记忆。
