from Database import Database

class PostDAO:
	def __init__(self, database: Database):
		self.database = database

	def get_posts(self, user_id: int):
		cursor = self.database.get_cursor()
		
		query = f"SELECT id, user_id, description, created_at, deleted_at FROM post WHERE user_id = {user_id};"
		cursor.get().execute(query)

		rows = cursor.get().fetchall()

		cursor.close()

		return rows

	def create_post(self, user_id: int, description: str):
		cursor = self.database.get_cursor()
		
		query = f"INSERT INTO post (user_id, description) VALUES ({user_id}, '{description}');"
		cursor.get().execute(query)
		cursor.connection.commit()

		cursor.close()

	def update_description(self, post_id: int, description: str):
		cursor = self.database.get_cursor()
		
		query = f"UPDATE post SET description = '{description}' WHERE id = {post_id};"
		cursor.get().execute(query)
		cursor.connection.commit()

		cursor.close()

	def delete_post(self, post_id: int):
		cursor = self.database.get_cursor()
		
		query = f"UPDATE post SET deleted_at = NOW() WHERE id = {post_id} AND deleted_at IS NULL;"
		cursor.get().execute(query)
		cursor.connection.commit()

		cursor.close()

	def get_comments(self, post_id: int):
		cursor = self.database.get_cursor()
		
		query = f"SELECT id, post_id, user_id, comment, created_at, deleted_at FROM comment WHERE post_id = {post_id};"
		cursor.get().execute(query)

		rows = cursor.get().fetchall()

		cursor.close()

		return rows

	def create_comment(self, post_id: int, user_id: int, comment: str):
		cursor = self.database.get_cursor()
		
		query = f"INSERT INTO comment (user_id, post_id, comment) VALUES ({user_id}, {post_id}, '{comment}');"
		cursor.get().execute(query)
		cursor.connection.commit()

		cursor.close()

	def update_comment(self, comment_id: int, comment: str):
		cursor = self.database.get_cursor()
		
		query = f"UPDATE comment SET comment = '{comment}' WHERE id = {comment_id};"
		cursor.get().execute(query)
		cursor.connection.commit()

		cursor.close()

	def delete_comment(self, comment_id: int):
		cursor = self.database.get_cursor()
		
		query = f"UPDATE comment SET deleted_at = NOW() WHERE id = {comment_id} AND deleted_at IS NULL;"
		cursor.get().execute(query)
		cursor.connection.commit()

		cursor.close()

	def get_favorites(self, post_id: int):
		cursor = self.database.get_cursor()
		
		query = f"SELECT post_id, user_id, created_at FROM favorite WHERE post_id = {post_id};"
		cursor.get().execute(query)

		rows = cursor.get().fetchall()

		cursor.close()

		return rows

	def add_favorite(self, post_id: int, user_id: int):
		cursor = self.database.get_cursor()
		
		query = f"INSERT INTO favorite (user_id, post_id) VALUES ({user_id}, {post_id});"
		cursor.get().execute(query)
		cursor.connection.commit()

		cursor.close()

	def remove_favorite(self, post_id: int, user_id: int):
		cursor = self.database.get_cursor()
		
		query = f"DELETE FROM favorite WHERE user_id = {user_id} AND post_id = {post_id};"
		cursor.get().execute(query)
		cursor.connection.commit()

		cursor.close()

	def close_connection():
		self.database_connection.close()
