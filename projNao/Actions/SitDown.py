from Action import Action

class SitDown(Action):
	def get_dependencies(self):
		return ["RobotPosture"]

	def execute(self, *args):
		fraction_max_speed = 0.8
		
		self.robotPosture.goToPosture("Sit", fraction_max_speed)
		print "I'm sitting down at {0} speed".format(fraction_max_speed)
