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

    def update(self, query):
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query)
                self.connection.commit()
            finally:
                self.connection.close()
                return True

