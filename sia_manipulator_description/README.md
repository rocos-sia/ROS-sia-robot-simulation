# sia_manipulation_description

6自由度协作机械臂的URDF描述文件

## 运行

```bash
$ cd /your/ros/workspace
$ catkin_make
$ source devel/setup.bash
$ roslaunch sia_manipulator_description sia_manipulator_description_rviz.launch or roslaunch sia_manipulator_description sia_manipulator_description_rviz.launch

```
## 夹爪和摄像头
1.摄像头和夹爪的描述文件都在urdf目录下，其中realsense摄像头的描述文件固定，而robotiq_2f_85的描述文件有两份，其中一份来自官方文件的更改，一份来自github网络作者，两份在对夹爪的描述上有一定的差别，官方文件更加细致。目前运行成功的是来自github的描述文件，但是描述不太细致。
## 简单抓取实验

```bash
$ cd /your/ros/workspace
$ catkin_make
$ source devel/setup.bash
$ roslaunch sia_manipulator_description sia_manipulator_description_rviz.launch or roslaunch sia_manipulator_description sia_force_sensor.launch

```
