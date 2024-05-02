#pragma once
#include <string>
#include <iostream>
#include <opencv2/opencv.hpp>
#include "CameraApi.h"
#include<chrono>
class MvCamera {
public:
    cv::Mat                     imag;
    int                     iCameraCounts;
    int                     iStatus;
    tSdkCameraDevInfo       tCameraEnumList;
    int                     hCamera;
    tSdkCameraCapbility     tCapability;      //设备描述信息
    tSdkFrameHead           sFrameInfo;
    BYTE*			        pbyBuffer;
    int                     channel;
    int                     explore_time;
    unsigned char           *g_pRgbBuffer;     //处理后数据缓存区
    unsigned int camera_num;//相机索引


public:
    cv::Mat convertToBGR(cv::Mat image);
    void open();
    void close();
    /**
     * @details 单位us
     * @param exposure_time
     */
    void setExposureTime(double exposure_time);
    // void setExposureTime(float exposure_time);
    /**
     * @param channel 0 Red 1 Green 2 Blue
     * @param ratio
     */
    // void setWhiteBalance(int channel,float ratio);

    /**
     *
     * @param value 
     */
    void setGain(int iRGain, int iGGain, int iBGain);
    cv::Mat getImage();
};



