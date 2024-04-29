import tensorflow as tf
from tensorflow.python.client import device_lib

print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

print(tf.__version__)

# 查看gpu和cpu的数量
gpus = tf.config.experimental.list_physical_devices(device_type='GPU')
cpus = tf.config.experimental.list_physical_devices(device_type='CPU')
print("gpus",gpus)
print("cpus",cpus)
print(device_lib.list_local_devices())
print(tf.config.list_physical_devices('GPU'))
print(tf.test.is_gpu_available())

tf.debugging.set_log_device_placement(True)
# 查看所有可用的 GPU 设备
gpus = tf.config.list_physical_devices('GPU')
print("Available GPUs:", gpus)

# 查看可用的 GPU 数量
num_gpus = len(gpus)
print("Number of available GPUs:", num_gpus)




print(tf.__version__)
# # Create some tensors
# a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
# b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
# c = tf.matmul(a, b)
# #显示了GPU运行
# print(c)

# 使用 pycuda 库查看可用的GPU数量
# import pycuda.driver as drv
#
# drv.init()
# print("Number of available GPUs:", drv.Device.count())
#
# # 使用 PyTorch 查看可用的GPU数量
# import torch
#
# print("Number of available GPUs:", torch.cuda.device_count())
