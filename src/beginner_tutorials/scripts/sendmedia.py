#!/usr/bin/env python
# license removed for brevity
import client
import rospy
import random
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from std_msgs.msg import String

def callback(data):
#control the bottom using data.linear.x data.linear.y data.angular.z
   
   size = 1000
    
   try: 
	   #client.send("EnableSystem")
#      client.send("SetRobotSpeed Vx " + str(data.linear.x * size))
#      client.send("SetRobotSpeed Vy "+ str(data.linear.y * size))
#      client.send("SetRobotSpeed Omega "+ str(data.angular.z * size))
	#rosinfo to the console
      pub = rospy.Publisher('cmd_vel1',geometry_msgs/Twist,queue_size = 100)
      rate = rospy.Rate(2)

      rospy.loginfo(rospy.get_caller_id()+"Set Vx:%d Vy:%d Wz:%d" ,int(data.linear.x*size),int(data.linear.y*size),int(data.angular.z*size))
      while not rospy.is_shutdown():
         theVel = geometry_msgs/Twist()
         theVel.linear.x = x
         theVel.linear.y = y
         theVel.linear.z = 0
         theVel.angular.x = 0
         theVel.angular.y = 0
         theVel.angular.z =z
         theStr = "%s send|| x:%d y:%d z:%d" %(rospy.get_time(),x,y,z)
         rospy.loginfo(theStr)
         pub.publish(theVel)
         rate.sleep()
   except:
      print("try1")

    


def mesosphere_twist():
    try:
        rospy.init_node('mesosphere_twist',anonymous=True)

        rospy.Subscriber("cmd_vel", Twist, callback)

        rospy.spin()
        
    except:
        print("try2")

if __name__ == '__main__':
    try:
#        client.send("EnableSystem")
        mesosphere_twist()
    except:
        print("try3")