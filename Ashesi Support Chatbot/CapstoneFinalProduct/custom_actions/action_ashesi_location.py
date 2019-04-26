import random
# from libraries.postgres import PostGres


class ActionLocation():
	"""docstring for ActionFees"""
	def __init__(self):
		self.mysqlconn = 'PostGres()'

	def makeLocationResponse(self, postgres, intent= 'ashesi_location', entity='ashesi_direction'):
		if(entity == "no_value"):
			response = postgres.selectQuery("SELECT * FROM ashesi_location WHERE entity = 'ashesi_location'")
		else:
			response = postgres.selectQuery("SELECT * FROM ashesi_location WHERE entity LIKE '%{0:s}%'".format(entity))
			#response = postgres.selectQuery("SELECT * FROM ashesi_location WHERE entity = '" + entity + "'")

		if len(response) > 0:
			toReturn = response[0]["responses"]
			return str(toReturn)
		else:
			no_data = ['I am afraid I cannot answer this concerning location. Contact us at: email: info@ashesi.edu.gh| call:  +233 302 610 330','I do not know about this location. Contact us at: email: info@ashesi.edu.gh| call:  +233 302 610 330', 'I am not sure about this location. Contact us at: email: info@ashesi.edu.gh| call:  +233 302 610 330 for more help', 'Hmmm, maybe I have forgotten the answer. Contact us at: email: info@ashesi.edu.gh| call:  +233 302 610 330']
			return random.choice(no_data)
