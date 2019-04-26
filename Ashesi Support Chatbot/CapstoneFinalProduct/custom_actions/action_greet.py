import random

class ActionGreetUser():
	def __init__(self):
		self.default = "Hello"

	def greetUser(self):
		answers = ["Hi User", "Hello there", "Hi ", "Hey dear"]
		return random.choice(answers)