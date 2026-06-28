# PROMPT_INDEX｜模块提示词索引

本目录用于让后续 ChatGPT 对话直接调用某个学习模块。

你不需要每次重新解释背景，只需要在新对话框中使用“通用调用指令”，并指定模块编号。

---

## 1. 通用调用指令

把下面内容复制到新对话框中，把 `<MODULE_ID>` 替换成你要学的模块编号，例如 `R1-M1`、`R2-M6`、`MP-A`。

```text
请连接并读取我的 GitHub 仓库：Mojiu13/ros2_

请优先读取以下文件：
1. README.md
2. LEARNING_STATUS.md
3. docs/COMMAND_CHEATSHEET.md
4. docs/ERROR_LOG.md
5. docs/SYSTEM_MAP.md
6. prompts/PROMPT_INDEX.md
7. prompts/ALL_MODULE_PROMPTS.md

我要学习的模块是：<MODULE_ID>

请在 prompts/ALL_MODULE_PROMPTS.md 中找到该模块对应的提示词，并严格按该模块提示词带我学习。

要求：
- 把我当作真正的新手；
- 不要百科式堆知识点；
- 先跑最小例子，再观察，再修改，再故障注入，再总结；
- 每次只给我少量命令，等我贴输出后再判断；
- 如果报错，先判断错误属于哪一层：环境层、workspace 层、launch 层、ROS2 通信层、URDF/TF 层、MoveIt 层、ros2_control 层、controller 层、RViz 层、GitHub 文档层；
- 每完成一个阶段，告诉我应该更新仓库里的哪个文件；
- 本模块结束时，帮我生成可提交到 GitHub 的总结文档。

现在请从该模块的第一步开始带我做。
```

---

## 2. 模块列表

### R0：准备层

| 编号 | 模块 |
|---|---|
| R0-M0 | 环境、仓库、学习记录基线 |

### R1：第一遍快速全链路

| 编号 | 模块 |
|---|---|
| R1-M1 | ROS2 最小通信与命令行观察 |
| R1-M2 | URDF / Xacro / TF 最小机器人模型 |
| R1-M3 | ros2_control 最小执行链路 |
| R1-M4 | MoveIt2 RViz 规划执行流程 |
| R1-M5 | MoveItPy Python 代码闭环 |
| R1-M6 | 全链路串联与最小故障定位 |
| R1-M7 | 第一遍整合小项目 |

### R2：第二遍工作能力深化

| 编号 | 模块 |
|---|---|
| R2-M1 | ROS2 工程组织：package / launch / parameter / YAML |
| R2-M2 | 机器人模型工程：URDF / Xacro / SRDF / TF / MoveIt config |
| R2-M3 | ros2_control 配置深化：controller / interface / lifecycle |
| R2-M4 | MoveIt 架构深化：RobotModel / RobotState / PlanningScene |
| R2-M5 | MoveIt Planning Pipeline 与 trajectory 生成 |
| R2-M6 | MoveIt Execution 与 controller 对接 |
| R2-M7 | ROS2 Action 与 C++ 工程基础 |
| R2-M8 | joint_trajectory_controller 源码主线 |
| R2-M9 | 自定义 controller 与 mock hardware，可选进阶 |

### MP：项目层

| 编号 | 模块 |
|---|---|
| MP-A | MoveItPy TaskNode 任务节点项目 |
| MP-B | arm + gripper 顺序执行项目 |
| MP-C | 故障注入与自动恢复项目 |
| MP-D | 自定义 controller 项目，可选 |

### JOB：求职表达层

| 编号 | 模块 |
|---|---|
| JOB-M1 | README / 架构图 / 调试文档 |
| JOB-M2 | 简历项目描述 |
| JOB-M3 | 面试问答库 |

---

## 3. 使用示例

### 示例 1：学习 R1-M1

```text
请连接并读取我的 GitHub 仓库：Mojiu13/ros2_

请读取 README.md、LEARNING_STATUS.md、docs/COMMAND_CHEATSHEET.md、docs/ERROR_LOG.md、docs/SYSTEM_MAP.md、prompts/PROMPT_INDEX.md、prompts/ALL_MODULE_PROMPTS.md。

我要学习的模块是：R1-M1。

请找到该模块提示词，并从第一步开始带我做。
```

### 示例 2：学习 MP-A

```text
请连接并读取我的 GitHub 仓库：Mojiu13/ros2_

我要学习的模块是：MP-A。

请根据 prompts/ALL_MODULE_PROMPTS.md 中的 MP-A 提示词，带我完成 MoveItPy TaskNode 任务节点项目。
```

---

## 4. 学习总原则

每个模块都遵守同一套训练节奏：

```text
运行 → 观察 → 修改 → 破坏 → 修复 → 总结 → 复述
```

每个模块结束必须留下：

```text
1. 可运行结果
2. 观察命令
3. 系统链路理解
4. 错误记录
5. README 或模块文档
6. 3～5 个面试问答
```
