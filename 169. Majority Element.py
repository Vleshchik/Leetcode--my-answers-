class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = max(nums)
        l = nums.count(n)
        for i in range(n,0,-1):
            if nums.count(i) > l:
                n = i
                l = nums.count(i)
        return n