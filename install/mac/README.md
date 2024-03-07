# install

## 참고

```
https://docs.ros.org/en/dashing/Installation/macOS-Install-Binary.html
```


## macOS
- macOS Sierra(10.12.x)

- brew install  
    ```
    https://brew.sh/ko/
    ```  
    ```
    brew install python3

    # install asio and tinyxml2 for Fast-RTPS
    brew install asio tinyxml2

    # install dependencies for robot state publisher
    brew install tinyxml eigen pcre poco

    # OpenCV isn't a dependency of ROS 2, but it is used by some demos.
    brew install opencv

    # install OpenSSL for DDS-Security
    brew install openssl
    # if you are using ZSH, then replace '.bashrc' with '.zshrc'
    echo "export OPENSSL_ROOT_DIR=$(brew --prefix openssl)" >> ~/.bashrc

    # install Qt for RViz
    brew install qt freetype assimp

    # install console_bridge for rosbag2
    brew install console_bridge

    # install dependencies for rcl_logging_log4cxx
    brew install log4cxx

    # install CUnit for Cyclone DDS
    brew install cunit
    ```



- ROS 2 Foxy Fitzroy - Patch Release 6.1  
    ```
    https://github.com/ros2/ros2/releases/tag/release-foxy-20211013
    ```

- 맥 os 버전이 맞지않고 특정 모듈들이 없는것으로 보아 설치 과정중 경로 잘못 설정했거나 호환 안될 가능성이 커보이고, 수정보다는 윈도우 or 리눅스에 설치 하는 방법이 좋아보인다.

    ![](./1.png)