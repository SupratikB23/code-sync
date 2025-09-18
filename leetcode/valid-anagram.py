class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = list(set([*s]))
        y = list(set([*t]))
        x.sort()
        y.sort()
        if len(t) == len(s) and len(x) == len(y):
            for i in range(len(x)):
                if x[i] != y[i] or s.count(x[i]) != t.count(y[i]):
                    return False
            else:
                return True
        else:
            return False