class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(len(nums1)-m):
            nums1[i+m] = nums2[i]
        nums1.sort()