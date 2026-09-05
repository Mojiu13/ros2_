# ENVIRONMENT_MANIFEST

状态：Not Verified。ENV-01 开始后填写真实值；不得猜测。

## Host

| Item | Verified value | Evidence/date |
|---|---|---|
| Ubuntu version | Pending ENV-01 | — |
| CPU architecture | Pending ENV-01 | — |
| GPU vendor/model | Pending ENV-01 | — |
| Docker version | Pending ENV-01 | — |
| Docker Compose version | Pending ENV-01 | — |
| Host UID/GID strategy | Pending ENV-01 | — |

## Container / Image

| Item | Verified value | Evidence/date |
|---|---|---|
| Base image tag | Pending ENV-01 | — |
| Base image digest（如可获得） | Pending ENV-01 | — |
| ROS_DISTRO | jazzy（待 ENV-01 验证） | — |
| Development user / UID/GID | Pending ENV-01 | — |
| Image build date | Pending ENV-01 | — |

## Just-In-Time dependency evolution

| Stage/module | Added capability | Package/release/version | Image identifier | Verification |
|---|---|---|---|---|
| ENV-01 | ROS2 base development | Pending | Pending | Pending |
| ROS-01/02/03 | ROS package/interface development | Pending | Pending | Pending |
| SYS-01 | Reference runtime / RViz if needed | Pending | Pending | Pending |
| SIM-01 | Gazebo Sim / ros_gz / graphics | Pending | Pending | Pending |
| CTRL-01 | ros2_control / ros2_controllers / Gazebo integration | Pending | Pending | Pending |
| MOVEIT-01 | MoveIt2 development dependencies | Pending | Pending | Pending |

不要 pin 每个 Ubuntu 包；记录足以回答“项目在哪套环境验证过”的关键版本、镜像和证据。
