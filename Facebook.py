posts = []
users = []

class User():
	def __init__(self, name, email, password):
		self.name = name
		self.email = email
		self.password = password
		self.friends_list = []
		self.posts = []

	def add_friend(self, email):
		self.friends_list.append(email)
		print(self.name + " has added " + email + " as a friend")
	def remove_friend(self, email):
		self.friends_list.remove(email)
		print(self.name + " has removed " + email + " as a friend")
	def post(self, text):
		print(self.name + " has posted: " + text)
		self.posts.append(text)
	def get_userInfo(self):
		print("Name: " + str(self.name))
		print("Email: " + str(self.email))
		print("Password: " + str(self.password))
		print("Friends: " + str(self.friends_list))
		print("Posts: " + str(self.posts))

class Post():
	def __init__(self, text):
		self.text = text
class Comment(Post):
	def __init__(self):
		self.comments = []
	def add_comment(self,comment_text):
		self.comment_text = comment_text
		self.comment.append(comment_text)

user1 = User("Loai", "Loai17@meet.mit.edu" , "myhiddenpassword123")
user2 = User("Yousef", "yousef8ansari@gmail.com", "mypasswordhidden321")

user1.add_friend("yousef8ansari@gmail.com")
user1.post("Hey Yousef")
user1.get_userInfo()
