#!/usr/bin/env python
import rospy
from my_scripts.msg import Topic_1
import numpy as np
from std_msgs.msg import Float64MultiArray
final = Float64MultiArray()

def convert_q_to_e(v, r, p, t):
        siny_cosp = 2*(v*t + r*p)
	cosy_cosp = 1-2*(p**2+t**2)
	euler_yaw = np.arctan2(siny_cosp, cosy_cosp)
	sinr_cosp = 2*(v*r + p*t)
	cosr_cosp = 1- 2*(r**2 + p**2)
	euler_roll = np.arctan2(sinr_cosp, cosr_cosp)
        sinp = 2*(v*p - t*r)
	euler_pitch = np.where( np.abs(sinp) >=1,np.sign(sinp)*(3.14159/2),np.arcsin(sinp) )
        return euler_roll, euler_pitch, euler_yaw
def callback(msg):
	final.data=convert_q_to_e(msg.r,msg.p,msg.t,msg.v)
	rospy.loginfo(final)
def function():
    	rospy.init_node('my_convertor', anonymous=True)
	subscribe=rospy.Subscriber("topic-1", Topic_1, callback)
   	publish=rospy.Publisher("topic-2", Float64MultiArray,queue_size=10)
        rate=rospy.Rate(1)
	
	while not rospy.is_shutdown():
		publish.publish(result)
		rate.sleep()
   
if __name__ == '__main__':
	try:
		function()
	except rospy.ROSInterruptionException:
		pass



