
import tensorflow as tf

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)

with tf.device('/GPU:0'):
    import math
    import numpy as np
    import dlib
    import cv2
    import mediapipe as mp

    # 判断是否塌腰
    def check_if_hunched_over(image_path):

        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose
        # 初始化 MediaPipe 模型
        pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)
        image = cv2.imread(image_path)
        if image is None:
            print('Failed to read the image.')
            exit()


        # Convert the color space from BGR to RGB and get Mediapipe results
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        # 获取关键点坐标
        if results.pose_landmarks is not None:
            keypoints = results.pose_landmarks.landmark
        else:
            return 0
        #print(keypoints)
        results = pose.process(image)

        waist_left = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]  # 左臀
        waist_right = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP]  # 右臀
        spine_middle = results.pose_landmarks.landmark[mp_pose.PoseLandmark.SPINE_CENTER]  # 脊椎中心

        waist_vector = np.array(
            [waist_right.x - waist_left.x, waist_right.y - waist_left.y, waist_right.z - waist_left.z])
        spine_vector = np.array(
            [spine_middle.x - (waist_left.x + waist_right.x) / 2, spine_middle.y - (waist_left.y + waist_right.y) / 2,
             spine_middle.z - (waist_left.z + waist_right.z) / 2])
        waist_angle = np.arccos(np.dot(waist_vector, spine_vector) / (
                np.linalg.norm(waist_vector) * np.linalg.norm(spine_vector))) * 180 / np.pi

        kyphosis_index = waist_angle / 30.0

        print("塌腰系数为：", kyphosis_index)

        HunchValue=kyphosis_index
        return HunchValue


    def main():
        image_path='images/test/4_0609.jpg'
        HunchValue=check_if_hunched_over(image_path)
        print(HunchValue)

    if __name__ == '__main__':
        main()
