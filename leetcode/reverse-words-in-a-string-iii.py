class Solution:
    def reverseWords(self, s: str) -> str:
        total = ''
        for i in s.split():
            total += str(i)[::-1] + ' '
        return total[:-1]