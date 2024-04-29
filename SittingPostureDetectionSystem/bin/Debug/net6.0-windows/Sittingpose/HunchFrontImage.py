import tensorflow as tf

import HunchFront

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)

with tf.device('/GPU:0'):
    import math
    import numpy as np
    import cv2
    import mediapipe as mp
    from PicProcess.SkeletonInfo import detect_pose

    # 判断是否塌腰
    def HunchImageInfo(image_path):

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
            return 0,0,0,0

        distAverage,distShoulder,distMounthToShoulder,distNoseToMounth=HunchFront.HunchInfo(keypoints)

        return distAverage,distShoulder,distMounthToShoulder,distNoseToMounth


    def main():

        image_path='images/4/4_0834.jpg'
        distAverage, distShoulder, distMounthToShoulder, distNoseToMounth=HunchImageInfo(image_path)
        print("distAverage,distShoulder,distMounthToShoulder,distNoseToMounth",distAverage,distShoulder,distMounthToShoulder,distNoseToMounth)
        # 获取图像分辨率

        image_path2 = 'images/0/0_0072.jpg'
        distAverage, distShoulder, distMounthToShoulder, distNoseToMounth = HunchImageInfo(image_path2 )
        # 获取图像分辨率

        print("distAverage,distShoulder,distMounthToShoulder,distNoseToMounth",distAverage,distShoulder,distMounthToShoulder,distNoseToMounth)

        cv2.waitKey(0)

    if __name__ == '__main__':
        main()
