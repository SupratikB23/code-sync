class Solution:
    def numberOfSteps(self, num: int) -> int:
        countr = 0
        if num != 0:
            while num != 1 :
                if num%2 == 0:
                    num = num/2
                    countr+=1
                else:
                    num = (num-1)/2
                    countr+=2
            return countr+1
        else:
            return 0