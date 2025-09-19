class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        n = 0
        for i in str(x):
            n+=int(i)
        if x%n == 0:
            return n
        else:
            return -1