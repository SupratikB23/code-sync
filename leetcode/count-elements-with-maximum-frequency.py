class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        import statistics
        a = nums.count(statistics.mode(nums))
        l = [] 
        for i in list(set(nums)):
            if nums.count(i)==a:
                l.append(nums.count(i))
        return sum(l)