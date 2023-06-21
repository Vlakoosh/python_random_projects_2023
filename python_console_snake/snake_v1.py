import time
import os

#game variables
WIDTH = 20
HEIGHT = 8
title = "snake v01"
direction = ">"

snake_tiles = [(  int(HEIGHT/2-1),int(WIDTH/3)  ),(  int(HEIGHT/2-1),int(WIDTH/3-1)  )]
snake_head = snake_tiles[1]
berries = [ (  int(HEIGHT/2-1),int(WIDTH-5) ) ]

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def update_snake():
	#move the head forward
	
	#check for berry
	#if no berry:
	#	remove the tail
	#else:
	#	increase score

	#check_collision()
	#if head collides with wall or snake body, it dies

def update_board():
	update_snake()
	#update_berries()

def generate_board():
	#generate title and top border
	print("\n", (int(WIDTH/2)-int(len(title)/2))*" ", title)
	print((WIDTH+2)*"#")

	for row in range(0,HEIGHT):
		print("#",end='')
		for col in range(0,WIDTH):
			if (row,col) in snake_head:
				print(direction,end='')
			elif (row,col) in snake_tiles:
				print("O",end='')
			elif (row,col) in berries:
				print("$",end='')
			else:
				print(" ",end='')
		print("#")
	print((WIDTH+2)*"#")


def wait(seconds):
	time.sleep(seconds)

def main():
	while True:
		clear()
		update_board()
		generate_board()
		wait(0.5)

if __name__ == "__main__":
	main()
