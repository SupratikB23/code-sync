class Solution:
    def average(self, salary: List[int]) -> float:
        a = min(salary)
        b = max(salary)
        s = sum(salary) - a - b
        ans = s/(len(salary)-2)
        return ans