class Action:
	def __init__(self, modules):
		self.modules = {}

		for dependency in self.get_dependencies():
			try:
				self.modules[dependency] = modules[dependency]
			except KeyError:
				raise Exception("Dependency {0} is not satisfied".format(dependency))


	def get_dependencies(self):
		return []		

	def __getattr__(self, attribute_name):
		formated_attribute_name = attribute_name[0].upper() + attribute_name[1:] # tracker => Tracker
		
		try:
			return self.modules[formated_attribute_name]
		except KeyError:
			raise AttributeError(attribute_name)
		
	def __str__(self):
		return "Action {0}, dependencies: {1}".format(self.__class__.__name__, self.get_dependencies())

	def __call__(self, args):
		self.execute(args)

	def execute(self, *args):
		pass