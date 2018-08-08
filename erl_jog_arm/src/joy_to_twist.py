#!/usr/bin/env python


# Take joystick cmds. Republish them as TwistStamped for
# e.g. jogging.

# RB: +x, LB: -x joy.buttons[4], joy.buttons[5]
# L on L dpad: +x
# Up on L dpad: +z joy.axes[1]

# START joy.buttons[7]
# BACK joy.buttons[6]

# R on R stick: +Rx
# Up on R stick: +Ry
# B: +Rz, A: -Rz


import rospy
from geometry_msgs.msg import TwistStamped
from sensor_msgs.msg import Joy
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint


class joy_to_twist:

    def __init__(self):
        self.pub = rospy.Publisher('/arm/twist_controller/command_twist_stamped', TwistStamped, queue_size=1)

    # Convert to TwistStamped and republish
    def callback(self, joy):
        #rospy.loginfo("Incoming joy: %s", joy)
        #rospy.loginfo("")
        linear_scale = 0.05
        angular_scale = 0.1
        ts = TwistStamped()
        gripper_cmd = JointTrajectory
        jtp = JointTrajectoryPoint

        ts.header.stamp = rospy.Time.now()
        ts.header.frame_id = "arm_podest_link"

        # These buttons are binary
        ts.twist.linear.x = linear_scale * (-joy.buttons[4] + joy.buttons[5])
        # Double buttons
        ts.twist.linear.y = linear_scale * joy.axes[0]
        ts.twist.linear.z = linear_scale * joy.axes[1]

        ts.twist.angular.x = angular_scale * (-joy.axes[3])
        ts.twist.angular.y = angular_scale * joy.axes[4]
        # These buttons are binary
        ts.twist.angular.z = angular_scale * (-joy.buttons[0] + joy.buttons[1])

        #rospy.loginfo("Outgoing ts: %s", ts)
        #rospy.loginfo("")

        self.pub.publish(ts)

    def republish(self):
        rospy.Subscriber("joy", Joy, self.callback)

        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('joy_to_twist', anonymous=True)
    republisher = joy_to_twist()
    republisher.republish()
