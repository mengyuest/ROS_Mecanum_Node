#!/usr/bin/env python
# license removed for brevity
import client
import rospy
import parameters
import class_pid
import os
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from std_msgs.msg import String

global_vel = Twist()
para = parameters.parameters()
pid_x = class_pid.class_pid()
pid_y = class_pid.class_pid()
pid_z = class_pid.class_pid()



def setLevel(data):
#update the Twist but not pub now (with a rate defined in main())  
    try:
        print"ACCEPT VELOCITY~~~~~~~~~~~~~~~~~~~~~~ \n \n"
        pid_x.init(data.linear.x * para.times)
        pid_y.init(data.linear.y * para.times)
        pid_z.init(data.angular.z * para.times)
    except:
        print("error happens in speed level setting, @PID @Twist")

def fixSpeed(data):

    try:
        print"RECEIVE ODOM~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n \n "
        global_vel.linear.x = pid_x.cal(data.twist.twist.linear.x)
        global_vel.linear.y = pid_y.cal(data.twist.twist.linear.y)
        global_vel.angular.z = pid_z.cal(data.twist.twist.angular.z)	
	
    except:
        print "error happens in speed calibration , @PID @Odometry"

if __name__ == '__main__': 
    #try:
#        client.send("EnableSystem"
    rospy.init_node('mesosphere_twist',anonymous=True)
    rospy.Subscriber("cmd_vel", Twist, setLevel)
    rospy.Subscriber("odom", Odometry, fixSpeed)
    rate = rospy.Rate(para.send_vel_rate)
    #except:
    #    print("try2")
    while not rospy.is_shutdown():
        try:
            client.send("EnableSystem")
 
            client.send("SetRobotSpeed Vx " + str(global_vel.linear.x * para.scale_to))
            client.send("SetRobotSpeed Vy " + str(global_vel.linear.y * para.scale_to))
            client.send("SetRobotSpeed Omega " + str(global_vel.angular.z * para.scale_to))

            rospy.loginfo(rospy.get_caller_id() + "\n Set Vx:%f Vy:%f Wz:%f", global_vel.linear.x, global_vel.linear.y, global_vel.angular.z)
            os.system()
            rate.sleep()
        except:
            print("socket timeout check if the wifi is live and the UDP link is ok")
            continue
