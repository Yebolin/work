# -*- coding:utf-8 -*-
# bolin 2017-09-22
# 题目如下
'''
现有一个 m × n (m,n 都小于 100)的网格，位于左上角的 A 要去寻找右下角的 B，A 只能向下或者向右行走
现在问题来了，按照刚才的规则，A 到达 B 一共有多少种不重复的路径？
'''

def uniquePath(m, n):
    '''
    :type m: int
    :type n: int
    :rtype: int
    '''
    if m == 1 or n==1:
        return 1
    if m > 1 and n > 1:
        return uniquePath(m-1, n) + uniquePath(m, n-1)

assert uniquePath(1, 2) == 1
assert uniquePath(3, 3) == 6
assert uniquePath(10, 20) == 6906900

print(uniquePath(2,4))
print(uniquePath(4,2))
print(uniquePath(5,5))
