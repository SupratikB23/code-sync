class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        import statistics
        return statistics.mode(nums)