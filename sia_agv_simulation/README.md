# sia_agv_simulation

移动平台AGV的Gazebo仿真

![sia_agv_simulation](./sia_agv_simulation.gif)

## 运行

运行Gazebo仿真环境

```bash
$ cd /your/ros/workspace
$ catkin_make
$ source devel/setup.bash
$ roslaunch sia_agv_simulation sia_agv_sim_on_gazebo.launch
```

让小车旋转起来

```bash
$ rostopic pub /sia_agv/cmd_vel geometry_msgs/Twist '[0, 0, 0]' '[0, 0, 1]'
```
