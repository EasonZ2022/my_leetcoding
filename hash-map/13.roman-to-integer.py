#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        val_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }     

        res = 0
        for i in range(len(s) - 1):
            if val_map[s[i]] < val_map[s[i + 1]]:
                res -= val_map[s[i]]
            else:
                res += val_map[s[i]]
        
        return res + val_map[s[-1]]
    
# @lc code=end

