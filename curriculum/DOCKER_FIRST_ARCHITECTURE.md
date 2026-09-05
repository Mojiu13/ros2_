# Docker-first ROS2 开发环境

~~~text
Ubuntu 24.04 Host
├─ Git repository / source ── bind mount ───────────────┐
├─ Docker Engine + Compose ── build/run/orchestration ─┤
├─ Desktop session (X11 / XWayland / Wayland) ─────────┤
├─ GPU driver + device/runtime (Intel/AMD/NVIDIA) ─────┤
├─ USB / serial / network devices（需要时显式授权）────┤
└─ Git + editor                                           │
                                                         ▼
ROS2 Jazzy Container
├─ /opt/ros/jazzy             ← ROS underlay
├─ /workspace/src             ← Host source bind mount（必须持久化）
├─ /workspace/build|install|log ← overlay 产物；可 bind/named volume/cache
├─ MoveIt2 + ros2_control + Gazebo ROS integration
├─ C++ / Python build and runtime dependencies
└─ RViz2 / Gazebo Sim ── display + GPU path ── Host desktop

Dockerfile ──build──> immutable image
compose.yaml ──configure──> container / mounts / network / GUI / devices
entrypoint.sh ──initialize──> ROS underlay + workspace overlay
~~~

## 边界

- Image 是可重建环境模板；container 是其运行实例。
- Bind mount 用于宿主源码；named volume 可用于缓存或构建产物，但不得成为唯一源码副本。
- `/opt/ros/jazzy` 是 underlay；工作区 `install` 是 overlay。
- 依赖变更最终写回 Dockerfile/环境定义；临时容器安装只能用于诊断。
- bridge 与 host networking 都必须基于发现实验选择；ROS_DOMAIN_ID 需要显式记录。

## GUI/GPU 决策

先检测宿主会话是 X11、XWayland 还是 Wayland，再采用当前官方、安全、最小授权方案。先识别 Intel/AMD/NVIDIA 和宿主 driver，再验证容器 OpenGL renderer，防止误把软件渲染当硬件加速。NVIDIA Container Toolkit 只在实际为 NVIDIA 且官方步骤要求时使用。

## Native Fallback

纯仿真默认 Docker。只有 GUI/GPU、USB/serial/camera/CAN/EtherCAT、vendor SDK、实时内核等出现已验证限制时才允许 native；必须记录证据、理由、环境差异和回归方式，不能因为不会配置 Docker 而跳过。
