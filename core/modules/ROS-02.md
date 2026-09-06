# ROS-02｜C++ / Python ROS 包与最小通信编程

> CORE TO APPLY · 工作量 L

## 为什么在 CORE

建立真实 ROS 编程能力，并在 TaskNode 前掌握最小 Action。

## Prerequisites

ROS-01

## 环境要求

使用 ENV-01 验收后的稳定 `ros2-dev`；正常情况下直接进入 ROS/机械臂任务。Docker、Linux、Git、CMake 只在当前步骤需要时解释最小部分。

## 开始时检查

读取 CORE_INDEX、本模块、prerequisite reports、LEARNING_STATUS、环境清单和当前项目真实证据；确认所需 node/package/配置基线。

## 核心实践

创建 ament_cmake、ament_python 和 custom interface package；用合理跨语言组合完成最小 pub/sub、service server/client、action server/client；Action 覆盖 goal response、feedback、result、cancel 与 goal handle，不重复刷两套完整 demo。

## 最小理论

package.xml、CMake/setup、rosidl、rclcpp/rclpy/rclcpp_action 的当前任务所需部分。

## 故障注入

依赖/接口未生成、未 source、类型不一致、goal 拒绝或 cancel 未结束。

## Deliverables

三个最小包、custom interfaces、跨语言运行证据和构建故障记录。

## Exit Criteria

能独立建包和接口；C++/Python 通过同一接口通信；最小 Action 生命周期可运行和解释。

## Anti-Rabbit-Hole

至少 80–90% 注意力留给当前任务。辅助知识只给继续实践所需的最小解释；值得深入时记录下列 DLC_REF 并立即返回主线：

DLC_REF: DLC-TOOLS；DLC_REF: DLC-ROS-RUNTIME

除非主题确实阻塞 CORE，或学习者明确说“进入 <DLC_ID>”，否则不得展开 DLC。

## 模块面试范围

跨语言通信、接口生成、Action 生命周期、CMake/ament 最小职责。

CORE 面试不得追问对应 DLC 的内部原理。

## 新对话恢复

读取 README、LEARNING_STATUS、core/CORE_INDEX.md、本文件、prerequisite reports、projects/PROJECTS.md、相关项目 README/evidence、prompts/TEACHING_PROTOCOL.md 和 prompts/MODULE_INTERVIEW_RULES.md；不得依赖上一聊天记忆。
