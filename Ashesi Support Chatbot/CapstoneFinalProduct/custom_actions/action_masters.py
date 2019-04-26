import random

class ActionGraduateProgram():
	def __init__(self):
		self.default = "We do not offer Post graduate programs yet"

	def makegraduateResponse(self):
		answers = ["We only have undergraduate programs only", "No Post Graduate at Ashesi ", "There is no graduate school here"]
		return random.choice(answers)