# GitHub 新目录结构

当前仍只维护课程设计和空白模板；正式学习时才生成真实代码、环境与证据。

~~~text
ros2_/
├── README.md
├── AUDIT.md
├── LEARNING_STATUS.md
├── REPOSITORY_STRUCTURE.md
├── docker/
│   ├── Dockerfile                 # ENV-01 中创建
│   ├── compose.yaml               # mounts/network/GUI/GPU/devices
│   ├── entrypoint.sh              # source underlay/overlay
│   └── README.md                  # 架构、构建、重建、Fallback
├── curriculum/
│   ├── CURRICULUM_INDEX.md
│   ├── ROLE_COMPETENCY_MATRIX.md
│   ├── TRACKS.md
│   ├── APPLICATION_GATE.md
│   ├── DOCKER_FIRST_ARCHITECTURE.md
│   └── modules/<MODULE_ID>.md
├── prompts/
│   ├── MODULE_TEACHING_PROMPT_TEMPLATE.md
│   ├── TEACHING_PROTOCOL.md
│   └── MODULE_INTERVIEW_RULES.md
├── docs/
│   ├── templates/
│   ├── modules/<MODULE_ID>/
│   ├── ENVIRONMENT_MANIFEST.md
│   ├── MINIMUM_RESUME_EVIDENCE.md   # Application Gate 时生成
│   ├── SYSTEM_MAP.md
│   ├── COMMAND_CHEATSHEET.md
│   ├── ERROR_LOG.md
│   ├── INTERVIEW_QA.md
│   └── templates/MINIMUM_RESUME_EVIDENCE.md
├── projects/
│   ├── PROJECTS.md
│   ├── project_a/
│   │   ├── a1_miniarm_learning/
│   │   └── a2_full_manipulator/
│   └── project_b_task_executor/
├── src/                           # 宿主持久化源码，bind mount 到 container workspace
└── test_reports/
~~~

## 持久化规则

- `src/` 和所有 Git 文件必须位于宿主仓库；container 删除不影响源码。
- build/install/log 可选择 bind mount、named volume 或可丢弃重建策略，但必须记录。
- 默认一个主 ros2-dev container；ROS-01 可临时启动第二个做 discovery 实验，不做微服务拆分。
- 依赖按阶段演化并回写 Dockerfile/Compose/entrypoint；不把手工改过的 container 当环境定义。
- Container development user 与 Host UID/GID 合理映射，避免 root-owned 文件。
- 每个 Project README 最终提供 clone→image→container→workspace build→launch 的复现链。
