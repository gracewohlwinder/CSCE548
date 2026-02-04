import mysql.connector

class Database:
	def get_connection(self) -> mysql.connector.MySQLConnection:
		return mysql.connector.connect(
			user='csce548', password='csce548', host='127.0.0.1', database='csce548_project')

	def get_cursor(self) -> mysql.connector.cursor.MySQLCursor:
		cursor = Cursor(self)
		cursor.open()

		return cursor

class Cursor:
	def __init__(self, database: Database):
		self.database   = database
		self.connection = None
		self.cursor     = None

	def open(self):
		if not self.connection:
			self.connection = self.database.get_connection()
			self.cursor = self.connection.cursor()

	def close(self):
		if self.connection:
			self.cursor.close()
			self.connection.close()

	def get(self) -> mysql.connector.cursor.MySQLCursor:
		return self.cursor
