class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ctr = 0
        for i in ransomNote:
            if i in magazine:
                if magazine.count(i)<ransomNote.count(i):
                    ctr+=1                    
            else:
                ctr+=1
        if ctr==0:
            return True
        else:
            return False