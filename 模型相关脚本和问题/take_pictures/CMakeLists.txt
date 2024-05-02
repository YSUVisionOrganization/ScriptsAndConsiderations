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

