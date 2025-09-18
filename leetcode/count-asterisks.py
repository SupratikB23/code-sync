class Solution:
    def countAsterisks(self, s: str) -> int:
        total = 0
        if s.count('|') == 0:
            return s.count('*')
        else:
            a = s.split('|')
            for i in range(len(a)):
                if i%2 == 0:
                    total += a[i].count('*')
            return total