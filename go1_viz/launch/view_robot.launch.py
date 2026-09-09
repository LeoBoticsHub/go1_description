import os
import xacro

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

go1_description_pkg_name = "go1_description" # name of the go1_description package
go1_viz_pkg_name         = "go1_viz"         # name of the go1_viz package

def process_xacro():
    pkg_path = os.path.join(get_package_share_directory(go1_description_pkg_name))
    xacro_file = os.path.join(pkg_path, 'xacro', 'robot.xacro')
    robot_description_config = xacro.process_file(xacro_file)
    return robot_description_config.toxml()

def generate_launch_description():

    rviz_config_file = os.path.join(get_package_share_directory(go1_viz_pkg_name), "rviz", "robot.rviz")
    robot_description = process_xacro()

    rviz = Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=["-d", rviz_config_file]
        )
    
    robot_state_pub = Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[
                {
                    'publish_frequency': 100.0,
                    'use_tf_static': True,
                    'robot_description': robot_description
                }
            ],
        )
    
    joint_state_pub = Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher',
            output='screen',
        )
    
    ld = LaunchDescription()
    
    ld.add_action(rviz)
    ld.add_action(robot_state_pub)
    ld.add_action(joint_state_pub)
    
    return ld