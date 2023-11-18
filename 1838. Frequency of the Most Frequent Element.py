class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = 0
        ans, total = 0, 0
        for i in range(len(nums)):
            total += nums[i]

            while nums[i] * (i - n + 1) > total + k:
                total -= nums[n]
                n += 1
            ans = max(ans, (i - n + 1))
        return ans