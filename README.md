# General important notice

For the arm and gripper to work with ROS and CANopen we have first to configure the modules to run in CANopen mode.  If we can connect to the robot and move it via the Schunk motion tool (SMT) then it means that CANopen is not configured and it wont work in ROS. To configure the arm modules to use CANopen  we use the windows CANopen tools provided by Schunk and more precisely the SMPT_ResetToCANopen.exe tool. Alternatively we can switch CANopen on in the SMT in each module individually.

## Dependencies

```
  sudo apt-get install ros-kinetic-ros-canopen
  sudo apt-get install ros-kinetic-cob-extern
  sudo apt-get install ros-kinetic-cob-common
  sudo apt-get install ros-kinetic-cob-control
  sudo apt-get install ros-kinetic-cob-command-gui
  sudo apt-get install ros-kinetic-cob-dashboard
  sudo apt-get install ros-kinetic-ros-controllers
  sudo apt-get install ros-kinetic-cob-helper-tools
  sudo apt-get install ros-kinetic-cob-gazebo-ros-control
  sudo apt-get install ros-kinetic-cob-gazebo-plugins
  sudo apt-get install ros-kinetic-moveit
```


## Using the lwa4d arm

 1. We first have to prepare/open the CANopen bus. For that, we run the `./prepare.sh` script with the arm connected to the usb via the adaptor.
 2. Then we run `roslaunch erl_lwa4d arm.launch`
 3. Then to initialize the arm we run `rosservice call /arm/driver/init`.
 4. If we want to have some more functionality via a dashboard we run `roslaunch erl_lwa4d dashboard.launch`.

## Using the pg70+ gripper

  1. Similar to above we first have to prepare/open the CANopen bus. For that, we run the `./prepare.sh` script. This is only if we want to run the gripper standalone. If we allready have the arm running the CANopen bus is already open.
  2. Then we run `roslaunch erl_pg70 gripper.launch`
  3. Then to initialize the arm we run `rosservice call /pg70/driver/init`.
  4. If we want to have some more functionality via a dashboard we run `roslaunch erl_pg70 dashboard.launch`.

## Using the simulated standalone arm with moveit!
 1. We first have to run the simulated arm in gazebo. For that `roslaunch erl_lwa4d sim.launch` to open gazebo and load the arm model.
 2. Then we run moveit! to control the arm: `roslaunch erl_lwa4d_moveit_config main_moveit.launch`.

## Using the simulated arm with pg70 gripper and moveit!
  1. We first have to run the simulated arm in gazebo. For that `roslaunch erl_lwa4d sim_with_gripper.launch` to open gazebo and load the unified arm + pg70 model.
  2. TODO Then we run moveit! to control the arm: `roslaunch erl_lwa4d_moveit_config main_moveit.launch`.
