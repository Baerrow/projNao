from Action import Action

class PointAtTarget(Action):
	def get_dependencies(self):
		return ["Tracker"]

	def execute(self, *args):
		fraction_max_speed = 0.8
		
		self.tracker.pointAt("LArm", self.tracker.getTargetPosition(0), 0, fraction_max_speed)
		print "I'm pointing my target at {0} speed".format(fraction_max_speed)