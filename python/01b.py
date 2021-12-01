#!/usr/bin/env python3

with open('./01_input.txt') as input_file:
    depths = [int(i) for i in input_file.read().splitlines()]

trio_depths = [depths[x]+depths[x+1]+depths[x+2] for x in range(len(depths)-2)]

counter = 0
for i in range(len(trio_depths)):
    try:
        if trio_depths[i] < trio_depths[i+1]:
            counter += 1
    except:
        print(counter)
