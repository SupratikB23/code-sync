class Solution:
    def maxFreqSum(self, s: str) -> int:
        total_vowel = 0
        total_consonant = 0
        for i in 'aeiou':
            if len(s)!=0 and s.count(i) > total_vowel:
                total_vowel = s.count(i)
                s = s.replace(i,"")
        for j in s:
            if j not in 'aeiou' and len(s)!=0 and s.count(j) > total_consonant:
                total_consonant = s.count(j)
                s = s.replace(j,"")
        return total_vowel+total_consonant