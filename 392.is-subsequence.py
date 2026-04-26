#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        
        pt1 = 0
        pt2 = 0

        while pt2 < len(t):
            if t[pt2] == s[pt1]:
                pt1 += 1

            if pt1 == len(s):
                return True
            
            pt2 += 1
        
        return False

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         sp = tp = 0

#         while sp < len(s) and tp < len(t):
#             if s[sp] == t[tp]:
#                 sp += 1
#             tp += 1
        
#         return sp == len(s)    
# @lc code=end

