#作者：TaoFighting1
#邮箱：1665636918@qq.com
#功能：本脚本用于删除数据集中某些类别

import os

# yolov5_path="E:/数据/5月装甲板/blue_4_长_50"
yolov5_path="E:/model/yolov5/datasets/Armor1labels"

# save_path="E:/model/YOLOX-main/datasets/yolo"
# save_path="E:/code_save_position/test/dedede"
save_path="E:/model/yolov5/datasets/innovation/label"


def Input(original_path):
    files=os.listdir(original_path)
    txt_files=[]
    for file in files:
        if file.endswith('.txt'):
            txt_files.append(file)
           # print(txt_files)
    return txt_files

def Change(txt_list,original_path,destination_path):
    # max_num=0
    num=0
    for txt in txt_list:
        # num=num+1
        path=os.path.join(original_path,txt)
      #  print(path)
        f=open(path,encoding='utf-8')
        lines=f.readlines()
        text=[]
        for line in lines:
            if line.isspace():
                continue
            else:
                line=line.replace("\n","")
                line=line.replace("\t","")
                text.append(line)
        finish_text=[]
        # for row in text:
        #     signs=row.split(' ')
        #     if int(signs[0])==22:
        #         num=21
        # print(str(num))

        for row in text:
            signs=row.split(' ')
            # if int(signs[0])==0 or int(signs[0])==3 :
            #     continue
            if int(signs[0])==24 :
                signs[0]=str(23)
            # if int(signs[0])==1 :
            #     signs[0]=str(0)
            # if int(signs[0])==2 :
            #     signs[0]=str(1)
            # if int(signs[0])==5 :
            #     signs[0]=str(1)
            # elif int(signs[0])==1:
            #     signs[0]=str(2)
            # signs[0]=str(int(24))
            finish_text.append(' '.join(signs))
        fw=open(destination_path+'/'+txt,"w")
        for fl in finish_text:
           fw.write(fl+"\n")
        fw.close()
        print(path+"->"+destination_path+'/'+txt)

x=Input(yolov5_path)
Change(x,yolov5_path,yolov5_path)
