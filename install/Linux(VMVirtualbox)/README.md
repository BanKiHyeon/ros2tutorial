# install

## 참고

```
https://docs.ros.org/en/foxy/Installation.html
```


## Oracle VM VirtualBox
- 버추얼 박스 설치

## ubuntu 20.04
- 공홈에서 .iso 파일 다운로드

## ROS 2 Foxy Fitzroy  install
1. 참고  

    ```
    https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html
    ```
2. 설치완료 확인
    ```
    source /opt/ros/foxy/setup.bash
    ros2 run demo_nodes_cpp talker
    ```
## turtlesim pkg 설치
```
sudo apt install ros-foxy-turtlesim
```

## turtlesim sample 실행

```
ros2 run turtlesim turtlesim_node
ros2 run turtlesim turtle_teleop_key
```  

![](./1.png)