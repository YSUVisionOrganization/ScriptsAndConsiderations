#作者：TaoFighting1
#邮箱：1665636918@qq.com
#功能：本脚本用于将labelme出来的json文件转换为txt格式的

import json
import os
def count_category_ids(json_data):
    key = "shapes"
    valuee = json_data.get(key)  # 获取键对应的值
    output_data = []
    for shape in valuee:
        data=""
        data= f"{shape['label']}"
        Point=shape['points']
        for i in Point:
            for j in i:
                num = float(j)
                num=format(num, '.6f')
                data=f"{data} {num}"
        output_data.append(data)
    return output_data




# 定义文件夹路径
folder_path = "C:\\Users\\JYT\\Desktop\\ji1"

# 遍历文件夹中的文件
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):  # 仅处理 JSON 文件
        # 构建文件路径
        json_file_path = os.path.join(folder_path, filename)
        txt_file_path = os.path.join(folder_path, os.path.splitext(filename)[0] + '.txt')

        # 从 JSON 文件读取数据
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
        # 处理数据（这里只是一个示例，可以根据实际情况进行处理）
        output_data = count_category_ids(data)

        # 将数据写入 TXT 文件
        with open(txt_file_path, 'w') as txt_file:
           for item in output_data:
                txt_file.write(item + '\n')