class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.sort(key=abs)
        if len(nums) > 1:
            if abs(nums[0]) in nums:
                return abs(nums[0])
            else:
                return nums[0]
        else:
            return nums[0]