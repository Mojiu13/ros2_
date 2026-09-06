# Final Audit｜CORE Supporting Knowledge Boundary

| 检查项 | 结果 | 依据 |
|---|---|---|
| Docker 基础是否足够理解环境 | Pass | ENV-01 明确 Host/container、image/container、Dockerfile、Compose、bind mount、workspace、source、rebuild、non-root 与 UID/GID。 |
| Linux 基础是否足够继续排错 | Pass | EMBEDDED_SKILLS + ENV-01/ROS-01/DBG-01 覆盖文件、检索、环境、进程、权限、apt 和证据使用。 |
| Git 基础是否贯穿开发 | Pass | status/diff/add/commit/log/branch/switch/restore/.gitignore 纳入 CORE；每完成一模块一次合理 commit。 |
| CMake/ament 是否真正理解最低用法 | Pass | ROS-02 覆盖 package.xml、CMakeLists、find_package、add_executable、依赖、ament_target_dependencies、install 与 rosidl。 |
| ROS middleware 最低直觉是否保留 | Pass | ROS-01 保留 DDS/middleware、discovery、ROS_DOMAIN_ID 和 host/container 发现边界。 |
| TF/pose/frame 数学直觉是否足够 | Pass | MODEL-01 覆盖 pose + frame、transform、base/tool frame、RPY/quaternion 用法、PoseStamped/frame_id 和 FK 直觉。 |
| Gazebo 最低物理知识是否足够 | Pass | SIM-01 覆盖 visual/collision/inertial、mass/inertia、damping/friction/gravity 与典型物理现象。 |
| ros2_control 闭环直觉是否足够 | Pass | CTRL-01/02 明确 interface、manager/controller/broadcaster、lifecycle、JointTrajectory/FJT 与命令—反馈闭环。 |
| MoveIt FK/IK/workspace 基础是否足够 | Pass | MOVEIT-01/02 保留 group/end effector/start/goal、FK/IK、可达性、workspace、limits、collision、PlanningScene 和奇异性直觉。 |
| APP 软件工程基础是否足够 | Pass | APP-01A/B、APP-02A 覆盖 requirement、acceptance、contract、validation、state machine、terminal state、cancel/timeout/deadline 与错误传播。 |
| Debugging 方法是否足够 | Pass | DBG-01 要求完整证据链、控制变量、单假设验证与回归，不只列五个答案。 |
| Testing 基础是否足够 | Pass | DELIVERY-01 要求 test case 结构、normal/boundary/failure/regression、6–10 cases 与 1–3 smoke tests。 |
| Documentation 基础是否足够 | Pass | DELIVERY-01 要求 README 受众、架构图、接口、需求摘要、测试报告、限制和复现步骤，并能解释写法。 |
| 是否还存在把必要知识错误扔进 DLC | Pass | 协议与每模块明确 Required Supporting Knowledge 优先于 DLC LOCK。 |
| 是否仍然避免了 Rabbit Hole | Pass | 深度限定为 Minimum Sufficient Depth；高级工具、数学、源码、实时、测试和文档体系仍在 DLC。 |
| CORE dependency 是否仍然连贯 | Pass | 18 个 Module 的顺序、Prerequisites 和 Application Gate 位置未变。 |
| Module Report 跨聊天闭环 | Pass | 所有 CORE 强制固定路径报告；状态表、协议、提示词、面试规则和 Gate 一致执行。 |

结论：CORE 已包含走通主线所需的必要辅助知识；DLC 仅保留非阻塞深化内容。
