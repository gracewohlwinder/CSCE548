from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from Database import Database
from User import UserDAO
from Post import PostDAO

api = FastAPI(title='Test API')

origins = [
	None,
    # "http://localhost",
    # "http://localhost:8000",
    "http://localhost:5174",
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

database = Database()

# @router.get('/users')
# async def get_users():
# 	return UserDAO(database).get_users()

@router.get('/users')
async def get_user_by_username(username: str | None = None):
	if username:
		return UserDAO(database).get_user_by_username(username)
	else:
		return UserDAO(database).get_users()

@router.get('/users/{user_id}')
async def get_user_by_id(user_id: int):
	return UserDAO(database).get_user_by_id(user_id)

@router.get('/users/{user_id}/followers')
async def get_followers(user_id: int):
	return UserDAO(database).get_followers(user_id)

@router.get('/users/{follower_id}/following')
async def get_following(follower_id: int):
	return UserDAO(database).get_following(follower_id)

@router.post('/users')
async def create_user(username: str):
	return UserDAO(database).create_user(username)

@router.post('/users/{user_id}')
async def update_username(user_id: int, username: str):
	return UserDAO(database).update_username(user_id, username)

@router.delete('/users/{user_id}')
async def delete_user(user_id: int):
	return UserDAO(database).delete_user(user_id)

@router.post('/users/{user_id}/followers')
async def add_follower(user_id: int, follower_id: int):
	return UserDAO(database).add_follower(user_id, follower_id)

@router.delete('/users/{user_id}/followers')
async def remove_follower(user_id: int, follower_id: int):
	return UserDAO(database).delete_follower(user_id, follower_id)

@router.get('/posts')
async def get_posts():
	return PostDAO(database).get_posts()

@router.get('/posts/deleted')
async def get_posts():
	return PostDAO(database).get_deleted_posts()

@router.get('/posts/{post_id}')
async def get_post_by_id(post_id: int):
	return PostDAO(database).get_post_by_id(post_id)

@router.get('/users/{user_id}/posts')
async def get_posts(user_id: int):
	return PostDAO(database).get_posts_by_user_id(user_id)

@router.get('/users/{user_id}/posts/deleted')
async def get_posts(user_id: int):
	return PostDAO(database).get_deleted_posts_by_user_id(user_id)

@router.post('/users/{user_id}/posts')
async def create_post(user_id: int, description: str):
	return PostDAO(database).create_post(user_id, description)

@router.post('/posts/{post_id}')
async def update_description(post_id: int, description: str):
	return PostDAO(database).update_description(post_id, description)

@router.delete('/posts/{post_id}')
async def delete_post(post_id: int):
	return PostDAO(database).delete_post(post_id)

@router.get('/comments')
async def get_comments():
	return PostDAO(database).get_comments()

@router.get('/comments/deleted')
async def get_deleted_comments():
	return PostDAO(database).get_deleted_comments()

@router.get('/users/{user_id}/comments')
async def get_user_comments(user_id: int):
	return PostDAO(database).get_user_comments(user_id)

@router.get('/users/{user_id}/comments/deleted')
async def get_user_comments(user_id: int):
	return PostDAO(database).get_deleted_user_comments(user_id)

@router.get('/posts/{post_id}/comments')
async def get_post_comments(post_id: int):
	return PostDAO(database).get_post_comments(post_id)

@router.get('/posts/{post_id}/comments/deleted')
async def get_post_comments(post_id: int):
	return PostDAO(database).get_deleted_post_comments(post_id)

@router.post('/posts/{post_id}/comments')
async def create_comment(post_id: int, user_id: int, comment: str):
	return PostDAO(database).create_comment(post_id, user_id, comment)

@router.post('/comments/{comment_id}')
async def update_comment(comment_id: int, comment: str):
	return PostDAO(database).update_comment(comment_id, comment)

@router.delete('/comments/{comment_id}')
async def delete_comment(comment_id: int):
	return PostDAO(database).delete_comment(comment_id)

@router.get('/favorites')
async def get_favorites():
	return PostDAO(database).get_favorites()

@router.get('/posts/{post_id}/favorites')
async def get_post_favorites(post_id: int):
	return PostDAO(database).get_favorites_by_post_id(post_id)

@router.get('/users/{user_id}/favorites')
async def get_user_favorites(user_id: int):
	return PostDAO(database).get_favorites_by_user_id(user_id)

@router.post('/posts/{post_id}/favorites')
async def add_favorite(post_id: int, user_id: int):
	return PostDAO(database).add_favorite(post_id, user_id)

@router.delete('/posts/{post_id}/favorites')
async def remove_favorite(post_id: int, user_id: int):
	return PostDAO(database).remove_favorite(post_id, user_id)

api.include_router(router)

