class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        if 0 <= abs(x - y) <= 1:
            return 2 * (x + y + z)
        else:
            return 2 * (2 * min (x, y) + z + 1)