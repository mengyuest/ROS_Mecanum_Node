#!/usr/bin/env python
# license removed for brevity
import client
import rospy
import parameters
import tf
import time
import geometry_msgs.msg
from tf.transformations import *
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from tf.msg import tfMessage

para = parameters.parameters()

def mesosphere_odom():
    pub = rospy.Publisher('odom',Odometry,queue_size=100)
    odom_broadcaster = tf.TransformBroadcaster()    
    rospy.init_node('mesospere_odom',anonymous=True)
    rate = rospy.Rate(para.send_odom_rate) # 10hz

    # state params 
    x = 0
    y = 0
    z = 0
    th = 0
    last_time = rospy.get_time()
    while not rospy.is_shutdown():
        try:
            current_time = rospy.get_time()
            dt = (current_time - last_time)
            last_time = current_time
    #       get speed and counts of four wheels and cal  x,y,z=0,th and Vx, Vy, Wz
            n1 = int(client.send("GetEncoderChange 1"))
            n2 = int(client.send("GetEncoderChange 2"))
            n3 = int(client.send("GetEncoderChange 3"))
            n4 = int(client.send("GetEncoderChange 4"))
            
            print("%d %d %d %d"%(n1,n2,n3,n4))
            w1 = 2 * para.pi * n1 / dt * para.scale_from
            w2 = 2 * para.pi * n2 / dt * para.scale_from
            w3 = 2 * para.pi * n3 / dt * para.scale_from
            w4 = 2 * para.pi * n4 / dt * para.scale_from
            print("%f %f %f %f"%(w1,w2,w3,w4))
            Vx = para.r / 4 * (w1 + w2 + w3 + w4)
            Vy = para.rr / 4 * (-w1 + w2 + w3 - w4)
            Wz = (para.r + para.rr)/(4 * para.lx + 4 * para.ly)*(-w1 + w2 - w3 + w4)
         
            x = x + Vx * dt
            y = y + Vy * dt
            th = (th + Wz * dt) % (para.pi*2)        

            # broadcast the transform matrix message
            odom_quat =  quaternion_from_euler(0,0,th)
            
            odom_trans = geometry_msgs.msg.TransformStamped()
            odom_trans.header.stamp = current_time
            odom_trans.header.frame_id = "odom"
            odom_trans.child_frame_id = "base_link"
            
            odom_trans.transform.translation.x = x
            odom_trans.transform.translation.y = y
            odom_trans.transform.translation.z = z
            odom_trans.transform.rotation = odom_quat
            odom_broadcaster.sendTransform((x,y,z),odom_quat,current_time,odom_trans.child_frame_id,odom_trans.header.frame_id)


        #       next publish the odometry message over ROS                
            theOdom = Odometry()
            theOdom.header.stamp = current_time
            theOdom.header.frame_id = "odom"
            theOdom.pose.pose.position.x = x
            theOdom.pose.pose.position.y = y
            theOdom.pose.pose.position.z = z
            theOdom.pose.pose.orientation = odom_quat

            theOdom.child_frame_id = "base_link"
         
            theOdom.twist.twist.linear.x = Vx
            theOdom.twist.twist.linear.y = Vy
            theOdom.twist.twist.angular.z = Wz

            theStr = "%s \n Odom x:%f y:%f th:%f | \n %s | Vx:%f Vy:%f Wz:%f \n" % ( current_time , theOdom.pose.pose.position.x , theOdom.pose.pose.position.y ,th , theOdom.child_frame_id , theOdom.twist.twist.linear.x ,  theOdom.twist.twist.linear.y , theOdom.twist.twist.angular.z)  
            rospy.loginfo(theStr)
            pub.publish(theOdom)

            rate.sleep()
	except:
		rospy.loginfo("strange!!! continue~")		
		continue

if __name__ == '__main__':
    try:
        mesosphere_odom()
    except rospy.ROSInterruptException:
        pass
