# ENVIRONMENT_MANIFEST

状态：Not Verified。ENV-01 中一次记录完整开发栈的真实验证值；环境没有变化时，后续模块无需重复更新。

## Host

| Item | Verified value | Evidence/date |
|---|---|---|
| Ubuntu version | Pending ENV-01 | — |
| CPU architecture | Pending ENV-01 | — |
| GPU vendor/model | Pending ENV-01 | — |
| Docker version | Pending ENV-01 | — |
| Docker Compose version | Pending ENV-01 | — |
| Host UID/GID strategy | Pending ENV-01 | — |

## ros2-dev Image

| Item | Verified value | Evidence/date |
|---|---|---|
| Base image tag | Pending ENV-01 | — |
| Base image digest（如可获得） | Pending ENV-01 | — |
| ROS_DISTRO | jazzy（待验证） | — |
| RViz2 version/package | Pending ENV-01 | — |
| Gazebo release | Pending ENV-01 | — |
| ros_gz version/package | Pending ENV-01 | — |
| ros2_control version/package | Pending ENV-01 | — |
| ros2_controllers version/package | Pending ENV-01 | — |
| Gazebo ros2_control integration | Pending ENV-01 | — |
| MoveIt2 version/package | Pending ENV-01 | — |
| Development user / UID/GID | Pending ENV-01 | — |
| Image build date | Pending ENV-01 | — |

## Environment changes after ENV-01

仅在真实缺包、版本修复或项目特定依赖导致 image 变化时记录：日期、原因、Dockerfile/Compose commit、重新构建结果和受影响模块。
