#!/usr/bin/env python
# license removed for brevity
import rospy
import random
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def fake_cmd_vel_talker():
    pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
    rospy.init_node('fake_cmd_vel_talker',anonymous = True)
    rate = rospy.Rate(10)
    newTwist = Twist()
    while not rospy.is_shutdown():
        hello_str = "Hello world %s" % rospy.get_time()
        newTwist.linear.x = random.uniform(1,10)
        newTwist.linear.y = random.uniform(1,10)
        newTwist.linear.z = random.uniform(1,10)
        newTwist.angular.x = random.uniform(1,10)
        newTwist.angular.y = random.uniform(1,10)
        newTwist.angular.z = random.uniform(1,10)
        rospy.loginfo(hello_str)
        pub.publish(newTwist)
        rate.sleep()

if __name__ == '__main__':
    try:
        fake_cmd_vel_talker()
    except rospy.ROSInterruptException:
        pass
