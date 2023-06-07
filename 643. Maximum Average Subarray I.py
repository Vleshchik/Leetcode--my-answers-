class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_n = sum(nums[:k])
        max_sum = sum_n
        for i in range(k, len(nums)):
            sum_n += nums[i] - nums[i-k]
            max_sum = max(max_sum, sum_n)
        return max_sum / k