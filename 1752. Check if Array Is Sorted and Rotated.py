class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            n = nums.pop(0)
            nums.append(n)
            if nums == sorted(nums):
                return True
        return False