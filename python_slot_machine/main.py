import random
import time
import os

MAX_BET = 100
MIN_BET = 5

bal = 0
bet = 20
win = 0
label = "ROLL ME"

slots = [
	['X', 'X', 'X'],
	['X', 'X', 'X'],
	['X', 'X', 'X']
]

symbols = { 
	"7" : 1,
	"$" : 1,
	"#" : 1,
	"%" : 1
}

symbol_multipliers = {
	"7" : 100,
	"$" : 20,
	"#" : 1,
	"%" : 1
}
def get_all_symbols(symbols):
	all_symbols = []
	for symbol, number in symbols.items():
		for _ in range(number):
			all_symbols.append(symbol)
	return all_symbols

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def deposit():
	global bal
	clear()
	while True:
		answer = input("Enter the amount of tokens you want to deposit: ")
		if answer.isdigit():
			break
		else:
			print("Please enter a whole number")
	bal = bal + int(answer)

def change_bet():
	global bet
	clear()
	while True:
		answer = input("Enter your new bet: ")
		if answer.isdigit():
			if int(answer) < MIN_BET:
				print(f"Please enter a bet greater than {MIN_BET}")
			elif int(answer) > MAX_BET:
				print(f"Please enter a bet smaller than {MAX_BET}")
			else:
				break
		else:
			print("Please enter a whole number")
	bet = int(answer)


def check_win():
	global label
	global bet
	global win
	global bal
	multiplier = 0
	if slots[1][0] == slots[1][1] and slots[1][1] == slots[1][2]:
		multiplier = symbol_multipliers[slots[1][1]]
		
	print(multiplier)
	current_win = bet * multiplier
	

	if multiplier >= 20:
		label = "JACKPOT"
		bal += current_win
	elif current_win > 0:
		label = "YOU WIN"
		win = current_win
		bal += current_win
	else:
		label = "NO LUCK"	



def animate_slots (symbols):
	symbols = get_all_symbols(symbols)
	for starting_row in range(0,3):

		for _ in range(15):
			clear()

			for col in range(starting_row, 3):
				
				for row in range(3):
					pass
					symbol = random.choice(symbols)
					slots[row][col] = symbol

			generate_machine(bal, bet, win, label)

			time.sleep(0.03)
	check_win()
	clear()
	generate_machine(bal, bet, win, label)
	return slots

def generate_slots():
	pass
	"|   | 7 | 7 | 7 |   |"
	"|  [| 7 | 7 | 7 |]  |"
	"|   | 7 | 7 | 7 |   |"
	print("|   |", end='')
	for col in slots[0]:
		print(f" {col} |", end='')
	print("   |")
	print("|  [|", end='')
	for col in slots[1]:
		print(f" {col} |", end='')
	print("]  |")
	print("|   |", end='')
	for col in slots[2]:
		print(f" {col} |", end='')
	print("   |")
	pass

def generate_top(bal, bet, win):
	print(f"=-------------------=")
	print(f"|  balance:  {bal:05d}  |")
	print(f"|  bet:      {bet:05d}  |")
	print(f"|  win:      {win:05d}  |")
	print(f"|                   |")
	print(f"|-------------------|")
	print(f"|                   |")

#Generates the part of the machine below the slots, with the win/lose label
def generate_bottom(label):
	print(f"|                   |")
	print(f"|     [{label}]     |")
	print(f"|                   |")
	print(f"=====================")

#Generates the entire machine screen
def generate_machine(bal, bet, win, label):
	
	generate_top(bal, bet, win)
	generate_slots()
	generate_bottom(label)
	

def main():
	global bal
	global label
	global bet
	global win
	while True:
		clear()
		generate_machine(bal,bet,win,label)
		print("")
		print("### press enter to play")
		print("'d' to deposit more money")
		print("'q' to quit ")
		print("'b' to change your bet")
		answer = input("Enter your option: ")
		if answer == '':
			if bal <= bet:
				print("You don't have enough balance to place that bet")
				input()
			else:
				label = "ROLLING"
				bal -= bet
				slots = animate_slots(symbols)
		elif answer == 'q':
			exit()
		elif answer == 'b':
			change_bet()
		elif answer == 'd':
			deposit()
main()