# Docker-first ROS2 开发环境

## 默认拓扑：一个主开发容器

~~~text
Ubuntu 24.04 Host
├─ Git repository / source ── bind mount ───────────────┐
├─ Docker Engine + Compose                              │
├─ Desktop + GPU driver（模块需要时）───────────────────┤
└─ Git + editor                                         │
                                                        ▼
ros2-dev development container（主容器）
├─ non-root development user（匹配 Host UID/GID）
├─ /opt/ros/jazzy              ← ROS underlay
├─ /workspace/src              ← Host source bind mount
├─ /workspace/install          ← workspace overlay
├─ build / log                 ← 可重建或可选 volume
└─ 随课程逐步加入 RViz/Gazebo/ros2_control/MoveIt/application
~~~

ROS-01 为网络发现实验可以临时启动第二个 container；课程不把 MoveIt、Gazebo、controller、TaskNode、RViz 强制拆成微服务容器，也不引入 Kubernetes。

## Image 逐步演化

~~~text
Stage 1  ENV-01   ROS2 Jazzy base development
   ↓
Stage 2  ROS-01/02/03   ROS package + interface development
   ↓
Stage 3  SYS-01/SIM-01  RViz runtime + Gazebo Sim + ros_gz + graphics
   ↓
Stage 4  CTRL-01        ros2_control + ros2_controllers + Gazebo integration
   ↓
Stage 5  MOVEIT-01      MoveIt2 development dependencies
~~~

这表示项目 image/environment definition 随课程演化，不要求创建五个永久 image，也不在 Day 1 安装全部机器人软件。每次依赖变化必须进入 Dockerfile/Compose/entrypoint 等版本化定义，重建并写入环境清单。

## 边界与复现

- Image 是模板，container 是运行实例；bind mount 保存宿主源码，named volume 可存缓存但不能成为唯一源码副本。
- Container 默认使用与 Host UID/GID 合理映射的 non-root development user，防止 workspace 出现大量 root-owned 文件。
- 临时 `docker exec`/`apt install` 仅可诊断，最终必须回写并重建。
- 命令位置容易混淆时显式标注 `[HOST]` 或 `[CONTAINER]`。
- 纯仿真 Docker-first；Native Fallback 需实际限制、理由、差异和回归记录。

## GUI/GPU 的 Just-In-Time 时机

ENV-01 只记录 GPU vendor，简单 GUI smoke test 可选且不构成 blocker。SYS-01 首次需要 RViz 时配置必要显示通道。SIM-01 才正式验证 Gazebo GUI、OpenGL renderer、hardware acceleration、GPU vendor 对应方案与 software rendering detection。
