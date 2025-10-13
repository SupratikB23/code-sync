class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)//2):
            a = min(nums)
            nums.remove(a)
            b = min(nums)
            nums.remove(b)
            arr.append(b)
            arr.append(a)
        return arr