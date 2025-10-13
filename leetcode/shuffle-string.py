class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        a = list(s)
        final = ''
        d = {}
        for i in range(len(a)):
            d[indices[i]] = a[i]
        new = dict(sorted(d.items()))
        for i in new:
            final+=new[i]
        return final