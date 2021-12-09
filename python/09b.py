#!/usr/bin/env python3
from collections import deque

def get_lows(array,x,y,cur_val):
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

def valid(array,coord):
    x = coord[1]
    y = coord[0]

    if x < 0 or x >= len(array[0]):
        return False
    if y < 0 or y >= len(array):
        return False
    return True

def check_adj(x,y):
    yield x+1, y
    yield x, y+1
    yield x-1, y
    yield x, y-1

def bfs (array, node):
    q = deque()
    visited = set()
    q.append(node)
    visited.add(node)

    while len(q) > 0:
        cur = q.popleft()

        for coord in check_adj(*cur):
            if coord not in visited and valid(array,coord):
                if array[coord[0]][coord[1]] < 9:
                    visited.add(coord)
                    q.append(coord)
    return visited


with open('./input/09_input.txt') as input_file:
    height_map = input_file.read().splitlines()

h_map = [ [int(char) for char in x] for x in height_map ] 
rows = len(height_map)
cols = len(height_map[0])
risk_sum = 0
lows = []
for y in range(rows):
    for x in range(cols):
        if get_lows(height_map, y,x,height_map[y][x]):
            lows.append((y,x))

answers = []
for coord in lows:
    answers.append(len(bfs(h_map,coord)))

answers = sorted(answers)[-3:]
print(answers[0]*answers[1]*answers[2])




