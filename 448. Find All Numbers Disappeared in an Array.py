class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        t = set(nums)
        l = []
        for i in range(1, len(nums)+1):
            if i not in t:
                l.append(i)
        return l
