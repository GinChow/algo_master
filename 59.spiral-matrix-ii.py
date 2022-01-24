#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
# https://leetcode-cn.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (77.94%)
# Total Accepted:    153.2K
# Total Submissions: 196.7K
# Testcase Example:  '3'
#
# 给你一个正整数 n ，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1
# 输出：[[1]]
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
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        #  side length
        side_len = n - 1

        res_matrix = [[0 for _ in range(n)] for _ in range(n)]
        count = 1

        for k in range(n//2):
            #  reset
            i, j = k, k
            #  right
            while j < k + side_len:
                res_matrix[i][j] = count
                count += 1
                j += 1
            
            #  down
            while i < k + side_len:
                res_matrix[i][j] = count
                count += 1
                i += 1

            #  left
            while j > k:
                res_matrix[i][j] = count
                count += 1
                j -= 1

            #  up
            while i > k:
                res_matrix[i][j] = count
                count += 1
                i -= 1
            side_len -= 2

        if n % 2 == 1:
            res_matrix[n // 2][n // 2] = count
        return res_matrix

