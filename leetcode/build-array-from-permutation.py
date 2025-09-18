class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        L = []
        for i in nums:
            L.append(nums[nums[nums.index(i)]])
        return L