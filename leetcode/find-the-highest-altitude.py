class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maximum = gain[0]
        total = 0
        for i in gain:
            total += i
            if total>maximum:
                maximum = total
        if maximum <0:
            return 0
        return maximum