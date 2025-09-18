class Solution:
    def scoreOfString(self, s: str) -> int:
        num = 0
        for i in range(len(s)-1):
            a = ord(s[i]) - ord(s[i+1])
            num += abs(a)
        return num