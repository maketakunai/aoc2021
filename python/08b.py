#!/usr/bin/env python3

with open('./input/08_input.txt') as input_file:
    signals = input_file.read().splitlines()

signals = [x.split(' | ') for x in signals]
total = 0

for code in signals:
    digits = [y.split() for y in code]
    temp_dict = {}

    one = [s for s in digits[0] if len(s) == 2][0]
    four = [s for s in digits[0] if len(s) == 4][0]
    seven = [s for s in digits[0] if len(s) == 3][0]
    eight = [s for s in digits[0] if len(s) == 7][0]
    
    length5 = [s for s in digits[0] if len(s) == 5]
    length6 = [s for s in digits[0] if len(s) == 6]

    four_minus_one = ''.join(c for c in four if c not in one)

    for i in length5:
        if set(one) <= set(i):
            three = i
        elif set(four_minus_one) <= set(i):
            five = i
        else:
            two = i

    three_and_four = list(set(three+four))
    three_and_four = ''.join(c for c in three_and_four)

    two_minus_one_plus_five = ''.join(c for c in two if c not in one) + five
    
    for j in length6:
        if set(three_and_four) == set(j):
            nine = j
        elif set(two_minus_one_plus_five) == set(j):
            six = j
        else:
            zero = j

    temp_dict[ ''.join(sorted(zero)) ] = 0
    temp_dict[ ''.join(sorted(one)) ] = 1
    temp_dict[ ''.join(sorted(two)) ] = 2
    temp_dict[ ''.join(sorted(three)) ] = 3
    temp_dict[ ''.join(sorted(four)) ] = 4
    temp_dict[ ''.join(sorted(five)) ] = 5
    temp_dict[ ''.join(sorted(six)) ] = 6
    temp_dict[ ''.join(sorted(seven)) ] = 7
    temp_dict[ ''.join(sorted(eight)) ] = 8
    temp_dict[ ''.join(sorted(nine)) ] = 9

    temp_string = ''
    for mystery in digits[1]:
        temp_string += str(temp_dict[  ''.join(sorted(mystery))  ])
    
    total += int(temp_string)
            
print(total)