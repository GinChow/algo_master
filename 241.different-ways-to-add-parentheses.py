#
# @lc app=leetcode.cn id=241 lang=python3
#
# [241] 为运算表达式设计优先级
#
# https://leetcode-cn.com/problems/different-ways-to-add-parentheses/description/
#
# algorithms
# Medium (73.57%)
# Total Accepted:    35.4K
# Total Submissions: 48.1K
# Testcase Example:  '"2-1-1"'
#
# 给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及
# * 。
# 
# 示例 1:
# 
# 输入: "2-1-1"
# 输出: [0, 2]
# 解释: 
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
# 
# 示例 2:
# 
# 输入: "2*3-4*5"
# 输出: [-34, -14, -10, -10, 10]
# 解释: 
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10
# 
#
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        #  backtracking
        def helper(s):
            if not s:
                return []
            res = []
            for i in range(len(s)):
                if s[i] in '+-*':
                    res1 = helper(s[:i])
                    res2 = helper(s[i+1:])
                    for j in res1:
                        for k in res2:
                            res.append(eval(str(j) + s[i] + str(k)))
            if not res:
                res.append(int(s))
            return res
        return helper(expression)
