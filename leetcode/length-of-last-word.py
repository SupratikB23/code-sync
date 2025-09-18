class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        L=s.split()
        return len(L[-1])