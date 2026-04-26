#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = []
        for i in range(numRows):
            rows.append("")
        
        direction = -1
        step = numRows - 1
        curr = 0

        for i in range(len(s)):
            if i % step == 0:
                direction *= -1               
            rows[curr] += s[i]
            curr += direction

        res = ""
        for row in rows:
            res += row
        return res
             

# @lc code=end

