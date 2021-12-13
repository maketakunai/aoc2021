#!/usr/bin/env python3

from collections import defaultdict

def find_paths(graph,path):
    if path[-1] == 'end':
        #print(path)
        return 1
    counter = 0
    for node in graph[path[-1]]:
        if node.isupper() or node not in path:
            path.append(node)
            counter += find_paths(graph,path)
            path.pop()
    return counter

with open('./input/12_input.txt') as input_file:
    g = [ tuple(line.split('-')) for line in input_file.read().splitlines()]
    
    graph = defaultdict(list)
    
    for edge in g:
        a,b = edge[0], edge[1]
        graph[a].append(b)
        graph[b].append(a)
    
    #print(graph)     
    print(find_paths(graph, ['start']))
