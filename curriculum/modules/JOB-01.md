# JOB-01｜项目答辩、简历证据与综合模拟面试

> Phase 4 · P0 · 工作量 M

## 为什么学习

在已经开始投递的基础上，把完整测试/文档证据转成可信求职表达，并吸收真实面试反馈。

## Prerequisites

DOC-01

## 环境要求

默认使用 ENV-01 验收通过的 Dockerized ROS2 Jazzy 环境；不假定 Host 安装 ROS。

如果本模块新增依赖，必须更新版本化环境定义、重建 image/container、验证并记录到 `docs/ENVIRONMENT_MANIFEST.md`。## 开始时检查

先确认 Docker Engine、目标 image/container、宿主 source bind mount、ROS underlay、workspace overlay，以及 prerequisite 报告/项目证据。

Application Gate 已达成；TEST-01 与 DOC-01 完成；不得包装未实现功能。## 核心实践任务

30秒/3分钟/10分钟项目介绍；解释 A1 学习价值与 A2 求职复杂度；Docker 可复现环境；能力证据表；白板链路；跨层故障、测试和需求追问；简历描述；把真实面试反馈写回状态。

## 最小理论

以技术证据为核心的 STAR；事实、推断和未完成项分开。

## 故障注入

夸大职责、把 A1 当工业项目、只背概念、无法链接证据、声称 Docker 可复现却未做删除重建。

## 输出文件 / Deliverables

INTERVIEW_QA、PROJECT_PITCH、RESUME_EVIDENCE、模拟/真实面试反馈。

## Exit Criteria

表达与仓库事实一致；能讲 Docker与6/7DOF 全链路、需求/错误/测试；薄弱项有定向回补。

除非证据、复述和模块面试全部完成，否则不得标记 Completed。

如果为了本模块在 running container 中临时安装或修改依赖，但没有回写 Dockerfile/Compose/entrypoint 等版本化环境定义并重建验证，则模块不得 Completed。

## 模块面试范围

本模块即综合面试：环境、机器人基础、架构、控制、MoveIt、应用、调试、测试和项目。

## 新对话上下文恢复

读取 `README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、当前 module、prerequisite reports、`curriculum/DOCKER_FIRST_ARCHITECTURE.md`、`docs/ENVIRONMENT_MANIFEST.md`，以及当前项目真实 README/evidence。不得依赖上一聊天记忆。
