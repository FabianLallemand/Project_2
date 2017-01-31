import pymysql


class mysql:

	def __init__(self, array = False):
		if not array:
			#set connection types
			self.connection = pymysql.connect(
				host='localhost',
				user='battleport',
				password='ditiseengeheim',
				db='highscores',
				cursorclass=pymysql.cursors.DictCursor
			)

	def select(self, query):
		with self.connection.cursor() as cursor:
			try:
				cursor.execute(query)
				result = cursor.fetchall()
			finally:
				self.connection.close()
				return result

	def insert(self, query):
		self.__alter_table(query)

	def update(self, query):
		self.__alter_table(query)

	def delete(self, query):
		self.__alter_table(query)

	def __alter_table(self, query):
		with self.connection.cursor() as cursor:
			try:
				with self.connection.cursor as cursor:
					cursor.execute(query)

				self.connection.commit()
			except:
				self.connection.rollback()
			finally:
				self.connection.close()
				return True
