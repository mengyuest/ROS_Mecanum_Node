#!/usr/bin/env python
# license removed for brevity
import rospy
import tf
import geometry_msgs.msg

if __name__ == '__main__':

    broadcaster = tf.TransformBroadcaster()
    rospy.init_node('robot_tf_publisher',anonymous = True)
    rate = rospy.Rate(100)

    while not rospy.is_shutdown():
        
        # for rotation in x y z axis in radius
        quat = tf.transformations.quaternion_from_euler(0,0,0)
        # for move in x, y, z direction in meters
        x = 10
        y = 5
        z = 3

        broadcaster.sendTransform((x,y,z), quat, rospy.Time.now(), "base_link", "base_laser")
        rate.sleep()
     

