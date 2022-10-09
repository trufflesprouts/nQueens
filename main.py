from collections import defaultdict
import numpy as np

valid = []

def validateBoard(n, queens):
    for (i, j) in queens:
        for k in range(i+1, n):
            if (k, j) in queens:
                return False
        for k in range(j+1, n):
            if (i, k) in queens:
                return False
        for k in range(i+1, n):
            for m in range(j+1, n):
                if (k, m) in queens:
                    return False
    return True

def rec(n, queens, i):
    if n == 0: return
    rec(n, queens, i+1)
    rec(n-1, queens + [i], i+1)

# def nQueens(n):
    # for z in range(n*n):
    #     board = [[0]*n]*n
    #     queens = n
    #     for i in range(n):
    #         for i in range(n):

def main():
    print(validateBoard(2, [(0,0), (1,1)]))

if __name__ == '__main__':
    main()