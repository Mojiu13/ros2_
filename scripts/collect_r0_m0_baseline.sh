#!/usr/bin/env bash
set -u

OUTPUT_DIR="r0_m0_baseline_logs"
TIMESTAMP="$(date +%Y%m%d_%H%M%S)"
OUTPUT_FILE="${OUTPUT_DIR}/baseline_${TIMESTAMP}.md"

mkdir -p "${OUTPUT_DIR}"

run_cmd() {
  local title="$1"
  local cmd="$2"

  {
    echo "## ${title}"
    echo
    echo '```bash'
    echo "${cmd}"
    echo '```'
    echo
    echo '```text'
    bash -lc "${cmd}" 2>&1 || true
    echo '```'
    echo
  } >> "${OUTPUT_FILE}"
}

{
  echo "# R0-M0 Baseline Log"
  echo
  echo "Generated at: ${TIMESTAMP}"
  echo
} > "${OUTPUT_FILE}"

run_cmd "OS information" "lsb_release -a"
run_cmd "Kernel" "uname -a"
run_cmd "ROS distro" "printenv ROS_DISTRO"
run_cmd "ros2 path" "which ros2"
run_cmd "ROS2 nodes" "ros2 node list"
run_cmd "ROS2 topics" "ros2 topic list"
run_cmd "ROS2 actions" "ros2 action list"
run_cmd "ROS2 services" "ros2 service list"
run_cmd "ros2_control controllers" "ros2 control list_controllers"
run_cmd "ros2_control hardware interfaces" "ros2 control list_hardware_interfaces"
run_cmd "move_group parameters" "ros2 param list /move_group"

echo "Baseline written to: ${OUTPUT_FILE}"
