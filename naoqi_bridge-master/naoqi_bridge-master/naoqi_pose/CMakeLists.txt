cmake_minimum_required(VERSION 2.8.3)
project(naoqi_pose)

# Find all required modules for compilation
find_package(catkin REQUIRED)

# This will install python libraries
catkin_python_setup()

# Declare info that other packages need to import messages generated here
catkin_package( )

#And this will install python nodes
catkin_install_python(PROGRAMS ./nodes/pose_controller.py ./nodes/pose_manager.py ./scripts/execute_pose.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

# Instructions to install launch files
install(DIRECTORY launch/
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch )

# Install config files
install(DIRECTORY config/
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/config)
