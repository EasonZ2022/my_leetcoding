#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
# 解法1：用python的一些神奇语法
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # 一定要用defaultdict，自动初始化为[]
        s_map = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            s_map[sorted_s].append(s)

        # 注意！！这里一定要转化为 list
        return list(s_map.values())

# 解法2: 可以记一下python里的ord函数：转化为ascii code
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
#         ans = defaultdict(list)

#         for s in strs:
#             count = [0] * 26

#             for c in s:
#                 count[ord(c) - ord("a")] += 1
#             ans[tuple(count)].append(s)
        
#         return list(ans.values())

# @lc code=end

