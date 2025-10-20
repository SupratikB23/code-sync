class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        total = 0
        a = len(pref)
        for i in words:
            if i[:a] == pref:
                total +=1
        return total