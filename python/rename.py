'''
把目标文件夹下的所有文件按照序号进行重命名
'''
import os
# 目标文件夹的路径
folder_path = 'C:\\Users\\dell\\Desktop\\A\\test\\'

files = os.listdir(folder_path)
# 将文件夹过滤掉
files = [file for file in files if os.path.isfile(os.path.join(folder_path, file))]

for index, file_name in enumerate(files):
    file_extension = os.path.splitext(file_name)[1]
    # 4位数字填充
    new_file_name = "%04d%s" % (index + 1, file_extension)
    old_path = os.path.join(folder_path, file_name)
    new_path = os.path.join(folder_path, new_file_name)
    os.rename(old_path, new_path)
    print("%s -> %s" % (file_name, new_file_name))
    
