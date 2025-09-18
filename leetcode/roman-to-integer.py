class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        rom = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        num = [1,5,10,50,100,500,1000]

        l = list(s)
        while l!=[]:
            if len(l) >1:
                if rom.index(l[0])<rom.index(l[1]):
                    total += num[rom.index(l[1])] - num[rom.index(l[0])]
                    del l[1]
                    del l[0]
                else:
                    total += num[rom.index(l[0])]
                    del l[0]
            else:
                total += num[rom.index(l[0])]
                del l[0]

        return total