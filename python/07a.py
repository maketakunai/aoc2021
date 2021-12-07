#!/usr/bin/env python3

with open('./input/07_input.txt') as input_file:
    h_pos = input_file.read().splitlines()

h_pos = list(map(int,h_pos[0].split(',')))
h_pos.sort()
mid = len(h_pos) // 2
median = h_pos[mid] + h_pos[~mid] // 2

smallest = float('inf')
for n in range(median):
    temp = sum([abs(x-n) for x in h_pos])
    
    if temp < smallest:
        smallest = temp

print(smallest)