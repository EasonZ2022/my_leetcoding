#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# 这题主要难在de-dup！算法很简单
# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 2):
            # tiny improvement:
            if nums[i] > 0:
                return res

            # de-dup: on same nums[i], 后一个i的case一定已经被前一个cover
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1

            while j < k:
                temp_sum = nums[i] + nums[j] + nums[k]
                if temp_sum < 0:
                    j += 1
                elif temp_sum > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    
                    # de-dup: 先尝试移动j，直到找到下一个不同的 nums[j]; k同理
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                    
                    k -= 1
                    while nums[k] == nums[k+1] and j < k:
                        k -= 1
        return res
# @lc code=end

