#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            temp_sum = numbers[l] + numbers[r]
            if temp_sum > target:
                r -= 1
            elif temp_sum < target:
                l += 1
            else:
                return [l+1, r+1] # +1 only because the answer needs 1-indexed
        return [l, r]
# @lc code=end

