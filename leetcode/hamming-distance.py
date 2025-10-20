class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = bin(x^y)
        t = a.count("1")
        return t