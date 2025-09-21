class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        a = num**0.5
        if a%1 == 0:
            return True
        else:
            return False