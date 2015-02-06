import rospy
import tf
import geometry_msgs.msg

if __name__ == '__main__':
    rospy.init_node('tf_listener')
    
    listener = tf.TransformListener()

    rate = rospy.Rate(10)

    laser_point = geometry_msgs.msg.PointStamped()
   
    laser_point.header.frame_id = "base_laser" #base_laser
    laser_point.header.stamp = rospy.Time.now()
    laser_point.point.x = 3
    laser_point.point.y = 4
    laser_point.point.z = 8    

    while not rospy.is_shutdown():
        base_point =geometry_msgs.msg.PointStamped()
#        try:
#            (trans,rot) = listener.lookupTransform('base_laser','base_link',rospy.Time(0))
#        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
#            continue
        base_point = listener.transformPoint("base_link", laser_point)
        rospy.loginfo("%s : (%.2f, %.2f, %.2f) ---> %s : (%.2f, %.2f, %.2f) at time %.2f",laser_point.header.frame_id, laser_point.point.x, laser_point.point.y, laser_point.point.z, base_point.header.frame_id, base_point.point.x, base_point.point.y, base_point.point.z, base_point.header.stamp.to_sec())
        rate.sleep()
