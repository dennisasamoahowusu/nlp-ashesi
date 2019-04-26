import mysql.connector

class MySqlLib:
	cnx = None # Mysql connection object
	cursor = None # connection cursor

	def __init__(self):
		"""
		This class handles all interactions to the mysql database
		"""
		try:
			self.cnx = mysql.connector.connect(host="ec2-54-83-17-151.compute-1.amazonaws.com", 
				user="kzfviegdrmodeo", password="a0a6f665e57a78938cac568045ea14e42cff92f642fdb52c091879573be20c40",
				database="dde7c0jgq5vp9d")
			self.cursor = self.cnx.cursor(buffered=True, dictionary=True)
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
			return response
		except Exception as e:
			raise e
			return None

	def insertQuery(self, sql):
		"""
		This function creates or writes content to the database
		"""
		try:
			mCursor = self.getInstanceCursor()
			mCursor.execute(sql)
			self.cnx.commit()
			return True
		except Exception as e:
			raise e
			return False

	def getInstanceCursor(self):
		"""
		This function returns an instance of the mysql cursor
		"""
		if self.cursor != None:
			return self.cursor
		pass

# if __name__ == '__main__':
# 	obj = MySqlLib()
# 	print(obj.selectQuery("SELECT * FROM admission"))
