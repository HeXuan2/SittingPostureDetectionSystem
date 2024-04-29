
# 视频分解图片
# 1 load 2 info 3 parse 4 imshow imwrite
import cv2

import os
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


filePath = '../video/'

outPutDirName = '../images/51/5/'  # 设置保存路径
# 改这
cap = cv2.VideoCapture(filePath + 'CrossLegLiuRui2.mp4')
#改这
cnt =48#编号
#要输出的标签号
label="5"


lis = os.listdir(filePath)
isOpened = cap.isOpened # 判断是否打开‘
print(isOpened)

# 获取信息 宽高
n_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print('总帧数：',n_frame) # 整个视频的总帧数
fps = cap.get(cv2.CAP_PROP_FPS) # 帧率 每秒展示多少张图片
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # w
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # h
print('帧数、宽度、高度分别为：',fps,width,height) # 帧率 宽 高

# 分辨率
height = 640
width = 480
i = 0 # 记录读取多少帧


frameFrequency = 4# 每frameFrequency保存一张图片
while(isOpened):
        # 结束标志是否读取到最后一帧
    if i == n_frame:
        break
    else:
        i = i+1
    (flag,frame) = cap.read() # read方法 读取每一张 flag是否读取成功 frame 读取内容
    frame = cv2.resize(frame, (480, 640))  # 调整图像大小为目标大小

    if not os.path.exists(outPutDirName):
            # 如果文件目录不存在则创建目录
        os.makedirs(outPutDirName)
    if i % frameFrequency == 0:
        cnt = cnt + 1
        if cnt<10:
            fileName = label+'_000' + str(cnt) + '.jpg'  # 名字累加
            # True表示读取成功 进行·写入
        elif cnt < 100:
            fileName = label+'_00' + str(cnt) + '.jpg'  # 名字累加
            # True表示读取成功 进行·写入
        else:
            fileName = label+'_0' + str(cnt) + '.jpg'

        print(outPutDirName+fileName)

        cv2.imwrite(outPutDirName+fileName,frame,[cv2.IMWRITE_JPEG_QUALITY,100])# 质量控制 100最高

print('end!')