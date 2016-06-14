from Action import Action

class StandUp(Action):
	def get_dependencies(self):
		return ["RobotPosture"]

	def execute(self, *args):
		fraction_max_speed = float(args[0])
		
		# self.robotPosture.goToPosture("StandInit", fraction_max_speed)
		print "I'm standing up at {0} speed".format(fraction_max_speed)
