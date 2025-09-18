class Solution:
    def firstUniqChar(self, s: str) -> int:
        ctr = 0
        if len(s)==1:
            return 0
        elif len(set(s)) == 1:
            return -1
        else:
            for i in s:
                if (s.find(i, (s.find(i)+1))) == -1:
                    a = [*s]
                    ctr+=1
                    return a.index(i)
                    break
            if ctr==0:
                return -1