# sia_manipulator_simulation

6自由度协作机械臂的Gazebo仿真
## 存在的问题

1.机械臂没有加关节角度限制
2.机械臂目前使用的是最简单的joint_state_controller

## 改进方向
1.模仿UR的仿真模型进行关节约束以及控制器的更换
2.编写简单的节点发送关节信息，控制机械臂运动
