import rarfile
def decompress_rar():
	# 找到rar文件
    z = rarfile.RarFile(r'E:\Python脚本\作业查重\2015090103石凯-新闻管理系统.rar')  
    # 指定解压输出的目录
    z.extractall(r'E:\Python脚本\作业查重\2015090103石凯-新闻管理系统')  
    z.close()
    # 删除压缩文件
    # os.remove(pathRar)
