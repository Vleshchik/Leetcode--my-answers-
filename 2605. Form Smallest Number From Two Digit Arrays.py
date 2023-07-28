class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        l = []
        for i in nums1:
            if i in nums2:
                l.append(i)
        if len(l) > 0:
            return min(l)
        return min(min(nums1), min(nums2)) * 10 + max(min(nums1), min(nums2))