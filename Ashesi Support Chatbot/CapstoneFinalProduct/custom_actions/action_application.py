import random
# from libraries.postgres import PostGres


class ActionApplication():
	"""docstring for ActionFees"""
	def __init__(self):
		self.mysqlconn = 'PostGres()'

	def makeApplicationResponse(self, postgres, intent= 'application', entity='application_fee'):
		if(entity == "no_value"):
			response = postgres.selectQuery("SELECT * FROM application WHERE entity = 'online_application'")
		else:
			response = postgres.selectQuery("SELECT * FROM application WHERE entity LIKE '%{0:s}%'".format(entity))
			#response = postgres.selectQuery("SELECT * FROM application WHERE entity = '" + entity + "'")


		
		if len(response) > 0:
			toReturn = response[0]["responses"]
			return str(toReturn)
		else:
			no_data =  ['You may want to revise your question so I can help you. Alternatively email admissions  at admissions@ashesi.edu.gh for more information about applying to Ashesi.',

			'I do not think I can help much on this question, email admissions  at admissions@ashesi.edu.gh for more information about applying to Ashesi.' ,
			'Hmmm, I think this is beyond my scope for now. Email info@ashesi.edu.gh for more information about applying to Ashesi.']

			return random.choice(no_data)
