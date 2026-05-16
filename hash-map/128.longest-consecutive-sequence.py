#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0

        # 注意：这里不要iterate on nums，会time out，因为可能有很多重复
        for n in nums_set:
            # current n 还不是这串序列的起点
            if n - 1 in nums_set:
                continue
            
            # 如果只有n自己一个，那么length=1
            length = 1
            while n + length in nums_set:
                length += 1
            
            res = max(length, res)

        return res

# @lc code=end

