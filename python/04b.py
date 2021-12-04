#!/usr/bin/env python3

with open('./input/04_input.txt') as input_file:
    data = input_file.read().splitlines()

def check_bingo(board):
    for row in board:
        if sum(row) == -5:
            return True

    col_sum = [sum(x) for x in zip(*board)]
    if -5 in col_sum:
        return True

    #diag_sum1 = sum(board[i][i] for i in range(5))
    #diag_sum2 = sum(board[i][5-i-1] for i in range(5))
    #if diag_sum1 == -5 or diag_sum2 == -5:
    #    return True
    
    return False

def get_board_sums(board):
    total = 0
    for line in board:
        line_sum = sum(i for i in line if i > 0)
        total += line_sum
    return total


bingo_sequence = data.pop(0)
bingo_sequence = [int(x) for x in bingo_sequence.split(',')]
data = [string for string in data if string != '']
bingo_boards = [data[n:n+5] for n in range(0, len(data), 5)]
bingo_boards = [[[int(i) for i in line.split()] for line in board ] for board in bingo_boards ]

done = False
for number in bingo_sequence:
    bingo_boards = [[[-1 if i == int(number) else i for i in line] for line in board ] for board in bingo_boards ]
    for board in bingo_boards:
        bingo = check_bingo(board)
        if bingo and len(bingo_boards) != 1:
            bingo_boards.remove(board)
        elif bingo and len(bingo_boards) == 1:
            print(number*get_board_sums(board))
            done = True
            break
    if done:
        break
        