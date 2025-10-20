class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = {}
        for i in range(len(names)):
            d[heights[i]] = names[i]
        sorted_heights = sorted(d.keys(), reverse=True) 
        l = []
        for j in sorted_heights:
            l.append(d[j])
        return l