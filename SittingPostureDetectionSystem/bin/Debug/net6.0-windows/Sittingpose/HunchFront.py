# import tensorflow as tf

# physical_devices = tf.config.list_physical_devices('GPU')
# tf.config.experimental.set_memory_growth(physical_devices[0], True)

# with tf.device('/GPU:0'):
import math
import numpy as np
import cv2
import mediapipe as mp
from joblib import load
from PicProcess.SkeletonInfo import detect_pose
from PIL import Image, ImageDraw, ImageFont
# 计算向量夹角
def get_angle(vec1, vec2):
    len1 = math.sqrt(vec1[0] ** 2 + vec1[1] ** 2)
    len2 = math.sqrt(vec2[0] ** 2 + vec2[1] ** 2)
    cos_value = (vec1[0] * vec2[0] + vec1[1] * vec2[1]) / (len1 * len2)
    angle = math.acos(cos_value)
    return angle


def distance(vec1, vec2):
    return math.sqrt((vec1.x- vec2.x) ** 2 + (vec1.y - vec2.y) ** 2)

def point_to_vector_distance(point, vec_start, vec_end):
    """
    计算点到向量的距离
    :param point: tuple, 表示一个点的坐标, 例如 (1, 2)
    :param vec_start: tuple, 表示向量起点的坐标, 例如 (0, 0)
    :param vec_end: tuple, 表示向量终点的坐标, 例如 (3, 4)
    :return: float, 表示点到向量的距离
    """
    # 计算向量的方向向量
    vec_direction = (vec_end[0] - vec_start[0], vec_end[1] - vec_start[1])
    vec_direction_len = math.sqrt(vec_direction[0] ** 2 + vec_direction[1] ** 2)  # 计算向量的模长
    vec_direction = (vec_direction[0] / vec_direction_len, vec_direction[1] / vec_direction_len)  # 计算向量的方向向量

    # 计算垂线的长度
    ap = (point[0] - vec_start[0], point[1] - vec_start[1])
    ap_dot = ap[0] * vec_direction[0] + ap[1] * vec_direction[1]
    perpendicular_len = abs(ap_dot / vec_direction_len)

    return perpendicular_len


# 计算腰部高度
def HunchInfo(keypoints):

    if keypoints is None:
        return 0,0,0,0

    left_shoulder = keypoints[12]
    right_shoulder = keypoints[11]
    eyeInner_right=keypoints[1]
    eyeOuter_right=keypoints[3]
    eye_right=keypoints[2]
    eye_left=keypoints[5]
    eyeInner_left = keypoints[4]
    eyeOuter_left = keypoints[6]
    mounth_left=keypoints[10]
    mounth_right=keypoints[9]
    nose=keypoints[0]


    keypoints480And640=[keypoints[0],keypoints[11],keypoints[12],keypoints[1],keypoints[2],keypoints[3],
                        keypoints[4],keypoints[5],keypoints[6],keypoints[9],keypoints[10]]

    for i in range(len(keypoints480And640)):
        keypoints480And640[i].x *= 480  # 将横坐标乘以 480
        keypoints480And640[i].y *= 640  # 将纵坐标乘以 640

    #当人面向电脑时，用这个阈值去限制
    # 计算眼睛的距离平均值
    dist1=distance(eye_left,eyeInner_left)
    dist2=distance(eye_left,eyeOuter_left)
    dist3=distance(eye_right,eyeInner_right)
    dist4=distance(eye_right,eyeOuter_right)
    distAverage=(dist1+dist2+dist3+dist4)/4

    #计算两个肩膀的距离值
    distShoulder=distance(left_shoulder,right_shoulder)

    #计算嘴巴和肩膀的垂直距离
    # 定义两个向量
    point1 = [abs((mounth_left.x-mounth_right.x)/2), abs((mounth_left.y-mounth_right.y))/2]
    point2 = [abs(left_shoulder.x-right_shoulder.x)/2,abs(left_shoulder.y-right_shoulder.y)/2]

    # 计算两点之间的距离
    distMounthToShoulder =math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
    #鼻子到嘴的距离
    nosePoint=[nose.x,nose.y]
    mounth_start=[(mounth_left.x-mounth_right.x)/2,(mounth_left.y-mounth_right.y)/2]
    # 计算两点之间的距离
    distNoseToMounth= math.sqrt((nosePoint[0] - mounth_start[0]) ** 2 + (nosePoint[1] - mounth_start[1]) ** 2)


    return distAverage,distShoulder,distMounthToShoulder,distNoseToMounth


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


def main():

    # video = cv2.VideoCapture()
    # video.open('video/Hunch1.mp4')
    # video.open('video/Hunch2.mp4')
    # video.open('video/Hunch6.mp4')
    video = cv2.VideoCapture(0)


    modelCrossLeg = load('update/rf_model_Hunch_1.joblib')


    mp_pose = mp.solutions.pose
    # 初始化 MediaPipe 模型
    pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)

    new_height, new_width = 640, 480  # 设置新的分辨率

    while video.isOpened():
        success, frame = video.read()
        if not success:
            break

        success, landmarks = detect_pose(frame, drawing=mp.solutions.drawing_utils)
        frame = cv2.resize(frame, (new_width, new_height))  # 缩放帧图像
        frame = cv2.flip(frame, 1)

        # 使用 MediaPipe 模型检测关键点
        results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        # 获取关键点坐标
        if results.pose_landmarks is not None:
            keypoints = results.pose_landmarks.landmark
        else:
            keypoints = None  # 根据实际情况进行处理

        distAverage, distShoulder,distMounthToShoulder,distNoseToMounth=HunchInfo(keypoints)
        print("distAverage, distShoulder,distMounthToShoulder,distNoseToMounth",distAverage, distShoulder,distMounthToShoulder,distNoseToMounth)


        Hunchtest = [[distAverage, distShoulder,distMounthToShoulder,distNoseToMounth]]
        Hunchprobs = modelCrossLeg.predict(Hunchtest)

        print("Hunchprobs ",Hunchprobs )

        if (Hunchprobs == 4  ):
            print("塌腰")
            textHunch = '塌腰'
        else:
            print("正常坐姿")
            textHunch = '正常坐姿'


        frame = cv2AddChineseText(frame, f"塌腰检测:{textHunch}", (30, 120), (255, 0, 0), 20)
        frame = cv2AddChineseText(frame, f"distAverage:{distAverage}", (30, 140), (255, 0, 0), 20)
        frame = cv2AddChineseText(frame, f"distShoulder:{distShoulder}", (30, 160), (255, 0, 0), 20)
        frame = cv2AddChineseText(frame, f"distMounthToShoulder:{distMounthToShoulder}", (30, 200), (255, 0, 0), 20)
        frame = cv2AddChineseText(frame, f"distNoseToMounth:{distNoseToMounth}", (30, 220), (255, 0, 0), 20)
        frame = cv2AddChineseText(frame, f"Hunchprobs:{Hunchprobs}", (30, 180), (255, 0, 0), 20)

        # cv2.waitKey(int(2000 / video.get(cv2.CAP_PROP_FPS)))
        # 显示结果
        cv2.imshow('frame',frame)

        # 按下 'q' 键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放资源
    video.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
