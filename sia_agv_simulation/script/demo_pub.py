#!/usr/bin/env python
#简单的向前走1m,开发中，后续尝试复现动态窗口算法
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist


def talker():
    pub = rospy.Publisher('/sia_agv/cmd_vel', Twist, queue_size=1)
    rospy.init_node('talker', anonymous=True)
    i=0
    rate=50
    # rate = rospy.Rate(10) # 10hz
    # 
    r=rospy.Rate(rate)
    linear_speed=0.2
    cmd_vel= Twist()
    goal_diatance=1
    linear_duration=goal_diatance/linear_speed
    ticks=int(linear_duration*rate)
    cmd_vel.linear.x=linear_speed
    for i in range(ticks):
        rospy.loginfo(cmd_vel)
        pub.publish(cmd_vel)
        r.sleep()
    cmd_vel.linear.x=0
    pub.publish(cmd_vel)
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass