class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        mean = max(nums)
        n = len(nums)
        for i in range(n//2):
            a = (min(nums) + max(nums)) / 2
            if a < mean:
                mean = a
            nums.remove(max(nums))
            nums.remove(min(nums))
        return mean