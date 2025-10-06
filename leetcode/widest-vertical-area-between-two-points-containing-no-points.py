class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        l = []
        for i in range(len(points)):
            a = points[i][0]
            l.append(a)
        l.sort()
        gap = 0
        for j in range(len(l)-1):
            if l[j+1]-l[j] > gap:
                gap = l[j+1]-l[j]
        return gap