import os
import xacro

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

# go1_description_pkg_name = "go1_description" # name of the go1_description package
go1_viz_pkg_name         = "go1_viz"         # name of the go1_viz package

# def process_xacro():
#     pkg_path = os.path.join(get_package_share_directory(go1_description_pkg_name))
#     xacro_file = os.path.join(pkg_path, 'xacro', 'robot.xacro')
#     robot_description_config = xacro.process_file(xacro_file)
#     return robot_description_config.toxml()

def generate_launch_description():

    rviz_config_file = os.path.join(get_package_share_directory(go1_viz_pkg_name), "rviz", "nav2.rviz")

    rviz = Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=["-d", rviz_config_file]
        )
    
    ld = LaunchDescription()
    
    ld.add_action(rviz)
    
    return ld