#!/usr/bin/env python
# license removed for brevity
import rospy
import client
import class_pid
import parameters
import time
import geometry_msgs.msg
import os
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

TWIST = Twist()
para = parameters.parameters()
ODOM = Odometry()


def recOdom(data):
    try:
        ODOM.twist.twist.linear.x = data.twist.twist.linear.x
        ODOM.twist.twist.linear.y = data.twist.twist.linear.y
        ODOM.twist.twist.angular.z = data.twist.twist.angular.z
    except:
        print("error happens in speed level setting, @PID @Twist")

def recTwist(data):

    try:
        TWIST.linear.x = data.linear.x * para.times
        TWIST.linear.y = data.linear.y * para.times
        TWIST.angular.z = data.angular.z * para.times
	
    except:
        print "error happens in speed calibration , @PID @Odometry"

if __name__ == '__main__': 
    rospy.init_node('m1',anonymous=True)
    rospy.Subscriber("cmd_vel", Twist, recTwist)
    rospy.Subscriber("odom", Odometry, recOdom)
    rate = rospy.Rate(para.monitor_rate)
    while not rospy.is_shutdown():
        a = os.system('clear')
        str1 = "ODOM___Vx: %.3f Vy: %.3f Vz: %.3f"%(ODOM.twist.twist.linear.x,ODOM.twist.twist.linear.y,ODOM.twist.twist.angular.z)
        rospy.loginfo(str1)
        str2 = "TWIST__Vx: %.3f Vy: %.3f Vz: %.3f"%(TWIST.linear.x, TWIST.linear.y, TWIST.angular.z)
        rospy.loginfo(str2)
        rate.sleep()
