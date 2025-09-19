class Solution:
    def getCommon(self, a: List[int], b: List[int]) -> int:
        return min({*a}&{*b} or [-1])