# JOB-01｜项目答辩、简历证据与综合模拟面试

> Phase 4 · P0 · 工作量 M

## 为什么学习

在已经开始投递的基础上，把完整测试/文档证据转成可信求职表达，并吸收真实面试反馈。

## Prerequisites

DOC-01

## 环境要求

默认使用 ENV-01 已构建并验收的完整 `ros2-dev` image；不假定 Host 安装 ROS。正常情况下只启动主 development container、进入容器并确认本模块所需 package 可用，然后直接开始 ROS/机器人软件学习。只有实际缺包、版本冲突或新增项目特定依赖时才修改环境定义、重建并更新 `docs/ENVIRONMENT_MANIFEST.md`。

## 开始时检查

[HOST] 如主环境未运行，启动既有 Compose 项目。[CONTAINER] 确认 workspace/source mount、ROS underlay、workspace overlay和本模块 prerequisite evidence；检查本模块所需 package 可用。环境正常时不重新审计 Docker。

Application Gate 已达成；TEST-01 与 DOC-01 完成；不得包装未实现功能。

## 核心实践任务

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

如果实际修改了运行环境，或为诊断在 running container 中临时安装了依赖，必须回写 Dockerfile/Compose/entrypoint、重建验证并更新 `docs/ENVIRONMENT_MANIFEST.md`；否则模块不得 Completed。

## 模块面试范围

本模块即综合面试：环境、机器人基础、架构、控制、MoveIt、应用、调试、测试和项目。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、当前 module、prerequisite reports、Docker architecture、ENVIRONMENT_MANIFEST 和当前项目真实 README/evidence。ENV-01 完成后默认环境稳定；除非出现容器、权限、GUI、缺包、污染或版本冲突，不重新展开 Docker 教学。
