#作者：TaoFighting1
#邮箱：1665636918@qq.com
#功能：本脚本用于将图片进行统一命名

#存在有问题


import os

def rename_files(folder_path, new_filename_format):
    t=2466
    # 遍历指定文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 构建旧文件路径和新文件路径
        old_file_path = os.path.join(folder_path, filename)
        t+=1
        # 判断路径是否为文件
        if os.path.isfile(old_file_path):
            rt=str(t).rjust(6,'0')
            if(filename.endswith(".jpg")):
                new_file_path = os.path.join(folder_path,rt+'.jpg')
            if(filename.endswith(".png")):
                new_file_path = os.path.join(folder_path,rt+'.png')
            # 执行文件名修改
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {old_file_path} -> {new_file_path}")

# 调用示例
folder_path = "E:\ArmorData\zi2"
new_filename_format = ""  # 使用大括号 {} 表示文件名的位置

rename_files(folder_path, new_filename_format)