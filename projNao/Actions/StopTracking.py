from Action import Action

class StopTracking(Action):
	def get_dependencies(self):
		return ["Tracker"]

	def execute(self, *args):
		self.tracker.stopTracker()
		print "I stopped tracking"
