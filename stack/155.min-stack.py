#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        # store a pair: [val, current min in current state]
        self.stk = []

    def push(self, val: int) -> None:
        if self.stk: # non-empty stack
            curr_min = self.getMin()
            curr_min = min(val, curr_min)
        else: # empty stack
            curr_min = val

        self.stk.append([val, curr_min])

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        # the last element
        return self.stk[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

