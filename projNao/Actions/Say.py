from Action import Action

class Say(Action):
	def get_dependencies(self):
		return ["TextToSpeech"]

	def execute(self, *args):
		text = args[0]
		# self.textToSpeech.say(text)
		print text