# Migration Table｜旧路线到 CORE / DLC

| 原模块 / 知识点 | 新位置 |
|---|---|
| ENV-01 最小 Docker 知识与完整 image | CORE `ENV-01` |
| Docker 多 container/network/native/device/GPU 深化 | `DLC-ENV-ADV`, `DLC-ROS-NETWORK`, `DLC-SIM-GRAPHICS` |
| ROS-01 graph/topic/service/action/CLI | CORE `ROS-01` |
| ROS-01 bridge/host、Container A/B 网络实验 | `DLC-ROS-NETWORK` |
| ROS-02 C++/Python/custom interface/最小通信 | CORE `ROS-02` |
| ROS-03 launch/YAML/parameter/namespace/remap | CORE `ROS-03` |
| 高级 Linux/Git/CMake | `DLC-TOOLS`；基础操作为 Embedded Skills |
| SYS-01 完整系统观察 | CORE `SYS-01`（削为 S，只参观终点） |
| MODEL-01 最低机器人学、URDF/TF/RViz | CORE `MODEL-01` |
| MODEL-02 mesh/mimic/Xacro architecture/model validation | `DLC-MODEL-ENGINEERING` |
| quaternion/rotation/DH/Jacobian/dynamics | `DLC-ROBOT-MATH` |
| SIM-01 spawn/stability/collision/inertial/2–3 参数实验 | CORE `SIM-01` |
| Gazebo physics/sensors/world/diagnostics | `DLC-SIM` |
| GPU/renderer/Mesa/EGL/GLX | `DLC-SIM-GRAPHICS` |
| CTRL-01 interfaces/controllers/minimal lifecycle | CORE `CTRL-01` |
| CTRL-02 FJT + A1/A2 direct baseline | CORE `CTRL-02` |
| CTRL-03 rates/tolerances/switching/gripper/multiple controllers | `DLC-CONTROL` |
| ADV-01 JTC source/realtime | `DLC-CONTROL-LOWLEVEL` |
| ADV-02 custom controller/mock hardware | `DLC-CONTROL-LOWLEVEL` |
| MOVEIT-01/02 配置、RViz、三类目标、C++/Python、简单 obstacle | CORE `MOVEIT-01/02` |
| MOVEIT-03 advanced PlanningScene/constraints/trajectory/parameters | `DLC-MOVEIT` |
| OMPL/MoveIt internals/trajectory optimization | `DLC-MOVEIT-INTERNALS` |
| ADV-03 运动学深化 | `DLC-ROBOT-MATH`；规划比较到 `DLC-MOVEIT` |
| INT-01 完整集成 | CORE `INT-01` |
| APP-01A 小规模需求与接口 | CORE `APP-01A`（限制为 5–10 FR、2–4 NFR） |
| APP-01B TaskNode/状态机/错误区分 | CORE `APP-01B` |
| APP-02A cancel/timeout/error propagation | CORE `APP-02A` |
| APP-02B retry/replan/recovery | `DLC-APP-RECOVERY` |
| DBG-01 五类高频故障 | CORE `DBG-01` |
| Docker/network/graphics/复合/性能排障 | `DLC-ENV-ADV`, `DLC-ROS-NETWORK`, `DLC-SIM-GRAPHICS`, `DLC-DEBUG` |
| TEST-01 最低 case/smoke evidence | CORE `DELIVERY-01` |
| TEST-01 完整 pytest/gtest/launch_testing/regression/CI | `DLC-TEST` |
| DOC-01 最低 README/design/diagram/report | CORE `DELIVERY-01` |
| DOC-01 traceability/ADR/change/formal plans | `DLC-DOC` |
| JOB-01 30秒/3分钟、核心问答、debug stories | CORE AFTER APPLY `JOB-01` |
| 大规模面试/压力题/系统设计 | `DLC-JOB` |
| ROS-04 QoS/Lifecycle/composition | `DLC-ROS-RUNTIME` |
| DDS/executor/middleware internals | `DLC-ROS-MIDDLEWARE` |
| 真机 vendor/总线/校准/安全边界 | `DLC-HARDWARE` |

结论：旧知识全部有 CORE 或 DLC 归宿，没有直接丢弃。
