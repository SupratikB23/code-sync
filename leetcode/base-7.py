class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        elif num>0:
            ans = ''
            while num!=0:
                a = num%7
                ans = ans+str(a)
                num = num//7
            return ans[::-1]
        else:
            ans = ''
            num = num*(-1)
            while num!=0:
                a = num%7
                ans = ans+str(a)
                num = num//7
            return '-'+ans[::-1]