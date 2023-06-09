class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        c = 0
        for i in range(len(grid)):
            l = []
            for j in range(len(grid)):
                l.append(grid[j][i])
            c += grid.count(l)
        return c