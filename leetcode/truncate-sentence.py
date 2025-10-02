class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        l = s.split(' ')
        total = ''
        for i in range(k):
            total += l[i]+' '
        return total[:-1]