class Solution:
    def addBinary(self, a: str, b: str) -> str:
        A = int(a,2)
        B = int(b,2)
        C = A+B
        C = bin(C)
        return C[2:]