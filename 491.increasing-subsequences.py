#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] 递增子序列
#
# https://leetcode-cn.com/problems/increasing-subsequences/description/
#
# algorithms
# Medium (53.94%)
# Total Accepted:    56.6K
# Total Submissions: 105K
# Testcase Example:  '[4,6,7,7]'
#
# 给你一个整数数组 nums ，找出并返回所有该数组中不同的递增子序列，递增子序列中 至少有两个元素 。你可以按 任意顺序 返回答案。
# 
# 数组中可能含有重复元素，如出现两个整数相等，也可以视作递增序列的一种特殊情况。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [4,6,7,7]
# 输出：[[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [4,4,3,2,1]
# 输出：[[4,4]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 15
# -100 <= nums[i] <= 100
# 
# 
#
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        #  dp solution
        dp_res = []
        start_idx = {}

        #  remove duplicate

        for i in range(len(nums)):
            if nums[i] not in start_idx:
                start = 0
                dp_res.append([nums[i]])
                start_idx[nums[i]] = len(dp_res) - 1
                end = len(dp_res) - 1
            else:
                start = start_idx[nums[i]]
                end = len(dp_res)
            for j in range(start, end):
                if nums[i] >= dp_res[j][-1] and (dp_res[j] + [nums[i]] not in dp_res):
                    dp_res.append(dp_res[j] + [nums[i]])
        #  print(dp_res)

        return [ele for ele in dp_res if len(ele) > 1]
