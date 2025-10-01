class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        a = sum(nums) % k
        return a