# -*- coding:utf-8 -*-
# 题目: https://www.codewars.com/kata/556f4a5baa4ea7afa1000046/train/python
from itertools import combinations
from functools import reduce
from collections import Counter


# 个数大于2，排序组成头部，反序组成尾部，中间取剩下的max. 0的话或者为空，需要判断处理
# input:int num
def find_largest_palindrome(n):
    n = str(n)
    digits = sorted(Counter(n).items(), reverse=True)
    sides = ''.join( int(v/2)*k for k,v in digits)
    center = max( int(v%2) * k for k,v in digits)           # max str,only have 0-9
    return int((sides + center + sides[::-1]).strip('0'))   # 两边对等，可以用strip去除0


def numeric_palindrome(*args):
    # print(args)
    n = len(args)
    L = []
    for i in range(2, n + 1):
        L = L + list(combinations(args, i))
    res = [reduce(lambda x, y: x * y, i) for i in L]
    print(res)
    return max(find_largest_palindrome(i) for i in res)

print(numeric_palindrome(*(8, 25, 125)))
