#!/usr/bin/env python3

with open('./input/03_input.txt') as input_file:
    nums = [list(map(int,i)) for i in input_file.read().splitlines()]

nums_copy = nums[:]
max_times = len(nums[0])

for i in range(max_times):
    sum_nums = [sum(x) for x in zip(*nums)]
    if sum_nums[i] > (len(nums)/2) or sum_nums[i] == (len(nums)/2):
        nums[:] = [j for j in nums if j[i] == 1]
    else:
        nums[:] = [j for j in nums if j[i] == 0]
    if len(nums) == 1:
        break

for i in range(max_times):
    sum_nums = [sum(x) for x in zip(*nums_copy)]
    if sum_nums[i] > (len(nums_copy)/2) or sum_nums[i] == (len(nums_copy)/2):
        nums_copy[:] = [j for j in nums_copy if j[i] == 0]
    else:
        nums_copy[:] = [j for j in nums_copy if j[i] == 1]
    if len(nums_copy) == 1:
        break

co2 = ''.join(map(str,nums_copy[0]))
print(co2)

oxygen = ''.join(map(str,nums[0]))
print(oxygen)

print(int(co2,2)*int(oxygen,2))