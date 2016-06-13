def execute1(motion):
	names = list()
	times = list()
	keys = list()

	names.append("HeadPitch")
	times.append([0.8, 1.6, 2.36, 3])
	keys.append([-0.171956, -0.0107799, 0.44175, 0.44175])

	names.append("HeadYaw")
	times.append([0.8, 1.6, 2.36, 3])
	keys.append([0.00172502, 0.0122299, 0.00149202, 0.00149202])

	names.append("LAnklePitch")
	times.append([0.8, 1.6, 2.36, 3])
	keys.append([0.0823971, 0.082794, 0.0843279, 0.0843279])

	names.append("LAnkleRoll")
	times.append([0.8, 1.6, 2.36, 3])
	keys.append([-0.127277, -0.11961, -0.11961, -0.11961])

	names.append("LElbowRoll")
	times.append([0.8, 1.6, 2.36, 3])
	keys.append([-0.403861, -0.351244, -0.31136, -0.31136])

	names.append("LElbowYaw")
	times.append([0.8, 1.6, 2.36, 3])
	keys.append([-1.1853, -1.18889, -0.98487, -0.98487])

	names.append("LHand")
	times.append([0.8, 1.6, 2.36, 3])
	keys.append([0.99, 0.9892, 0.452, 0.452])

	names.append("LHipPitch")
	times.append([0.8, 1.6, 2.36, 3])
	keys.append([0.132689, 0.135034, 0.135034, 0.135034])

	names.append("LHipRoll")
	times.append([0.8, 1.6, 2.36, 3])
	keys.append([0.0928004, 0.0890141, 0.0890141, 0.0890141])

	names.append("LHipYawPitch")
	times.append([0.8, 1.6, 2.36, 3])
	keys.append([-0.178726, -0.184038, -0.184038, -0.184038])

	names.append("LKneePitch")
	times.append([0.8, 1.6, 2.36, 3])
	keys.append([-0.0873984, -0.0874801, -0.0874801, -0.0874801])

	names.append("LShoulderPitch")
	times.append([0.8, 1.6, 2.36, 3])
	keys.append([0.247484, 0.530722, 0.45709, 0.267885])

	names.append("LShoulderRoll")
	times.append([0.8, 1.6, 2.36, 3])
	keys.append([0.121161, -0.224006, -0.213268, -0.213269])

	names.append("LWristYaw")
	times.append([0.8, 1.6, 2.36, 3])
	keys.append([-0.3574, -0.480184, -0.569156, -0.569155])

	names.append("RAnklePitch")
	times.append([0.8, 1.6, 2.36, 3])
	keys.append([0.082773, 0.0844119, 0.0859461, 0.0859461])

	names.append("RAnkleRoll")
	times.append([0.8, 1.6, 2.36, 3])
	keys.append([0.126719, 0.130432, 0.130432, 0.130432])

	names.append("RElbowRoll")
	times.append([0.8, 1.6, 2.36, 3])
	keys.append([0.390409, 0.34826, 0.30991, 0.309909])

	names.append("RElbowYaw")
	times.append([0.8, 1.6, 2.36, 3])
	keys.append([1.17936, 1.1658, 0.984786, 0.984786])

	names.append("RHand")
	times.append([0.8, 1.6, 2.36, 3])
	keys.append([0.991084, 0.9864, 0.4932, 0.4932])

	names.append("RHipPitch")
	times.append([0.8, 1.6, 2.36, 3])
	keys.append([0.132636, 0.124212, 0.122678, 0.122678])

	names.append("RHipRoll")
	times.append([0.8, 1.6, 2.36, 3])
	keys.append([-0.0972695, -0.098134, -0.098134, -0.0981341])

	names.append("RHipYawPitch")
	times.append([0.8, 1.6, 2.36, 3])
	keys.append([-0.170646, -0.184038, -0.184038, -0.184038])

	names.append("RKneePitch")
	times.append([0.8, 1.6, 2.36, 3])
	keys.append([-0.0903801, -0.0889301, -0.0889301, -0.0889301])

	names.append("RShoulderPitch")
	times.append([0.8, 1.6, 2.36, 3])
	keys.append([0.247861, 0.533874, 0.458708, 0.267885])

	names.append("RShoulderRoll")
	times.append([0.8, 1.6, 2.36, 3])
	keys.append([-0.120718, 0.263806, 0.220854, 0.220854])

	names.append("RWristYaw")
	times.append([0.8, 1.6, 2.36, 3])
	keys.append([0.792125, 0.562936, 0.584412, 0.584411])

	try:
	  motion.angleInterpolation(names, keys, times, True)
	except BaseException, err:
	  print err
