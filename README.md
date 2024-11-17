원본 프로젝트: [STELLA_N1_ROS2](https://github.com/ntrexlab/STELLA_N1_REMOTEPC_X4_ROS2_v2.0)

Robot platform : Stella N1

LIDAR : YDLIDAR x4 or YDLIDAR x4 Pro

ROS ver : ROS2 Humble for PC / ROS2 Foxy for Lattepanda

Linux ver : Ubuntu 22.04 for PC / Ubuntu 20.04 for Lattepanda
Where to use : Computer

- Stella_MD 패키지에서 odom에 대한 토픽만 발행하고, tf는 꺼야됨
- /odom, /imu 토픽을 "ekf"에서 받은 후에 새로운 /odometry/filtered 토픽과 /tf/odom 를 발행함 
- /tf/odom을 기준으로 AMCL 실행 후 /tf/map 발행

-[Stella_N1_Lattepanda](https://github.com/Gyeongrok-Jang/Stella_N1_Lattepanda)
