class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        l1 = []
        l2 = []
        for i in nums:
            if i not in l1 and len(l1)<len(nums)/2:
                if nums.count(i)<=2:
                    l1.append(i)
                else:
                    return False
                    break
            else:
                l2.append(i)
        if len(l1) == len(l2):
            return True
        else:
            return False