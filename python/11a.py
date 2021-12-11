#!/usr/bin/env python3

def valid(array,coord):
    x = coord[1]
    y = coord[0]
    if x < 0 or x >= len(array[0]):
        return False
    if y < 0 or y >= len(array):
        return False
    return True

def check_adj(x,y):
    yield x-1, y-1
    yield x, y-1
    yield x+1, y-1
    yield x-1, y
    yield x+1, y
    yield x-1, y+1
    yield x, y+1
    yield x+1, y+1

def flash(rows, cols, grid):
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] > 9:
                grid[y][x] = 0
                cur = (y,x)
                for coord in check_adj(*cur):
                    if valid(grid,coord) and grid[coord[0]][coord[1]] != 0:
                        grid[coord[0]][coord[1]] += 1

def check_lists(rows, cols, grid):
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] > 9:
                return True
    return False


with open('./input/11_input.txt') as input_file:
    grid = input_file.read().splitlines()
    grid = [list(map(int,x)) for x in grid]
    
    rows = len(grid)
    cols = len(grid[0])
    steps = 100
    counter = 0

    for _ in range(steps):

        grid = [[num+1 for num in line] for line in grid]


        while check_lists(rows,cols,grid):
            flash(rows,cols,grid)

        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == 0:
                    counter += 1

    print(counter)  
                
