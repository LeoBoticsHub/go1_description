cmake_minimum_required(VERSION 3.5)
project(go1_description)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY config meshes xacro rviz urdf launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
