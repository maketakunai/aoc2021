#!/usr/bin/env python3

with open('./input/01_input.txt') as input_file:
    depths = [int(i) for i in input_file.read().splitlines()]
    
counter = 0
for i in range(len(depths)):
    try:
        if depths[i] < depths[i+1]:
            counter += 1
    except:
        print(counter)
