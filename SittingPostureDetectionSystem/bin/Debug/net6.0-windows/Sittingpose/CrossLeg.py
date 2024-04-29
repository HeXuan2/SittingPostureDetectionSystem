# import tensorflow as tf
# physical_devices = tf.config.list_physical_devices('GPU')
# tf.config.experimental.set_memory_growth(physical_devices[0], True)

# with tf.device('/GPU:0'):
import math
import cv2
import mediapipe as mp
import numpy as np
import HunchFront
import head
import CrossLeg
from joblib import load
from PicProcess.SkeletonInfo import detect_pose
from PIL import Image, ImageDraw, ImageFont
import os

# 计算向量夹角
def get_angle(vec1, vec2):
    len1 = math.sqrt(vec1[0] ** 2 + vec1[1] ** 2)
    len2 = math.sqrt(vec2[0] ** 2 + vec2[1] ** 2)
    cos_value = (vec1[0] * vec2[0] + vec1[1] * vec2[1]) / (len1 * len2)
    angle = math.acos(cos_value)
    return angle


# 定义向量叉积函数
def cross(vec1, vec2):
    return vec1[0] * vec2[1] - vec1[1] * vec2[0]


def get_intersection_point(vec_start1, vec_end1, vec_start2, vec_end2):
    """
    计算两条线段的交点
    :param vec_start1: tuple, 表示第一条线段的起点坐标
    :param vec_end1: tuple, 表示第一条线段的终点坐标
    :param vec_start2: tuple, 表示第二条线段的起点坐标
    :param vec_end2: tuple, 表示第二条线段的终点坐标
    :return: tuple or None, 表示交点的坐标，如果不存在交点则返回 None
    """
    # 计算线段的斜率和截距（点斜式）
    k1 = (vec_end1[1] - vec_start1[1]) / (vec_end1[0] - vec_start1[0]) if vec_end1[0] != vec_start1[0] else float(
        'inf')
    b1 = vec_start1[1] - k1 * vec_start1[0]

    k2 = (vec_end2[1] - vec_start2[1]) / (vec_end2[0] - vec_start2[0]) if vec_end2[0] != vec_start2[0] else float(
        'inf')
    b2 = vec_start2[1] - k2 * vec_start2[0]

    iscrossDot=1
    isInLine=1
    x=0
    y=0

    # 判断是否平行
    if k1 == k2:
        iscrossDot=0

    if(iscrossDot==1):
        # 计算交点的坐标
        if k1 == float('inf'):
            x = vec_start1[0]
            y = k2 * x + b2
        elif k2 == float('inf'):
            x = vec_start2[0]
            y = k1 * x + b1
        else:
            x = (b2 - b1) / (k1 - k2)
            y = k1 * x + b1

        # 判断交点是否在 vec_start1或者2上
        if x < vec_start1[0] or x > vec_end1[0] or y <vec_start1[1] or y >vec_end1[1]:
            isInLine=0
        if x < vec_start2[0] or x > vec_end2[0] or y <vec_start2[1] or y >vec_end2[1]:
            isInLine=0

    crossDot=[x,y]

    return crossDot


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


def CrossLegInfo(keypoints):

    if keypoints is None:
        return [0,0],0,[0,0],0,[0,0],0,0,[0,0],0,0

    hip_left = keypoints[23]
    hip_right = keypoints[24]
    knee_left = keypoints[25]
    knee_right = keypoints[26]
    ankle_left = keypoints[27]
    ankle_right = keypoints[28]


    keypoints480And640=[keypoints[23],keypoints[24],keypoints[25],keypoints[26],keypoints[27],keypoints[28]]

    for i in range(len(keypoints480And640)):
        keypoints480And640[i].x *= 480  # 将横坐标乘以 480
        keypoints480And640[i].y *= 640  # 将纵坐标乘以 640

    # 左大腿线段起始点
    vec_start_leftThigh = (hip_left.x, hip_left.y)
    vec_end_leftThigh = (knee_left.x, knee_left.y)
    #右边小腿线段起始点
    vec_start_rightCalf = (knee_right.x, knee_right.y)
    vec_end_rightCalf = (ankle_right.x,ankle_right.y)

    # 右大腿线段起始点
    vec_start_rightThigh = (hip_right.x, hip_right.y)
    vec_end_rightThigh = (knee_right.x, knee_right.y)
    # 左边小腿线段起始点
    vec_start_leftCalf = (knee_left.x, knee_left.y)
    vec_end_leftCalf = (ankle_left.x, ankle_left.y)


    #计算左大腿和右小腿的交点到左大腿的距离
    crossDot1=get_intersection_point(vec_start_leftThigh, vec_end_leftThigh, vec_start_rightCalf, vec_end_rightCalf)

    point1 = (crossDot1[0], crossDot1[1])
    distance1= point_to_vector_distance(point1,vec_start_leftThigh,vec_end_leftThigh)


    # 计算右大腿和左小腿的交点到右大腿的距离
    crossDot2 = get_intersection_point(vec_start_rightThigh, vec_end_rightThigh,vec_start_leftCalf, vec_end_leftCalf)

    point2 = (crossDot2[0], crossDot2[1])
    distance2 = point_to_vector_distance(point2,vec_start_rightThigh,vec_end_rightThigh)

    #计算左右小腿的交点并判断是否在左小腿或者右小腿上

    # 计算右小腿和左小腿的交点到左右小腿距离的最小值
    crossDot3 = get_intersection_point(vec_start_leftCalf, vec_end_leftCalf, vec_start_rightCalf,vec_end_rightCalf)
    point3=(crossDot3[0],crossDot3[1])
    distance31= point_to_vector_distance(point3, vec_start_leftCalf, vec_end_leftCalf)
    distance32 = point_to_vector_distance(point3, vec_start_rightCalf,vec_end_rightCalf)
    distance3 = min(distance32,distance32)

    #两个膝盖中心点
    knee_mid=[(knee_left.x+knee_right.x)/2,(knee_right.y+knee_left.y)/2]

    #小腿交点到膝盖中心点的距离
    distance4=math.sqrt((crossDot3[0] - knee_mid[0])**2 + (crossDot3[1] - knee_mid[1])**2)

    #计算左右大腿的交点到左右大腿的最小值

    crossDot5 = get_intersection_point(vec_start_leftThigh, vec_end_leftThigh,
                                                                vec_start_rightThigh, vec_end_rightThigh)
    point5 = (crossDot5[0], crossDot5[1])
    distance51 = point_to_vector_distance(point3, vec_start_leftThigh, vec_end_leftThigh)
    distance52 = point_to_vector_distance(point3, vec_start_rightThigh, vec_end_rightThigh)
    distance5 = min(distance31, distance32)

    # 大腿交点到膝盖中心点的距离
    distance6= math.sqrt((crossDot5[0] - knee_mid[0]) ** 2 + (crossDot5[1] - knee_mid[1]) ** 2)


    return crossDot1,distance1,crossDot2,distance2,crossDot3,distance3,distance4, crossDot5,distance5,distance6


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

    #采用直接导入视频的方式
    video = cv2.VideoCapture()
    # video.open('video/CrossLegHuangLi3.mp4')
    # video.open('video/CrossLegHuangLi.mp4')

    video.open('video/CrossLegHuangLi2.mp4')



    #采用外设摄像头
    # video = cv2.VideoCapture(0)


    modelCrossLeg = load('update/rf_model_CrossLeg_1.joblib')



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

        crossDot1,distance1, crossDot2,distance2,crossDot3,distance3,distance4,crossDot5,distance5,\
            distance6 =CrossLegInfo(keypoints)
        print("crossDot1,distance1,crossDot2,distance2"
                "crossDot3 ,distance3,distance4, crossDot5,distance5,\
            distance6",
                crossDot1,distance1,
                crossDot2,distance2,
                crossDot3,distance4,crossDot5,distance5,\
            distance6)

        mindist=min(distance1,distance2)

        CrossLegtest = [[distance1, distance2, distance3, distance4, distance5, distance6]]
        CrossLegprobs = modelCrossLeg.predict(CrossLegtest)

        print("CrossLegprobs", CrossLegprobs)

        if (CrossLegprobs == 5 or (distance4<300 and distance6<300)):
            print("跷二郎腿")
            textCrossLeg = '跷二郎腿'
        else:
            print("正常坐姿")
            textCrossLeg = '正常坐姿'

        # if (mindist<2 and distance3<2 and distance4<300 and distance6<300) or ((mindist<2 and distance3<2 and distance4<300 and distance6<300) and CrossLegprobs==5) :
        #     print("跷二郎腿")
        #     textCrossLeg = '跷二郎腿'
        #
        # else:
        #     print("正常坐姿")
        #     textCrossLeg = '正常坐姿'

        frame = cv2AddChineseText(frame, f"翘二郎腿检测:{textCrossLeg}", (30, 120), (255, 0, 0), 20)
        frame = cv2AddChineseText(frame, f"distance1:{distance1}", (30, 140), (255, 0, 0), 20)
        frame = cv2AddChineseText(frame, f"distance2:{distance2}", (30, 160), (255, 0, 0), 20)
        frame = cv2AddChineseText(frame, f"distance3:{distance3}", (30, 180), (255, 0, 0), 20)
        frame = cv2AddChineseText(frame, f"distance4:{distance4}", (30, 200), (255, 0, 0), 20)
        frame = cv2AddChineseText(frame, f"distance6:{distance6}", (30, 220), (255, 0, 0), 20)
        frame = cv2AddChineseText(frame, f"CrossLegprobs:{CrossLegprobs}", (30, 240), (255, 0, 0), 20)



        x=int(crossDot1[0])
        y=int(crossDot1[1])
        cv2.circle(frame,(x,y),1,(0,0,255),5)

        x = int(crossDot2[0])
        y = int(crossDot2[1])
        cv2.circle(frame, (x, y), 1, (0, 0, 255), 5)

        x = int(crossDot3[0])
        y = int(crossDot3[1])
        cv2.circle(frame, (x, y), 1, (0, 255, 255), 5)

        x = int(crossDot5[0])
        y = int(crossDot5[1])
        cv2.circle(frame, (x, y), 1, (255, 0, 0), 5)


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