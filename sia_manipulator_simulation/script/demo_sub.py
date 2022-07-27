#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped, Pose
from sensor_msgs.msg import JointState
    
def listener():

    
    rospy.init_node('listener', anonymous=True)
    print(1)
    data= rospy.wait_for_message("/joint_states", JointState)
    print(2)
    print(data.position)
    # spin() simply keeps python from exiting until this node is stopped
    

if __name__ == '__main__':
    listener()