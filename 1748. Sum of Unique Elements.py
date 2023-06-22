class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        c = 0
        for i in nums:
            if nums.count(i) == 1:
                c += i
        return c