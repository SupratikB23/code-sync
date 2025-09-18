class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        b = len(nums)
        for i in range(b+1):
            if i not in nums:
                return i
                break