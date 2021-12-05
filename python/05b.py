#!/usr/bin/env python3

with open('./input/05_input.txt') as input_file:
    data = input_file.read().splitlines()

# part 2: use y=mx+c to find all points in diagonals

point_dict = {}

data = [i.split(' -> ') for i in data]
for line in data:
    line = [j.split(',') for j in line]
    x1 = int(line[0][0])
    y1 = int(line[0][1])
    x2 = int(line[1][0])
    y2 = int(line[1][1])

    if x1 == x2: #vertical line
        min_val = min(y1, y2)
        max_val = max(y1, y2)+1
        for y in range(min_val, max_val):
            if (x1,y) in point_dict:
                point_dict[(x1,y)] += 1
            else:
                point_dict[(x1,y)] = 1
    elif y1 == y2: #horizontal line
        min_val = min(x1, x2)
        max_val = max(x1, x2)+1
        for x in range(min_val, max_val):
            if (x,y1) in point_dict:
                point_dict[(x,y1)] += 1
            else:
                point_dict[(x,y1)] = 1
    else: #diagonal line
        slope = (y1-y2)//(x1-x2)
        c = y1-x1 * slope
        min_val = min(x1, x2)
        max_val = max(x1, x2)+1
        for x in range(min_val, max_val):
            y = slope*x+c
            if (x,y) in point_dict:
                point_dict[(x,y)] += 1
            else:
                point_dict[(x,y)] = 1


counter = 0
for k,v in point_dict.items():
    if v >= 2:
        counter += 1

print(counter)