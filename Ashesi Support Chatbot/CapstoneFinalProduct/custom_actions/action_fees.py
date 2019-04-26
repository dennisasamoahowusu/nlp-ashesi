import random
# from libraries.postgres import PostGres


class ActionFees():
	"""docstring for ActionFees"""
	def __init__(self):
		self.mysqlconn = 'PostGres()'

	def makeFeesResponse(self, postgres, intent= 'fees', entity='tuition_exchange_student'):
		if(entity == "no_value"):
			response = postgres.selectQuery("SELECT * FROM fees WHERE entity = 'tuition'")
		else:
			response = postgres.selectQuery("SELECT * FROM fees WHERE entity LIKE '%{0:s}%'".format(entity))
			#response = postgres.selectQuery("SELECT * FROM fees WHERE entity = '" + entity + "'")

		
		if len(response) >0:
			toReturn = response[0]["responses"]
			return str(toReturn)
		else:
			no_data = ['I have no adequate information about this question. This contact may be helpful to you admissions@ashesi.edu.gh ',
			 'I am sorry I cannot help. Contact us @ admissions@ashesi.edu.gh for clarification on the payment amount and methods.',
			  'Hmmm, maybe I\'m too dumb to answer this, contact admissions @admissions@ashesi.edu.gh for more help']
			return random.choice(no_data)
