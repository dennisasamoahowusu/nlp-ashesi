import random
# from libraries.postgres import PostGres

class ActionOffices():
	def __init___(self):
		self.mysqlconn = 'PostGres()'
	
	def makeOfficesResponse(self, postgres, intent= 'offices', entity='Prim'):
		if(entity == "no_value"):
			response = postgres.selectQuery("SELECT * FROM offices WHERE entity = 'Francis Gatsi'")
		else:
			#response = self.mysqlconn.selectQuery("SELECT * FROM admission WHERE entity = '" + entity + "'")
			#response = mysqlconn.selectQuery("SELECT * FROM offices WHERE entity LIKE '%' + entities + '%' Limit 5")
			response = postgres.selectQuery("SELECT * FROM offices WHERE entity LIKE '%{0:s}%'".format(entity))
			#response = postgres.selectQuery("SELECT * FROM offices WHERE entity = '" + entity + "'")

			#ran_index = random.randint(0,1)
			#response = response[ran_index]
		
		if len(response) > 0:
			toReturn = response[0]["responses"]
			return str(toReturn)
		else:
			no_data = ['You may want to revise your question so I can help you or email: info@ashesi.edu.gh',
			'I do not think I can help much on this question, email: info@ashesi.edu.gh' ,
			'Hmmm, maybe I\'m too dumb to answer this. Email: info@ashesi.edu.gh']
			return random.choice(no_data)
