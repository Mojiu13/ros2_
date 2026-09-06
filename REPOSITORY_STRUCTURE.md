# Repository Structure

~~~text
ros2_/
├── README.md
├── LEARNING_STATUS.md
├── AUDIT.md
├── core/
│   ├── CORE_INDEX.md
│   ├── APPLICATION_GATE.md
│   ├── ROLE_COMPETENCY_MATRIX.md
│   ├── EMBEDDED_SKILLS.md
│   └── modules/<CORE_ID>.md
├── dlc/
│   ├── README.md
│   ├── DLC_INDEX.md
│   └── modules/<DLC_ID>.md
├── migration/
│   └── MIGRATION_TABLE.md
├── prompts/
│   ├── CORE_TEACHING_PROMPT_TEMPLATE.md
│   ├── DLC_TEACHING_PROMPT_TEMPLATE.md
│   ├── TEACHING_PROTOCOL.md
│   └── MODULE_INTERVIEW_RULES.md
├── docker/
│   ├── Dockerfile
│   ├── compose.yaml
│   ├── entrypoint.sh
│   └── README.md
├── docs/
│   ├── ENVIRONMENT_MANIFEST.md
│   ├── MINIMUM_RESUME_EVIDENCE.md
│   ├── modules/README.md
│   ├── modules/<CORE_ID>/MODULE_REPORT.md
│   └── templates/
├── projects/
│   ├── PROJECTS.md
│   ├── project_a/
│   └── project_b/
└── src/                    # 正式学习中产生的 ROS packages
~~~

当前只创建课程、索引、报告规则和模板；运行证据、模块报告与代码必须在学习时真实产生，不预造。每个报告固定保存到 `docs/modules/<CORE_ID>/MODULE_REPORT.md`。
