class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums_sort = nums.copy()
        nums_sort.sort(key = lambda x: (nums.count(x), -x))
        return nums_sort