class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        total = 0
        for i in range(len(nums)):
            bs = format(i, 'b')
            x = bs.count('1')
            if x == k:
                total += nums[i]
        return total