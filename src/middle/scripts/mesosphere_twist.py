#!/usr/bin/env python
# license removed for brevity
import client
import rospy
import parameters
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from std_msgs.msg import String

global_vel = Twist()
para = parameters.parameters()

def callback(data):
#update the Twist but not pub now (with a rate defined in main())
    
    try: 
        global_vel.linear.x = data.linear.x * para.times 
        global_vel.linear.y = data.linear.y * para.times 
        global_vel.angular.z = data.angular.z * para.times 
    except:
        print("try1")

    

if __name__ == '__main__':
     
    #try:
#        client.send("EnableSystem")
    rospy.init_node('mesosphere_twist',anonymous=True)
    rospy.Subscriber("cmd_vel", Twist, callback)

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
            rate.sleep()
        except:
            print("try3")
            continue
