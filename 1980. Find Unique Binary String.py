class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        s = '0' * n
        while s in nums:
            s = '1' + s[:-1]
        return s