class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        x = list(str(n))
        sums = 0
        product = 1
        for i in range(len(x)):
            sums+=int(x[i])
            product*=int(x[i])
        return product - sums