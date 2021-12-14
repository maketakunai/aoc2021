#!/usr/bin/env python3

def insert_char(input, rules):
    orig = [c for c in input]
    new = []
    new_polymer = []
    for i in range(len(input)-1):
        to_find = start_seq[i:i+2]
        new.append(rules[to_find])

    a = len(orig)
    b = len(new)
    for j in range(max(a, b)):
        if j < a:
            new_polymer.append(orig[j])
        if j < b:
            new_polymer.append(new[j])
    return ''.join(new_polymer)

with open('./input/14_input.txt') as input_file:
    input = input_file.read().splitlines()
    
    start_seq = input[0]

    directions = input[2:]
    rules = {}

    for d in directions:
        d = d.split(' -> ')
        if d[0] not in rules.keys():
            rules[d[0]] = d[1]

    counter = 0

    while counter < 10:
        start_seq = insert_char(start_seq, rules)
        counter += 1
    
    letter_freq = {}

    for c in start_seq:
        if c in letter_freq:
            letter_freq[c] += 1
        else:
            letter_freq[c] = 1
    
    print(letter_freq)
    min_let = min(letter_freq, key=letter_freq.get)
    max_let = max(letter_freq, key=letter_freq.get)

    print(letter_freq[max_let] - letter_freq[min_let])
