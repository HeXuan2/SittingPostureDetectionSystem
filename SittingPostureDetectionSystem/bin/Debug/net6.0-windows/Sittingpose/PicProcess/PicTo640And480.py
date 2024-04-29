import os
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

def produceImage(file_in, width, height, file_out):
    image = Image.open(file_in)
    resized_image = image.resize((width, height), Image.LANCZOS)
    resized_image.save(file_out)


if __name__ == '__main__':
    file_in_path = '../images/12/'
    file_out_path = '../images/12/'
    if not os.path.exists(file_out_path):
        os.makedirs(file_out_path)
    lis = os.listdir(file_in_path)
    cnt = 1 #计数
    for file_name in lis:
        file_in = file_in_path + file_name
        # 分辨率
        height = 640
        width = 480
        #命名  这里也要改
        file_out = file_out_path + '3_' + str(cnt).rjust(4, '0') + '.jpg'
        print(file_out)
        cnt += 1
        produceImage(file_in, width, height, file_out)