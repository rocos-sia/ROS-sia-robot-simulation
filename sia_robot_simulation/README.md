# sia_robot_simulation

移动复合机器人的Gazebo仿真

## 前提准备
### 1.利用传递参数，让模型处于自己希望的位置
### 前提：base_link中添加  <kinematic>1</kinematic>（不然模型会被拉回来）
gazebo启动后可以运行下面的指令更改模型位置
rosservice call gazebo/set_link_state '{link_state: {link_name: base_link, pose: {position: {x: 0, y: 0, z: 1.2}}}}'

### 2.利用cmd/vel话题发布速度指令，指令如下
机器人转圈
rostopic pub -r 10 /cmd_vel geometry_msgs/Twist '{linear: {x: 0, y: 0, z: 0}, angular: {x: 0, y: 0, z: 0.5}}'
机器人直行：
rostopic pub -r 10 /cmd_vel geometry_msgs/Twist '{linear: {x: 0.5, y: 0, z: 0}, angular: {x: 0, y: 0, z: 0}}'
### 3.生成urdf树状图
urdf_to_graphiz sia_717.urdf.xacro
### 4.ROS中提供了一个比较好用的键盘控制功能包: ros-noetic-teleop-twist-keyboard，该功能包，可以控制机器人的运动(重点是消息类型)
安装指令：
sudo apt install ros-noetic-teleop-twist-keyboard
话题：/cmd_vel
运行：rosrun teleop_twist_keyboard teleop_twist_keyboard.py
     rosrun teleop_twist_keyboard teleop_twist_keyboard.py _speed:=0.9 _turn:=0.8
     rosrun teleop_twist_keyboard teleop_twist_keyboard.py cmd_vel:=my_cmd_vel(发布在不同的话题上)
     rosrun teleop_twist_keyboard teleop_twist_keyboard.py _repeat_rate:=10.0(发布的重复频率)
     rosrun teleop_twist_keyboard teleop_twist_keyboard.py _key_timeout:=0.6(按键超时:如果在 0.6 秒内未收到按键，则停止机器人)
### 5.teleop_twist_keyboard详细介绍
http://wiki.ros.org/teleop_twist_keyboard
### 6.源码安装
https://github.com/ros-teleop/teleop_twist_keyboard
## 指令运行
### 环境配置
mkdir ${name}/src
cd ${name}
catkin build/catkin_make
source ./devel/setup.bash
### gazebo启动
roslaunch sia_agv3 demo.launch
### rviz启动
roslaunch sia_agv3 demo1.launch

