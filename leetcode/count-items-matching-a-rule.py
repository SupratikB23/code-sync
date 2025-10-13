class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        l = ["type", "color", "name"]
        a = l.index(ruleKey)
        count = 0
        for i in items:
            if i[a] == ruleValue:
                count+=1
        return count