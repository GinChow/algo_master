#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#
# https://leetcode-cn.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (43.54%)
# Total Accepted:    207.3K
# Total Submissions: 475.8K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
# 
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
# 
# 
# 
# 示例 1:
# 
# 
# 
# 
# 输入：heights = [2,1,5,6,2,3]
# 输出：10
# 解释：最大的矩形为图中红色区域，面积为 10
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入： heights = [2,4]
# 输出： 4
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 
# 
#
#  class Solution:
#      def largestRectangleArea(self, heights: List[int]) -> int:
#          dp = [height for height in heights] # the largest rectangle height
#
#          #  O(n^2) Solution time limit exceeded
#          for i in range(len(heights)):
#              #  left
#              left = i - 1
#              while left >= 0 and heights[left] >= heights[i]:
#                  dp[i] += heights[i]
#                  left -= 1
#
#              # right
#              right = i + 1
#              while right < len(heights) and heights[right] >= heights[i]:
#                  dp[i] += heights[i]
#                  right += 1
#
#          return max(dp)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #  monotonic stack
        #  O(n)

        #  前后加0，方便处理
        heights.append(0)
        heights.insert(0, 0)

        st = [0]
        i = 1
        max_area = 0
        while i < len(heights):
            while len(st) > 0 and heights[i] < heights[st[-1]]:
                idx = st.pop()
                h = heights[idx]
                if len(st) == 0:
                    w = i
                else:
                    w = i - st[-1] - 1
                max_area = max(max_area, h * w)
            st.append(i)
            i += 1

        return max_area
