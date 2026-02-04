from Database import Database
from Post import PostDAO
from User import UserDAO

database = Database()

user_dao = UserDAO(database)
post_dao = PostDAO(database)

print('--- User ---')
print(' - list users')
users = user_dao.get_users()
for user in users:
	print(user)

print()
print(' - create user')
user_dao.create_user("demo_username")
users = user_dao.get_users()
for user in users:
	print(user)

new_user = users[-1]

print()
print(' - update username')
user_dao.update_username(new_user[0], 'demo_username_updated')
print(user_dao.get_users()[-1])

print()
print(' - delete user')
user_dao.delete_user(new_user[0])
users = user_dao.get_users()
for user in users:
	print(user)


first_user = users[0]

print()
print(' - get followers')
followers = user_dao.get_followers(first_user[0])
for follower in followers:
	print(follower)


print()
print(' - add follower')
user_dao.add_follower(first_user[0], 4)
followers = user_dao.get_followers(first_user[0])
for follower in followers:
	print(follower)

print()
print(' - delete follower')
user_dao.delete_follower(first_user[0], 4)
followers = user_dao.get_followers(first_user[0])
for follower in followers:
	print(follower)

print()
print()
print()
print('--- Post ---')
print(' - list posts')
posts = post_dao.get_posts(first_user[0])
for post in posts:
	print(post)

print()
print(' - create post')
post_dao.create_post(first_user[0], "demo post")
posts = post_dao.get_posts(first_user[0])
for post in posts:
	print(post)

new_post = posts[-1]

print()
print(' - update post')
post_dao.update_description(new_post[0], 'edited description')
print(post_dao.get_posts(first_user[0])[-1])

print()
print(' - delete post')
post_dao.delete_post(new_post[0])
posts = post_dao.get_posts(first_user[0])
for post in posts:
	print(post)


first_post = posts[0]

print()
print(' - list favorites')
favorites = post_dao.get_favorites(first_post[0])
for favorite in favorites:
	print(favorite)

print()
print(' - add favorite')
post_dao.add_favorite(first_post[0], users[-1][0])
favorites = post_dao.get_favorites(first_user[0])
for favorite in favorites:
	print(favorite)

print()
print(' - delete favorite')
post_dao.remove_favorite(first_post[0], users[-1][0])
favorites = post_dao.get_favorites(first_user[0])
for favorite in favorites:
	print(favorite)

print()
print(' - list comments')
comments = post_dao.get_comments(first_post[0])
for comment in comments:
	print(comment)

print()
print(' - create comment')
post_dao.create_comment(first_post[0], first_user[0], "demo comment")
comments = post_dao.get_comments(first_post[0])
for comment in comments:
	print(comment)

new_post = posts[-1]

print()
print(' - update comment')
post_dao.update_comment(comments[-1][0], 'edited comment')
print(post_dao.get_comments(first_post[0])[-1])

print()
print(' - delete comment')
post_dao.delete_comment(comments[-1][0])
comments = post_dao.get_comments(first_post[0])
for comment in comments:
	print(comment)
