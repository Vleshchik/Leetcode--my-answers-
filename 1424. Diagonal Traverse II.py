class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonal_elements = []
        for row_index, row in enumerate(nums):
            for column_index, value in enumerate(row):
                diagonal_elements.append((row_index + column_index, column_index, value))
        diagonal_elements.sort()
        return [element[2] for element in diagonal_elements]