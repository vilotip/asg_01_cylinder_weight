#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

from ros_tutorial.msg import Cylinder

from math import pi

# because real-time
radius = 0
radius_squared = 0
height = 0
radius_found = False
radius_squared_found = False
height_found = False

def radius_function(data):
    global radius
    global radius_found
    radius = data.data
    radius_found = True

def radius_squared_function(data):
    global radius_squared
    global radius_squared_found
    radius_squared = data.data
    radius_squared_found = True

def height_function(data):
    global height
    global height_found
    height = data.data
    height_found = True
    
def calculate():
    if radius_found and radius_squared_found and height_found:
        msg = Cylinder()
        msg.volume = pi*radius_squared*height
        msg.surf_area = (2*pi*radius_squared)+(2*pi*radius*height)
        pub.publish(msg)

rospy.init_node("volume_surf_area")
rospy.Subscriber("/radius", Float64, radius_function)
rospy.Subscriber("/radius_squared", Float64, radius_squared_function)
rospy.Subscriber("/height", Float64, height_function)

pub = rospy.Publisher("/volume_surf_area", Cylinder, queue_size=10)

while not rospy.is_shutdown():
    calculate()
    rospy.sleep(0.1)
