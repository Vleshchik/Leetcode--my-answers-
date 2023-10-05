class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) / 3
        l = []
        for i in set(nums):
            if nums.count(i) > n:
                l.append(i)
        return l