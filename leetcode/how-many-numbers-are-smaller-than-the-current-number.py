class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l = []
        for i in nums:
            count = 0
            for j in nums:
                if i>j:
                    count+=1
            l.append(count)
        return l