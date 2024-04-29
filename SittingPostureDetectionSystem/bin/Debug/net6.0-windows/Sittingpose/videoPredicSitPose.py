import sys

# import tensorflow as tf
#
# from update.CNNtestFinal import Model
#
# physical_devices = tf.config.list_physical_devices('GPU')
# tf.config.experimental.set_memory_growth(physical_devices[0], True)
#
# with tf.device('/GPU:0'):
import HunchFront
import head
import CrossLeg
from joblib import load
from PicProcess.SkeletonInfo import detect_pose
from PIL import Image, ImageDraw, ImageFont
import cv2
import mediapipe as mp
import numpy as np

# font = cv2.FONT_HERSHEY_SIMPLEX
# font_path = "SimHei.ttf"


# 加载预训练模型

modelHead = load('model3/model/ModelHead.pkl')
modelHunch = load('update/rf_model_Hunch_1.joblib')
modelCrossLeg = load('update/rf_model_CrossLeg_1.joblib')
# modelHunch = load('model3/model/ModelHunch.pkl')
# modelCrossLeg=load('model3/model/ModelCrossLeg.pkl')

# model = Model()
# model.load_state_dict(torch.load("update/modelf.pth"))



def cv2AddChineseText(img, text, position, textColor=(0, 255, 0), textSize=30):
    if (isinstance(img, np.ndarray)):  # 判断是否OpenCV图片类型
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)
    # 字体的格式
    fontStyle = ImageFont.truetype(
        "simsun.ttc", textSize, encoding="utf-8")
    # 绘制文本
    draw.text(position, text, textColor, font=fontStyle)
    # 转换回OpenCV格式
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)


mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# 初始化 MediaPipe 模型
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# 用外设摄像头
cap = cv2.VideoCapture(1)
cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame', 480,640)

# 导入视频
# cap = cv2.VideoCapture()
# cap.open('video/CrossLegHuangLi3.mp4')


# new_height, new_width = 640, 480  # 设置新的分辨率

while cap.isOpened():
    # 读取当前帧
    success, frame = cap.read()
    if not success:
        break

    pitch, yaw, roll = head.HeadInfo(frame)

    success, landmarks = detect_pose(frame, drawing=mp.solutions.drawing_utils)

    # frame = cv2.resize(frame, (new_width, new_height))  # 缩放帧图像
    frame = cv2.flip(frame, 1)

    # 使用 MediaPipe 模型检测关键点

    results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # 获取关键点坐标
    if results.pose_landmarks is not None:
        keypoints = results.pose_landmarks.landmark
    else:
        keypoints = None  # 根据实际情况进行处理

    # print("pitch, yaw, roll", pitch, yaw, roll)

    Headtest = [[pitch, yaw, roll]]

    # pred_x =[pitch, yaw, roll]
    # pred_x = torch.Tensor(pred_x)
    # outputs = model(pred_x)
    # max_idx = torch.argmax(outputs)
    #
    # print(max_idx)
    #
    # print("Headprobs",max_idx)
    #
    # if max_idx == 1 or pitch < -20:
    #     print("低头")
    #     textHead = '低头'
    # elif max_idx == 2:
    #     print("歪脖")
    #     textHead = '歪脖'
    # elif (max_idx == 3):
    #     print("伸脖子")
    #     textHead = '伸脖子'
    # else:
    #     print("正常坐姿")
    #     textHead = '正常坐姿'
    #
    # frame = cv2AddChineseText(frame, f"头部检测:{textHead}", (30, 100), (255, 0, 0), 20)


    Headprobs = modelHead.predict(Headtest)

    # print("Headprobs", Headprobs)

    if Headprobs == 1 or pitch < -20:
        print(1)
        sys.stdout.flush()
        # print("低头")
        textHead = '低头'
    elif Headprobs == 2:
        print(2)
        sys.stdout.flush()
        # print("歪脖")
        textHead = '歪脖'
    elif (Headprobs == 3):
        print(3)
        sys.stdout.flush()
        # print("伸脖子")
        textHead = '伸脖子'
    else:
        sys.stdout.flush()
        # print("正常坐姿")
        textHead = '正常坐姿'

    # frame = cv2AddChineseText(frame, f"头部检测:{textHead}", (30, 120), (255, 0, 0),40)

    frame = cv2AddChineseText(frame, f"头部检测:{textHead}", (30, 100), (255, 0, 0), 20)


    distAverage, distShoulder, distMounthToShoulder, distNoseToMounth =HunchFront.HunchInfo(keypoints)
    # print("distAverage, distShoulder,distMounthToShoulder,distNoseToMounth", distAverage, distShoulder,
    #       distMounthToShoulder, distNoseToMounth)

    Hunchtest = [[distAverage, distShoulder, distMounthToShoulder, distNoseToMounth]]
    Hunchprobs = modelHunch.predict(Hunchtest)

    # print("Hunchprobs ", Hunchprobs)

    if (Hunchprobs == 4):
        print(4)
        sys.stdout.flush()
        # print("塌腰")
        textHunch = '塌腰'
    else:

        sys.stdout.flush()
        # print("正常坐姿")
        textHunch = '正常坐姿'

    # frame = cv2AddChineseText(frame, f"塌腰检测:{textHunch}", (30, 160), (255, 0, 0), 40)
    frame = cv2AddChineseText(frame, f"塌腰检测:{textHunch}", (30, 120), (255, 0, 0), 20)

    crossDot1, distance1, crossDot2, distance2, crossDot3, distance3, distance4, crossDot5, distance5,distance6 = CrossLeg.CrossLegInfo(keypoints)
    # print("crossDot1,distance1,crossDot2,distance2"
    #       "crossDot3 ,distance3,distance4, crossDot5,distance5,\
    #     distance6",
    #       crossDot1, distance1,
    #       crossDot2, distance2,
    #       crossDot3, distance4, crossDot5, distance5, \
    #       distance6)


    CrossLegtest = [[distance1, distance2, distance3, distance4, distance5, distance6]]
    CrossLegprobs = modelCrossLeg.predict(CrossLegtest)

    # print("CrossLegprobs", CrossLegprobs)

    if (CrossLegprobs == 5 or (distance4 < 300 and distance6 < 300)):
        print(5)
        sys.stdout.flush()
        # print("跷二郎腿")
        textCrossLeg = '跷二郎腿'
    else:

        sys.stdout.flush()
        # print("正常坐姿")
        textCrossLeg = '正常坐姿'


    if (Hunchprobs==0 and Headprobs==0 and CrossLegprobs==0):
        print(0)
        sys.stdout.flush()



    # frame = cv2AddChineseText(frame, f"翘二郎腿检测:{textCrossLeg}", (30, 200), (255, 0, 0), 40)
    frame = cv2AddChineseText(frame, f"翘二郎腿检测:{textCrossLeg}", (30, 140), (255, 0, 0), 20)

    x = int(crossDot1[0])
    y = int(crossDot1[1])
    cv2.circle(frame, (x, y), 1, (0, 0, 255), 5)

    x = int(crossDot2[0])
    y = int(crossDot2[1])
    cv2.circle(frame, (x, y), 1, (0, 0, 255), 5)

    x = int(crossDot3[0])
    y = int(crossDot3[1])
    cv2.circle(frame, (x, y), 1, (0, 255, 255), 5)

    x = int(crossDot5[0])
    y = int(crossDot5[1])
    cv2.circle(frame, (x, y), 1, (255, 0, 0), 5)

    # 显示结果
    cv2.imshow('frame',frame)

    # 按下 'q' 键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()
