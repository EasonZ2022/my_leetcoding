#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# 滑动窗口题take away：以right bound为indexing很关键!
# @lc code=start
# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
#         l = 0
#         r = 0
#         res = len(nums) + 1
#         curr_sum = 0

#         for r in range(len(nums)):
#             curr_sum += nums[r]

#             # shrinking the window
#             while curr_sum >= target:
#                 res = min(res, r - l + 1)
#                 curr_sum -= nums[l]
#                 l += 1

#         return 0 if res == len(nums) + 1 else res
    

# 我的解法2: works but annoying，没有搞清楚以什么为indexing
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        r = 0
        res = len(nums) + 1
        curr_sum = nums[0]
        
        while r < len(nums):
            
            if curr_sum < target:
                r += 1
                if r < len(nums):
                    curr_sum += nums[r]
            else: 
                # shrinking
                res = min(res, r - l + 1)
                curr_sum -= nums[l]
                l += 1
             

        return 0 if res == len(nums) + 1 else res    
# @lc code=end

