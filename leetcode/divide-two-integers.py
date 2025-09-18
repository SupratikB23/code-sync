class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        import math
        a = dividend / divisor
        if a >= 2**31:
            return math.trunc(2**31-1)
        else:
            return math.trunc(a)