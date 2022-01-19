#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (77.29%)
# Total Accepted:    406.1K
# Total Submissions: 525.4K
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1
# 输出：["()"]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 8
# 
# 
#
class Solution:
    def dfs(self, l, r, s, res):
        if r < l or l < 0 or r < 0:
            return

        if l == 0 and r == 0:
            res.append(s)
            return
        
        self.dfs(l - 1, r, s + "(", res)
        self.dfs(l, r-1, s + ")", res)

    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        res = []
        self.dfs(n, n, "", res)
        return res
