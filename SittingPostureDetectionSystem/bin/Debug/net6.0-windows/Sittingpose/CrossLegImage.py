
import tensorflow as tf

import CrossLeg

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)

with tf.device('/GPU:0'):
    import cv2
    import mediapipe as mp
    import numpy as np
    import math


    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    # 初始化 MediaPipe 模型
    pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5, min_tracking_confidence=0.5)


    def CrossLegImageInfo(image_path):
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
        else:
            return 0, 0, 0,0,0,0,0,0,0,0

        crossDot1,distance1,crossDot2,distance2,crossDot3,distance3,distance4, crossDot5,distance5,distance6=CrossLeg.CrossLegInfo(keypoints)
        return crossDot1,distance1,crossDot2,distance2,crossDot3,distance3,distance4, crossDot5,distance5,distance6


    def main():

        image_path='images/5/5_0371.jpg'
        crossDot1, distance1, crossDot2, distance2, crossDot3, distance3, distance4, crossDot5, distance5, distance6=CrossLegImageInfo(image_path)
        print(distance1, distance2, distance3, distance4,distance5,distance6)

        image_path2='images/5/5_0504.jpg'
        crossDot1, distance1, crossDot2, distance2, crossDot3, distance3, distance4, crossDot5, distance5, distance6=CrossLegImageInfo(image_path2)
        print(distance1, distance2, distance3, distance4, distance5, distance6)



        image_path3 = 'images/0/0_0029.jpg'
        crossDot1, distance1, crossDot2, distance2, crossDot3, distance3, distance4, crossDot5, distance5, distance6= CrossLegImageInfo(image_path3)
        print(distance1, distance2, distance3, distance4, distance5, distance6)


        cv2.waitKey(0)



    if __name__ == '__main__':
        main()
