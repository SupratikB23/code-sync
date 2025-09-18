class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ctr = 0
        for i in nums:
            if i < k:
                ctr+=1
        return ctr