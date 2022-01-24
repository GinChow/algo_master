#
# @lc app=leetcode.cn id=361 lang=python3
#
# [361] 轰炸敌人
#
# https://leetcode-cn.com/problems/bomb-enemy/description/
#
# algorithms
# Medium (56.63%)
# Total Accepted:    3.8K
# Total Submissions: 6.8K
# Testcase Example:  '[["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]'
#
# 给你一个大小为 m x n 的矩阵 grid ，其中每个单元格都放置有一个字符：
# 
# 
# 'W' 表示一堵墙
# 'E' 表示一个敌人
# '0'（数字 0）表示一个空位
# 
# 
# 返回你使用 一颗炸弹 可以击杀的最大敌人数目。你只能把炸弹放在一个空位里。
# 
# 由于炸弹的威力不足以穿透墙体，炸弹只能击杀同一行和同一列没被墙体挡住的敌人。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
# 输出：3
# 
# 
# 示例 2：
# 
# 
# 输入：grid = [["W","W","W"],["0","0","0"],["E","E","E"]]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid[i][j] 可以是 'W'、'E' 或 '0'
# 
# 
#
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        dp_map = [[0] * len(grid[0]) for _ in range(len(grid))]

        #  横向
        for i in range(len(grid)):
            #  forward 
            enemies = 0
            for j in range(len(grid[0])):
                if grid[i][j] == 'W':
                    enemies = 0
                elif grid[i][j] == 'E':
                    enemies += 1
                elif grid[i][j] == '0':
                    dp_map[i][j] += enemies
            # backward
            enemies = 0
            for j in range(len(grid[0]) - 1, -1, -1):
                if grid[i][j] == 'W':
                    enemies = 0
                elif grid[i][j] == 'E':
                    enemies += 1
                elif grid[i][j] == '0':
                    dp_map[i][j] += enemies
                
        # 纵向
        for j in range(len(grid[0])):
            #  forward 
            enemies = 0
            for i in range(len(grid)):
                if grid[i][j] == 'W':
                    enemies = 0
                elif grid[i][j] == 'E':
                    enemies += 1
                elif grid[i][j] == '0':
                    dp_map[i][j] += enemies
            # backward
            enemies = 0
            for i in range(len(grid) - 1, -1, -1):
                if grid[i][j] == 'W':
                    enemies = 0
                elif grid[i][j] == 'E':
                    enemies += 1
                elif grid[i][j] == '0':
                    dp_map[i][j] += enemies

        return max(max(row) for row in dp_map)
