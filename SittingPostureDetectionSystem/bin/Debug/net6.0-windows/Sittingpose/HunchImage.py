
import tensorflow as tf

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)

with tf.device('/GPU:0'):
    import math
    import numpy as np
    import cv2
    import mediapipe as mp
    from PicProcess.SkeletonInfo import drawSkeletonSingelImage


    # 计算向量夹角
    def get_angle(vec1, vec2):
        len1 = math.sqrt(vec1[0] ** 2 + vec1[1] ** 2)
        len2 = math.sqrt(vec2[0] ** 2 + vec2[1] ** 2)
        cos_value = (vec1[0] * vec2[0] + vec1[1] * vec2[1]) / (len1 * len2)
        angle = math.acos(cos_value)
        return angle

    # 计算
    def compute_waist_height(keypoints):
        # 获取脊椎中心、髋部左右两侧和肩部左右两侧这几个关键点
        hip_left= keypoints[23]
        hip_right= keypoints[24]
        left_shoulder = keypoints[11]
        right_shoulder = keypoints[12]
        knee_left = keypoints[25]
        knee_right = keypoints[26]
        nose=keypoints[0]

        hip_left.x = hip_left.x * 480
        hip_right.x = hip_right.x * 480
        left_shoulder.x = left_shoulder.x * 480
        right_shoulder.x = right_shoulder.x * 480
        knee_left.x = knee_left.x * 480
        knee_right.x = knee_right.x * 480
        nose.x = nose.x * 480

        hip_left.y = hip_left.y * 640
        hip_right.y = hip_right.y * 640
        left_shoulder.y = left_shoulder.y * 640
        right_shoulder.y = right_shoulder.y * 640
        knee_left.y = knee_left.y * 640
        knee_right.y = knee_right.y * 640
        nose.y = nose.y * 640

        #计算膝关节到肩膀的距离
        distKneeToShoulder1= np.sqrt(( knee_left.x - left_shoulder.x) ** 2 + (knee_left.y - left_shoulder.y) ** 2)
        distKneeToShoulder2 = np.sqrt((knee_right.x - right_shoulder.x) ** 2 + (knee_right.y - right_shoulder.y) ** 2)
        distKneeToShoulder = max( distKneeToShoulder1,distKneeToShoulder2)  # 取最小值

        #计算 11 23 25三个关键的夹角
        left_thigh_vec = [knee_left.x - hip_left.x,
                          knee_left.y - hip_left.y]
        right_thigh_vec = [knee_right.x - hip_right.x,
                           knee_right.y - hip_right.y]

        left_body_vec= [left_shoulder.x - hip_left.x,
                          left_shoulder.y - hip_left.y]
        right_body_vec=[right_shoulder.x - hip_left.x,
                          right_shoulder.y - hip_left.y]
        left_angle = get_angle(left_thigh_vec, left_body_vec)
        right_angle = get_angle(right_thigh_vec, right_body_vec)

        bodyAngle=max(left_angle,right_angle)
        bodyAngle= np.rad2deg(bodyAngle)

        # 计算脊椎中心点的坐标
        spine_center_x = (hip_left.x + hip_right.x+left_shoulder.x+right_shoulder.x) / 4
        spine_center_y = (hip_left.y + hip_right.y+left_shoulder.y+right_shoulder.y) / 4
        spine_center_z = (hip_left.z + hip_right.z+left_shoulder.z+right_shoulder.z) / 4
        spine_center = [spine_center_x, spine_center_y, spine_center_z]
        #print("spine_center_x, spine_center_y",spine_center_x, spine_center_y)

        # 计算臀部中心点、颈项中心点的坐标
        hip_center_x = (hip_left.x + hip_right.x) / 2
        hip_center_y = (hip_left.y + hip_right.y) / 2
        hip_center_z = (hip_left.z + hip_right.z) / 2
        hip_center = [hip_center_x,hip_center_y, hip_center_z]

        #print(" hip_center_x,hip_center_y", hip_center_x,hip_center_y)

        neck_center_x =nose.x
        neck_center_y =nose.y
        neck_center_z =nose.z
        neck_center = [neck_center_x, neck_center_y, neck_center_z]

        # 计算臀部中心点、脊椎中心点和颈项中心点构成的角度
        spine_angle = math.degrees(math.acos((neck_center_y - spine_center_y) / math.sqrt(
            (neck_center_x - spine_center_x) ** 2 + (neck_center_y - spine_center_y) ** 2)))

        return distKneeToShoulder,bodyAngle,spine_angle

    # 判断是否塌腰
    def HunchImageInfo(image_path):

        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose
        # 初始化 MediaPipe 模型
        pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)
        image = cv2.imread(image_path)
        height, width, channels = image.shape
        if image is None:
            print('Failed to read the image.')
            exit()

        # Convert the color space from BGR to RGB and get Mediapipe results
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # height, width, channels = image.shape
        results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        # 获取关键点坐标
        if results.pose_landmarks is not None:
            keypoints = results.pose_landmarks.landmark
            # for kp in keypoints:
            #     kp.x *= width
            #     kp.y *=height
        else:
            return 0,0,0

        distKneeToShoulder, bodyAngle, spine_angle=compute_waist_height(keypoints)


        return distKneeToShoulder, bodyAngle, spine_angle


    def main():
        image_path='images/4/4_0200.jpg'
        distKneeToShoulder, bodyAngle, spine_angle=HunchImageInfo(image_path)
        # 获取图像分辨率

        print("distKneeToShoulder, bodyAngle, spine_angle",distKneeToShoulder, bodyAngle, spine_angle)
        drawSkeletonSingelImage(image_path)

        image_path2 = 'images/0/0_0200.jpg'
        distKneeToShoulder, bodyAngle, spine_angle = HunchImageInfo(image_path2)
        # 获取图像分辨率

        print("distKneeToShoulder, bodyAngle, spine_angle", distKneeToShoulder, bodyAngle, spine_angle)

        cv2.waitKey(0)

    if __name__ == '__main__':
        main()
