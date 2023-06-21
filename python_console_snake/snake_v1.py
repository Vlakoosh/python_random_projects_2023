import time
import os
import random
from pytimedinput import timedKey

#game variables
WIDTH = 20
HEIGHT = 8
title = "snake v01"
direction = ">"
score = 0

snake_tiles = [(  int(HEIGHT/2-1),int(WIDTH/3)  ),(  int(HEIGHT/2-1),int(WIDTH/3-1)  )]
snake_head = snake_tiles[0]
berries = [ (  int(HEIGHT/2-1),int(WIDTH-5) ) ]

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def shift_right(lst):
    try:
        return [lst[-1]] + lst[:-1]
    except IndexError:
        return lst

def place_berry(spot):
	index = berries.index(snake_tiles[0])
	#repeat until a berry is placed in a spot "without snake"
	while berries[index] in snake_tiles:
		berries[index] = (random.randint(0,HEIGHT-1), random.randint(0,WIDTH-1))

def check_collision():
	if snake_tiles[0] in snake_tiles[1:len(snake_tiles)-1]:
		return False
	return True

def update_snake():
	global snake_tiles
	global snake_head
	global berries
	global score
	if snake_tiles[0] in berries:
		score += 5
		place_berry(snake_tiles[0])
		snake_tiles.append((-1,-1)) #creates a new list element at the end of the list
	#last element moves to first position to be replaced by the head
	#if didn't eat a berry, tail element will now be used as head
	snake_tiles = shift_right(snake_tiles)

	#move the head forward and check for edges
	if direction == ">":
		if snake_tiles[1][1] == WIDTH-1:
			return False
		snake_tiles[0] = (snake_tiles[1][0], snake_tiles[1][1]+1)
	elif direction == "<":
		if snake_tiles[1][1] == 0:
			return False
		snake_tiles[0] = (snake_tiles[1][0], snake_tiles[1][1]-1)
	elif direction == "^":
		if snake_tiles[1][0] == 0:
			return False
		snake_tiles[0] = (snake_tiles[1][0]-1, snake_tiles[1][1])
	elif direction == "v":
		if snake_tiles[1][0] == HEIGHT-1:
			return False
		snake_tiles[0] = (snake_tiles[1][0]+1, snake_tiles[1][1])
	snake_head = snake_tiles[0] 
	return check_collision()

	#if head collides with wall or snake body, it dies

def get_player_input():
	global direction
	userText, timedOut = timedKey(": ", 1, False)
	if timedOut:
		pass
	elif userText == "w":
		direction = "^"
	elif userText == "s":
		direction = "v"
	elif userText == "a":
		direction = "<"
	elif userText == "d":
		direction = ">"

def generate_board():
	#generate title and top border
	print(title," "*(WIDTH-4-len(title)), "%04d" % (score))
	print((WIDTH+2)*"#")

	for row in range(0,HEIGHT):
		print("#",end='')
		for col in range(0,WIDTH):
			if (row,col) == snake_head:
				print(direction,end='')
			elif (row,col) in snake_tiles:
				print("O",end='')
			elif (row,col) in berries:
				print("$",end='')
			else:
				print(" ",end='')
		print("#")
	print((WIDTH+2)*"#")

def check_finish():
	game_over = not update_snake() 
	if game_over:
		exit()

def wait(seconds):
	time.sleep(seconds)

def main():
	while True:
		clear()
		check_finish()
		generate_board()
		get_player_input()

if __name__ == "__main__":
	main()
