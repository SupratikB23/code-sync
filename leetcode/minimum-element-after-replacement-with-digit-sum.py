class Solution:
    def minElement(self, nums: List[int]) -> int:
        m = nums[0]
        for j in nums:
            sum = 0
            i = j
            while i != 0:
                last = i % 10
                sum += last
                i //= 10
            if sum<m:
                m = sum
        return m