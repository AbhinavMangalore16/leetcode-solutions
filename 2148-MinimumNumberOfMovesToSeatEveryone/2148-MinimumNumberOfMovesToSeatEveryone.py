# Last updated: 3/31/2026, 9:33:01 PM
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        return sum(abs(seat - student) for seat, student in zip(seats, students))