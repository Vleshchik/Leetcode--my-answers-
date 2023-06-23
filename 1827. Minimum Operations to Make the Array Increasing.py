class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = 0
        if len(nums) > 1:
            for i in range(1,len(nums)):
                n = nums[i]
                if nums[i] <= nums[i-1]:

                    nums[i] = max(nums[i],nums[i-1]) + 1

                    c += (nums[i] - n)

        return c