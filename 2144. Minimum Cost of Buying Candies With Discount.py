class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        counter = 0
        c = 0
        cost = sorted(cost, reverse = True)
        while len(cost) != 0:
            c += 1
            counter += max(cost)
            cost.pop(cost.index(max(cost)))
            if c == 2 and len(cost) > 0:
                cost.pop(0)
                c = 0
        return counter