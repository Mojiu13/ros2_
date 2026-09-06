# CORE / DLC 重构审计

- 主线是否最短：Pass。17 个 Gate 前模块均直接支撑下一步或最低岗位证据。
- Docker 是否喧宾夺主：Pass。只在 ENV-01 集中处理。
- Linux/Git/CMake 是否 Just-In-Time：Pass。作为 Embedded Skills。
- Network/DDS 是否过度：Pass。CORE 只保留发现直觉；实验/内部进入 DLC。
- GPU/Graphics 是否过度：Pass。正常不研究；真实问题触发 DLC。
- Test 是否过度：Pass。CORE 仅 6–10 cases、1–3 smoke tests。
- Documentation 是否过度：Pass。CORE 仅最低可复现交付。
- Robotics theory 是否过度：Pass。CORE 只保留使用直觉。
- Controller/MoveIt 核心是否被误删：Pass。interfaces、FJT、A2 baseline、SRDF、三类目标和编程闭环完整。
- 所有被删内容是否进入 DLC：Pass。见 migration/MIGRATION_TABLE.md。
- Application Gate 是否需要 DLC：Pass。Gate 明确禁止 DLC prerequisite。

结论：CORE / DLC 边界通过审计。
