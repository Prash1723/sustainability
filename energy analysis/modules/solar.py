

# Energy produced per square feet

orientation = ['north', 'south', 'east', 'west']

class solar:
    def __init__(self, hours, watts, builtup_area, numbers):
        self.hours = hours
        self.watts = watts
        self.builtup_area = builtup_area
        self.numbers = numbers

    def pv_daily(hours, watts):
    	return hours * watts/1000 * 0.75

    def tilt_angle(month, latitude):
        if month == 'summer':
            ang = latitude-15
        else:
            ang = latitude+15

        return ang

    def tilt_angle2(month, latitude):
        if month == 'summer':
            ang = (latitude * 0.9) + 29
        elif month == 'winter':
            ang = (latitude * 0.9) - 29
        elif month == 'fall':
            ang = ((latitude - 2.5) * 0.9) + 29
        else:
            ang = ((latitude - 2.5) * 0.9) - 29

        return ang
