# -*- coding:utf-8 -*-
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        L=[root]
        vals=[] # 本层数据
        res=[]  # 最后返回的结果
        while L:
            Ltemp=[]
            for i in L:
                vals.append(i.val)
                if i.left:
                    Ltemp.append(i.left)
                if i.right:
                    Ltemp.append(i.right)
            L=Ltemp #临时列表转入
            res.append(vals) # 保存本层数据
            vals=[] # 保存后，清空本层
        return res[::-1]