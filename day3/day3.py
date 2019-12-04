""" 
this code heavily relies on @johnchoiniere
https://github.com/johnchoiniere/advent_of_code_2019/blob/master/day_3/day3.py
I will comment at the places where I learned something completely new

"""

puzzle_input = open('day3/input.txt', 'r')
wires = puzzle_input.read().split()
red_wire = wires[0].split(',')
blue_wire = wires[1].split(',')

#wires = red_wire + blue_wire


def cross_finder(wire1, wire2):

    coords_w1 = []
    coords_w2 = []
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    for i in wire1:
        d = i[0] 
        n = int(i[1:]) 
        for j in range(n):
            if d == 'U':
                y1 += 1
                coords_w1.append([x1,y1]) 
            elif d == 'D':
                y1 -= 1
                coords_w1.append([x1,y1])
            elif d == 'R':
                x1 += 1
                coords_w1.append([x1,y1])
            elif d == 'L':
                x1 -= 1
                coords_w1.append([x1,y1])

    for i in wire2:
        d = i[0]
        n = int(i[1:])
        for i in range(n):
            if d == 'R':
                x2 += 1
                coords_w2.append([x2,y2])
            elif d == 'L':
                x2 -= 1
                coords_w2.append([x2,y2])
            elif d == 'U':
                y2 += 1
                coords_w2.append([x2,y2])
            elif d == 'D':
                y2 -= 1
                coords_w2.append([x2,y2])
    
    intersections = [i for i in coords_w1 if i in coords_w2] #comparing lists is new to me

    distances = [abs(c[0])+abs(c[1]) for c in intersections] 
    part_1 = min(distances)

    steps = [coords_w1.index(i) + coords_w2.index(i) + 2 for i in intersections]
    part_2 = min(steps)

    return part1, part2

answer1, answer2 = cross_finder(blue_wire, red_wire) #assining more than one variable at once is new


print (part1, part2)