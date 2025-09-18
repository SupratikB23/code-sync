class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total = 0
        for i in jewels:
            if i in stones:
                total+=stones.count(i)
        return total