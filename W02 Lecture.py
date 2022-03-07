import math

def compute_circle_area(radius):
    return radius ** 2 * math.pi

def prompt_user_for_raidus():
    user_radius = float(input("Please enter a raidus: "))
    return user_radius

def display_area(area):
    print(area)

area = round(compute_circle_area(prompt_user_for_raidus()),2)

display_area(area)

