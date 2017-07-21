import random
import time
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
green = [0]

player_money = 50000

def choice():
	global player_money
	print("Your Money: " + str(player_money))
	if player_money <= 0:
		print("Game Over! You went bankrupt!")
	else:
		choice = int(input("What type of bet do you want to do? \n1. Number vs Number(35-1) \n2. Even vs Odd(1-1) \n3. Black vs Red(1-1) \n4. Dozen(2-1) \n5. Game Over \n"))
		if choice == 1:
			time.sleep(.8)
			print('...')
			time.sleep(.8)
			number()
		elif choice == 2:
			time.sleep(.8)
			print('...')
			time.sleep(.8)
			even_odd()
		elif choice == 3:
			time.sleep(.8)
			print('...')
			time.sleep(.8)
			color()
		elif choice == 4:
			time.sleep(.8)
			print("...")
			time.sleep(.8)
			dozen()
		elif choice == 5: 
			time.sleep(.8)
			print('...')
			time.sleep(.8)
			print("Game Over! You leave roulette with " + str(player_money) + " dollars.")
		


def number():
	global player_money
	bet = input("How much money do you want to bet?")
	if bet == "all":
		bet = player_money
	else:
		bet = int(bet)
	guess = input("What number do you want to bet on between 0 and 36? ")
	answer = random.randint(0, 36)
	
	if guess == answer:
		print("You win!")
		player_money = player_money + (bet * 35)
		print("It landed on " + str(answer))
	else :
		print("You lose!")
		player_money = player_money - bet
		print("It landed on " + str(answer))
	
	time.sleep(.8)
	print('...')
	time.sleep(.8)
	choice()


def even_odd():
	global player_money
	bet = input("How much money do you want to bet?")
	if bet == "all":
		bet = player_money
	else:
		bet = int(bet)
	guess = input("Do you bet even or odd?")
	answer = random.randint(0, 36)

	if answer % 2 == 0:
		huh = 'even'
	elif answer % 2 == 1:
		huh = 'odd'


	if answer == 0:
		print("You lose!")
		player_money = player_money - bet
		print("It landed on green.")
	elif (answer % 2 == 0) and (guess == 'even'):
		print("You win!")
		player_money = player_money + bet
		print("It landed on " + huh)
	elif (answer % 2 == 1) and (guess == 'odd'):
		print("You win!")
		player_money = player_money + bet 
		print("It landed on " + huh)
	else: 
		print("You lose!")
		player_money = player_money - bet
		print("It landed on " + huh)
	
	time.sleep(.8)
	print('...')
	time.sleep(.8)
	choice()

def color(): 
	global player_money
	bet = input("How much money do you want to bet?")
	if bet == "all":
		bet = player_money
	else: 
		bet = int(bet)
	guess = input("Do you bet red or black? ")
	answer = random.randint(0, 36)

	if answer in black:
		color = 'black'
	elif answer in red:
		color = 'red'
	elif answer in green:
		color = 'green'		

	if guess == 'red':
		if answer in red:
			print("You win!")
			player_money = player_money + bet
			print("The color is " + color)
		else:
			print("You lose!")
			player_money = player_money - bet
			print("The color is " + color)
	elif guess == 'black':
		if answer in black:
			print("You win!")
			player_money = player_money + bet
			print("The color is " + color)
		else:
			print("You lose!")
			player_money = player_money - bet
			print("The color is " + color)
	
	time.sleep(.8)
	print('...')
	time.sleep(.8)
	choice()		
			
def dozen():
	global player_money
	d1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
	d2 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
	d3 = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
	
	bet = input("How much money do you want to bet?")
	if bet == "all":
		bet = player_money
	else: 
		bet = int(bet)
	
	
	
	guess = int(input("Which dozen do you want to bet on?\n 1. 1-12\n 2. 13-24\n 3. 25-26\n"))
	answer = random.randint(0, 36)
	if guess == 1:
		if answer in d1:
			print("You win!")
			player_money = player_money +(bet * 2)
			print("It landed on " + str(answer))
		else: 
			print("You lose!")
			player_money = player_money - bet
			print("It landed on " + str(answer))
	elif guess == 2:
		if answer in d2:
			print("You win!")
			player_money = player_money +(bet * 2)
			print("It landed on " + str(answer))
		else: 
			print("You lose!")
			player_money = player_money - bet
			print("It landed on " + str(answer))
	elif guess == 3:
		if answer in d3:
			print("You win!")
			player_money = player_money +(bet * 2)
			print("It landed on " + str(answer))
		else: 
			print("You lose!")
			player_money = player_money - bet
			print("It landed on " + str(answer))
	time.sleep(.8)
	print('...')
	time.sleep(.8)
	choice()

choice()

