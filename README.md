# Welcome to StackEdit!

Hi! I'm your first Markdown file in **StackEdit**. If you want to learn about StackEdit, you can read me. If you want to play with Markdown, you can edit me. If you have finished with me, you can just create new files by opening the **file explorer** on the left corner of the navigation bar.


# General important notice

For the arm to work with ROS and CANopen we have first to configure the modules to run in CANopen mode.  If we can connect to the robot and move it via the Schunk motion tool then it means that CANopen is not configured and it wont work in ROS. To configure the arm modules to use CANopen  we use the windoes CANopen tools provided by Schunk and more precisely the SMPT_ResetToCANopen.exe tool. 

## Dependencies

    sudo apt-get install ros-kinetic-schunk-modular-robotics
    sudo apt-get install ros-kinetic-ros-canopen
	sudo apt-get install ros-kinetic-cob-extern
	sudo apt-get install ros-kinetic-cob-common
	sudo apt-get install ros-kinetic-cob-control
	sudo apt-get install ros-kinetic-cob-command-gui
	sudo apt-get install ros-kinetic-cob-dashboard
	sudo apt-get install ros-kinetic-ros-controllers

## Using the arm 

 1. We first have to prepare/open the CANopen bus. For that, we run the `./prepare.sh` script with the arm connected to the usb via the adaptor.
 2. Then we run `roslaunch taurob_schunk_lwa4d arm.launch`
 3. Then to initialize the arm we run `rosservice call /arm/driver/init`.
 4. If we want to have some more functionality via a dashboard we run `roslaunch taurob_schunk_lwa4d dashboard.launch`.




