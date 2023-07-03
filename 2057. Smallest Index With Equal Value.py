class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        n = 101
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                n = min(n, i)
        return -1 if n == 101 else n