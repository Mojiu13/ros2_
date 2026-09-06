# ROS2 机械臂应用开发｜CORE + DLC 学习仓库

唯一目标：让具备 C++ / Python 基础、ROS / 机器人接近零基础的学习者，尽快达到第一份 ROS2 机械臂应用开发岗位的可项目、可排错、可面试水平。现在只设计并维护课程体系；具体教学从 `ENV-01` 另行开始。

## 三层知识结构

1. **CORE Skill**：ROS2 与机械臂应用开发主技能。
2. **CORE Supporting Knowledge**：完成实践、排错、理解后续模块和应对第一份岗位常见面试所必需的辅助知识。
3. **DLC**：完全跳过也不会阻塞 CORE 的深化内容。

因此不是“ROS = CORE、其他 = DLC”。例如 CMake 基础、quaternion 用法、controller lifecycle 和 expected/actual test case 都属于 CORE Supporting Knowledge；高级 CMake、quaternion 代数、controller 实时内部和完整测试架构才属于 DLC。

## CORE 成功链

~~~text
完整开发环境
→ ROS2 graph / communication / programming
→ Launch / YAML / Parameter
→ 参观完整 6/7 DOF 系统
→ MiniArm URDF / TF / RViz
→ Gazebo
→ ros2_control
→ Direct FollowJointTrajectory + A2 controller baseline
→ MoveIt2 RViz + programming
→ 6/7 DOF integration
→ TaskNode
→ Cancel / Timeout / Error
→ 五类高频故障
→ 最低测试与文档交付
→ Application Gate
→ 立即投递
~~~

CORE 顺序与 18 个 Module 均已冻结；17 个 Gate 前模块 + 1 个投递后模块。DLC 不参与 CORE completion、Application Gate 或开始投递。

## Anti-Rabbit-Hole Rule

遇到看似辅助的主题时，依次判断：

1. 不理解它是否会导致复制粘贴、无法排错、阻塞未来 1–2 个模块、遗漏第一份岗位高频问题，或破坏系统链路理解？任一为“是”，它就是 CORE Supporting Knowledge。
2. 在当前实践中讲到 **Minimum Sufficient Depth**，并通过观察、修改或故障证据确认理解。
3. 只有完全跳过也不阻塞 CORE 的更深内容，才记录 `DLC_REF: <DLC_ID>` 并返回主线。

实践占主导是方向，不是 80–90%/10–20% 的死配额。必要支撑知识不得为了满足比例被强行省略。

## CORE 完成闭环

每个 CORE 只有在以下四项都完成后才能标记 `Completed`：

~~~text
practice + real evidence + docs/modules/<MODULE_ID>/MODULE_REPORT.md + interview
~~~

同时更新 `LEARNING_STATUS.md`，并形成一次范围合理的 Git commit。报告模板见 `docs/templates/MODULE_REPORT.md`。

## 入口

- [CORE 索引](core/CORE_INDEX.md)
- [Embedded Skills](core/EMBEDDED_SKILLS.md)
- [Application Gate](core/APPLICATION_GATE.md)
- [DLC 索引](dlc/DLC_INDEX.md)
- [CORE 教学提示词](prompts/CORE_TEACHING_PROMPT_TEMPLATE.md)
- [Teaching Protocol](prompts/TEACHING_PROTOCOL.md)
- [迁移表](migration/MIGRATION_TABLE.md)

Docker 在 ENV-01 一次建立稳定基础设施；Linux、Git、CMake/ament、YAML、CLI/日志和基础排错作为 Required Supporting Knowledge 随任务掌握。高级工具和内部机制仍留在 DLC。

范围外：强化学习、Isaac Lab、灵巧手、视觉伺服、触觉、CUDA/TensorRT、具身智能和高级控制算法。除非目标岗位改变，不进入 CORE。
