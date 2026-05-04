#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start

# takeway: 1/用dot标记已经访问过的entry 2/how to switch direction
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_max = len(matrix)
        col_max = len(matrix[0])

        r = 0
        c = 0
        dr = 0
        dc = 1
        # all directions: 0,1; 1,0; 0,-1; -1,0
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        dirs_index = 0

        res = []
        for _ in range(row_max * col_max):
            # check next one
            if r + dr < 0 or r + dr >= row_max or c + dc < 0 or c + dc >= col_max or matrix[r+dr][c+dc]==".":
                # 更聪明的办法：
                # dc, dr = -1*dr, dc
                dr, dc = dirs[(dirs_index + 1) % 4]
                dirs_index += 1
            # add the current one
            res.append(matrix[r][c])
            matrix[r][c] = "."
            r += dr
            c += dc

        return res

# @lc code=end

