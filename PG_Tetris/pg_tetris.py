# pg_tetris.py
# Tetris clone, built with Python and PyGame
# Author: Jackie P, aka TheDataElemental

# Work in progress as of 12/27/21


import pygame
import random


# Falling "tetris block" / "tetris piece". Tiles arranged in a shape
class Block:
	def __init__(self, tile, shape):
		self.tile = tile  # Image repeated for each tile of the block
		self.shape = shape  # Shape of block (2D array of 0's and 1's)
		# Starting position at top of screen
		self.x = 240
		self.y = 64


# Draw background and blocks
def render_screen():
	# Draw background
	screen.blit(background, (0,0))
	screen.blit(pygame_text_display, (56, 24))
	screen.blit(tetris_text_display, (56, 56))
	screen.blit(copyright_text_display, (96, 456))
	
	screen.blit(lines_text_display, (56, 168))
	lines_counter = text_font.render(str(lines), True, WHITE)
	screen.blit(lines_counter, (84, 192))
	
	screen.blit(level_text_display, (56, 296))
	level_counter = text_font.render(str(level), True, WHITE)
	screen.blit(level_counter, (84, 320))
	
	screen.blit(next_text_display, (400, 136))
	
	# Draw falling block
	render_x = current_block.x
	render_y = current_block.y
	for row in current_block.shape:
		for bit in row:
			if bit == 1:
				screen.blit(current_block.tile, (render_x, render_y))
			render_x += 16
		render_x = 240
		render_y += 16
		
	pygame.display.flip()
	

# Generate and spawn a new block at the top of the screen	
def new_block():
	global current_block
	
	block_color = block_tiles[random.randint(0, 6)]
	block_shape = block_shapes[random.randint(0, 6)]
	current_block = Block(block_color, block_shape)


# Start game window
pygame.init()
screen = pygame.display.set_mode((512, 480), \
	pygame.HWSURFACE | pygame.DOUBLEBUF, vsync = 1)
pygame.display.set_caption("PG TETRIS")

clock = pygame.time.Clock()
fall_speed = 1
text_font = pygame.font.Font("NESfont.ttf", 14)
WHITE = (255, 255, 255)
lines = 0
level = 1

# Define block shapes
# Shapes are represented internally as 4x4 arrays of 0's and 1's.
# 1 = tile, 0 = no tile.
# This shape array is used for both collision and rendering.
O_shape_1 = [
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 1, 1, 0],
	[0, 1, 1, 0],
	]

I_shape_1 = [
	[0, 1, 0, 0],
	[0, 1, 0, 0],
	[0, 1, 0, 0],
	[0, 1, 0, 0],
	]

T_shape_1 = [
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 1, 0, 0],
	[1, 1, 1, 0],
	]

J_shape_1 = [
	[0, 0, 0, 0],
	[0, 1, 0, 0],
	[0, 1, 0, 0],
	[1, 1, 0, 0],
	]
	
	
L_shape_1 = [
	[0, 0, 0, 0],
	[0, 1, 0, 0],
	[0, 1, 0, 0],
	[0, 1, 1, 0],
	]

S_shape_1 = [
	[0, 0, 0, 0],
	[0, 1, 0, 0],
	[0, 1, 1, 0],
	[0, 0, 1, 0],
	]

Z_shape_1 = [
	[0, 0, 0, 0],
	[0, 0, 1, 0],
	[0, 1, 1, 0],
	[0, 1, 0, 0],
	]

fill_well_shape = [
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	]

# Load tile images
red_tile = pygame.image.load("Assets/Exports/red_tile.png")
blue_tile = pygame.image.load("Assets/Exports/blue_tile.png")
yellow_tile = pygame.image.load("Assets/Exports/yellow_tile.png")
gray_tile = pygame.image.load("Assets/Exports/gray_tile.png")
purple_tile = pygame.image.load("Assets/Exports/purple_tile.png")
green_tile = pygame.image.load("Assets/Exports/green_tile.png")
orange_tile = pygame.image.load("Assets/Exports/orange_tile.png")

black_screen = pygame.image.load("Assets/Exports/black_screen.png")
background = pygame.image.load("Assets/Exports/tetris_background.png")

# Generate UI Text
lines_text = "LINES: "
lines_text_display = text_font.render(lines_text, True, WHITE)

next_text = "NEXT: "
next_text_display = text_font.render(next_text, True, WHITE)

level_text = "LEVEL: "
level_text_display = text_font.render(level_text, True, WHITE)

pygame_text = "PYGAME"
pygame_text_display = text_font.render(pygame_text, True, WHITE)

tetris_text = "TETRIS"
tetris_text_display = text_font.render(tetris_text, True, WHITE)

copyright_text = "2022  THE DATA ELEMENTAL"
copyright_text_display = text_font.render(copyright_text, True, WHITE)

# Make tetris blocks
O_block = Block(orange_tile, O_shape_1)
I_block = Block(gray_tile, I_shape_1)
T_block = Block(yellow_tile, T_shape_1)
J_block = Block(purple_tile,  J_shape_1)
L_block = Block(green_tile, L_shape_1)
S_block = Block(red_tile, S_shape_1)
Z_block = Block(blue_tile, Z_shape_1)
fill_well_block = Block(red_tile, fill_well_shape)
	
block_tiles = [
	orange_tile,
	gray_tile,
	yellow_tile,
	purple_tile,
	green_tile,
	red_tile,
	blue_tile,
	]

block_shapes = [
	O_shape_1,
	I_shape_1,
	T_shape_1,
	J_shape_1,
	L_shape_1,
	S_shape_1,
	Z_shape_1,
	]
	

# TODO: make other three variations (rotations) for each block shape
# TODO: write code to use arrays for collision and rendering
# TODO: controls - left and right, down boost, piece rotation
# TODO: main game loop, score, random pieces
# TODO: lose state, win state, line clearing


new_block()

# Main game loop
while True:
	pygame.event.pump()
	render_screen()
	clock.tick(5 * fall_speed)
	current_block.y +=16
	if current_block.y == 336:
		new_block()





