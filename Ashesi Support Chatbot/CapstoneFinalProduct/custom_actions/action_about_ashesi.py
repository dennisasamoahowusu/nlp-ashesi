import random
# from libraries.postgres import PostGres


class ActionAboutAshesi():
	"""docstring for ActionFees"""
	def __init__(self):
		self.mysqlconn = 'PostGres()'

	def makeAboutAshesiResponse(self, postgres, intent= 'about_ashesi', entity='personality'):
		if(entity == "no_value"):
			response = postgres.selectQuery("SELECT * FROM about_ashesi WHERE entity = 'history'")
		else:
			response = postgres.selectQuery("SELECT * FROM about_ashesi WHERE entity = '" + entity + "'")


		
		if len(response) > 0:
			toReturn = response[0]["responses"]
			return str(toReturn)
		else:
			no_data = ['I do not think I know the exact answer.  For more information visit our about page : https://www.ashesi.edu.gh/about.html',
			 'I think I didn\'t do my homework well. Email info@ashesi.edu.gh for clarification',
			 'Hmmm, maybe I\'m too dumb to answer this question about scholarship. For more information visit our about page : https://www.ashesi.edu.gh/about.html']			
			return random.choice(no_data)

