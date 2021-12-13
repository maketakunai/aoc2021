#!/usr/bin/env python3

with open('./input/13_input.txt') as input_file:
    paper = [ line for line in input_file.read().splitlines()]
    
    chop = paper.index('')
    
    points =  [ list(map(int,line.split(','))) for line in paper[:chop] ]

    directions = [ line.replace('fold along ', '') for line in paper[chop+1:]]

    for d in directions:
        d = d.split('=')
        axis_v = int(d[1])
        if d[0] == 'x':
            points = set( (x,y) if x < axis_v else (axis_v+axis_v-x,y) for (x,y) in points )
        else:
            points = set( (x,y) if y < axis_v else (x,axis_v+axis_v-y) for (x,y) in points )

    
    max_x = max([int(p[0]) for p in points])
    max_y = max([int(p[1]) for p in points])
    
    origami = [['.' for _ in range(max_x+1)] for _ in range(max_y+1)]
    
    for coord in points:
        y = int(coord[1])
        x = int(coord[0])
        origami[y][x] = '#'

    for line in origami:
        print(''.join(line))