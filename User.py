from Database import Database

class UserDAO:
	def __init__(self, database: Database):
		self.database = database

	def get_users(self):
		cursor = self.database.get_cursor()
		
		query = "SELECT id, username, description, created_at FROM user;"
		cursor.get().execute(query)

		rows = cursor.get().fetchall()

		cursor.close()

		return rows

	def create_user(self, username: str):
		cursor = self.database.get_cursor()

		query = f"INSERT INTO user (username) VALUES ('{username}');"
		cursor.get().execute(query)
		cursor.connection.commit()

		cursor.close()

	def update_username(self, user_id: int, username: str):
		cursor = self.database.get_cursor()
		
		query = f"UPDATE user SET username = '{username}' WHERE id = {user_id};"
		cursor.get().execute(query)
		cursor.connection.commit()

		cursor.close()

	def delete_user(self, user_id: int):
		cursor = self.database.get_cursor()
		
		query = f"DELETE FROM user WHERE id = {user_id};"
		cursor.get().execute(query)
		cursor.connection.commit()

		cursor.close()

	def get_followers(self, user_id: int):
		cursor = self.database.get_cursor()
		
		query = f"SELECT user_id, follower_id, created_at FROM follower WHERE user_id = {user_id};"
		cursor.get().execute(query)

		rows = cursor.get().fetchall()

		cursor.close()

		return rows

	def add_follower(self, user_id: int, follower_id: int):
		cursor = self.database.get_cursor()
		
		query = f"INSERT INTO follower (user_id, follower_id) VALUES ({user_id}, {follower_id});"
		cursor.get().execute(query)
		cursor.connection.commit()

		cursor.close()

	def delete_follower(self, user_id: int, follower_id: int):
		cursor = self.database.get_cursor()
		
		query = f"DELETE FROM follower WHERE user_id = {user_id} AND follower_id = {follower_id};"
		cursor.get().execute(query)
		cursor.connection.commit()

		cursor.close()
