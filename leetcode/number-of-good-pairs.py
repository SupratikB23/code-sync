class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        total = 0
        a = set(nums)
        for i in a:
            n = nums.count(i)
            total += n * (n - 1) // 2
        return total