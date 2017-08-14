signed_in = False


class user:
	def __init__(self, name):
		self.username = name
		self.email = "empty"
		self.password = "password"
	def setEmail(self, email):
		self.email = email
	def setPassword(self, password):
		self.password = password

def makeUser():
	if password == password2:
		newUser = user(username)
		newUser.setEmail = email
		newUser.setPassword = password
	else:
		account_error()
	