class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        l = []
        for i in range(len(nums)):
            n = (len(set(nums[:i+1]))) - len(set(nums[i+1:]))
            l.append(n)
        return l