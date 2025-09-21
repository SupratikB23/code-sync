class Solution:
    def isUgly(self, n: int) -> bool:
        if n ==0:
            return False
        l = [2,3,5]
        for i in l:
            while n%i==0:
               n= n//i
        if n!=1:
            return False
        else:
            return True