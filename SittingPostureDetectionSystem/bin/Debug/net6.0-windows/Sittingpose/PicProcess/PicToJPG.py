from PIL import Image
import os

# 原始图片所在文件夹路径
input_folder = 'images/NoSeqPic/c_upscayled (3)'
# 转换后的图片保存路径
output_folder = 'images/NoSeqPic/c'

# 如果输出文件夹不存在，则创建该文件夹
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历原始图片文件夹中的所有图片，并将它们转换为 jpg 格式
for file_name in os.listdir(input_folder):
    # 构造输入文件的完整路径
    file_path = os.path.join(input_folder, file_name)

    # 如果当前文件是图片且不是 jpg 格式，则转换为 jpg 格式并保存
    if os.path.isfile(file_path) and file_name.lower().endswith(('.png', '.jpeg', '.bmp', '.gif')):
        img = Image.open(file_path)
        output_file_path = os.path.join(output_folder, f'{os.path.splitext(file_name)[0]}.jpg')
        img.convert('RGB').save(output_file_path, format='JPEG')

print('Done.')
