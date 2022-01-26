#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
# https://leetcode-cn.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (61.43%)
# Total Accepted:    233.9K
# Total Submissions: 380.9K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的每个数字在每个组合中只能使用 一次 。
# 
# 注意：解集不能包含重复的组合。 
# 
# 
# 
# 示例 1:
# 
# 
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# 
# 示例 2:
# 
# 
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ]
# 
# 
# 
# 提示:
# 
# 
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
# 
# 
#
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)
        def backtrack(candidates, target, path, index):
            if target == sum(path):
                res.append(path)
                return
            if target < sum(path):
                return
            #  just use the visited list is not enough
            for i in range(index, len(candidates)):
                if i > index and  candidates[i] == candidates[i-1]:
                    continue
                else:
                    backtrack(candidates, target, path + [candidates[i]], i + 1)

        backtrack(candidates, target, [], 0)
        return res
