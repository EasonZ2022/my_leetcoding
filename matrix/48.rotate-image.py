#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
# 两种方法：1/先上下再轴对称；2/先轴对称再左右
# implementation-wise: 1 is easier
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # 1. vertical
        for i in range(n // 2):
            matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]
        
        # 2. transpose
        for r in range(n):
            for c in range(r, n): # 这里！！注意范围是对角线
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
# @lc code=end

