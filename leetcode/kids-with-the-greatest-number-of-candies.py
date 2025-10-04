class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a = max(candies)
        L = []
        for i in candies:
            if i+extraCandies >= a:
                L.append(True)
            else:
                L.append(False)
        return L