#!/usr/bin/env python3

with open('./input/02_input.txt') as input_file:
    directions = [i.split() for i in input_file.read().splitlines()]
    
horizontal = 0
depth = 0
for steps in directions:
    if steps[0] == 'forward':
        horizontal += int(steps[1])
    elif steps[0] == 'down':
        depth += int(steps[1])
    elif steps[0] == 'up':
        depth -= int(steps[1])

print(horizontal*depth)