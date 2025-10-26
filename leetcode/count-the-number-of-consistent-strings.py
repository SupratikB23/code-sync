class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        x = {char: True for char in allowed}  # Dictionary of allowed chars
        count = 0
        for word in words:
            valid = True
            for j in word:
                if j not in x:  # ✅ Fixed: Check existence (no remove)
                    valid = False
                    break
            if valid:
                count += 1
        return count