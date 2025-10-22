class Solution:
    def sortSentence(self, s: str) -> str:
        ans = ''
        a = s.split(' ')
        l = [None] * len(a)
        for i in a:
            x = i[-1]
            l[int(x)-1] = i[:-1]
        return " ".join(l)