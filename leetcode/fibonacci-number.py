class Solution:
    def fib(self, n: int) -> int:
        fib = ((1 + (5**0.5)) / 2) ** n - ((1 - (5**0.5)) / 2) ** n
        return round(fib / (5**0.5))