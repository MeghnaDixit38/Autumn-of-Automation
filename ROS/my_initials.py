#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

rospy.init_node('robot_cleaner', anonymous=True)

def rotate(speed,angle,clockwise):

    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()


    #Converting from angles to radians
    angular_speed = speed*2*PI/360
    relative_angle = angle*2*PI/360

    #We wont use linear components
    vel_msg.linear.x=0
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    
    if clockwise:
        vel_msg.angular.z = -abs(angular_speed)
    else:
        vel_msg.angular.z = abs(angular_speed)
    
    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while(current_angle < relative_angle):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)
    vel_msg.angular.z = 0

def move(speed,distance):

    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    vel_msg.linear.x = speed
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    t0 = rospy.Time.now().to_sec()
    current_distance = 0
    while(current_distance < distance):
          velocity_publisher.publish(vel_msg)
          t1=rospy.Time.now().to_sec()
          current_distance= speed*(t1-t0)
    vel_msg.linear.x = 0


if __name__ == '__main__':
    try:
        rotate(30,90,0)
        move(1,3)
        rotate(50,150,1)
        move(1,2)
        rotate(50,135,0)
        move(1,2)
        rotate(50,150,1)
        move(1,2)
        
    except rospy.ROSInterruptException: pass
