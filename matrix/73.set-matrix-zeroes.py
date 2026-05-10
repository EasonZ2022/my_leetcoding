#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
# 解法1: 0的数量=x，用了O(x)的space，还可以优化
# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         rows = []
#         cols = []
#         m = len(matrix)
#         n = len(matrix[0])
#         for r in range(m):
#             for c in range(n):
#                 if matrix[r][c] == 0:
#                     rows.append(r)
#                     cols.append(c)
#         for r in rows:
#             matrix[r] = [0] * n
#         for c in cols:
#             for i in range(m):
#                 matrix[i][c] = 0

# 解法2: O(1)的space，用第一行和第一列来记录这里是否有0
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row_has_zero = False
        first_col_has_zero = False

        m = len(matrix)
        n = len(matrix[0])

        # 1: only check first row/col
        for c in range(n):
            if matrix[0][c] == 0:
                first_row_has_zero = True
                break               # good point!!! as time improvement
        for r in range(m):
            if matrix[r][0] == 0:
                first_col_has_zero = True
                break
        
        # 2: scan all
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        # 3: set zeros
        for c in range(1, n):
            if matrix[0][c] == 0:
                # set this whole col to be 0
                for r in range(1, m):
                    matrix[r][c] = 0

        for r in range(1, m):
            if matrix[r][0] == 0:
                # set this whole row to be 0
                for c in range(1, n):
                    matrix[r][c] = 0
        
        # 4: set first row/col
        if first_col_has_zero:
            for r in range(m):
                matrix[r][0] = 0

        if first_row_has_zero:
            for c in range(n):
                matrix[0][c] = 0
# @lc code=end

