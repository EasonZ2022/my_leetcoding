#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p, s] for p, s in zip(position, speed)]
        stk = []

        # 从离target最近的车开始考虑
        for p, s in sorted(cars, reverse=True):
            time = (target - p) / s

        # 如果不能追上，那就创建一个单独的fleet
            if not stk or time > stk[-1]:
                stk.append(time)
        # 如果能追上前一辆车，那就do nothing，因为前一辆车的时间已经在stack中，用于代表一个fleet
        
        return len(stk)      

# @lc code=end

