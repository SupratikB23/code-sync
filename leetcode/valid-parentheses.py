class Solution:
    def isValid(self, s: str) -> bool:
        tick=0
        L1=['(','{','[',]
        L2=[')','}',']']
        stack = []
        if s[0] in L2:
            return False
        if len(s)==1:
            return False
        else:
            for i in s:
                if i in L1:
                    stack.append(i)
                else:
                    if stack!=[]:
                        a = stack[-1]
                        if L1.index(a)==L2.index(i):
                            del stack[-1]
                        else:
                            tick+=1
                            break
                    else:
                        tick+=1
                        break
            if tick!=0 or stack!=[]:
                return False
            else:
                return True