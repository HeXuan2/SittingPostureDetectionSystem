找原图的

import os
import shutil

# 定义文件夹1和文件夹2的路径
folder1_path = 'images/input'
folder2_path = 'images/HaoDe'

# 定义输出文件夹的路径
output_folder_path = 'images/OriginGoodImage'

# 如果输出文件夹存在，则先删除该文件夹及其所有内容
if os.path.exists(output_folder_path):
    shutil.rmtree(output_folder_path)

# 创建输出文件夹
os.mkdir(output_folder_path)

# 获取文件夹1和文件夹2中的文件名列表
folder1_files = os.listdir(folder1_path)
folder2_files = os.listdir(folder2_path)

# 将两个文件夹中的文件名都转换为小写字母，以便比较
folder1_files_lower = [file.lower() for file in folder1_files]
folder2_files_lower = [file.lower() for file in folder2_files]

# 遍历文件夹1中的每一个文件，如果该文件也存在于文件夹2中，则将该文件复制到输出文件夹中
for i, file_name in enumerate(folder1_files):
    if file_name.lower() in folder2_files_lower:
        file_path1 = os.path.join(folder1_path, file_name)
        file_path2 = os.path.join(folder2_path, folder2_files[folder2_files_lower.index(file_name.lower())])
        output_file_path = os.path.join(output_folder_path, file_name)
        # 如果两个文件相同，则跳过
        if file_path1 == file_path2:
            continue
        # 复制文件到输出文件夹中
        shutil.copy(file_path1, output_file_path)
        print(f'已复制第{i+1}个文件到输出文件夹中。')

print('所有操作已完成！')