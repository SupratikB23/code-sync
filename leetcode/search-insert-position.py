class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            if target > max(nums):
                return len(nums)
            elif target < min(nums):
                return 0
            else:
                for i in range(len(nums)):
                    if nums[i]<target and nums[i+1]>target:
                        return i+1
                        break