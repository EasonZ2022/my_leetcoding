#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            curr_area = min(height[l], height[r]) * (r - l)
            res = max(res, curr_area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res

# @lc code=end

