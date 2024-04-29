import math

import cv2
import mediapipe as mp
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch import device

last_pred = None
pred_cnt = 0

class Swish(nn.Module):
    def forward(self, x):
        return x * torch.sigmoid(x)

class Model(nn.Module):
    def __init__(self):
        super().__init__()

        self.fc1 = nn.Linear(3, 16)  # 隐藏层1,宽度加大
        self.dropout1 = nn.Dropout(0.1)  # dropout1
        self.fc2 = nn.Linear(16, 4)  # 隐藏层2
        # self.dropout2 = nn.Dropout(0.1)  # dropout2
        # self.fc3 = nn.Linear(16, 4)  # 隐藏层3
        # self.fc4 = nn.Linear(16, 4)  # 输出层,输出大小为1,回归任务
        self.lstm = None  # 删除LSTM层
    def forward(self, x):
        self.swish = Swish()
        x = F.leaky_relu(self.fc1(x))
        x = self.dropout1(x)
        x = self.fc2(x)
        # x = F.relu(self.fc2(x))
        # x = self.dropout2(x)
        # x = self.swish(self.fc3(x))  # 使用自定义的Swish激活层
        # x = self.fc4(x)
        # x = self.fc3(x)
        return x
#

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5,
                                  min_tracking_confidence=0.5)
cap = cv2.VideoCapture(0)
cv2.waitKey(100)
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


while cap.isOpened():
    success, image = cap.read()

    # Convert the color space from BGR to RGB and get Mediapipe results
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(image)

    # Convert the color space from RGB to BGR to display well with Opencv
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    face_coordination_in_real_world = np.array([
        [285, 528, 200],
        [285, 371, 152],
        [197, 574, 128],
        [173, 425, 108],
        [360, 574, 128],
        [391, 425, 108]
    ], dtype=np.float64)

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

            text0 = '你好'
            if max_idx == 2:
                print("出现2了")
                cv2.putText(image, text0, (200, 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 0, 200), 2)
            # cv2.putText(image, f"{max_idx}", (200, 20),
            #             cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 0, 200), 2)
            text1 = 'The head is tilted to the right'
            text2 = 'The head is tilted to the left'
            if result[2] >= 20:
                print("头往右方歪了")
                cv2.putText(image, text1, (200, 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 0, 200), 2)
            elif result[2] <= -20:
                print("头往左方歪了")
                cv2.putText(image, text2, (200, 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 0, 200), 2)
            # elif result[0] >=
            for i, info in enumerate(zip(('pitch', 'yaw', 'roll'), result)):
                k, v = info
                text = f'{k}: {int(v)}'
                cv2.putText(image, text, (20, i*30 + 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 0, 200), 2)


    cv2.imshow('Head Pose Angles', image)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()

