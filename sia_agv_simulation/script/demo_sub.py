#!/usr/bin/env python
#得到odom实时位置（需要tf变换到base_link)
import rospy
from geometry_msgs.msg import PoseStamped, Pose
from nav_msgs.msg import Odometry
    
def listener():

    
    rospy.init_node('listener', anonymous=True)
    data= rospy.wait_for_message("/sia_agv/odom", Odometry)
    print(data.pose.pose.position.x)
    # spin() simply keeps python from exiting until this node is stopped
    

if __name__ == '__main__':
    listener()