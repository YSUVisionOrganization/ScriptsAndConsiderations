import os

def Change_Signal(position):
    files=os.listdir(position)
    i=0
    for file in files:
        print(i)
        i+=1
        txt_files=[]
        if file.endswith(".txt"):
            txt_files.append(file)
        for txt in txt_files:
            path=os.path.join(position,txt)
            f=open(path,'r')
            lines = f.readlines()
            line_list=[]
            for item in lines:
                signal=item.split(' ')
                print(signal) 
                signal[0]='30'
                signal[4]=signal[4][:8]
                print(signal) 
                s=""
                for j in signal:
                    s+=(j+' ')
                line_list.append(s)
            print(line_list)
            fw=open(path,'w')
            for change_list in line_list:
                fw.write(change_list+'\n')
            


re_position="E:\装甲板数据集\新建文件夹"
Change_Signal(re_position)