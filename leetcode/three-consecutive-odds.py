class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        ctr = 0
        for i in arr:
            if i%2 != 0:
                ctr+=1
                if ctr == 3:
                    return True
            else:
                ctr = 0
        return False