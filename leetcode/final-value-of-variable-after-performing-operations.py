class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        f1 = operations.count("--X")
        f2 = operations.count("X--")
        f3 = operations.count("++X")
        f4 = operations.count("X++")
        return ((-1)*(f1+f2))+(1*(f3+f4))