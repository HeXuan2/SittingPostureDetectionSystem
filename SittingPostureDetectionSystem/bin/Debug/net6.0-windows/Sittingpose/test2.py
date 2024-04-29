import tensorflow as tf

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)

with tf.device('/GPU:0'):
    import HunchFront
    import head
    import CrossLeg
    from joblib import load
    from PicProcess.SkeletonInfo import detect_pose
    from PIL import Image, ImageDraw, ImageFont
    import math
    import numpy as np
    import cv2
    import mediapipe as mp



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

    # 计算向量夹角
    def get_angle(vec1, vec2):
        len1 = math.sqrt(vec1[0] ** 2 + vec1[1] ** 2)
        len2 = math.sqrt(vec2[0] ** 2 + vec2[1] ** 2)
        cos_value = (vec1[0] * vec2[0] + vec1[1] * vec2[1]) / (len1 * len2)
        angle = math.acos(cos_value)
        return angle

    def distance(vec1, vec2):
        return math.sqrt((vec1.x - vec2.x) ** 2 + (vec1.y - vec2.y) ** 2)

    def check_if_hunched_over(keypoints):

        if keypoints is None:
            return 0, 0, 0

        # 获取髋部左右两侧和肩部左右两侧、膝盖左右两侧、鼻子这几个关键点
        hip_left = keypoints[23]
        hip_right = keypoints[24]
        left_shoulder = keypoints[11]
        right_shoulder = keypoints[12]
        knee_left = keypoints[25]
        knee_right = keypoints[26]
        nose = keypoints[0]
        mouth_left = keypoints[10]
        mouth_right = keypoints[9]
        eyeInner_right = keypoints[1]
        eyeOuter_right = keypoints[3]
        eye_right = keypoints[2]
        eye_left = keypoints[5]
        eyeInner_left = keypoints[4]
        eyeOuter_left = keypoints[6]

        print("yuan",keypoints[23])

        keypoints480And640 = [keypoints[23], keypoints[24], keypoints[11], keypoints[12],
                              keypoints[25], keypoints[26], keypoints[0], keypoints[10], keypoints[9],
                              keypoints[1], keypoints[2], keypoints[3], keypoints[4], keypoints[5], keypoints[6]]

        for i in range(len(keypoints480And640)):
            keypoints480And640[i][0] *= 480  # 将横坐标乘以 480
            keypoints480And640[i][1] *= 640  # 将纵坐标乘以 640

        print("hou",keypoints[23])



        # 计算膝关节到肩膀的距离
        distKneeToShoulder1 = np.sqrt((knee_left.x - left_shoulder.x) ** 2 + (knee_left.y - left_shoulder.y) ** 2)
        distKneeToShoulder2 = np.sqrt((knee_right.x - right_shoulder.x) ** 2 + (knee_right.y - right_shoulder.y) ** 2)
        distKneeToShoulder = max(distKneeToShoulder1, distKneeToShoulder2)  # 取最小值

        # 计算 11 23 25三个关键的夹角
        left_thigh_vec = [knee_left.x - hip_left.x,
                          knee_left.y - hip_left.y]
        right_thigh_vec = [knee_right.x - hip_right.x,
                           knee_right.y - hip_right.y]

        left_body_vec = [left_shoulder.x - hip_left.x,
                         left_shoulder.y - hip_left.y]
        right_body_vec = [right_shoulder.x - hip_left.x,
                          right_shoulder.y - hip_left.y]
        left_angle = get_angle(left_thigh_vec, left_body_vec)
        right_angle = get_angle(right_thigh_vec, right_body_vec)
        bodyAngle = max(left_angle, right_angle)

        # 计算脊椎中心点的坐标
        spine_center_x = (hip_left.x + hip_right.x + left_shoulder.x + right_shoulder.x) / 4
        spine_center_y = (hip_left.y + hip_right.y + left_shoulder.y + right_shoulder.y) / 4
        spine_center_z = (hip_left.z + hip_right.z + left_shoulder.z + right_shoulder.z) / 4
        spine_center = [spine_center_x, spine_center_y, spine_center_z]
        # print("spine_center_x, spine_center_y",spine_center_x, spine_center_y)

        # 计算臀部中心点、颈项中心点的坐标
        hip_center_x = (hip_left.x + hip_right.x) / 2
        hip_center_y = (hip_left.y + hip_right.y) / 2
        hip_center_z = (hip_left.z + hip_right.z) / 2
        hip_center = [hip_center_x, hip_center_y, hip_center_z]

        # print(" hip_center_x,hip_center_y", hip_center_x,hip_center_y)

        neck_center_x = nose.x
        neck_center_y = nose.y
        neck_center_z = nose.z
        neck_center = [neck_center_x, neck_center_y, neck_center_z]

        # 计算臀部中心点、脊椎中心点和颈项中心点构成的角度
        spine_angle = math.degrees(math.acos((neck_center_y - spine_center_y) / math.sqrt(
            (neck_center_x - spine_center_x) ** 2 + (neck_center_y - spine_center_y) ** 2)))

        # 计算嘴角到肩膀连线的垂直距离,变化不大，不适用
        # k = (right_shoulder.y - left_shoulder.y) / (right_shoulder.x - left_shoulder.x)
        # b = right_shoulder.y - k * right_shoulder.x
        # mouth_mid_x = (mouth_left.x + mouth_right.x) / 2
        # mouth_mid_y = (mouth_left.y + mouth_right.y) / 2
        # distMouthToShoulder = abs(k * mouth_mid_x - mouth_mid_y + b) / math.sqrt(k ** 2 + 1)

        # 计算眼睛的距离平均值
        dist1 = distance(eye_left, eyeInner_left)
        dist2 = distance(eye_left, eyeOuter_left)
        dist3 = distance(eye_right, eyeInner_right)
        dist4 = distance(eye_right, eyeOuter_right)
        distAverage = (dist1 + dist2 + dist3 + dist4) / 4

        return distKneeToShoulder, bodyAngle, spine_angle, distAverage


    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    # 初始化 MediaPipe 模型
    pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)
    cap = cv2.VideoCapture(1)
    new_height, new_width = 640, 480  # 设置新的分辨率

    while True:
        # 读取当前帧
        success, frame = cap.read()
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

        #print(keypoints)
        # pitch, yaw, roll = head.HeadInfo(frame)
        distKneeToShoulder, bodyAngle, spine_angle,distAverage =Hunch.check_if_hunched_over(keypoints)

        print("distKneeToShoulder, bodyAngle, spine_angle,distAverage",distKneeToShoulder, bodyAngle, spine_angle)

        if (distKneeToShoulder <= 620):
            print("塌腰")
            textHunch = '塌腰'
        else:
            print("正常坐姿")
            textHunch = '正常坐姿'

        cv2.putText(frame, f"distKneeToShoulder:{distKneeToShoulder}", (30, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
        cv2.putText(frame, f", bodyAngle:{bodyAngle}", (30, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255, 0, 0), 2)
        cv2.putText(frame, f"spine_angle:{spine_angle}", (30, 160), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255, 0, 0), 2)
        cv2.putText(frame, f"distAverage:{distAverage}", (30, 180), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

        # 显示结果
        cv2.imshow('frame',frame)

        # 按下 'q' 键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放资源
    cap.release()
    cv2.destroyAllWindows()
