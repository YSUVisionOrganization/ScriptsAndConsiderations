#作者：TaoFighting1
#邮箱：1665636918@qq.com
#功能：本脚本用于将Yolov5训练格式数据转为Yolox训练格式数据

import os

#yolov5_path="E:/code_save_position/test/yolov5"
yolov5_path="E:/model/yolov5/datasets/Armor/labels"

yolox_path="E:/code_save_position/test/yolox"

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
            reviseSigns=[]
            for col in signs:
                if(len(col)>8):
                    col=col[:8]
                reviseSigns.append(col)
            #print(reviseSigns)
            signal=reviseSigns[0]
            x_center=float(reviseSigns[1])
            y_center=float(reviseSigns[2])
            w=float(reviseSigns[3])
            h=float(reviseSigns[4])
            r_u_x=x_center+w/2
            r_u_y=y_center-h/2
            l_u_x=x_center-w/2
            l_u_y=y_center-h/2
            l_d_x=x_center-w/2
            l_d_y=y_center+h/2
            r_d_x=x_center+w/2
            r_d_y=y_center+h/2
            finished_sign=[]
            finished_sign.append(signal)
            finished_sign.append(format(r_u_x, '.6f'))
            finished_sign.append(format(r_u_y, '.6f'))
            finished_sign.append(format(l_u_x, '.6f'))
            finished_sign.append(format(l_u_y, '.6f'))
            finished_sign.append(format(l_d_x, '.6f'))
            finished_sign.append(format(l_d_y, '.6f'))
            finished_sign.append(format(r_d_x, '.6f'))
            finished_sign.append(format(r_d_y, '.6f'))
            #print(finished_sign)
            finish_text.append(' '.join(finished_sign))
        #print(finish_text)
        fw=open(destination_path+'/'+txt,"w")
        for fl in finish_text:
            fw.write(fl+"\n")
        fw.close()
        print(path+"->"+destination_path+'/'+txt)


        

txt_list=Input(yolov5_path)
Change(txt_list,yolov5_path,yolox_path)