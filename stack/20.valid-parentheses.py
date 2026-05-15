#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stk = []
        for ch in s:
            if ch in mapping:
                stk.append(mapping[ch])
            else: # not in left part
                if (not stk) or ch != stk[-1]: # empty or not match
                    return False
                else: # match
                    stk.pop()
                
        return not stk




# ( [ {} ] )
# @lc code=end

