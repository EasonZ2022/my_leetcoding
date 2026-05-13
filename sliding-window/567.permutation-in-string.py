#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)

        if len1 > len2:
            return False

        s1_count = {}
        s2_count = {}

        for i in range(len1):
            s1_count[s1[i]] = 1 + s1_count.get(s1[i], 0)
            s2_count[s2[i]] = 1 + s2_count.get(s2[i], 0)
        # 这题必须不能用defaultdict，必须用这个get!!!!!!!!!!!!

        if s1_count == s2_count:
            return True
        
        l = 0
        for r in range(len1, len2):
            s2_count[s2[r]] = 1 + s2_count.get(s2[r], 0)
            
            # maintain left side 
            s2_count[s2[l]] -= 1
            if s2_count[s2[l]] == 0:
                del s2_count[s2[l]]
            l += 1
            
            if s1_count == s2_count:
                return True
        return False


# @lc code=end

