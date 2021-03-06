#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (59.29%)
# Total Accepted:    381.3K
# Total Submissions: 643.2K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
# 
# 
# 示例 2：
# 
# 
# 输入：height = [4,2,0,3,2,5]
# 输出：9
# 
# 
# 
# 
# 提示：
# 
# 
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
# 
# 
#
class Solution:
    def trap(self, height: List[int]) -> int:
        #  monotonic stack Solution
        mono_stack = []
        res = 0

        for idx in range(len(height)):
            if not mono_stack or height[idx] <= height[mono_stack[-1]]:
                mono_stack.append(idx)
            else:
                while mono_stack and height[idx] > height[mono_stack[-1]]:
                    tail = mono_stack.pop()
                    if not mono_stack:
                        break
                    res += (min(height[idx], height[mono_stack[-1]]) - height[tail]) * (idx - mono_stack[-1] - 1)
                mono_stack.append(idx)
        return res
        
        
