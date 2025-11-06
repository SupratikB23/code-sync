class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        a = s.count('1')
        b = s.count('0')
        c = ('1'*(a-1))+('0'*b)+'1'
        return c