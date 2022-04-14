# Harvest 3x3
# A simple text based farming game written in Python
# By Jackie P, aka TheDataElemental
# April 2022


import random
import time
import os


# Show farm
def show_farm():
	os.system('cls')
	print('')
	print('H A R V E S T  3 x 3')
	print('\n')
	print("DAY:", day)
	print("GOLD:", gold)
	print('')
	print('---------')
	print('|', stages[tiles[0]], stages[tiles[1]], stages[tiles[2]],'|')
	print('|',stages[tiles[3]], stages[tiles[4]], stages[tiles[5]],'|')
	print('|',stages[tiles[6]], stages[tiles[7]], stages[tiles[8]],'|')
	print('---------\n')
	
gold = 0
day = 1
	
# Make terminal text green
os.system('color 02') 

# Define 'art' for the 3 stages of plant growth
level_1 = '.' # Seed
level_2 = 'v' # Sprout
level_3 = '@' # Flower

stages = [level_1, level_2, level_3]

# Initialize the 9 tiles of plants to level 1 (seeds)
tiles = [0, 0, 0, 0, 0, 0, 0, 0, 0]

show_farm()

# Main game loop
while True:
	# Prompt user w harvest choice
	harvest_choice = input("Harvest? y/n: ")
	if harvest_choice == 'y':
		for x in range(0, 9):
			if tiles[x] == 2:
				gold += 50
			tiles[x] = 0
	
	# Update display after harvest
	show_farm()
	time.sleep(3)
	day += 1

	# Make plants grow
	for i in range(0, 9):
		growth_chance = random.randint(0, 1)
		if growth_chance == 1:
			if tiles[i] < (len(stages) - 1):
				tiles[i] += 1
	
	# Update display after growth
	show_farm()
