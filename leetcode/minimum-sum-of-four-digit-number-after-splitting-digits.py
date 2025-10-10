class Solution:
    def minimumSum(self, num: int) -> int:
        list1=list(str(num))
        min1=min(list1)
        max1=max(list1)
        num1= int(str(min1)+str(max1))
        list1.remove(min1)
        list1.remove(max1)
        min2=min(list1)
        max2=max(list1)
        num2= int(str(min2)+str(max2))
        return num1+num2