#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
# class Solution:
#     def hIndex(self, citations: List[int]) -> int:
#         citations.sort(reverse=True)

#         res = 0
#         for i in range(len(citations)):
#             if min(i+1, citations[i]) > res:
#                 res = min(i+1, citations[i])
#             else:
#                 break
#         return res
    
# 解法2: 不用sort，需要更多空间，time: O(n), space: O(n)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        frequency = [0 for _ in range(n+1)]

        for v in citations:
            if v > n:
                frequency[n] += 1
            else:
                frequency[v] += 1

        total = 0
        for i in range(n, -1, -1):
            total += frequency[i]
            if total >= i:
                return i

# @lc code=end

