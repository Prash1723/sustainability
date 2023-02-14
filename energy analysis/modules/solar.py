

# Energy produced per square feet

orientation = ['north', 'south', 'east', 'west']

def pv_daily(hours, watts):
	return hours * watts * 0.75

def tilt_angle(month, latitude):
	if month == 'summer':
		ang = latitude - 15
	else:
		ang = latitude + 15

	return ang

def tilt_angle2(month, latitude):
	if month == 'summer':
		ang = (latitude * 0.9) + 29
	elif month == 'winter':
		ang = (latitude * 0.9) - 29
	elif month == 'fall':
		ang = ((latitdue - 2.5) * 0.9) + 29
	else:
		ang = ((latitude - 2.5) * 0.9) - 29

	return ang