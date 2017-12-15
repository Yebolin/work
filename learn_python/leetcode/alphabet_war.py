# -*- coding:utf-8 -*-
'''
http://www.codewars.com/kata/alphabet-wars-reinforces-massacre/train/python

'''
import re

def alphabet_war(reinforces, airstrikes):
    battlefield = list(map(list, zip(*reinforces)))  # 转置二维数组
    print(battlefield)
    for line in airstrikes:
        for k,v in enumerate(re.sub(r'(?<=\*) | (?=\*)', '*', line)):
            if v=='*':
                battlefield[k].pop(0)
    print(battlefield)
    return battlefield



reinforces=["g964xxxxxxxx",
            "myjinxin2015",
            "steffenvogel",
            "smile67xxxxx",
            "giacomosorbi",
            "freywarxxxxx",
            "bkaesxxxxxxx",
            "vadimbxxxxxx",
            "zozofouchtra",
            "colbydauphxx" ]
airstrikes=["* *** ** ***",
            " ** * * * **",
            " * *** * ***",
            " **  * * ** ",
            "* ** *   ***",
            "***   ",
            "**",
            "*",
            "*" ]

assert alphabet_war(reinforces, airstrikes)=='codewars'