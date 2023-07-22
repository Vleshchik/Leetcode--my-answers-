# first variant
'''
class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        c = 0
        if nums[0] == 1 and nums[-1] == len(nums):
            return c
        else:
            while nums[0] != 1 or nums[-1] != len(nums):
                if nums[0] != 1:
                    n = nums.index(1)
                    nums[n], nums[n - 1] = nums[n - 1], nums[n]
                    c += 1
                if nums[-1] != len(nums):
                    n = nums.index(len(nums))
                    nums[n], nums[n + 1] = nums[n + 1], nums[n]
                    c += 1
        return c
'''
# second variant
'''
class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        c = 0
        if nums[0] == 1 and nums[-1] == len(nums):
            return c
        c += nums.index(1)
        c += len(nums) - 1 - nums.index(len(nums))
        if nums.index(1) > nums.index(len(nums)):
            c -= 1
        return c
'''