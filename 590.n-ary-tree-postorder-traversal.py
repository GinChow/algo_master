#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N-ary Tree Postorder Traversal
#
# https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/description/
#
# algorithms
# Easy (76.41%)
# Total Accepted:    68.4K
# Total Submissions: 89.5K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# 给定一个 N 叉树，返回其节点值的 后序遍历 。
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
# 输出：[5,6,3,2,4,1]
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：root =
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# 输出：[2,6,14,11,7,3,12,8,4,13,9,10,5,1]
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
#      def postorder(self, root: 'Node') -> List[int]:
#          if not root: return []
#
#          result = []
#
#          def dfs(root):
#              if not root: return
#              for child in root.children:
#                  dfs(child)
#              result.append(root.val)
#          dfs(root)
#
#          return result
        
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        st = [root]
        result = []

        while len(st) > 0:
            node = st.pop()
            if node:
                st.append(node)
                st.append(None)
                for child in node.children[::-1]:
                    if child: st.append(child)
            else:
                result.append(st.pop().val)
    
        return result
