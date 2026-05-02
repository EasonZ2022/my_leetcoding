#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start

# 解法1: 用set记录
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         seen = set()
#         res = 0
#         l = 0

#         for r in range(len(s)):
#             if s[r] not in seen:
#                 seen.add(s[r])
#                 res = max(res, r - l + 1)
#             else:
#                 # s[r] has been seen -> move the l until it's removed
#                 while s[r] in seen:
#                     seen.discard(s[l])
#                     l += 1

#                 # DON't forget to add the s[r] back!!!
#                 seen.add(s[r])
            
#         return res
        
# 解法2:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        res = 0
        l = 0
        for r in range(len(s)):
            # if (s[r] not in seen) or (l > seen[s[r]]):
            #     seen[s[r]] = r
            #     res = max(res, r - l + 1)
            # else:
            #     # it has been seen and within range
            #     l = seen[s[r]] + 1
            #     seen[s[r]] = r

            # 我的第一版逻辑，可以被simplify为：
            if (s[r] in seen) and (l <= seen[s[r]]):
                l = seen[s[r]] + 1
            seen[s[r]] = r
            res = max(res, r - l + 1)
        return res

# @lc code=end

