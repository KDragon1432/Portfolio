#medievalspiderman.py

import time


a = 0
b = 0
c = 0
d = 0

def introduction():
	print("Welcome to Medieval Spiderman")
	print("Once upon a time, Green Goblin invents a time machine to get Spiderman out of the way and takeover New York City.")
	print("His plan is successful and Spiderman is sent into the 17th century. Help Spiderman get back to the 21st century!")
	time.sleep(.8)
	print("...")
	time.sleep(.8)
	print("...")
	time.sleep(.8)
	print("Mordred: Intruder! Intruder! There is an intruder in the castle!")
	time.sleep(.5)
	print("Spiderman: Wait!... I'm not... there is a mis... ")
	time.sleep(.5)
	print("Mordred: Save your excuses for the dungeons you criminal!")
	mordred()
	
def mordred():
	global a
	global b
	global c
	global d 
	d = d + 1
	time.sleep(.5)
	print("[Mordred draws his sword and Spiderman must decide what to do. Help Spiderman make the best decision to get back to the 21st century.\nType in 1, 2, or 3 and then press ENTER.]")
	answer = int(input("1. Knock Him Out! \n2. Run Away \n3. Resort to Reason \n"))
	if answer == 1:
		print("[Spiderman performs a backflip and kicks Mordred in the face to knock him out.]")
		a = a + 1 
		kingarthur()
	elif answer == 2:
		print("[Mordred chases after the fleeing Spiderman.]")
		b = b + 1 
		if b >= 3:
			capture()
		else:
			kingarthur()
	elif answer == 3:
		print("Spiderman: I'm not a criminal! I'm a superhero from the future! I live in New York and I save people!")
		time.sleep(.5)
		print("Mordred: Where the hell is New York you insane criminal?! Did you think I would be gullible enough to believe your lies?")
		time.sleep(.5)
		print("[Spiderman fails to reason with Mordred and flees the scene.]")
		c = c + 1
		kingarthur()
		

def kingarthur():
	global a
	global b 
	global c 
	global d
	d = d + 1
	time.sleep(.8)
	print("...")
	time.sleep(.5)
	print("...")
	time.sleep(.8)
	print("[After Spiderman's encounter with Mordred, he comes across King Arthur!]")
	time.sleep(.5)
	print("King Arthur: HALT, intruder! What are you doing, trampling inside my castle in such an insulting costume? Did you come to assassinate me?!")
	time.sleep(.5)
	print("Spiderman: I don't want to assassinate you. I don't kill people. I don't even know you... ")
	time.sleep(.8)
	print("King Arthur:... ")
	time.sleep(.8)
	print("King Arthur:... ")
	time.sleep(.5)
	print("King Arthur: I am KING Arthur! What is a peasant like you doing inside this castle?")
	time.sleep(.5)
	print("...")
	answer = int(input("1. Knock Him Out! \n2. Run Away \n3. Resort to Reason \n"))
	if answer == 1:
		a = a + 1
		print("[Spiderman attaches himself to the ceiling and launches himself at the king to knock him out.]")
		lancelot()
	elif answer == 2:
		b = b + 1	
		print("[Spiderman flees and the King calls the guards to give chase.]")
		if b >= 3:
			capture()
		else:
			lancelot()
	elif answer == 3:
		c = c + 1 
		print("Spiderman: I am not a killer, I'm just lost!")
		time.sleep(.5)
		print("King Arthur: Lost?")
		time.sleep(.5)
		print("[Spiderman explains his situation. King Arthur is suspicious but he chooses to believe Spiderman.]")
		time.sleep(.8)
		print("King Arthur: I shall choose to believe you. If I find out you are lying I'll execute you. Let you visit Gaius, the Court Physician, he may be able to help you.")
		gaius()
		
	
def lancelot():
	global a
	global b
	global c
	global d 
	d = d + 1
	time.sleep(.5)
	print("[In the training grounds for Knights, Spiderman runs into Lancelot.]")

	

def gaius():
	global a 
	global b 
	global c 
	global d 
	d = d + 1
	time.sleep(.5)
	print("...")
	time.sleep(.5)
	print("...")
	time.sleep(.5)
	print("King Arthur: Gaius! Gaius!")
	time.sleep(.5)
	print("...")
	time.sleep(.5)
	print("Gaius: King Arthur! Is there anything you need? And this person is... ?")
	time.sleep(.5)
	print("King Arthur: This is...")
	print("Spiderman: Spiderman.")
	time.sleep(.5)
	print("Gaius: Pleased to meet you, Spiderman.")
	time.sleep(.5)
	print("Spiderman: You as well...")
	time.sleep(.1)
	print("King Arthur: Gaius, he claims to be of the future. Do you have any way of confirming this?")
	time.sleep(.3)
	print("Gaius: The future? Um, yes. A simple truth potion should comfirm it.")
	time.sleep(.8)
	print("...")
	time.sleep(.8)
	print("...")
	time.sleep(.8)
	print("...")
	time.sleep(.5)
	print("Gaius: My goodness, he really is from the future. How on earth did you travel to the past?")
	time.sleep(.5)
	print("Spiderman: Haha... ha. Um, I would ask if you had anyway to send me back to the future?")
	time.sleep(.5)
	print("Gaius: Can I? Of course, I can. It'll take me a few months to brew the required potion, but you'll definitely get home.")
	time.sleep(.8)
	print("[Spiderman spends the next 6 months helping Gaius brew the required potion to get home, but eventually he sees the skyscrapers of New York City.]")
	print("GAME OVER" + "Spiderman met " + str(d) + " people.")

	
	

def capture():
	time.sleep(.5)
	print("...")
	time.sleep(.5)
	print("...")
	print("[Too many people are chasing after Spiderman and he is eventually cornered and captured.]")
	if (a + b) > c:
		print("[Spiderman tries to reason with the people, but they do not believe him. He is thrown into a dungeon and his execution is scheduled.]")
		print("GAME OVER" + "Spiderman met " + str(d) + " people.")
	else:
		print("[Using his negotiation skills, Spiderman successfully pursues them that he is not a criminal and they agree to help get him back to the 21st century. He meets the Court Physician, Gaius, who helps him brew a potion to get home. After 6 months, he reunites with his modern day girlfriend.]")
		print("GAME OVER" + "Spiderman met " + str(d) + " people.")

		

introduction()