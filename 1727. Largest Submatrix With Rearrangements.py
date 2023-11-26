from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        for row in range(1, len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col]:
                    matrix[row][col] = matrix[row - 1][col] + 1
        max_area = 0
        for row in matrix:
            row.sort(reverse=True)
            for index, height in enumerate(row):
                width = index + 1
                area = width * height
                max_area = max(max_area, area)
        return max_area