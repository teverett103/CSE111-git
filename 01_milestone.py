import math
from datetime import date
current_date = date.today()

width = int(input('Enter the width of the tire in mm (ex 205): '))
aspect = int(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))

volume = (math.pi* (width * width) * aspect * (width * aspect + 2540 * diameter))/10000000000

print(f"The approximate volume is {volume:.2f} liters")

answer = (str(input('Would you like to save this information (YES or NO): ').lower()))

#This will apend the information put in by the user if the so choose to. 
    if answer == 'yes':
        open volumes.txt