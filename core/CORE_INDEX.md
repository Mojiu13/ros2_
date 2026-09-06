# CORE INDEX

判断标准不再只是“它是不是 ROS 主技能”，而是：

- 是否完成当前模块和验收所必需；
- 是否用于解释现象、排错或理解完整链路；
- 是否会在未来 1–2 个模块复用；
- 是否是第一份 ROS2 机械臂岗位的常见基础。

满足任一且不可安全跳过的内容，作为 **CORE Supporting Knowledge** 教到 Minimum Sufficient Depth。只有完全跳过也不阻塞主线的深化内容才进入 DLC。

## CORE TO APPLY

| 顺序 | Module | 名称 | Prerequisites | 工作量 |
|---:|---|---|---|---|
| 1 | [ENV-01](modules/ENV-01.md) | 完整 Dockerized ROS2 Jazzy 开发环境 | C++ / Python 基础；基本 Ubuntu 使用 | L |
| 2 | [ROS-01](modules/ROS-01.md) | ROS 2 计算图、接口与 CLI | ENV-01 | M |
| 3 | [ROS-02](modules/ROS-02.md) | C++ / Python ROS 包与最小通信编程 | ROS-01 | L |
| 4 | [ROS-03](modules/ROS-03.md) | Launch、Parameter、YAML、Namespace 与 Remap | ROS-02 | M |
| 5 | [SYS-01](modules/SYS-01.md) | 参观 6/7 DOF 完整机械臂系统 | ROS-03 | S |
| 6 | [MODEL-01](modules/MODEL-01.md) | MiniArm URDF、Xacro、TF 与 RViz | SYS-01 | L |
| 7 | [SIM-01](modules/SIM-01.md) | MiniArm Gazebo Sim 基础 | MODEL-01 | M |
| 8 | [CTRL-01](modules/CTRL-01.md) | ros2_control 与 Controller 最小闭环 | SIM-01 | L |
| 9 | [CTRL-02](modules/CTRL-02.md) | Direct FollowJointTrajectory 与 A2 控制基线 | CTRL-01 | L |
| 10 | [MOVEIT-01](modules/MOVEIT-01.md) | A2 MoveIt2 配置与 RViz Plan/Execute | CTRL-02 | L |
| 11 | [MOVEIT-02](modules/MOVEIT-02.md) | A2 C++ / Python 编程规划执行 | MOVEIT-01 | L |
| 12 | [INT-01](modules/INT-01.md) | 6/7 DOF 完整系统集成 | MOVEIT-02 | M |
| 13 | [APP-01A](modules/APP-01A.md) | 最小需求、Task.action 与 Server 骨架 | INT-01 | M |
| 14 | [APP-01B](modules/APP-01B.md) | MoveIt TaskNode 与基本状态机 | APP-01A | L |
| 15 | [APP-02A](modules/APP-02A.md) | Cancel、Timeout 与明确错误传播 | APP-01B | M |
| 16 | [DBG-01](modules/DBG-01.md) | 五类高频故障核心包 | APP-02A | M |
| 17 | [DELIVERY-01](modules/DELIVERY-01.md) | 最低测试、文档与项目交付 | DBG-01 | L |

完成 `DELIVERY-01` 并通过 [APPLICATION_GATE](APPLICATION_GATE.md) 后立即开始投递。顺序没有变化，DLC 不是 prerequisite。

## CORE AFTER APPLY

| Module | 名称 | Prerequisites | 工作量 |
|---|---|---|---|
| [JOB-01](modules/JOB-01.md) | 投递期项目表达与面试闭环 | DELIVERY-01；Application Gate 已通过并已开始投递 | M |

投递期间继续 JOB-01，并按真实反馈选择 DLC；不得因为 DLC 未完成而延迟投递。

## 每模块完成定义

`practice + real evidence + report + interview` 缺一不可。报告固定落到 `docs/modules/<MODULE_ID>/MODULE_REPORT.md`，随后更新 `LEARNING_STATUS.md` 并形成一次合理 commit。
