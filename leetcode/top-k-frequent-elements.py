class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import statistics as st
        x = st.mode(nums)
        L = [x]
        for i in range(k-1):
            nums = [i for i in nums if i!=x]
            x = st.mode(nums)
            L.append(x)
        return L