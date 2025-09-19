class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        total = 0
        for i in nums:
            a = max(str(i))
            n = int(str(a)*len(str(i)))
            total+=n
        return total