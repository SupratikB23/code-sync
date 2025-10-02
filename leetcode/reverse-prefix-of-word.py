class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            a = word.index(ch)
            new = word[:a+1]
            new2 = new[::-1] + word[a+1:]
            return new2
        else:
            return word