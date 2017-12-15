# -*- coding:utf-8 -*-
# https://leetcode.com/problems/sudoku-solver/description/
'''
解决数独
'''

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows=[[], [], [], [], [], [], [], [], []]
        lines=[[], [], [], [], [], [], [], [], []]
        subs=[[], [], [], [], [], [], [], [], []]
        for i in range(9):
            for j in range(9):
                num=board[i][j]
                k=i//3*3+j//3  # 所在方格编号
                # print i,j,k,num,rows[i],lines[j],subs[k]
                if num != '.':
                    if num in rows[i]:
                        return False
                    else:
                        rows[i].append(num)
                    if num in lines[j]:
                        return False
                    else:
                        lines[j].append(num)
                    if num in subs[k]:
                        return False
                    else:
                        subs[k].append(num)
        return True

    def tryit(self, board):
        for x in range(9):
            for y in range(9):
                if board[x][y]=='.':
                    for value in range(1,10):
                        board[x][y]=str(value)
                        if self.isValidSudoku(board):   # 本层是否有效
                            if not self.tryit(board):          # 进入下一层




test=Solution()
board=[[".",".","9","7","4","8",".",".","."],
       ["7",".",".",".",".",".",".",".","."],
       [".","2",".","1",".","9",".",".","."],
       [".",".","7",".",".",".","2","4","."],
       [".","6","4",".","1",".","5","9","."],
       [".","9","8",".",".",".","3",".","."],
       [".",".",".","8",".","3",".","2","."],
       [".",".",".",".",".",".",".",".","6"],
       [".",".",".","2","7","5","9",".","."]
    ]

print(test.solveSudoku(board))