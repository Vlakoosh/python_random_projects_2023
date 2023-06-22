import string
import os

characters = string.printable
characters.replace(" ", "")
p = "123"

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def key_score(key):
	score = 0
	for char in key:
		score += ord(char)
	return score

def clamp_movement(movement):
	while movement < 0:
		movement += len(characters)
	while movement > len(characters):
		movement -= len(characters)
	return movement

def mystery(text, key='', decode = False):
	if decode:
		movement = len(characters) - key_score(key)
	else:
		movement = key_score(key)

	movement = clamp_movement(movement)

	new_text = ''
	for index, char in enumerate(text):
		char_pos = characters.index(char)
		new_text = new_text + characters[char_pos - movement]
	return new_text

def welcome():
	print("Welcome to your account manager")
	while True:
		password = input("To access your data, enter the correct password: ")
		if password == p:
			break
		else:
			print("Wrong password")
	print("welcome")

def prompt():
	print("Enter what you would like to do:")
	print("('d') to view you data")
	print("('a') to make a new entry")
	prompt = input(": ")
	if prompt == "d":
		clear()
		data = open("data.txt","r")



def main():
	welcome()

	'''
	password = "monkey@gmail.com"
	key = "123"
	password = mystery(password, key)
	print(password)
	password = mystery(password, key, True)
	print(password)
	'''
if __name__ == "__main__":
	main()