CMAKE_MINIMUM_REQUIRED(VERSION 3.0)

PROJECT(LLDBTest)

FIND_PACKAGE(OpenCV REQUIRED)
IF (OpenCV_FOUND)
    MESSAGE("Found OpenCV" ${OpenCV_VERSION})
ELSE ()
    MESSAGE("OpenCV not Found")
ENDIF ()

# 设置输出的路径
SET(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)

# 设置头文件路径
INCLUDE_DIRECTORIES(${PROJECT_SOURCE_DIR}/include)

# test printMat with 1~4 channels
SET(SOURCES printMatTest.cpp)
ADD_EXECUTABLE(lldb_printMat_test ${SOURCES})
TARGET_LINK_LIBRARIES(lldb_printMat_test ${OpenCV_LIBS})

# test printMat with img and transpose
SET(SOURCES imgTest.cpp)
ADD_EXECUTABLE(lldb_img_test ${SOURCES})
TARGET_LINK_LIBRARIES(lldb_img_test ${OpenCV_LIBS})
