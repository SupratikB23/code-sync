class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l = []
        for i in range(0,len(nums),2):
            x = [nums[i+1]]
            x = x*nums[i]
            l.extend(x)
        return l