#!/usr/bin/python3
""" N queens """

import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

n_value = int(sys.argv[1])

if n_value < 4:
    print("N must be at least 4")
    exit(1)

def find_queen_positions(n, i=0, col_safe=[], diag1_safe=[], diag2_safe=[]):
    """ Find possible positions for queens """
    if i < n:
        for j in range(n):
            if j not in col_safe and i + j not in diag1_safe and i - j not in diag2_safe:
                yield from find_queen_positions(n, i + 1, col_safe + [j], diag1_safe + [i + j], diag2_safe + [i - j])
    else:
        yield col_safe

def solve_nqueens(n):
    """ Solve the N-Queens problem and print solutions """
    solution_list = []
    solution_count = 0
    for solution in find_queen_positions(n, 0):
        for col in solution:
            solution_list.append([solution_count, col])
            solution_count += 1
        print(solution_list)
        solution_list = []
        solution_count = 0

solve_nqueens(n_value)

