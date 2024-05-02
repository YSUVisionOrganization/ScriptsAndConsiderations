#作者：周彦
#邮箱：zy5290341@gmail.com
#功能：本脚本用于拍数据集，利用工摄

cmake_minimum_required(VERSION 3.11 )
project(take_pictures)

find_package(OpenCV REQUIRED)
include_directories(
        ${OpenCV_INCLUDE_DIRS}
        /usr/include
)


add_executable(
        ${PROJECT_NAME}
        main.cpp
        Camera/MvCamera.cpp
)

target_link_libraries(${PROJECT_NAME}  ${OpenCV_LIBS})

#Camera
link_directories(/usr/lib)
target_link_libraries(${PROJECT_NAME} MVSDK)

