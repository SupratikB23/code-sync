class Solution:
    def mirrorDistance(self, n: int) -> int:
        x = int(str(n)[::-1])
        return abs(x-n)