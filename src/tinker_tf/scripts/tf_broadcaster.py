#!/usr/bin/env python
# license removed for brevity
import rospy
import tf
import geometry_msgs.msg

if __name__ == '__main__':

    broadcaster = tf.TransformBroadcaster()
    broadcaster1 = tf.TransformBroadcaster()
    broadcaster2 = tf.TransformBroadcaster()
    rospy.init_node('tinker_tf',anonymous = True)
    rate = rospy.Rate(100)

    while not rospy.is_shutdown():
        
        # for rotation in x y z axis in radius
        quat = tf.transformations.quaternion_from_euler(0,0,0)
        # for move in x, y, z direction in meters
        x = 0 
        y = 0
        z = 0

        broadcaster.sendTransform((x,y,z), quat, rospy.Time.now(), "laser", "base_link")
   #     broadcaster1.sendTransform((x,y,z), quat, rospy.Time.now(), "base_footprint", "base_link")
    #    broadcaster2.sendTransform((x,y,z), quat, rospy.Time.now(), "map", "odom")
        rate.sleep()
     

