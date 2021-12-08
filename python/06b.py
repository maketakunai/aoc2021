#!/usr/bin/env python3

with open('./input/06_input.txt') as input_file:
    fish = input_file.read().splitlines()
fish = list(map(int,fish[0].split(',')))

#changed approach since trying to brute force part 2 would not be fun

fish_data = {x:0 for x in range(9)}
input = {i : fish.count(i) for i in fish}
fish_data.update(input)

for _ in range(256):
    age_zero = fish_data[0]
    for i in range(8):
        fish_data[i] = fish_data[i+1]
    fish_data[8] = age_zero
    fish_data[6] += age_zero

print(sum(fish_data.values()))