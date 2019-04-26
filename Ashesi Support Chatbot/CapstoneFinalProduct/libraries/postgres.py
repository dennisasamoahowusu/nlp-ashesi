import psycopg2, psycopg2.extras

class PostGres:
	cnx = None # PostGres connection object
	cursor = None # connection cursor

	def __init__(self):
		"""
		This class handles all interactions to the mysql database
		"""
		try:
			self.cnx = psycopg2.connect(host="ec2-75-101-131-79.compute-1.amazonaws.com", 
				user="dkbzkfrfpbnilt", password="7bf3491ccd38dcb5de2c4dd5ae07615a4b3c89dcea2ca9e104e517d569fcfac9",
				database="dd278jhf0njsd5")
			self.cursor = self.cnx.cursor(cursor_factory=psycopg2.extras.DictCursor)
			print("Successful connection")
		except Exception as e:
			raise e
			print("Error connecting to DB")

	def selectQuery(self, sql):
		"""
		This functions gets / reads content from the database
		"""
		try:
			mCursor = self.getInstanceCursor()
			mCursor.execute(sql)
			print(sql)
			response = mCursor.fetchall()
			self.cnx.close()

			return response
		except Exception as e:
			raise e
			return None

	def insertQuery(self, sql):
		"""This function creates or writes content to the database"""
		try:
			mCursor = self.getInstanceCursor()
			mCursor.execute(sql)
			self.cnx.commit()
			self.cnx.close()
			return True
		except Exception as e:
			raise e
			return False

	def getInstanceCursor(self):
		"""This function returns an instance of the mysql cursor"""
		if self.cursor != None:
			return self.cursor
		pass


