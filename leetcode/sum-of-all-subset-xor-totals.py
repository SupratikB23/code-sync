class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        for i in range(2**len(nums)):
            x = 0
            for j in range(len(nums)):
                if i & 1<<j:
                    x ^= nums[j]
            total += x
        return total