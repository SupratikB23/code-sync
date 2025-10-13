class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        total = 0
        for i in nums:
            a = i+diff
            if a in nums:
                b = a+diff
                if b in nums:
                    total+=1
        return total