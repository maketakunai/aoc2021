#!/usr/bin/env python3

def insert_char(input, rules):
    new_input = dict(input)
    for seq in input:
        if input[seq] > 0:
            first = seq[0]+rules[seq]
            second = rules[seq]+seq[1]
            num = input[seq]

            new_input[seq] -= num
            new_input[first] += num
            new_input[second] += num
    return new_input

with open('./input/14_input.txt') as input_file:
    input = input_file.read().splitlines()
    
    start_seq = input[0]

    directions = input[2:]
    rules = {}

    for d in directions:
        d = d.split(' -> ')
        if d[0] not in rules.keys():
            rules[d[0]] = d[1]

    seq_freq = {key:0 for key in rules}

    for i in range(len(start_seq)-1):
        to_find = start_seq[i:i+2]
        seq_freq[to_find] += 1

    counter = 0
    while counter < 40:
        seq_freq = insert_char(seq_freq, rules)
        counter += 1

    letter_freq = {}

    for k,v in seq_freq.items():
        if k[0] in letter_freq:
            letter_freq[k[0]] += v//2
        else:
            letter_freq[k[0]] = v//2
        if k[1] in letter_freq:
            letter_freq[k[1]] += v//2
        else:
            letter_freq[k[1]] = v//2
    
    print(letter_freq)
    
    min_let = min(letter_freq, key=letter_freq.get)
    max_let = max(letter_freq, key=letter_freq.get)

    print(letter_freq[max_let] - letter_freq[min_let])