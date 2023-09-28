class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums2 = sorted(nums, key = lambda x: x % 2 == 1)
        print(nums2)
        return nums2