#!/usr/bin/env python3

with open('./input/10_input.txt') as input_file:
    chunks = input_file.read().splitlines()

left = ['[', '<', '(', '{']

to_discard = []
for line in chunks:
    stack = []
    for c in line:
        if c in left:
            stack.append(c)
        else:
            temp = stack.pop()
            if temp == '{' and c == '}':
                continue
            elif temp == '(' and c == ')':
                continue
            elif temp == '<' and c == '>':
                continue
            elif temp == '[' and c == ']':
                continue
            else:
                to_discard.append(line)


incomplete = [x for x in chunks if x not in to_discard]

answer = []
for line in incomplete:
    stack = []
    for c in line:
        if c in left:
            stack.append(c)
        else:
            temp = stack.pop()
            if temp == '{' and c == '}':
                continue
            elif temp == '(' and c == ')':
                continue
            elif temp == '<' and c == '>':
                continue
            elif temp == '[' and c == ']':
                continue
    r_total = 0
    for item in stack[::-1]:
        if item == '(':
            r_total *= 5
            r_total += 1
        elif item == '[':
            r_total *= 5
            r_total += 2
        elif item == '{':
            r_total *= 5
            r_total += 3
        elif item == '<':
            r_total *= 5
            r_total += 4
    answer.append(r_total)

answer.sort()

mid_idx = (len(answer) - 1 )//2
print(answer[mid_idx])
