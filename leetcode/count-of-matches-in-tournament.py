class Solution:
    def numberOfMatches(self, n: int) -> int:
        total = 0
        while n>0:
            if n%2 != 0:
                a = n//2 + 1
                total += a-1
            else:
                a = n//2
                total += a
            n = a
            if n==1:
                break
        return total