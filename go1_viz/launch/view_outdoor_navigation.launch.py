import os
import xacro

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

go1_viz_pkg_name = "go1_viz"         # name of the go1_viz package

def generate_launch_description():

    rviz_config_file = os.path.join(get_package_share_directory(go1_viz_pkg_name), "rviz", "outdoor_nav2.rviz")

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