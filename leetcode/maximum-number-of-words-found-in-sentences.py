class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        total = 0
        for i in sentences:
            x = i.split(' ')
            if len(x) > total:
                total = len(x)

        return total