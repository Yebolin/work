# -*- coding:utf8 -*-
'''
https://leetcode.com/problems/guess-number-higher-or-lower/description/
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!

'''

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        mins=1
        maxs=n
        while mins!=maxs:
            i=(mins+maxs)//2
            if guess(i)==0:
                return i
            elif guess(i)==-1:
                maxs=i-1
            elif guess(i)==1:
                mins=i+1
        return mins