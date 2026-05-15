#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }
        for t in tokens:
            if t in ops:
                b = stk.pop()
                a = stk.pop()
                stk.append(ops[t](a, b))
            else:
                stk.append(int(t))
        return stk[-1]

# @lc code=end

