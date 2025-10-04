class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        total = 0
        for i in accounts:
            if sum(i)>total:
                total = sum(i)
        return total