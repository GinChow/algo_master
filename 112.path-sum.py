#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#
# https://leetcode-cn.com/problems/path-sum/description/
#
# algorithms
# Easy (52.82%)
# Total Accepted:    314.1K
# Total Submissions: 594.6K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点
# 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。
# 
# 叶子节点 是指没有子节点的节点。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# 输出：true
# 解释：等于目标和的根节点到叶节点路径如上图所示。
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1,2,3], targetSum = 5
# 输出：false
# 解释：树中存在两条根节点到叶子节点的路径：
# (1 --> 2): 和为 3
# (1 --> 3): 和为 4
# 不存在 sum = 5 的根节点到叶子节点的路径。
# 
# 示例 3：
# 
# 
# 输入：root = [], targetSum = 0
# 输出：false
# 解释：由于树是空的，所以不存在根节点到叶子节点的路径。
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点的数目在范围 [0, 5000] 内
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#  recursive
#  class Solution:
#      def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#          if not root:
#              return False
#          res_sum = []
#          def traverse(node, sum_val):
#              if not node:
#                  return
#              sum_val += node.val
#              if not node.left and not node.right:
#                  res_sum.append(sum_val)
#              traverse(node.left, sum_val)
#              traverse(node.right, sum_val)
#          traverse(root, 0)
#          return targetSum in res_sum

#  iterative
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        st = [root]
        res = 0

        #  post-order traversal
        while len(st) > 0:
            node = st.pop()
            if node:
                res += node.val
                if not node.left and not node.right:
                    if res == targetSum:
                        return True
                st.append(node)
                st.append(None)
                if node.right:
                    st.append(node.right)
                if node.left:
                    st.append(node.left)
            else:
                res -= st.pop().val

        return False
