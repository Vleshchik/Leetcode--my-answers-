class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        c = 0
        while len(seats) > 0:
            c += abs(min(seats)-min(students))
            seats.pop(seats.index(min(seats)))
            students.pop(students.index(min(students)))
        return c