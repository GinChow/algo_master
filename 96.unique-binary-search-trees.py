#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#
# https://leetcode-cn.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (69.94%)
# Total Accepted:    187.8K
# Total Submissions: 268.4K
# Testcase Example:  '3'
#
# 给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 3
# 输出：5
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 
# 
#

#  def numTrees(n):
#      """
#      :type n: int
#      :rtype: int
#      """
#      if n == 0:
#          return 0
#      if n == 1:
#          return 1
#      dp = [0] * (n + 1)
#      dp[0] = 1
#      dp[1] = 1
#      for i in range(2, n + 1):
#          for j in range(1, i + 1):
#              dp[i] += dp[j - 1] * dp[i - j]
#      return dp[n]



class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]

        return dp[n]
