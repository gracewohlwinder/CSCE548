from Database import Database
from Models import Post, Favorite, Comment
from datetime import datetime
from typing import List

class PostDAO:
	def __init__(self, database: Database):
		self.database = database

	def get_post_by_id(self, post_id: int) -> Post:
		cursor = self.database.get_cursor()
		
		query = f"SELECT id, user_id, description, created_at, deleted_at FROM post WHERE id = {post_id} LIMIT 1;"
		cursor.get().execute(query)

		p = cursor.get().fetchone()
		post = Post(p[0], p[1], p[2], p[3], p[4])

		cursor.close()

		return post

	def get_posts(self) -> List[Post]:
		cursor = self.database.get_cursor()
		
		query = f"SELECT id, user_id, description, created_at, deleted_at FROM post WHERE deleted_at IS NULL"
		cursor.get().execute(query)

		posts = [Post(p[0], p[1], p[2], p[3], p[4]) for p in cursor.get().fetchall()]

		cursor.close()

		return posts

	def get_deleted_posts(self) -> List[Post]:
		cursor = self.database.get_cursor()
		
		query = f"SELECT id, user_id, description, created_at, deleted_at FROM post WHERE deleted_at IS NOT NULL"
		cursor.get().execute(query)

		posts = [Post(p[0], p[1], p[2], p[3], p[4]) for p in cursor.get().fetchall()]

		cursor.close()

		return posts

	def get_posts_by_user_id(self, user_id: int) -> List[Post]:
		cursor = self.database.get_cursor()
		
		query = f"SELECT id, user_id, description, created_at, deleted_at FROM post WHERE user_id = {user_id} AND deleted_at IS NULL;"
		cursor.get().execute(query)

		posts = [Post(p[0], p[1], p[2], p[3], p[4]) for p in cursor.get().fetchall()]

		cursor.close()

		return posts

	def get_deleted_posts_by_user_id(self, user_id: int) -> List[Post]:
		cursor = self.database.get_cursor()
		
		query = f"SELECT id, user_id, description, created_at, deleted_at FROM post WHERE user_id = {user_id} AND deleted_at IS NOT NULL;"
		cursor.get().execute(query)

		posts = [Post(p[0], p[1], p[2], p[3], p[4]) for p in cursor.get().fetchall()]

		cursor.close()

		return posts

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

	def get_comments(self) -> List[Comment]:
		cursor = self.database.get_cursor()
		
		query = f"SELECT id, post_id, user_id, comment, created_at, deleted_at FROM comment WHERE deleted_at IS NULL;"
		cursor.get().execute(query)

		comments = [Comment(c[0], c[1], c[2], c[3], c[4], c[5]) for c in cursor.get().fetchall()]

		cursor.close()

		return comments

	def get_deleted_comments(self) -> List[Comment]:
		cursor = self.database.get_cursor()
		
		query = f"SELECT id, post_id, user_id, comment, created_at, deleted_at FROM comment WHERE deleted_at IS NOT NULL;"
		cursor.get().execute(query)

		comments = [Comment(c[0], c[1], c[2], c[3], c[4], c[5]) for c in cursor.get().fetchall()]

		cursor.close()

		return comments

	def get_user_comments(self, user_id: int) -> List[Comment]:
		cursor = self.database.get_cursor()
		
		query = f"SELECT id, post_id, user_id, comment, created_at, deleted_at FROM comment WHERE user_id = {user_id} AND deleted_at IS NULL;"
		cursor.get().execute(query)

		comments = [Comment(c[0], c[1], c[2], c[3], c[4], c[5]) for c in cursor.get().fetchall()]

		cursor.close()

		return comments

	def get_deleted_user_comments(self, user_id: int) -> List[Comment]:
		cursor = self.database.get_cursor()
		
		query = f"SELECT id, post_id, user_id, comment, created_at, deleted_at FROM comment WHERE user_id = {user_id} AND deleted_at IS NOT NULL;"
		cursor.get().execute(query)

		comments = [Comment(c[0], c[1], c[2], c[3], c[4], c[5]) for c in cursor.get().fetchall()]

		cursor.close()

		return comments

	def get_post_comments(self, post_id: int) -> List[Comment]:
		cursor = self.database.get_cursor()
		
		query = f"SELECT id, post_id, user_id, comment, created_at, deleted_at FROM comment WHERE post_id = {post_id} AND deleted_at IS NULL;"
		cursor.get().execute(query)

		comments = [Comment(c[0], c[1], c[2], c[3], c[4], c[5]) for c in cursor.get().fetchall()]

		cursor.close()

		return comments

	def get_deleted_post_comments(self, post_id: int) -> List[Comment]:
		cursor = self.database.get_cursor()
		
		query = f"SELECT id, post_id, user_id, comment, created_at, deleted_at FROM comment WHERE post_id = {post_id} AND deleted_at IS NOT NULL;"
		cursor.get().execute(query)

		comments = [Comment(c[0], c[1], c[2], c[3], c[4], c[5]) for c in cursor.get().fetchall()]

		cursor.close()

		return comments

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

	def get_favorites(self) -> List[Favorite]:
		cursor = self.database.get_cursor()
		
		query = f"SELECT post_id, user_id, created_at FROM favorite;"
		cursor.get().execute(query)

		favorites = [Favorite(f[0], f[1], f[2]) for f in cursor.get().fetchall()]

		cursor.close()

		return favorites

	def get_favorites_by_post_id(self, post_id: int) -> List[Favorite]:
		cursor = self.database.get_cursor()
		
		query = f"SELECT post_id, user_id, created_at FROM favorite WHERE post_id = {post_id};"
		cursor.get().execute(query)

		favorites = [Favorite(f[0], f[1], f[2]) for f in cursor.get().fetchall()]

		cursor.close()

		return favorites

	def get_favorites_by_user_id(self, user_id: int) -> List[Favorite]:
		cursor = self.database.get_cursor()
		
		query = f"SELECT post_id, user_id, created_at FROM favorite WHERE user_id = {user_id};"
		cursor.get().execute(query)

		favorites = [Favorite(f[0], f[1], f[2]) for f in cursor.get().fetchall()]

		cursor.close()

		return favorites

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
