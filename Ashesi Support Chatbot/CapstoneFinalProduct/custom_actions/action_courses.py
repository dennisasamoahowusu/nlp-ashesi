import random
# from libraries.postgres import PostGres


class ActionCourses():
	"""docstring for ActionFees"""
	def __init__(self):
		self.mysqlconn = 'PostGres()'

	def makeCoursesResponse(self, postgres, intent= 'majors', entity='courses'):
		if(entity == "no_value"):
			response = postgres.selectQuery("SELECT * FROM majors WHERE entity = 'courses'")
		else:
			#response = postgres.selectQuery("SELECT * FROM majors WHERE entity LIKE '%{0:s}%'".format(entity))
			response = postgres.selectQuery("SELECT * FROM majors WHERE entity = '" + entity + "'")
		
		if len(response) >0:
			toReturn = response[0]["responses"]
			return str(toReturn)
		else:
			no_data = ['You may want to revise your question so I can help you to with the response you want about majors/courses. Or Email admissions  at admissions@ashesi.edu.gh', 'Please contact Ashesi admissions team for more information about majors @ admissions@ashesi.edu.gh', 'Hmmm, maybe I\'m too dumb to answer this concerning academics: Email: @admissions@ashesi.edu.gh']
			return random.choice(no_data)
