class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for i in digits:
            s = str(s)+str(i)
        ans = int(s)+1
        num = [int(x) for x in str(ans)]
        return num