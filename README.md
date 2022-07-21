# ROS-sia-robot-simulation

:warning:Unfinished~

此代码仓库为中国科学院沈阳自动化研究所机器人学研究室承担的无人实验室自主操作项目的基于ROS仿真场景，采用了移动复合机器人来实现无人实验室中的相关作业任务（试管取放、离心机操作、烘干机操作等），代码目前仍在开发当中。

## 软件包介绍

本项目包含以下软件包(仍在开发中)：

| 软件包名称  | 内容  |
|    ----    | -------  |
| ros_sia_robot_simulation | Metapackage元包，依赖所有package |
| sia_agv_description      | 移动平台AGV的URDF描述文件 |
| sia_agv_simulation       | 移动平台AGV的Gazebo仿真 |
| sia_manipulator_description | 协作机械臂的URDF描述文件 |
| sia_manipulator_simulation | 协作机械臂的Gazebo仿真 |
| sia_robot_description | 移动复合机器人的URDF描述文件 |
| sia_robot_simulation  | 移动复合机器人的Gazebo仿真 |

## 环境

- Ubuntu 20.04
- ROS noetic

## 作者

- 罗阳 luoyang@sia.cn
- 孙锦程 jcsun@sia.cn
- 吴昊 wuhao@sia.cn
