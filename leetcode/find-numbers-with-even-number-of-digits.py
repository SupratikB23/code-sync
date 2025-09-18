class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        countr = 0
        for i in nums:
            if len(str(i))%2 == 0: countr+=1
        return countr