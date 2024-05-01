#作者：TaoFighting1
#邮箱：1665636918@qq.com
#功能：本脚本用于


import os
import cv2
 
 #将其它格式的图片转为jpg格式,存疑
 
dataDir="E:/code_save_position/test/dede/"
saveDir="E:/code_save_position/test/dedede/"
if not os.path.exists(saveDir):
    os.makedirs(saveDir)
 
for one_pic in os.listdir(dataDir):
    one_path=dataDir+one_pic
    one_img=cv2.imread(one_path)
    new_path=saveDir+one_pic
    cv2.imwrite(new_path, one_img)