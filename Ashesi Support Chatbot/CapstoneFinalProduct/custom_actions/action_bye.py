import random

class ActionSayBye():
	def __init__(self):
		self.default = "Goodbye"
	def makeByebyeResponse(self):
		answers = ["See You later", "Yeah thanks for reaching out", "Until Next time", "Alright bye"]
		return random.choice(answers)

