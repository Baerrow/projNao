# Choregraphe bezier export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.8, 1.6, 2.36, 3])
keys.append([[-0.171956, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.0107799, [3, -0.266667, -0.104907], [3, 0.253333, 0.0996617]], [0.44175, [3, -0.253333, 0], [3, 0.213333, 0]], [0.44175, [3, -0.213333, 0], [3, 0, 0]]])

names.append("HeadYaw")
times.append([0.8, 1.6, 2.36, 3])
keys.append([[0.00172502, [3, -0.266667, 0], [3, 0.266667, 0]], [0.0122299, [3, -0.266667, 0], [3, 0.253333, 0]], [0.00149202, [3, -0.253333, 0], [3, 0.213333, 0]], [0.00149202, [3, -0.213333, 0], [3, 0, 0]]])

names.append("LAnklePitch")
times.append([0.8, 1.6, 2.36, 3])
keys.append([[0.0823971, [3, -0.266667, 0], [3, 0.266667, 0]], [0.082794, [3, -0.266667, -0.000330051], [3, 0.253333, 0.000313549]], [0.0843279, [3, -0.253333, 0], [3, 0.213333, 0]], [0.0843279, [3, -0.213333, 0], [3, 0, 0]]])

names.append("LAnkleRoll")
times.append([0.8, 1.6, 2.36, 3])
keys.append([[-0.127277, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.11961, [3, -0.266667, 0], [3, 0.253333, 0]], [-0.11961, [3, -0.253333, 0], [3, 0.213333, 0]], [-0.11961, [3, -0.213333, 0], [3, 0, 0]]])

names.append("LElbowRoll")
times.append([0.8, 1.6, 2.36, 3])
keys.append([[-0.403861, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.351244, [3, -0.266667, -0.0158121], [3, 0.253333, 0.0150215]], [-0.31136, [3, -0.253333, -4.34844e-07], [3, 0.213333, 3.66185e-07]], [-0.31136, [3, -0.213333, 0], [3, 0, 0]]])

names.append("LElbowYaw")
times.append([0.8, 1.6, 2.36, 3])
keys.append([[-1.1853, [3, -0.266667, 0], [3, 0.266667, 0]], [-1.18889, [3, -0.266667, 0], [3, 0.253333, 0]], [-0.98487, [3, -0.253333, 0], [3, 0.213333, 0]], [-0.98487, [3, -0.213333, 0], [3, 0, 0]]])

names.append("LHand")
times.append([0.8, 1.6, 2.36, 3])
keys.append([[0.99, [3, -0.266667, 0], [3, 0.266667, 0]], [0.9892, [3, -0.266667, 0.000800014], [3, 0.253333, -0.000760013]], [0.452, [3, -0.253333, 3.53903e-08], [3, 0.213333, -2.98023e-08]], [0.452, [3, -0.213333, 0], [3, 0, 0]]])

names.append("LHipPitch")
times.append([0.8, 1.6, 2.36, 3])
keys.append([[0.132689, [3, -0.266667, 0], [3, 0.266667, 0]], [0.135034, [3, -0.266667, 0], [3, 0.253333, 0]], [0.135034, [3, -0.253333, 0], [3, 0.213333, 0]], [0.135034, [3, -0.213333, 0], [3, 0, 0]]])

names.append("LHipRoll")
times.append([0.8, 1.6, 2.36, 3])
keys.append([[0.0928004, [3, -0.266667, 0], [3, 0.266667, 0]], [0.0890141, [3, -0.266667, 0], [3, 0.253333, 0]], [0.0890141, [3, -0.253333, 0], [3, 0.213333, 0]], [0.0890141, [3, -0.213333, 0], [3, 0, 0]]])

names.append("LHipYawPitch")
times.append([0.8, 1.6, 2.36, 3])
keys.append([[-0.178726, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.184038, [3, -0.266667, 0], [3, 0.253333, 0]], [-0.184038, [3, -0.253333, 0], [3, 0.213333, 0]], [-0.184038, [3, -0.213333, 0], [3, 0, 0]]])

names.append("LKneePitch")
times.append([0.8, 1.6, 2.36, 3])
keys.append([[-0.0873984, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.0874801, [3, -0.266667, 0], [3, 0.253333, 0]], [-0.0874801, [3, -0.253333, 0], [3, 0.213333, 0]], [-0.0874801, [3, -0.213333, 0], [3, 0, 0]]])

names.append("LShoulderPitch")
times.append([0.8, 1.6, 2.36, 3])
keys.append([[0.247484, [3, -0.266667, 0], [3, 0.266667, 0]], [0.530722, [3, -0.266667, 0], [3, 0.253333, 0]], [0.45709, [3, -0.253333, 0.0469629], [3, 0.213333, -0.0395477]], [0.267885, [3, -0.213333, 0], [3, 0, 0]]])

names.append("LShoulderRoll")
times.append([0.8, 1.6, 2.36, 3])
keys.append([[0.121161, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.224006, [3, -0.266667, 0], [3, 0.253333, 0]], [-0.213268, [3, -0.253333, 0], [3, 0.213333, 0]], [-0.213269, [3, -0.213333, 0], [3, 0, 0]]])

names.append("LWristYaw")
times.append([0.8, 1.6, 2.36, 3])
keys.append([[-0.3574, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.480184, [3, -0.266667, 0.0361976], [3, 0.253333, -0.0343877]], [-0.569156, [3, -0.253333, 0], [3, 0.213333, 0]], [-0.569155, [3, -0.213333, 0], [3, 0, 0]]])

names.append("RAnklePitch")
times.append([0.8, 1.6, 2.36, 3])
keys.append([[0.082773, [3, -0.266667, 0], [3, 0.266667, 0]], [0.0844119, [3, -0.266667, -0.000542404], [3, 0.253333, 0.000515284]], [0.0859461, [3, -0.253333, -3.95313e-08], [3, 0.213333, 3.32895e-08]], [0.0859461, [3, -0.213333, 0], [3, 0, 0]]])

names.append("RAnkleRoll")
times.append([0.8, 1.6, 2.36, 3])
keys.append([[0.126719, [3, -0.266667, 0], [3, 0.266667, 0]], [0.130432, [3, -0.266667, 0], [3, 0.253333, 0]], [0.130432, [3, -0.253333, 0], [3, 0.213333, 0]], [0.130432, [3, -0.213333, 0], [3, 0, 0]]])

names.append("RElbowRoll")
times.append([0.8, 1.6, 2.36, 3])
keys.append([[0.390409, [3, -0.266667, 0], [3, 0.266667, 0]], [0.34826, [3, -0.266667, 0.0137606], [3, 0.253333, -0.0130725]], [0.30991, [3, -0.253333, 7.90626e-07], [3, 0.213333, -6.6579e-07]], [0.309909, [3, -0.213333, 0], [3, 0, 0]]])

names.append("RElbowYaw")
times.append([0.8, 1.6, 2.36, 3])
keys.append([[1.17936, [3, -0.266667, 0], [3, 0.266667, 0]], [1.1658, [3, -0.266667, 0.0135608], [3, 0.253333, -0.0128828]], [0.984786, [3, -0.253333, 0], [3, 0.213333, 0]], [0.984786, [3, -0.213333, 0], [3, 0, 0]]])

names.append("RHand")
times.append([0.8, 1.6, 2.36, 3])
keys.append([[0.991084, [3, -0.266667, 0], [3, 0.266667, 0]], [0.9864, [3, -0.266667, 0.00468379], [3, 0.253333, -0.0044496]], [0.4932, [3, -0.253333, 0], [3, 0.213333, 0]], [0.4932, [3, -0.213333, 0], [3, 0, 0]]])

names.append("RHipPitch")
times.append([0.8, 1.6, 2.36, 3])
keys.append([[0.132636, [3, -0.266667, 0], [3, 0.266667, 0]], [0.124212, [3, -0.266667, 0.00161473], [3, 0.253333, -0.00153399]], [0.122678, [3, -0.253333, 7.90626e-08], [3, 0.213333, -6.6579e-08]], [0.122678, [3, -0.213333, 0], [3, 0, 0]]])

names.append("RHipRoll")
times.append([0.8, 1.6, 2.36, 3])
keys.append([[-0.0972695, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.098134, [3, -0.266667, 0], [3, 0.253333, 0]], [-0.098134, [3, -0.253333, 0], [3, 0.213333, 0]], [-0.0981341, [3, -0.213333, 0], [3, 0, 0]]])

names.append("RHipYawPitch")
times.append([0.8, 1.6, 2.36, 3])
keys.append([[-0.170646, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.184038, [3, -0.266667, 0], [3, 0.253333, 0]], [-0.184038, [3, -0.253333, 0], [3, 0.213333, 0]], [-0.184038, [3, -0.213333, 0], [3, 0, 0]]])

names.append("RKneePitch")
times.append([0.8, 1.6, 2.36, 3])
keys.append([[-0.0903801, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.0889301, [3, -0.266667, 0], [3, 0.253333, 0]], [-0.0889301, [3, -0.253333, 0], [3, 0.213333, 0]], [-0.0889301, [3, -0.213333, 0], [3, 0, 0]]])

names.append("RShoulderPitch")
times.append([0.8, 1.6, 2.36, 3])
keys.append([[0.247861, [3, -0.266667, 0], [3, 0.266667, 0]], [0.533874, [3, -0.266667, 0], [3, 0.253333, 0]], [0.458708, [3, -0.253333, 0.0475333], [3, 0.213333, -0.040028]], [0.267885, [3, -0.213333, 0], [3, 0, 0]]])

names.append("RShoulderRoll")
times.append([0.8, 1.6, 2.36, 3])
keys.append([[-0.120718, [3, -0.266667, 0], [3, 0.266667, 0]], [0.263806, [3, -0.266667, 0], [3, 0.253333, 0]], [0.220854, [3, -0.253333, 9.88282e-08], [3, 0.213333, -8.32238e-08]], [0.220854, [3, -0.213333, 0], [3, 0, 0]]])

names.append("RWristYaw")
times.append([0.8, 1.6, 2.36, 3])
keys.append([[0.792125, [3, -0.266667, 0], [3, 0.266667, 0]], [0.562936, [3, -0.266667, 0], [3, 0.253333, 0]], [0.584412, [3, -0.253333, 0], [3, 0.213333, 0]], [0.584411, [3, -0.213333, 0], [3, 0, 0]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys)
except BaseException, err:
  print err
