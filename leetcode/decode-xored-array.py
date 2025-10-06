class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        l = [first]
        a = first
        for i in range(len(encoded)):
            x = a^encoded[i]
            l.append(x)
            a = x
        return l