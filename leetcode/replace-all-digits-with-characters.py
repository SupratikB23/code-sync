class Solution:
    def replaceDigits(self, s: str) -> str:
        a = ''
        for i in s:
            if i.isalpha():
                a+=i
            elif i.isnumeric():
                x = a[-1]
                y = chr(ord(x)+int(i))
                a+=y
        return a