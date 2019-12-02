import math

puzzle_input = open('day1/input.txt', 'r')
mass_list = puzzle_input.read().splitlines()
mass_list = [int(i) for i in mass_list]
#three = 3
#two = 2
fuel = 0

#part 1 solution
#fuel = sum([math.floor(x / three) - two for x in mass_list])

#part 2 solution
for i in mass_list: 
    fuel_level = i 
    while fuel_level > 0:
        fuel_level = math.floor(fuel_level/3)-2
        if fuel_level > 0:
            fuel += fuel_level

print(fuel)