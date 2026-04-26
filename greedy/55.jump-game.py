#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    # def canJump(self, nums: List[int]) -> bool:
    #     cover = nums[0]
        
    #     i = 0
    #     while i <= cover:
    #         cover = max(nums[i] + i, cover)
    #         if cover >= len(nums) - 1:
    #             return True
    #         i += 1
    #     return False


    # 解法2: 当成汽车加油问题
    def canJump(self, nums: List[int]) -> bool:
        gas = 0

        for i in range(len(nums)):
            if gas < 0:
                return False
            if nums[i] > gas:
                gas = nums[i]
            gas -= 1

        return True

# @lc code=end

