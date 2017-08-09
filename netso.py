

class user:
	def __init__(self, username):
		self.username = username
		self.connections = []
	def add_connection(self, who_else):
		self.connections.append(who_else)
class network:
	def __init__(self):
		self.all = []
	def add_newUser(self, user2add):
		self.all.append(user2add)

def createUser():
	name = input("please enter a username")
	User = user(name)
	my_network.add_newUser(User)	
	operation()
def allUser():
	for i in range(0, len(my_network.all)):
		print(my_network.all.pop(0).username)
		operation()
def addC():
	
def operation():
	print("What do you want to do?")
	print("0. exit")
	print("1. create a user")
	print("2. show all users")
	print("3. add connections")
	operation = int(input(""))
	if operation == 0:
		print("Bye-Bye! Come back again!")
	if operation == 1:
		createUser()
	if operation == 2:
		allUser()
	if operation == 3:
		addC()
def main():
	global my_network
	print("Welcome to NETSO!")
	my_network = network()
	operation()
		
	
main()