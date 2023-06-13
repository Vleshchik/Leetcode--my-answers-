class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            n = nums[-1]
            nums.pop()
            nums.insert(0, n)
        """
        Do not return anything, modify nums in-place instead.
        """