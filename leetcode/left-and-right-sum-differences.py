class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l1 = [0]
        l2 = [0]
        total1 = 0
        total2 = 0
        for i in range(len(nums)-1):
            total1 += nums[i]
            l1.append(total1)
        for j in range(1,len(nums)):
            total2 += nums[-j]
            l2.append(total2)
        l2.reverse()
        l3 = []
        for k in range(len(nums)):
            a = l1[k]-l2[k]
            l3.append(abs(a))
        return l3