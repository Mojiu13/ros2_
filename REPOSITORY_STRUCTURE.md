# GitHub 新目录结构

当前提交只创建课程设计与空白模板；真正教学开始后再按模块生成代码和证据，不预造空项目成果。

~~~text
ros2_/
├── README.md
├── AUDIT.md
├── LEARNING_STATUS.md
├── REPOSITORY_STRUCTURE.md
├── curriculum/
│   ├── CURRICULUM_INDEX.md
│   ├── ROLE_COMPETENCY_MATRIX.md
│   ├── TRACKS.md
│   └── modules/<MODULE_ID>.md
├── prompts/
│   ├── MODULE_TEACHING_PROMPT_TEMPLATE.md
│   ├── TEACHING_PROTOCOL.md
│   └── MODULE_INTERVIEW_RULES.md
├── docs/
│   ├── templates/
│   ├── modules/<MODULE_ID>/MODULE_REPORT.md
│   ├── SYSTEM_MAP.md
│   ├── COMMAND_CHEATSHEET.md
│   ├── ERROR_LOG.md
│   └── INTERVIEW_QA.md
├── projects/
│   ├── PROJECTS.md
│   ├── project_a_sim_stack/
│   │   ├── README.md
│   │   ├── design/
│   │   ├── evidence/
│   │   ├── test/
│   │   └── src/
│   └── project_b_task_executor/
│       ├── README.md
│       ├── design/
│       ├── evidence/
│       ├── test/
│       └── src/
├── src/                         # 教学中形成的 ROS packages
└── test_reports/                # 有版本与日期的最终测试报告
~~~

## 记录规则

- 课程定义只放 `curriculum/`，不得混入运行日志。
- 每个模块的证据放 `docs/modules/<MODULE_ID>/`，并从 LEARNING_STATUS 链接。
- 可复用源码放 `src/`；项目 README 只引用真实包，不复制代码。
- 原始日志/截图放项目 evidence，摘要写模块报告；大文件避免直接进入 Git。
- TEST_PLAN 可持续维护；每次 TEST_REPORT 固定版本、环境和日期。
- 所有“完成”必须有链接，不能只改状态文本。
