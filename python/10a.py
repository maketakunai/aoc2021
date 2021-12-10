#!/usr/bin/env python3

with open('./input/10_input.txt') as input_file:
    chunks = input_file.read().splitlines()

left = ['[', '<', '(', '{']

answer = []
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
                answer.append(c)

total = 0
for symbol in answer:
    if symbol == ')':
        total += 3
    elif symbol == ']':
        total += 57
    elif symbol == '}':
        total += 1197
    elif symbol == '>':
        total += 25137

print(total)