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
from sensor_msgs.msg import Joy
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint


class gripper_cmd:

    def __init__(self):
        self.pub = rospy.Publisher('/pg70/joint_trajectory_controller/command', JointTrajectory, queue_size=1)

    # Convert to TwistStamped and republish
    def callback(self, joy):
        #rospy.loginfo("Incoming joy: %s", joy)
        #rospy.loginfo("")

        gripper_cmd = JointTrajectory()
        jtp = JointTrajectoryPoint()

        gripper_cmd.joint_names = ["pg70_finger_left_joint"]
        gripper_cmd.header.stamp = rospy.Time.now()
        gripper_cmd.header.frame_id = "pg70_finger_left_link"

        # gripper commands

        if (joy.buttons[7] and (not joy.buttons[6])):
            jtp.positions = [0.02]
            gripper_cmd.points.append(jtp)
            self.pub.publish(gripper_cmd)

        if (joy.buttons[6] and (not joy.buttons[7])):
            jtp.positions = [0.0]
            gripper_cmd.points.append(jtp)
            self.pub.publish(gripper_cmd)


        #rospy.loginfo("Outgoing ts: %s", ts)
        #rospy.loginfo("")


    def republish(self):
        rospy.Subscriber("joy", Joy, self.callback)

        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('gripper_cmd', anonymous=True)
    republisher = gripper_cmd()
    republisher.republish()
