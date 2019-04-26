import random
# from libraries.postgres import PostGres


class ActionMajors():
	"""docstring for ActionFees"""
	def __init__(self):
		self.mysqlconn = 'PostGres()'

	def makeMajorsResponse(self, postgres, intent= 'majors', entity='courses'):
		if(entity == "no_value"):
			response = postgres.selectQuery("SELECT * FROM majors WHERE entity = 'courses'")
		else:

			#response = postgres.selectQuery("SELECT * FROM majors WHERE entity = '" + entity + "'")
			response = postgres.selectQuery("SELECT * FROM majors WHERE entity LIKE '%{0:s}%'".format(entity))

		if len(response) > 0:
			toReturn = response[0]["responses"]
			return str(toReturn)
		else:
			no_data =  ['Please contact Ashesi admissions team for more information about majors @admissions@ashesi.edu.gh',
			 'We may not have that, email us admissions @admissions@ashesi.edu.gh for clarification' , 
			 'I do not have detailed knowledge about this, visit our www.ashesi.edu.gh for detailed information']
			return random.choice(no_data)
