class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        l =[]
        for i in words:
            a = b = c = 0
            for j in i:
                if j.lower() in "qwertyuiop":
                    a += 1
                elif j.lower() in "asdfghjkl":
                    b += 1
                elif j.lower() in "zxcvbnm":
                    c += 1
            x = len(i)
            if a == x or b == x or c == x:
                l.append(i)
        return l