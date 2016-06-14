from Action import Action

class Crouch(Action):
	def get_dependencies(self):
		return ["RobotPosture"]

	def execute(self, *args):
		fraction_max_speed = float(args[0])
		
		# self.robotPosture.goToPosture("Crouch", fraction_max_speed)
		print "I'm crouching at {0} speed".format(fraction_max_speed)
