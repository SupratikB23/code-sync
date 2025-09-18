class Solution:
    def customSortString(self, order: str, s: str) -> str:
        str1 = ''
        for i in order:
            for j in s:
                if i==j:
                    str1+=i
        str2 = ''
        for k in s:
            if k not in str1 and k not in str2:
                a = s.count(k)
                str2+=k*a
        str2 = ''.join(sorted(str2))
        return str1+str2