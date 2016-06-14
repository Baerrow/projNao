from Action import Action

class StartTracking(Action):
	def get_dependencies(self):
		return ["Tracker"]

	def execute(self, *args):
		target_name = args[0]
		
		# self.tracker.track(target_name)
		print "I'm tracking {0}".format(target_name)
