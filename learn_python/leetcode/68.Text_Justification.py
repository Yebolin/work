# -*- coding:utf-8 -*-
'''
按长度L，格式化字符
https://leetcode.com/problems/text-justification/description/
'''

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res=[]
        LEN=0
        for i in words:
            if len(i)<=maxWidth:
                LEN=len(i)