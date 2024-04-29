# import tensorflow as tf
# physical_devices = tf.config.list_physical_devices('GPU')
# tf.config.experimental.set_memory_growth(physical_devices[0], True)

# with tf.device('/GPU:0'):

import math

import cv2
import mediapipe as mp
import numpy as np
from PicProcess.SkeletonInfo import detect_pose
from PIL import Image, ImageDraw, ImageFont
from joblib import load

def rotation_matrix_to_angles(rotation_matrix):
    """
    Calculate Euler angles from rotation matrix.
    :param rotation_matrix: A 3*3 matrix with the following structure
    [Cosz*Cosy  Cosz*Siny*Sinx - Sinz*Cosx  Cosz*Siny*Cosx + Sinz*Sinx]
    [Sinz*Cosy  Sinz*Siny*Sinx + Sinz*Cosx  Sinz*Siny*Cosx - Cosz*Sinx]
    [  -Siny             CosySinx                   Cosy*Cosx         ]
    :return: Angles in degrees for each axis
    """
    x = math.atan2(rotation_matrix[2, 1], rotation_matrix[2, 2])
    y = math.atan2(-rotation_matrix[2, 0], math.sqrt(rotation_matrix[0, 0] ** 2 +
                                                        rotation_matrix[1, 0] ** 2))
    z = math.atan2(rotation_matrix[1, 0], rotation_matrix[0, 0])
    return np.array([x, y, z]) * 180. / math.pi


mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5,
                                    min_tracking_confidence=0.5)

face_coordination_in_real_world = np.array([
            [285, 528, 200],
            [285, 371, 152],
            [197, 574, 128],
            [173, 425, 108],
            [360, 574, 128],
            [391, 425, 108]
        ], dtype=np.float64)

def HeadInfo(image):



    results = face_mesh.process(image)



    h, w, _ = image.shape
    face_coordination_in_image = []

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            for idx, lm in enumerate(face_landmarks.landmark):
                if idx in [1, 9, 57, 130, 287, 359]:
                    x, y = int(lm.x * w), int(lm.y * h)
                    face_coordination_in_image.append([x, y])

            face_coordination_in_image = np.array(face_coordination_in_image,
                                                    dtype=np.float64)

            # The camera matrix
            focal_length = 1 * w
            cam_matrix = np.array([[focal_length, 0, w / 2],
                                    [0, focal_length, h / 2],
                                    [0, 0, 1]])

            # The Distance Matrix
            dist_matrix = np.zeros((4, 1), dtype=np.float64)

            # Use solvePnP function to get rotation vector
            success, rotation_vec, transition_vec = cv2.solvePnP(
                face_coordination_in_real_world, face_coordination_in_image,
                cam_matrix, dist_matrix)

            # Use Rodrigues function to convert rotation vector to matrix
            rotation_matrix, jacobian = cv2.Rodrigues(rotation_vec)

            result = rotation_matrix_to_angles(rotation_matrix)

            # print(result)
            pitch = result[0]
            yaw = result[1]
            roll = result[2]
            return pitch,yaw,roll
    else:
        return 0,0,0

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
    # 使用外设摄像头
    video = cv2.VideoCapture(0)

    #导入视频
    # video = cv2.VideoCapture()
    # video.open('video/Normal1.mp4')
    modelHead = load('model3/model/ModelHead.pkl')

    mp_pose = mp.solutions.pose
    # 初始化 MediaPipe 模型
    pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)

    new_height, new_width = 640, 480  # 设置新的分辨率

    print(video.isOpened())

    while video.isOpened():
        success, frame = video.read()
        if not success:
            break
        pitch, yaw, roll = HeadInfo(frame)

        success, landmarks = detect_pose(frame, drawing=mp.solutions.drawing_utils)
        frame = cv2.resize(frame, (new_width, new_height))  # 缩放帧图像
        frame = cv2.flip(frame, 1)

        print("pitch, yaw, roll", pitch, yaw, roll)

        Headtest = [[pitch, yaw, roll]]
        Headprobs = modelHead.predict(Headtest)

        print("Headprobs",Headprobs)

        if Headprobs==1 or pitch<-20:
            print("低头")
            textHead='低头'
        elif Headprobs==2:
            print("歪脖")
            textHead = '歪脖'
        elif (Headprobs==3):
            print("伸脖子")
            textHead = '伸脖子'
        else :
            print("正常坐姿")
            textHead='正常坐姿'


        frame = cv2AddChineseText(frame, f"头部检测:{textHead}", (30, 00), (255, 0, 0), 20)
        frame = cv2AddChineseText(frame, f"头部检测:{ Headprobs}", (30, 20), (255, 0, 0), 20)
        frame = cv2AddChineseText(frame, f"pitch:{pitch}", (30, 100), (255, 0, 0), 20)
        frame = cv2AddChineseText(frame, f"yaw:{yaw}", (30, 120), (255, 0, 0), 20)
        frame = cv2AddChineseText(frame, f"roll:{roll}", (30, 140), (255, 0, 0), 20)


        # cv2.waitKey(int(3000 / video.get(cv2.CAP_PROP_FPS)))
        # 显示结果
        cv2.imshow('frame', frame)

        # 按下 'q' 键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放资源
    video.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
