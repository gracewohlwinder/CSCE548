from Database import Database
from Models import User
from datetime import datetime
from typing import List

class UserDAO:
	def __init__(self, database: Database):
		self.database = database

	def get_user_by_id(self, user_id: int) -> User:
		cursor = self.database.get_cursor()
		
		query = f"SELECT id, username, description, created_at FROM user WHERE id = {user_id} LIMIT 1;"
		cursor.get().execute(query)

		u = cursor.get().fetchone()
		user = User(u[0], u[1], u[2], u[3])

		cursor.close()

		return user

	def get_user_by_username(self, username: str) -> User:
		cursor = self.database.get_cursor()
		
		query = f"SELECT id, username, description, created_at FROM user WHERE username = '{username}' LIMIT 1;"
		cursor.get().execute(query)

		u = cursor.get().fetchone()
		user = User(u[0], u[1], u[2], u[3])

		cursor.close()

		return user

	def get_users(self) -> List[User]:
		cursor = self.database.get_cursor()
		
		query = "SELECT id, username, description, created_at FROM user;"
		cursor.get().execute(query)

		users = [User(u[0], u[1], u[2], u[3]) for u in cursor.get().fetchall()]

		cursor.close()

		return users

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

	def get_followers(self, user_id: int) -> List[User]:
		cursor = self.database.get_cursor()
		
		query = f"SELECT user.id, user.username, user.description, user.created_at FROM follower JOIN user ON user.id = follower.follower_id WHERE user_id = {user_id};"
		cursor.get().execute(query)

		users = [User(u[0], u[1], u[2], u[3]) for u in cursor.get().fetchall()]

		cursor.close()

		return users

	def get_following(self, follower_id: int) -> List[User]:
		cursor = self.database.get_cursor()
		
		query = f"SELECT user.id, user.username, user.description, user.created_at FROM follower JOIN user ON user.id = follower.user_id WHERE follower_id = {follower_id};"
		cursor.get().execute(query)

		users = [User(u[0], u[1], u[2], u[3]) for u in cursor.get().fetchall()]

		cursor.close()

		return users

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
