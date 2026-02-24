from datetime import datetime
from typing import List

class User:
	def __init__(self, user_id: int, username: str,
		description: str, created_at: datetime):

		self.id            = user_id
		self.username      = username
		self.description   = description
		self.created_at    = created_at


class Post:
	def __init__(self, post_id: int, user_id: int, description: str,
		created_at: datetime, deleted_at: datetime):

		self.id          = post_id
		self.user_id     = user_id
		self.description = description
		self.created_at  = created_at
		self.deleted_at  = deleted_at


class Favorite:
	def __init__(self, post_id: int, user_id: int, created_at: datetime):

		self.post_id    = post_id
		self.user_id    = user_id
		self.created_at = created_at


class Comment:
	def __init__(self, comment_id: int, post_id: int, user_id: int,
			comment: str, created_at: datetime, deleted_at: datetime):

		self.id         = comment_id
		self.post_id    = post_id
		self.user_id    = user_id
		self.comment    = comment
		self.created_at = created_at
		self.deleted_at = deleted_at

