class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        total = s[:k][::-1] + s[k:]
        return total