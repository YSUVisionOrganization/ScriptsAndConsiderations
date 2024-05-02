#include "Camera/MvCamera.h"
#include <opencv2/opencv.hpp>
int main()
{
    MvCamera camera;
    camera.open();
    int cnt = 1;
    while (1)
    {
        cv::Mat src = camera.getImage();
        if (cv::waitKey(10) == 'p')
        {
            std::string outputPath = "/home/zhouyan/code/pictures/" + std::to_string(cnt) + ".jpg";  
            // 使用imwrite函数保存图片 
            bool success = cv::imwrite(outputPath, src); 
            cnt += 1;
        }
        cv::imshow("test", src);
    }
}
