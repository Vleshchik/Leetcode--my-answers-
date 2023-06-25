class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l = []
        for i in range(len(nums)):
            if not i%2:
                for j in range(nums[i]):
                    l.append(nums[i + 1])
        return l