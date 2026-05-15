#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
# 解法1: 从尾部开始，更好理解！！！
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         res = [0] * len(temperatures)
        
#         # store pair [val, indexs]
#         stk = []


#         for i in range(len(temperatures)-1, -1, -1):
#             # Remove all useless candiddates
#             while stk and stk[-1][0] <= temperatures[i]:
#                 stk.pop()
            
#             # Now left with one good candidate
#             if stk:
#                 res[i] = stk[-1][1] - i
            
#             stk.append([temperatures[i], i])
        
#         return res

# 解法2: 从头开始
# 其实不需要存（val，index）pair，只要存index就可以
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stk = []

        for i in range(len(temperatures)):
            while stk and temperatures[i] > temperatures[stk[-1]]:
                res[stk[-1]] = i - stk[-1]
                stk.pop()
            stk.append(i)
        
        return res
# @lc code=end

