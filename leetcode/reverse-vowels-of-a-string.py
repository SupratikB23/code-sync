class Solution:
    def reverseVowels(self, s: str) -> str:
        l = []
        for i in s:
            if i in 'AIEOUaeiou':
                l.append(i)
        l.reverse()
        final = ''
        for j in s:
            if j in 'AIEOUaeiou':
                final += l[0]
                del l[0]
            else:
                final += j
        return final