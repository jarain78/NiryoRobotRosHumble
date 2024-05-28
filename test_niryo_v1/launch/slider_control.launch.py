import os

from ament_index_python import get_package_share_directory
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import Command, LaunchConfiguration
import launch_ros.descriptions

def generate_launch_description():
    res = []

    model_launch_arg = DeclareLaunchArgument("model", default_value=os.path.join(get_package_share_directory("niryo_one_description"), "urdf/v1/niryo_one.urdf.xacro"))

    
    res.append(model_launch_arg)

    rvizconfig_launch_arg = DeclareLaunchArgument("rvizconfig", default_value=os.path.join(get_package_share_directory("niryo_one_description"), "config/default_config.rviz"))
    res.append(rvizconfig_launch_arg)

    gui_launch_arg = DeclareLaunchArgument("gui", default_value="true")
    res.append(gui_launch_arg)
    
    #robot_description = ParameterValue(Command(['xacro ', LaunchConfiguration('model')]), value_type=str)
    robot_description = ParameterValue(Command(['xacro ',os.path.join(get_package_share_directory("niryo_one_description"), "urdf/v1/niryo_one.urdf.xacro")]), value_type=str)  

    robot_state_publisher_node = Node(
        name="robot_state_publisher",
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{'robot_description': robot_description}]
    )
    res.append(robot_state_publisher_node)

    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        condition=IfCondition(LaunchConfiguration('gui'))
    )
    res.append(joint_state_publisher_gui_node)

    rviz_node = Node(
        name="rviz2",
        package="rviz2",
        executable="rviz2",
        output="screen",
        arguments=['-d', LaunchConfiguration("rvizconfig")],
    )
    res.append(rviz_node)
    
    slider_control_node = Node(
        package="test_niryo_v1",
        executable="test_niryo_v1",
        name="slider_control",
        output="screen"
    )
    res.append(slider_control_node)

    return LaunchDescription(res)
