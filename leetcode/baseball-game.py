class Solution:
    def calPoints(self, ops: List[str]) -> int:
        L = []
        for i in ops:
            if i =="C":
                del L[-1]
            elif i=="D":
                x = L[-1]
                L.append(2*x)
            elif i=="+":
                x = L[-1]
                y = L[-2]
                L.append(x+y)
            else:
                L.append(int(i))
        a = sum(L)
        return a