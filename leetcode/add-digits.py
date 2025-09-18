class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            if len(str(num))!=1:
                L = [*str(num)]
                sum = 0
                for i in L:
                    sum+=int(i)
                num = sum
            else:
                return num
                break