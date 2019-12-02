import math

puzzle_input = open('c:/Users/woern/Documents/aoc_2019/day1/input.txt', 'r')
mass_list = puzzle_input.read().splitlines()
mass_list = [int(i) for i in mass_list]
three = 3
two = 2

fuel = sum([math.floor(x / three) - two for x in mass_list])

print(fuel)