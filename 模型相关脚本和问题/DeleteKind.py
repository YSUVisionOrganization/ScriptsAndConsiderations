#作者：TaoFighting1
#邮箱：1665636918@qq.com
#功能：本脚本用于删除数据集中某些类别

import os

yolov5_path="E:/code_save_position/test/de"

save_path="E:/model/yolov5/datasets/Armor/labels"
# save_path="E:/code_save_position/test/dedede"

def Input(original_path):
    files=os.listdir(original_path)
    txt_files=[]
    for file in files:
        if file.endswith('.txt'):
            txt_files.append(file)
           # print(txt_files)
    return txt_files

def Change(txt_list,original_path,destination_path):
    for txt in txt_list:
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
        for row in text:
            signs=row.split(' ')
            if int(signs[0])>23 and int(signs[0])<30 :
                continue
            else :
                if int(signs[0])==30:
                    signs[0]=str(24)
                finish_text.append(' '.join(signs))
        fw=open(destination_path+'/'+txt,"w")
        for fl in finish_text:
            fw.write(fl+"\n")
        fw.close()
        print(path+"->"+destination_path+'/'+txt)

x=Input(yolov5_path)
Change(x,yolov5_path,save_path)
