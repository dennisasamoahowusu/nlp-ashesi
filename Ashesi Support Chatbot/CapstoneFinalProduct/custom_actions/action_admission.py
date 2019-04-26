import random
# from libraries.postgres import PostGres


class ActionAdmissions():
	"""docstring for ActionFees"""
	def __init__(self):
		self.mysqlconn = 'PostGres()'

	def makeAdmissionResponse(self, postgres, intent= 'admission', entity='text_books'):
		if(entity == "no_value"):
			response = postgres.selectQuery("SELECT * FROM admission WHERE entity = 'selection_criteria'")
		else:
			#response = postgres.selectQuery("SELECT * FROM admission WHERE entity = '" + entity + "'")

			response = postgres.selectQuery("SELECT * FROM admission WHERE entity LIKE '%{0:s}%'".format(entity))


			

		
		if len(response) > 0:
			toReturn = response[0]["responses"]
			return str(toReturn)
		else:
			no_data = ['You may want to revise your question so I can help you. Alternatively email admissions  at admissions@ashesi.edu.gh for more information.',
			'I do not think I can help much on this question, email admissions  at admissions@ashesi.edu.gh for more information.', 
			'Hmmm, I think this is beyond my scope for now. Email admissions@ashesi.edu.gh for more information.']
			return random.choice(no_data)
