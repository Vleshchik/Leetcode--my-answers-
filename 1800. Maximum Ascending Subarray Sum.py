class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        mx = nums[0]
        l = []
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                mx += nums[i]
            else:
                l.append(mx)
                mx = nums[i]
        l.append(mx)
        return max(l)