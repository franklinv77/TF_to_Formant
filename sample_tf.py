#!/usr/bin/env python  
import roslib
import rospy
import math
import tf
import geometry_msgs.msg
import std_msgs.msg

if __name__ == '__main__':
    rospy.init_node('turtle_tf_listener')

    world_x_pub = rospy.Publisher("world_x", std_msgs.msg.Float64, queue_size=10)
    world_y_pub = rospy.Publisher("world_y", std_msgs.msg.Float64, queue_size=10)
    world_z_pub = rospy.Publisher("world_z", std_msgs.msg.Float64, queue_size=10)
    

    listener = tf.TransformListener()

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('odom', 'base_footprint', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        x, y, z = trans

        world_x_pub.publish(std_msgs.msg.Float64(x))
        world_y_pub.publish(std_msgs.msg.Float64(y))
        world_z_pub.publish(std_msgs.msg.Float64(z))

        rate.sleep() 
