#作者：TaoFighting1
#邮箱：1665636918@qq.com
#功能：本脚本用于将labelme产出的标注信息，将大小转换为百分比大小
#存在缺陷：只能转换同一大小的图片


import os

def process_file(file_path):
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split()
            processed_data = [data[0]]  # 保留第一个数不做处理
            for i in range(1, len(data)):
                if i % 2 == 1:  # 奇数位除以1440
                    num = float(data[i]) / 1280
                    num=format(num, '.6f')
                    processed_data.append(str(num))
                else:  # 偶数位除以810
                    num = float(data[i]) / 1024
                    num=format(num, '.6f')
                    processed_data.append(str(num))
            processed_line = ' '.join(processed_data) + '\n'
            lines.append(processed_line)
    
    with open(file_path, 'w') as file:
        file.writelines(lines)

def process_files_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            process_file(file_path)

# 用法示例
folder_path = "C:/Users/JYT/Desktop/jyt"  # 替换为实际的文件夹路径
process_files_in_directory(folder_path)