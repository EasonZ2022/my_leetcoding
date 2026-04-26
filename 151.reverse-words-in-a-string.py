#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        res = ""

        for i in range(len(words) - 1, -1, -1):
            res += words[i] + " "
        return res[:-1]

# 有解法2: two pointer
# in place swap the head word and the tail word
# no extra space needed
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        res = ""
        l = 0
        r = len(s) - 1

        while l < r:
            words[l], words[r] = words[r], words[l]
            l += 1
            r -= 1
        return "".join(words)
        

# @lc code=end

