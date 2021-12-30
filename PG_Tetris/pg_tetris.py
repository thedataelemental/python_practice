# pg_tetris.py
# Tetris clone, built with Python and PyGame
# Author: Jackie P, aka TheDataElemental

# Work in progress as of 12/27/21


import pygame
import random


# Falling "tetris block" / "tetris piece". Tiles arranged in a shape
class Block:
	def __init__(self, tile, shapes):
		# Image repeated for each tile of the block
		self.tile = tile 
		# List of shapes (rotations) of block (2D arrays of 0's and 1's)
		self.shapes = shapes  
		# Starting position at top of screen
		self.x = 240
		self.y = 64
		# Default shape / rotation
		self.shape_index = 0
		self.current_shape = self.shapes[self.shape_index]


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
	for row in current_block.current_shape:
		for bit in row:
			if bit == 1:
				screen.blit(current_block.tile, (render_x, render_y))
			render_x += 16
		render_x = current_block.x
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
frame_counter = 0

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

O_shape_2 = [
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 1, 1, 0],
	[0, 1, 1, 0],
	]
	
O_shape_3 = [
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 1, 1, 0],
	[0, 1, 1, 0],
	]
	
O_shape_4 = [
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 1, 1, 0],
	[0, 1, 1, 0],
	]
	
O_shapes = [O_shape_1, O_shape_2, O_shape_3, O_shape_4]


I_shape_1 = [
	[0, 1, 0, 0],
	[0, 1, 0, 0],
	[0, 1, 0, 0],
	[0, 1, 0, 0],
	]
	
I_shape_2 = [
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[1, 1, 1, 1],
	[0, 0, 0, 0],
	]

I_shape_3 = [
	[0, 1, 0, 0],
	[0, 1, 0, 0],
	[0, 1, 0, 0],
	[0, 1, 0, 0],
	]
	
I_shape_4 = [
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[1, 1, 1, 1],
	[0, 0, 0, 0],
	]

I_shapes = [I_shape_1, I_shape_2, I_shape_3, I_shape_4]


T_shape_1 = [
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 1, 0, 0],
	[1, 1, 1, 0],
	]
	
T_shape_2 = [
	[0, 0, 0, 0],
	[0, 1, 0, 0],
	[0, 1, 1, 0],
	[0, 1, 0, 0],
	]

T_shape_3 = [
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[1, 1, 1, 0],
	[0, 1, 0, 0],
	]

T_shape_4 = [
	[0, 0, 0, 0],
	[0, 1, 0, 0],
	[1, 1, 0, 0],
	[0, 1, 0, 0],
	]
	
T_shapes = [T_shape_1, T_shape_2, T_shape_3, T_shape_4]
	

J_shape_1 = [
	[0, 0, 0, 0],
	[0, 1, 0, 0],
	[0, 1, 0, 0],
	[1, 1, 0, 0],
	]
	
J_shape_2 = [
	[0, 0, 0, 0],
	[1, 0, 0, 0],
	[1, 1, 1, 0],
	[0, 0, 0, 0],
	]
	
J_shape_3 = [
	[0, 0, 0, 0],
	[0, 1, 1, 0],
	[0, 1, 0, 0],
	[0, 1, 0, 0],
	]
	
J_shape_4 = [
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[1, 1, 1, 0],
	[0, 0, 1, 0],
	]
	
J_shapes = [J_shape_1, J_shape_2, J_shape_3, J_shape_4]
	
	
L_shape_1 = [
	[0, 0, 0, 0],
	[0, 1, 0, 0],
	[0, 1, 0, 0],
	[0, 1, 1, 0],
	]
	
L_shape_2 = [
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[1, 1, 1, 0],
	[1, 0, 0, 0],
	]
	
L_shape_3 = [
	[0, 0, 0, 0],
	[1, 1, 0, 0],
	[0, 1, 0, 0],
	[0, 1, 0, 0],
	]
	
L_shape_4 = [
	[0, 0, 0, 0],
	[0, 0, 1, 0],
	[1, 1, 1, 0],
	[0, 0, 0, 0],
	]

L_shapes = [L_shape_1, L_shape_2, L_shape_3, L_shape_4]


S_shape_1 = [
	[0, 0, 0, 0],
	[0, 1, 0, 0],
	[0, 1, 1, 0],
	[0, 0, 1, 0],
	]

S_shape_2 = [
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 1, 1, 0],
	[1, 1, 0, 0],
	]
	
S_shape_3 = [
	[0, 0, 0, 0],
	[0, 1, 0, 0],
	[0, 1, 1, 0],
	[0, 0, 1, 0],
	]
	
S_shape_4 = [
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 1, 1, 0],
	[1, 1, 0, 0],
	]

S_shapes = [S_shape_1, S_shape_2, S_shape_3, S_shape_4]


Z_shape_1 = [
	[0, 0, 0, 0],
	[0, 0, 1, 0],
	[0, 1, 1, 0],
	[0, 1, 0, 0],
	]
	
Z_shape_2 = [
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[1, 1, 0, 0],
	[0, 1, 1, 0],
	]

Z_shape_3 = [
	[0, 0, 0, 0],
	[0, 0, 1, 0],
	[0, 1, 1, 0],
	[0, 1, 0, 0],
	]
	
Z_shape_4 = [
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[1, 1, 0, 0],
	[0, 1, 1, 0],
	]
	
Z_shapes = [Z_shape_1, Z_shape_2, Z_shape_3, Z_shape_4]
	

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
	O_shapes,
	I_shapes,
	T_shapes,
	J_shapes,
	L_shapes,
	S_shapes,
	Z_shapes,
	]
	

# TODO: make other three variations (rotations) for each block shape
# TODO: write code to use arrays for collision and rendering
# TODO: controls - left and right, down boost, piece rotation
# TODO: main game loop, score, random pieces
# TODO: lose state, win state, line clearing


new_block()
action_frame = 0

# Main game loop
while True:
	# Quit game if window is closed
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			sys.exit()
	
	# Rotate block left and right
	key = pygame.key.get_pressed()
	if key[pygame.K_e]:
		if done_action == False:
			current_block.shape_index += 1
			if current_block.shape_index >= 4:
				current_block.shape_index = 0
			current_block.current_shape = \
				current_block.shapes[current_block.shape_index]
			done_action = True
			action_frame = frame_counter
			
	elif key[pygame.K_r]:
		if done_action == False:
			current_block.shape_index -= 1
			if current_block.shape_index <= -1:
				current_block.shape_index = 3
			current_block.current_shape = \
				current_block.shapes[current_block.shape_index]
			done_action = True
			action_frame = frame_counter
	
	# Move block left and right
	elif key[pygame.K_LEFT] or key[pygame.K_a]:
		if (done_action == False) and (current_block.x > 176):
			current_block.x -= 16
			done_action = True
			action_frame = frame_counter
	
	elif key[pygame.K_RIGHT] or key[pygame.K_d]:
		if (done_action == False) and (current_block.x < 320):
			current_block.x += 16
			done_action = True
			action_frame = frame_counter
	
	render_screen()
	clock.tick(60)
	
	frame_counter += 1
	
	# Wait a few frames before block can be rotated again
	if abs(frame_counter - action_frame) >= 10:
		done_action = False
	
	# Make blocks fall
	if frame_counter == (10 / level):
		current_block.y +=16
		
	if frame_counter >= 60:
		frame_counter = 0
	
	# Make new block
	if current_block.y == 336:
		new_block()





