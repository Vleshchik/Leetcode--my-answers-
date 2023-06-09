class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        l = []
        l.append([i for i in nums1 if i not in nums2])
        l.append([i for i in nums2 if i not in nums1])
        return l