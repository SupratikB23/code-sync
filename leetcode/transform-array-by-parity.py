class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        L = []
        for i in nums:
            if i%2 == 0:
                L.append(0)
            else:
                L.append(1)
        L.sort()
        return L