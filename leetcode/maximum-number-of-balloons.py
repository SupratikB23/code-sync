class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = text.count('b')
        a = text.count('a')
        l = text.count('l')
        o = text.count('o')
        n = text.count('n')
        l = [b, a, floor(l/2), floor(o/2), n]
        if min(l) != 0:
            return min(l)
        else:
            return 0