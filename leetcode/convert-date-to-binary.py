class Solution:
    def convertDateToBinary(self, date: str) -> str:
        L = date.split('-')
        L2 = []
        final = ''
        for i in L:
            a = bin(int(i))[2:]
            L2.append(str(a))
        b = '-'.join(L2)
        return b