#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
#
# https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/description/
#
# algorithms
# Easy (74.72%)
# Total Accepted:    96.7K
# Total Submissions: 129.5K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# 给定一个 N 叉树，返回其节点值的 前序遍历 。
# 
# N 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。
# 
# 
# 
# 
# 
# 进阶：
# 
# 递归法很简单，你可以使用迭代法完成此题吗?
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：root = [1,null,3,2,4,null,5,6]
# 输出：[1,3,5,6,2,4]
# 
# 示例 2：
# 
# 
# 
# 
# 输入：root =
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# 输出：[1,2,3,6,7,11,14,4,8,12,5,9,13,10]
# 
# 
# 
# 
# 提示：
# 
# 
# N 叉树的高度小于或等于 1000
# 节点总数在范围 [0, 10^4] 内
# 
# 
# 
# 
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

#  class Solution:
#      def preorder(self, root: 'Node') -> List[int]:
#          if not root: return []
#          result = []
#
#          def dfs(root):
#              if not root: return
#              result.append(root.val)
#              for child in root.children:
#                  dfs(child)
#          dfs(root)
#          return result

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        st = [root]
        result = []

        while len(st) > 0:
            node = st.pop()
            if node:
                for child in node.children[::-1]:
                    if child: st.append(child)
                st.append(node)
                st.append(None)
            else:
                result.append(st.pop().val)
        return result
