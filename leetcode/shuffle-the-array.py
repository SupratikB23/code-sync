class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a = nums[:n+1]
        b = nums[n:]
        L = []
        for i in range(n):
            L.append(a[i])
            L.append(b[i])
        return L