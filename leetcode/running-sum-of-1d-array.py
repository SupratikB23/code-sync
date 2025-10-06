class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l = []
        total = 0
        for i in nums:
            total += i
            l.append(total)
        return l