# -*- coding:utf-8 -*-
'''
http://www.codewars.com/kata/sudoku-solver/train/python
'''
def sudoku(puzzle):
    for x in range(9):
        for y in range(9):
            if puzzle[x][y]=0:
                for i in range(1,10):
                    if check(x,y,puzzle):
                        puzzle[x][y]=i
                        if sudoku(puzzle):
                            pass
                        else:
                            puzzle[x][y]=0
                            return False

def check(x,y,puzzle):
    p = puzzle[x][y]
    if p in puzzle[x]:  # row
        return False
    if p in [i[y] for i in puzzle]:  # line
        return False
    x0,y0 = x//3*3,y//3*3
    if p in puzzle[x0][y0:y0+3]+puzzle[x0+1][y0:y0+3]+puzzle[x0+2][y0:y0+3]: # block
        return False
    return True