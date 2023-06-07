class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        nums.sort()
        left = 0
        right = len(nums)-1
        while left < right:
            sum_num = nums[left] + nums[right]
            if k == sum_num:
                count += 1
                right -= 1
                left += 1
            elif k < sum_num:
                right -= 1
            else:
                left += 1
        return count