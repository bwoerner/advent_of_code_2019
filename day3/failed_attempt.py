#this is how far I got when I realized I don't know enough to solve the problem 


puzzle_input = open('day3/input.txt', 'r')
wires = puzzle_input.read().split()
red_wire = wires[0].split(',')
blue_wire = wires[1].split(',')

wires = red_wire + blue_wire


for i in range(len(wires)):
  d = wires[i][0] #direction
  n = int(wires[i][1:]) #number of spaces

  if d == 'U':
    print (d, n)
  elif d == 'D':
    print (d, n)
  elif d == 'R':
    print (d, n)
  elif d == 'L':
    print (d, n)