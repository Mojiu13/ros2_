# CORE / DLC 模块面试规则

## CORE 面试

每个 CORE 结束前问 5–8 题，覆盖：

- Core Skill 的概念边界与系统角色；
- Required Supporting Knowledge 如何服务当前任务；
- CLI / log / graph / TF / controller state 等真实证据；
- 故障的 layer、hypothesis、verification、root cause、fix 与 regression；
- 当前 deliverables 的项目表达。

先出题，学习者回答；基于回答指出概念、证据和表达漏洞；要求重答；最后才整理标准答案。不能只会背定义，必须能把辅助知识用于解释当前模块的现象。

不得追问 DLC 深度，例如 DDS/RTPS/executor internals、quaternion/DH/Jacobian 推导、controller realtime/source、Docker internals、完整测试/文档体系或 OMPL 内部。但这些主题在 CORE 中列出的最低使用直觉仍属于面试范围。

## DLC 面试

只有明确进入并完成某 DLC 后，才在其独立记录中提问；DLC 成绩不影响 CORE completion 或 Application Gate。

## 完成

只有以下内容全部存在且与真实项目一致，模块才可标记 `Completed`：

`practice + real evidence + docs/modules/<MODULE_ID>/MODULE_REPORT.md + interview`

报告写入 interview result，随后更新 `LEARNING_STATUS.md` 并形成一次范围合理的 Git commit。缺一项保持 `In Progress`。
