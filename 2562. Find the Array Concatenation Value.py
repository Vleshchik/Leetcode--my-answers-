class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        n = 0
        while len(nums) > 1:
            n += int(str(nums[0]) + str(nums[-1]))
            nums.pop(0)
            nums.pop(-1)
        if len(nums) == 1:
            n += nums[0]
        return n