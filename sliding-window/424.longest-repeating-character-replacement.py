#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    # Since the problem mentions to find the "shortest/longest/min/max" 
    # substring given some constraint, 
    # we must think of the sliding window pattern.
    def characterReplacement(self, s: str, k: int) -> int:
        freq_dict = defaultdict(int)    # important!!!!!

        res = 0
        l = 0

        for r in range(len(s)):
            freq_dict[s[r]] += 1

            while r - l + 1 - max(freq_dict.values()) > k:
            # invalid -> need to shrink the window
                freq_dict[s[l]] -= 1
                l += 1
                
            # valid -> compare now
            res = max(res, r - l + 1)
        return res
        
# @lc code=end


"""
A generic template for dynamic sliding window finding max window length

def longest_window(nums, condition):
    i = 0
    max_length = 0
    result = None

    for j in range(len(nums)):
        # Expand the window
        # Add nums[j] to the current window logic

        # Shrink the window if the condition is violated
        while not condition():  
            # Shrink the window from the left
            # Remove nums[i] from the current window logic
            i += 1

        # Update the result if the current window is larger
        if j - i + 1 > max_length:
            max_length = j - i + 1
            # Add business logic to update result

    return result
"""