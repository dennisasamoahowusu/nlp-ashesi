import random
# from libraries.postgres import PostGres


class ActionEducation():
	"""docstring for ActionFees"""
	def __init__(self):
		self.mysqlconn = 'PostGres()'

	def makeEducationResponse(self, postgres, intent= 'ashesi_education', entity='class_size'):
		if(entity == "no_value"):
			response = postgres.selectQuery("SELECT * FROM ashesi_education WHERE entity = 'liberal_art'")
		else:
			response = postgres.selectQuery("SELECT * FROM ashesi_education WHERE entity LIKE '%{0:s}%'".format(entity))
			#response = postgres.selectQuery("SELECT * FROM ashesi_education WHERE entity = '" + entity + "'")


		
		if len(response) > 0:
			toReturn = response[0]["responses"]
			return str(toReturn)
		else:
			no_data = ['I have no adequate information about this question concerning Ashesi Education.Contact us @ admissions@ashesi.edu.gh for clarification ',
			 			'I am sorry I cannot help. Contact us @ admissions@ashesi.edu.gh for clarification on Ashesi Education',
			  			'Hmmm, maybe I\'m too dumb to answer this, contact admissions @ @admissions@ashesi.edu.gh for more help']
			return random.choice(no_data)
