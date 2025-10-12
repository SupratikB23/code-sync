class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        a = sum(nums)
        total = 0
        for i in nums:
            while i > 0:
                digit = i % 10 
                total += digit  
                i //= 10
        return abs(total-a)