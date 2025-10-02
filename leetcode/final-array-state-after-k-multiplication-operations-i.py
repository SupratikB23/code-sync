class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            a = min(nums)
            x = nums.index(a)
            nums[x] = nums[x]*multiplier
        return nums