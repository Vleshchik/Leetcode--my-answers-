class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        c = 0
        while len(grid[0]) > 0:
            l = []
            for i in grid:
                l.append(i.pop(i.index(max(i))))
            c += max(l)
        return c