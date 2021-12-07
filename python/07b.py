#!/usr/bin/env python3

with open('./input/07_input.txt') as input_file:
    h_pos = input_file.read().splitlines()
h_pos = list(map(int,h_pos[0].split(',')))

smallest = float('inf')
for n in range(len(h_pos)):
    temp = [abs(x-n) for x in h_pos]
    temp = sum([sum(range(y+1)) for y in temp])
    if temp < smallest:
        smallest = temp

print(smallest)