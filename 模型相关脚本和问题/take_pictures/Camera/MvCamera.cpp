#include "MvCamera.h"
using namespace std;

void MvCamera::open()
{
    iCameraCounts = 1;
    iStatus=-1;
    tCameraEnumList;
    hCamera;
    tCapability;      //设备描述信息
    sFrameInfo;
    pbyBuffer;
    channel=3;

    CameraSdkInit(1);
    //枚举设备，并建立设备列表
    //CameraEnumerateDeviceEx();
    //没有连接设备
    if(iCameraCounts==0){
        std::cout << "没有连接设备" << std::endl;
        return;
    }

    //相机初始化。初始化成功后，才能调用任何其他相机相关的操作接口
    // iStatus = CameraInit(&tCameraEnumList,-1,-1,&hCamera);
    iStatus = CameraInitEx(camera_num, -1, -1, &hCamera);
    //初始化失败
    if(iStatus!=CAMERA_STATUS_SUCCESS){
        std::cout << "初始化失败" << std::endl;
        return;
    }
    //获得相机的特性描述结构体。该结构体中包含了相机可设置的各种参数的范围信息。决定了相关函数的参数
    CameraGetCapability(hCamera,&tCapability);

    g_pRgbBuffer = (unsigned char*)malloc(tCapability.sResolutionRange.iHeightMax*tCapability.sResolutionRange.iWidthMax*3);


    /*让SDK进入工作模式，开始接收来自相机发送的图像
    数据。如果当前相机是触发模式，则需要接收到
    触发帧以后才会更新图像。    */
    CameraPlay(hCamera);

    if(tCapability.sIspCapacity.bMonoSensor){
        channel=1;
        CameraSetIspOutFormat(hCamera,CAMERA_MEDIA_TYPE_MONO8);
    }else{
        channel=3;
        CameraSetIspOutFormat(hCamera,CAMERA_MEDIA_TYPE_BGR8);
    }
}

void MvCamera::close()
{
    CameraUnInit(hCamera);
    free(g_pRgbBuffer);
}


void MvCamera::setExposureTime(double exposure_time)
{
    CameraSetExposureTime(hCamera,exposure_time);
}


void MvCamera::setGain(int iRGain, int iGGain, int iBGain)
{
    CameraSetGain(hCamera, iRGain, iGGain, iBGain);
}

cv::Mat MvCamera::getImage()
{
    if(CameraGetImageBuffer(hCamera,&sFrameInfo,&pbyBuffer,1000) == CAMERA_STATUS_SUCCESS)
    {
        CameraImageProcess(hCamera, pbyBuffer, g_pRgbBuffer,&sFrameInfo);
        cv::Mat matImage = cv::Mat(
                cv::Size(sFrameInfo.iWidth,sFrameInfo.iHeight), 
                CV_8UC3,
                g_pRgbBuffer
                );
        // matImage = convertToBGR(matImage);
        // //在成功调用CameraGetImageBuffer后，必须调用CameraReleaseImageBuffer来释放获得的buffer。
        // //否则再次调用CameraGetImageBuffer时，程序将被挂起一直阻塞，直到其他线程中调用CameraReleaseImageBuffer来释放了buffer
        CameraReleaseImageBuffer(hCamera,pbyBuffer);
        return matImage;
    }   
}