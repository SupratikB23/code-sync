class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        L = [x**2 for x in nums]
        L.sort()
        return L