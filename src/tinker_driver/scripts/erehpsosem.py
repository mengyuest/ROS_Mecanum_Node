#!/usr/bin/env python
# license removed for brevity
import rospy
import client
import parameters
import tf
import time
import geometry_msgs.msg
import os
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from std_msgs.msg import String

global_vel = Twist()
para = parameters.parameters()

timer = 0

def vToBase(vType, velocity):
    baseVelocity = 0
    if(velocity >= 0):
        if(velocity < para.maxV1[vType] and velocity > para.minV1[vType]):
            baseVelocity = velocity * para.a1[vType] + para.b1[vType]
    else:
        if(velocity < para.maxV2[vType] and velocity > para.minV2[vType]):
            baseVelocity = velocity * para.a2[vType] + para.b2[vType]
    return baseVelocity

def updateVel(data):
#update the Twist but not send Vel to base now
#    try:
        print"catch velocity"
	global_vel.linear.x = vToBase('Vx', data.linear.x)#data.twist.twist.linear.x)
        global_vel.linear.y = vToBase('Vy', data.linear.y)#data.twist.twist.linear.y)
        global_vel.angular.z = vToBase('Vz',data.angular.z)# data.twist.twist.angular.z) 
        print"ACCEPT VELOCITY~~ " + str(data.linear.x) + " " + str(data.linear.y) + " " + str(data.angular.z) + " " + str(global_vel.linear.x) + " " + str(global_vel.linear.y) + " " + str(global_vel.angular.z) + "\n\n " 
   
#    except:
#        print"error in updateVel(data) : can't cal Vel properly"
        
def isVelocityValid():
    if global_vel.linear.x < para.maxVBase['Vx'] and global_vel.linear.x > -1 * para.maxVBase['Vx']:
        if  global_vel.linear.y < para.maxVBase['Vy'] and global_vel.linear.y > -1 * para.maxVBase['Vy']:
            if  global_vel.angular.z < para.maxVBase['Vz'] and global_vel.angular.z > -1 * para.maxVBase['Vz']:
                return True
    return False

if __name__ == '__main__': 

#INITIALIZATION: create the ROS node, set frquency, add trigger functions 
    rospy.init_node('erehpsosem',anonymous=True)

    pub = rospy.Publisher('odom',Odometry,queue_size=100)
    odom_broadcaster = tf.TransformBroadcaster()   

    rospy.Subscriber("cmd_vel", Twist, updateVel)

    rate = rospy.Rate(para.send_vel_rate)
	
    x = 0
    y = 0
    z = 0
    th = 0
    judge = True
    #last_time = rospy.get_time()
    last_time = rospy.Time.now()

    while not rospy.is_shutdown():
#        try:
#BLOCK I : get encoder change from the base, then calculate and send to the Odom
			
            current_time = rospy.Time.now()
            dt = 1.0 / para.send_vel_rate
            last_time = current_time
# get speed and counts of four wheels and cal  x,y,z=0,th and Vx, Vy, Wz
 #           n1 = int(client.send("GetEncoderChange 1"))
 #           n2 = int(client.send("GetEncoderChange 2"))
 #           n3 = int(client.send("GetEncoderChange 3"))
 #           n4 = int(client.send("GetEncoderChange 4"))
            n1 = 0
            n2 = 0
            n3 = 0
            n4 = 0            
            w1 = 2 * para.pi * n1 / dt * para.scale_from
            w2 = 2 * para.pi * n2 / dt * para.scale_from
            w3 = 2 * para.pi * n3 / dt * para.scale_from
            w4 = 2 * para.pi * n4 / dt * para.scale_from
            Vx = para.r / 4 * (w1 + w2 + w3 + w4)
            #Vy = para.rr / 4 * (-w1 + w2 + w3 - w4)
            Vy = para.rr / 4 * (w1 - w2 -w3 + w4)
            Wz = (para.r + para.rr)/(4 * para.lx + 4 * para.ly)*(-w1 + w2 - w3 + w4)
 
            x = x + Vx * dt
            y = y + Vy * dt
            th = (th + Wz * dt) % (para.pi*2)        

            # broadcast the transform matrix message
            odom_quat =  tf.transformations.quaternion_from_euler(0,0,th)      

            odom_broadcaster.sendTransform((x,y,z), odom_quat, current_time, "base_link", "odom")
               
            theOdom = Odometry()
            
            theOdom.header.stamp = current_time
            theOdom.header.frame_id = "odom"
 
            theOdom.pose.pose.position.x = x
            theOdom.pose.pose.position.y = y
            theOdom.pose.pose.position.z = z

            theOdom.pose.pose.orientation.x = odom_quat[0]
            theOdom.pose.pose.orientation.y = odom_quat[1]
            theOdom.pose.pose.orientation.z = odom_quat[2]
            theOdom.pose.pose.orientation.w = odom_quat[3]            

            theOdom.child_frame_id = "base_link"
       
            theOdom.twist.twist.linear.x = Vx
            theOdom.twist.twist.linear.y = Vy
            theOdom.twist.twist.angular.z = Wz

  #          theStr = "%s \n Odom x:%f y:%f th:%f | \n %s | Vx:%f Vy:%f Wz:%f  \n  " % ( current_time , theOdom.pose.pose.position.x , theOdom.pose.pose.position.y ,th , theOdom.child_frame_id , theOdom.twist.twist.linear.x ,  theOdom.twist.twist.linear.y , theOdom.twist.twist.angular.z)  
 #           rospy.loginfo(theStr)
            pub.publish(theOdom)

  
#BLOCK II: send velocity to the base with PID calibration
            if isVelocityValid()==True:
                
#                client.send("RobotSpeedSet Vx " + str(vToBase('Vx',global_vel.linear.x)))
#                client.send("RobotSpeedSet Vy " + str(vToBase('Vy',global_vel.linear.y)))
#                client.send("RobotSpeedSet Omega " + str(vToBase('Vz',global_vel.angular.z)))
                rospy.loginfo("the base number is" + str(global_vel.linear.x))
                client.send("SetRobotSpeed Vx " + str(global_vel.linear.x))
                client.send("SetRobotSpeed Vy " + str(global_vel.linear.y))
                client.send("SetRobotSpeed Omega " + str(global_vel.angular.z))
                client.send("EnableSystem")
#                judge = False


            else:

#                judge = True
#            rospy.loginfo(rospy.get_caller_id() + "\n Set Vx:%f Vy:%f Wz:%f", global_vel.linear.x, global_vel.linear.y, global_vel.angular.z)
                timer = (timer + 1)%6
#            if(timer == 1):
#                a = os.system('clear') 
            rate.sleep()
#        except:
#            print("socket timeout check if the wifi is live and the UDP link is ok")
            continue
