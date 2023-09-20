class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total_sum = sum(nums)
        left = 0
        current_sum = 0
        max_length = -1
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum > total_sum - x and left <= right:
                current_sum -= nums[left]
                left += 1
            if current_sum == total_sum - x:
                max_length = max(max_length, right - left + 1)
        if max_length == -1:
            return -1
        else:
            return len(nums) - max_length