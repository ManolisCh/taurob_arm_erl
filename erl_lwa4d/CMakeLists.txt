cmake_minimum_required(VERSION 2.8.3)
project(erl_lwa4d)

find_package(catkin REQUIRED COMPONENTS roslaunch rostest)

catkin_package()

### TESTING ###
if(CATKIN_ENABLE_TESTING)
    roslaunch_add_file_check(launch)
    add_rostest(urdf/test/urdf.test)
endif()

### INSTALL ###
install(DIRECTORY config launch urdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(PROGRAMS scripts/move_lin.py scripts/move_circ.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}/scripts
)
