#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
# 从右到左，再从左到右，in place记录：对于这个位置[i]，右边的所有product，然后左边所有的product
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        # first pass:
        run_prod = 1
        for i in range(n - 1, -1, -1):
            res[i] = run_prod
            run_prod = run_prod * nums[i]
        
        run_prod = 1
        for i in range(n):
            res[i] = res[i] * run_prod
            run_prod *= nums[i]
        
        return res


# @lc code=end

