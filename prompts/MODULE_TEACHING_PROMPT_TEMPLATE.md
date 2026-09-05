# MODULE_TEACHING_PROMPT_TEMPLATE

把 `<MODULE_ID>` 替换为课程编号，在全新 ChatGPT 对话中使用。

~~~text
请连接并读取 GitHub 仓库 Mojiu13/ros2_。

我要学习的模块是：<MODULE_ID>。

开始前依次读取 README.md、LEARNING_STATUS.md、curriculum/CURRICULUM_INDEX.md、curriculum/modules/<MODULE_ID>.md、该模块 prerequisites 的真实报告、curriculum/DOCKER_FIRST_ARCHITECTURE.md、prompts/TEACHING_PROTOCOL.md、prompts/MODULE_INTERVIEW_RULES.md。

默认环境是 Ubuntu 24.04 Host + Docker + ROS2 Jazzy Container。先检查 Docker Engine、目标 container、mount、network、ROS underlay 和 workspace overlay 状态；不要假定宿主机安装 ROS。

依赖应优先写入 Dockerfile/image 或受版本管理的环境定义。为诊断而在运行中 container 临时安装时，验证后必须回写 Dockerfile/Compose/entrypoint 并重建确认。删除 container 后，源码、配置和课程证据必须仍在且环境可恢复。

GUI/GPU/hardware 问题先判断 Host、Docker、graphics、ROS、application 哪层。先识别 X11/XWayland/Wayland 和 Intel/AMD/NVIDIA，再按当前官方方案选择最小权限配置；不要盲抄 xhost 或默认 NVIDIA。纯仿真 Docker first；Native Fallback 必须有已验证限制、理由和环境差异记录。

所有版本敏感步骤优先查 ROS2 Jazzy、Gazebo、MoveIt、Docker 及 GPU vendor 的当前官方文档，不从旧教程猜测。

如果仓库与口述冲突，以真实文件、命令输出和日志为准。严格以模块文件为边界，不提前教学后续模块。

每轮只给一个可验证目标和少量命令/代码，说明观察点，然后等我贴真实输出；不得假定成功。错误先归层、收集证据、提出一个主要假设并验证，不要罗列十几种修复。

必须完成运行、观察、修改、单一故障注入、定位、修复、回归、文档、复述和模块面试。先不要给标准面试答案。

现在先报告读取文件、模块目标/边界/Exit Criteria，以及开始前缺少的可验证前提；随后只给第一小步。
~~~
