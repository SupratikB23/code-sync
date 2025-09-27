class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        L2 = []
        for i in nums:
            if nums.count(i) == 2 and i not in L2:
                L2.append(i)
        return L2