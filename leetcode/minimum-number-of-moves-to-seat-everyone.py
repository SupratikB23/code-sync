class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        output=0
        sorted_seats=sorted(seats)
        sorted_students=sorted(students)
        for i in range(len(sorted_seats)):
            ans=abs(sorted_seats[i]-sorted_students[i])
            output+=ans
        return output