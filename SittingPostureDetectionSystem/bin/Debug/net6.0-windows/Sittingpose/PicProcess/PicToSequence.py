import os
import cv2
import shutil




# 输入文件夹和输出文件夹路径
input_folder = '../images/Hunch/4'
output_folder = '../images/Hunch/4total'
label="4"
i=0


if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# 遍历输入文件夹中的所有子文件夹
for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.endswith('.jpg'):
            # 构造输出文件路径
            output_file_name = f'{label}_{i + 1:04d}.jpg'
            i=i+1
            output_file_path = os.path.join(output_folder, output_file_name)
            # 复制文件到输出文件夹中
            shutil.copy2(os.path.join(root, file), output_file_path)


















