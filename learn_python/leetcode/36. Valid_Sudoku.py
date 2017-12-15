#！/bin/python
'''
https://leetcode.com/problems/valid-sudoku/description/
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
验证一个数独是否是一个有效的数独，只验证有效性，不验证是否可以解决
思路：
	一个原始对应3个list(所在行i，所在列j，所在子方格k),分别放入对应的list中，检查是否存在，存在返回false
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
                k=i/3*3+j/3  # 所在方格编号
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