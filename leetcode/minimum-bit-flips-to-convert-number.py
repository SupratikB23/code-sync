class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        a = bin(start^goal)
        t = a.count("1")
        return t