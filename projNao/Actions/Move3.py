from Action import Action

class Move1(Action):
	def get_dependencies(self):
		return ["Motion"]

	def execute(self, *args):
		
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([1.4, 2.6])
		keys.append([[0.44175, [3, -0.466667, 0], [3, 0.4, 0]], [0.44175, [3, -0.4, 0], [3, 0, 0]]])

		names.append("HeadYaw")
		times.append([1.4, 2.6])
		keys.append([[0.00149202, [3, -0.466667, 0], [3, 0.4, 0]], [0.00149202, [3, -0.4, 0], [3, 0, 0]]])

		names.append("LAnklePitch")
		times.append([1.4, 2.6])
		keys.append([[0.0843279, [3, -0.466667, 0], [3, 0.4, 0]], [0.0843279, [3, -0.4, 0], [3, 0, 0]]])

		names.append("LAnkleRoll")
		times.append([1.4, 2.6])
		keys.append([[-0.11961, [3, -0.466667, 0], [3, 0.4, 0]], [-0.11961, [3, -0.4, 0], [3, 0, 0]]])

		names.append("LElbowRoll")
		times.append([1.4, 2.6])
		keys.append([[-0.31136, [3, -0.466667, 0], [3, 0.4, 0]], [-0.31136, [3, -0.4, 0], [3, 0, 0]]])

		names.append("LElbowYaw")
		times.append([1.4, 2.6])
		keys.append([[-0.98487, [3, -0.466667, 0], [3, 0.4, 0]], [-0.98487, [3, -0.4, 0], [3, 0, 0]]])

		names.append("LHand")
		times.append([1.4, 2.6])
		keys.append([[0.452, [3, -0.466667, 0], [3, 0.4, 0]], [0.452, [3, -0.4, 0], [3, 0, 0]]])

		names.append("LHipPitch")
		times.append([1.4, 2.6])
		keys.append([[0.135034, [3, -0.466667, 0], [3, 0.4, 0]], [0.135034, [3, -0.4, 0], [3, 0, 0]]])

		names.append("LHipRoll")
		times.append([1.4, 2.6])
		keys.append([[0.0890141, [3, -0.466667, 0], [3, 0.4, 0]], [0.0890141, [3, -0.4, 0], [3, 0, 0]]])

		names.append("LHipYawPitch")
		times.append([1.4, 2.6])
		keys.append([[-0.184038, [3, -0.466667, 0], [3, 0.4, 0]], [-0.184038, [3, -0.4, 0], [3, 0, 0]]])

		names.append("LKneePitch")
		times.append([1.4, 2.6])
		keys.append([[-0.0874801, [3, -0.466667, 0], [3, 0.4, 0]], [-0.0874801, [3, -0.4, 0], [3, 0, 0]]])

		names.append("LShoulderPitch")
		times.append([1.4, 2.6])
		keys.append([[0.45709, [3, -0.466667, 0], [3, 0.4, 0]], [0.267885, [3, -0.4, 0], [3, 0, 0]]])

		names.append("LShoulderRoll")
		times.append([1.4, 2.6])
		keys.append([[-0.213269, [3, -0.466667, 0], [3, 0.4, 0]], [-0.213269, [3, -0.4, 0], [3, 0, 0]]])

		names.append("LWristYaw")
		times.append([1.4, 2.6])
		keys.append([[-0.569155, [3, -0.466667, 0], [3, 0.4, 0]], [-0.569155, [3, -0.4, 0], [3, 0, 0]]])

		names.append("RAnklePitch")
		times.append([1.4, 2.6])
		keys.append([[0.0859461, [3, -0.466667, 0], [3, 0.4, 0]], [0.0859461, [3, -0.4, 0], [3, 0, 0]]])

		names.append("RAnkleRoll")
		times.append([1.4, 2.6])
		keys.append([[0.130432, [3, -0.466667, 0], [3, 0.4, 0]], [0.130432, [3, -0.4, 0], [3, 0, 0]]])

		names.append("RElbowRoll")
		times.append([1.4, 2.6])
		keys.append([[0.309909, [3, -0.466667, 0], [3, 0.4, 0]], [0.309909, [3, -0.4, 0], [3, 0, 0]]])

		names.append("RElbowYaw")
		times.append([1.4, 2.6])
		keys.append([[0.984786, [3, -0.466667, 0], [3, 0.4, 0]], [0.984786, [3, -0.4, 0], [3, 0, 0]]])

		names.append("RHand")
		times.append([1.4, 2.6])
		keys.append([[0.4932, [3, -0.466667, 0], [3, 0.4, 0]], [0.4932, [3, -0.4, 0], [3, 0, 0]]])

		names.append("RHipPitch")
		times.append([1.4, 2.6])
		keys.append([[0.122678, [3, -0.466667, 0], [3, 0.4, 0]], [0.122678, [3, -0.4, 0], [3, 0, 0]]])

		names.append("RHipRoll")
		times.append([1.4, 2.6])
		keys.append([[-0.0981341, [3, -0.466667, 0], [3, 0.4, 0]], [-0.0981341, [3, -0.4, 0], [3, 0, 0]]])

		names.append("RHipYawPitch")
		times.append([1.4, 2.6])
		keys.append([[-0.184038, [3, -0.466667, 0], [3, 0.4, 0]], [-0.184038, [3, -0.4, 0], [3, 0, 0]]])

		names.append("RKneePitch")
		times.append([1.4, 2.6])
		keys.append([[-0.0889301, [3, -0.466667, 0], [3, 0.4, 0]], [-0.0889301, [3, -0.4, 0], [3, 0, 0]]])

		names.append("RShoulderPitch")
		times.append([1.4, 2.6])
		keys.append([[0.458707, [3, -0.466667, 0], [3, 0.4, 0]], [0.267885, [3, -0.4, 0], [3, 0, 0]]])

		names.append("RShoulderRoll")
		times.append([1.4, 2.6])
		keys.append([[0.220854, [3, -0.466667, 0], [3, 0.4, 0]], [0.220854, [3, -0.4, 0], [3, 0, 0]]])

		names.append("RWristYaw")
		times.append([1.4, 2.6])
		keys.append([[0.584411, [3, -0.466667, 0], [3, 0.4, 0]], [0.584411, [3, -0.4, 0], [3, 0, 0]]])


		try:
		  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
		  # motion = ALProxy("ALMotion", IP, 9559)
		  # motion = ALProxy("ALMotion")
		  self.motion.angleInterpolationBezier(names, times, keys)
		except BaseException, err:
		  print err
