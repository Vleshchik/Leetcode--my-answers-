class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = nums.count(0)
        for i in range(n):
            nums.append(0)
            nums.pop(nums.index(0))
        """
        Do not return anything, modify nums in-place instead.
        """