class Solution:
    def maxSum(self, nums: List[int]) -> int:
        mx = -1

        def digits(x):
            h = 0
            while x > 0:
                h = max(h, x % 10)
                x //= 10
            return h

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if digits(nums[i]) == digits(nums[j]):
                    mx = max(mx, (nums[i] + nums[j]))
        return mx