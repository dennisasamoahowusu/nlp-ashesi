import random
# from libraries.postgres import PostGres


class ActionScholarships():
	"""docstring for ActionFees"""
	def __init__(self):
		self.mysqlconn = 'PostGres()'

	def makeScholarshipsResponse(self, postgres, intent= 'scholarships', entity='scholarship_selection'):
		if(entity == "no_value"):
			response = postgres.selectQuery("SELECT * FROM scholarships WHERE entity = 'scholarship_covers'")
		else:
			#response = self.mysqlconn.selectQuery("SELECT * FROM scholarships WHERE entity = '" + entity + "'")
			#response = postgres.selectQuery("SELECT * FROM scholarships WHERE entity LIKE '%{0:s}%'".format(entity))
			response = postgres.selectQuery("SELECT * FROM scholarships WHERE entity = '" + entity + "'")

		if len(response) > 0:
			toReturn = response[0]["responses"]
			return str(toReturn)
		else:
			no_data = ['I do not think I know the exact answer. For more information about scholarship visit: https://www.ashesi.edu.gh/admissions/scholarships.html', 
			'I think I didn\'t do my homework well. Email info@ashesi.edu.gh for clarification',
			 'Hmmm, maybe I\'m too dumb to answer this question about scholarship. For more information about scholarship visit: https://www.ashesi.edu.gh/admissions/scholarships.html']
			return random.choice(no_data)
