#!/usr/bin/env python3

def check_adj(array,x,y,cur_val):
    adj = []
    if x > 0:
        adj.append(int(array[x-1][y]))
    if x + 1 < len(array):
        adj.append(int(array[x+1][y]))
    if y > 0:
        adj.append(int(array[x][y-1]))
    if y + 1 < len(array[0]):
        adj.append(int(array[x][y+1]))
    
    for x in adj:
        if int(cur_val) >= x:
            return 0
    
    return (int(cur_val)+1)


with open('./input/09_input.txt') as input_file:
    height_map = input_file.read().splitlines()

rows = len(height_map)
cols = len(height_map[0])
risk_sum = 0

for y in range(rows):
    for x in range(cols):
        risk_sum += check_adj(height_map, y,x,height_map[y][x])

print(risk_sum)


