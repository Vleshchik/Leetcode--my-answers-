class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        l = [0 for i in range(num_people)]
        n = 0
        while candies > 0:
            person = 0
            n += 1
            for _ in range(len(l)):
                if candies >= n:
                    l[person] += n
                    person += 1
                    candies -= n
                    if person <= (len(l) - 1):
                        n += 1
                else:
                    l[person] += candies
                    return l
        return l
