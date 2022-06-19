#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
from ros_tutorial.msg import Cylinder

density = 0
density_found = False
volume = 0
volume_found = False

def density_function(data):
    global density
    global density_found
    density = data.data
    density_found = True

def volume_function(data):
    global volume
    global volume_found
    volume = data.volume
    volume_found = True

def calculate():
    if density_found and volume_found:
        weight = density*volume
        pub.publish(weight)


rospy.init_node("weight")
rospy.Subscriber("/density", Float64, density_function)
rospy.Subscriber("/volume_surf_area", Cylinder, volume_function)

pub = rospy.Publisher("/weight", Float64, queue_size=10)

while not rospy.is_shutdown():
    calculate()
    rospy.sleep(0.1)
