# world_clock.py
# Tells the time in major cities around the world.
# Author: Jackie P, aka TheDataElemental


import time
import os


# Calculate time in other time zones
def update_hours():
	global world_hours
	
	local_hour = (int(time.strftime("%H", time.localtime())))
	seattle_hour = local_hour - local_offset - 8
	new_york_hour = local_hour - local_offset - 5
	london_hour = local_hour - local_offset - 0
	tokyo_hour = local_hour - local_offset + 9
	cairo_hour = local_hour - local_offset + 2

	world_hours = {
		'local_hour': local_hour,
		'seattle_hour': seattle_hour,
		'new_york_hour': new_york_hour,
		'london_hour': london_hour,
		'tokyo_hour': tokyo_hour,
		'cairo_hour': cairo_hour,
		}

	for hour in world_hours:
		if world_hours[hour] > 24:
			world_hours[hour] -= 24


# Get local time zone
local_offset = \
	int(input("Enter local timezone's offset from GMT (as a number): "))
	
update_hours()

# Main clock loop
while True:
	# Clear terminal (Windows only)
	os.system('cls')
	
	# Display times
	print("\nWorld Clock")
	print("\nLocal Time: " + str(world_hours['local_hour']) + \
		time.strftime(":%M:%S", time.localtime()))

	print("Seattle: " + str(world_hours['seattle_hour']) + \
		time.strftime(":%M:%S", time.localtime()))

	print("New York: " + str(world_hours['new_york_hour']) + \
		time.strftime(":%M:%S", time.localtime()))

	print("London: " + str(world_hours['london_hour']) + \
		time.strftime(":%M:%S", time.localtime()))
		
	print("Cairo: " + str(world_hours['cairo_hour']) + \
		time.strftime(":%M:%S", time.localtime()))
		
	print("Tokyo: " + str(world_hours['tokyo_hour']) + \
		time.strftime(":%M:%S", time.localtime()))
	
	# Check for hour update
	if int(time.strftime("%H")) != world_hours['local_hour']:
		update_hours()
	
	time.sleep(1)
