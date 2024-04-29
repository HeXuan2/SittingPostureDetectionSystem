import os
import cv2
import mediapipe as mp
import numpy as np
import shutil


mp_drawing_global = mp.solutions.drawing_utils

# 初始化 Mediapipe Pose 模型
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# 定义检测人体姿态的函数
def detect_pose(frame, drawing=mp.solutions.drawing_utils):
    # 将图像转换为 RGB 格式
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = pose.process(image)
    # 绘制检测结果
    if results.pose_landmarks is not None:
        success = True
        landmarks = []
        for id, lm in enumerate(results.pose_landmarks.landmark):

            # h, w, c = image.shape
            h=640
            w=480
            cx, cy = int(lm.x * w), int(lm.y * h)
            landmarks.append((cx, cy))
            #print("画骨架")
            # 绘制骨架信息
            drawing.draw_landmarks(
                frame,
                results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=drawing.DrawingSpec(color=(255, 255, 0), thickness=2, circle_radius=2),
                connection_drawing_spec=drawing.DrawingSpec(color=(0, 255, 255), thickness=2, circle_radius=2))
    else:
        success = False
        landmarks = []
    return success, landmarks

def drawSkeletonSingelImage(imagePath):
    # 加载图片

    image = cv2.imread(imagePath)

    # 从结果中提取骨架信息
    success, pose_landmarks = detect_pose(image)

    image_with_landmarks = image.copy()

    # 将图像转换为 RGB 格式
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    # 调整图像的大小，避免图像失真。
    image = cv2.resize(image, (480, 640), interpolation=cv2.INTER_AREA)

    # 判断是否识别到骨架
    if not success:
        # 如果未识别到骨架
        print("未识别到骨架")

    else:
        # 显示图片
        cv2.imshow('image', image)



def drawSkeletonfolder():

    input_folder = 'images/test'
    output_folder= 'images/test'
    # 遍历 images 文件夹
    for file_name in os.listdir(input_folder):
        # 加载图片
        image = cv2.imread(os.path.join(input_folder, file_name))
        # 检查图像是否为空
        if image is None:
            continue
        # 从结果中提取骨架信息
        success,pose_landmarks = detect_pose(image)

        image_with_landmarks = image.copy()

        # 将图像转换为 RGB 格式
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        # 调整图像的大小，避免图像失真。
        resized_image = cv2.resize(image, (640, 480), interpolation=cv2.INTER_AREA)

        # 判断是否识别到骨架
        if not success:
            print("11")
            # 如果未识别到骨架，将图片移动到输出文件夹
            shutil.move(os.path.join(input_folder, file_name), os.path.join('images/UndetectedImage', file_name))
        else:
            # 保存结果图像
            print("##")
            if not os.path.exists(output_folder):
                os.mkdir(output_folder)
            cv2.imwrite(os.path.join(output_folder, file_name), cv2.cvtColor(image_with_landmarks, cv2.COLOR_RGB2BGR))


def main():
    imagePath="../images/Hunch/0/0_0064.jpg"
    drawSkeletonSingelImage(imagePath)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()




