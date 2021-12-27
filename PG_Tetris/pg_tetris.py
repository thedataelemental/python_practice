# pg_tetris.py
# Tetris clone, built with Python and PyGame
# Author: Jackie P, aka TheDataElemental

# Work in progress as of 12/27/21


import pygame


# Falling "tetris block" / "tetris piece". Tiles arranged in a shape
class Block:
	def __init__(self, tile, shape):
		self.tile = tile  # Image repeated for each tile of the block
		self.shape = shape  # Shape of block (2D array of 0's and 1's)


# Start game window
pygame.init()
screen = pygame.display.set_mode((512, 480), \
	pygame.HWSURFACE | pygame.DOUBLEBUF, vsync = 1)
pygame.display.set_caption("PG TETRIS")

# Define block shapes
# Shapes are represented internally as 4x4 arrays of 0's and 1's.
# 1 = tile, 0 = no tile.
# This shape array is used for both collision and rendering.
O_shape_1 = [
	[0, 0, 0, 0],
	[0, 1, 1, 0],
	[0, 1, 1, 0],
	[0, 0, 0, 0],
	]

I_shape_1 = [
	[0, 1, 0, 0],
	[0, 1, 0, 0],
	[0, 1, 0, 0],
	[0, 1, 0, 0],
	]

T_shape_1 = [
	[0, 0, 0, 0],
	[0, 1, 0, 0],
	[1, 1, 1, 0],
	[0, 0, 0, 0],
	]

J_shape_1 = [
	[0, 1, 0, 0],
	[0, 1, 0, 0],
	[0, 1, 0, 0],
	[1, 1, 0, 0],
	]
	
	
# L_shape_1 = [

# S_shape_1 = [

# Z_shape_1 = [


# Load tile images
red_tile = pygame.image.load("Assets/Exports/red_tile.png")
blue_tile = pygame.image.load("Assets/Exports/blue_tile.png")
yellow_tile = pygame.image.load("Assets/Exports/yellow_tile.png")
gray_tile = pygame.image.load("Assets/Exports/gray_tile.png")
purple_tile = pygame.image.load("Assets/Exports/purple_tile.png")
green_tile = pygame.image.load("Assets/Exports/green_tile.png")
# orange_tile = pygame.image.load("Assets/Exports/orange_tile.png")

# Make tetris blocks
square_block = Block(red_tile, O_shape_1)
line_block = Block(blue_tile, I_shape_1)


# TODO: write code to use arrays for collision and rendering
# TODO: main game loop, controls, score, random pieces
# TODO: make other three variations for each block shape
# TODO: lose state, win state, line clearing, score
