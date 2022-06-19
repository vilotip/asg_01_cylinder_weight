#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

def radius_function(data):
    radius=data.data
    radius_squared = radius*radius
    rospy.loginfo("radius: %f, radius_squared: %f", radius, radius_squared)
    pub.publish(radius_squared)

rospy.init_node("radius_squared_n")
pub = rospy.Publisher("/radius_squared", Float64, queue_size=10)
rospy.Subscriber("/radius", Float64, radius_function)
rospy.spin()
