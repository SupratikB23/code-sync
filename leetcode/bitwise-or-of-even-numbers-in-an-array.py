class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        nums2 = [i for i in nums if i%2==0]
        ans = 0
        for i in nums2:
            ans |= i
        return ans