class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        L = []
        for i in order:
            if i in friends:
                L.append(i)
        return L