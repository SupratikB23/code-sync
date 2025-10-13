class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            for j in range(max(0, i - nums[i]),i+1):
                total += nums[j]
        return total