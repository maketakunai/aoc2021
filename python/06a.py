#!/usr/bin/env python3

with open('./input/06_input.txt') as input_file:
    fish = input_file.read().splitlines()

fish = list(map(int,fish[0].split(',')))
counter = 0
new_born = []

while counter != 80:
    fish.extend(new_born)
    fish = [x-1 for x in fish]
    fish = [6 if y==-1 else y for y in fish]
    new_born = fish.count(0) * [int(9)]
    counter += 1

print(len(fish))