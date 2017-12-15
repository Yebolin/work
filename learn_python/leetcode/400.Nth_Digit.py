# -*- coding:utf-8 -*-
'''
# https://leetcode.com/problems/nth-digit/description/
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...
sequence='123456789101112.....'  n < 2^31
3->3   11->0
解题：
1.确定宽度，1-9是9，10-99，最大是180，100-999最大是900*。根据差值确定位数
2.根据位数，确定当前的数字
3.根据取模结果，确定当前数字的第几位  mod  1:第一  2：第二  。。。 0:最后一位
'''

class Solution(object):
    def findNthDigit(self, n):
        n -= 1
        for digits in range(1, 11):
            first = 10 ** (digits - 1)
            if n < 9 * first * digits:
                return int(str(first + n / digits)[n % digits])
            n -= 9 * first * digits
