#作者：TaoFighting1
#邮箱：1665636918@qq.com
#功能：本脚本用于将数据集标注信息在图片中展示

import os
import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as pat
import cv2 as cv
from PIL import Image, ImageDraw

name="001938"

img_path="E:/model/YOLOX-main(WASTE)/datasets/VOCdevkit1/VOC2007/JPEGImages/"+name+".jpg"
txt_path="E:/model/yolov5/datasets/Armor/labels/"+name+".txt"
# txt_path="C:/Users/JYT/Desktop/DesktopPremier/TUP/datasets/data_latest/labels/four203.txt"
# img_path="C:/Users/JYT/Desktop/DesktopPremier/TUP/datasets/data_latest/images/four203.jpg"

src_img=cv2.imread(img_path)

img_matplot = plt.imread(img_path)
height=img_matplot.shape[0]
width=img_matplot.shape[1]
print(str(height)+" "+str(width))


f=open(txt_path,encoding='utf-8')
txt=f.readlines()

for line in txt:
    data=line.split(' ')
    center_x=width*float(data[1])
    center_y=height*float(data[2])
    w=width*float(data[3])/2
    h=height*float(data[4])/2
    # print(center_x)
    # print(center_y)
    # print(h)
    # print(w)
    cv.rectangle(src_img, (int(center_x-w), int(center_y-h)), (int(center_x+w), int(center_y+h)), (0, 0, 255), 2)
    # cv.rectangle(src_img, (int(width*float(data[3])), int(height*float(data[4]))), (int(width*float(data[7])), int(height*float(data[8]))), (0, 0, 255), 2)
    # cv.rectangle(src_img, (int(width*float(data[1])), int(height*float(data[2]))), (int(width*float(data[5])), int(height*float(data[6]))), (0, 0, 255), 2)
    #cv.rectangle(src_img, (int(width*float(data[3])), int(height*float(data[4]))), (int(width*float(data[1])), int(height*float(data[2]))), (0, 0, 255), 2)

# rectangle 坐标的参数格式为左上角（x1, y1），右下角（x2, y2）。

cv.namedWindow('img', cv.WINDOW_NORMAL)
cv.imshow('img', src_img)
cv.waitKey(0)
