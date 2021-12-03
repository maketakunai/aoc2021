#!/usr/bin/env python3

with open('./input/03_input.txt') as input_file:
    nums = [map(int,i) for i in input_file.read().splitlines()]

sum_nums = [sum(x) for x in zip(*nums)]
gamma = ''
epsilon = ''

for n in sum_nums:
    if n > (len(nums)//2):
        gamma += str(1)
        epsilon += str(0)
    else:
        gamma += str(0)
        epsilon += str(1)


print(int(gamma,2)*int(epsilon,2))