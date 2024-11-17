import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # 기본 설정값들
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    map_dir = LaunchConfiguration(
        'map',
        default=os.path.join(
            get_package_share_directory('stella_navigation2'),
            'map',
            '/home/jang/colcon_ws/src/STELLA_N1_REMOTEPC_X4_ROS2_v2.0-Humble/stella_navigation2/map/my_map.yaml'))

    param_dir = LaunchConfiguration(
        'params_file',
        default=os.path.join(
            get_package_share_directory('stella_navigation2'),
            'param',
            'stella.yaml'))

    nav2_launch_file_dir = os.path.join(get_package_share_directory('nav2_bringup'), 'launch')

    rviz_config_dir = os.path.join(
        get_package_share_directory('stella_navigation2'),
        'rviz',
        'stella_navigation2.rviz')

    # EKF 설정 파일 경로 추가
    ekf_config_dir = os.path.join(
        get_package_share_directory('stella_navigation2'),
        'param',
        'ekf.yaml')  # EKF 파라미터 파일 경로

    # Launch Description 반환
    return LaunchDescription([
    
        # EKF 노드 실행 추가
        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            output='screen',
            parameters=[ekf_config_dir, {'use_sim_time': use_sim_time}],

        ),
        
        # 맵 파일 경로 설정
        DeclareLaunchArgument(
            'map',
            default_value=map_dir,
            description='Full path to map file to load'),

        # 파라미터 파일 경로 설정
        DeclareLaunchArgument(
            'params_file',
            default_value=param_dir,
            description='Full path to param file to load'),

        # 시뮬레이션 시간 사용 여부 설정
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),

        # Nav2 bringup 실행
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([nav2_launch_file_dir, '/bringup_launch.py']),
            launch_arguments={
                'map': map_dir,
                'use_sim_time': use_sim_time,
                'params_file': param_dir}.items(),
        ),

        # RViz2 실행
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config_dir],
            parameters=[{'use_sim_time': use_sim_time}],
            output='screen'),


    ])

