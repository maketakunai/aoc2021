#!/usr/bin/env python3

with open('./input/08_input.txt') as input_file:
    signals = input_file.read().splitlines()

signals = [x.split(' | ') for x in signals]
counter = 0
for code in signals:
    digits = [y.split() for y in code]
    for num in digits[1]:
        if len(num) in [2,3,4,7]:
            counter +=1

print(counter)