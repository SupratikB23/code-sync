import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 536870912:
            return True
        if n <= 0:
            return False
        a = math.log(n) / math.log(2)
        if a%1 == 0:
            return True
        else:
            return False