
import random
from time import sleep

class ActionAffirmitiveNegative():
	def __init__(self):
		self.action = "action_affirmative_negative"
	def makeAffirmativeNegative(self, intent):
		positive_response = ["I'm Impressed", "Thanks you find it useful", "Glad to hear that", "Great it did help"]
		negative_response = ["I'm sorry I couldn't help at this time", "Oops sorry", "Kindly email Ashesi for further help"]
		if intent == "affirmative":
			return random.choice(positive_response)
		elif intent == "negative":
			return random.choice(negative_response)
			sleep(2)
			return "You may want to revise your question so I can help you"
		else:
			return "Okay"

	