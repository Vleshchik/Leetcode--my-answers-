class Solution:
    def minimumSum(self, num: int) -> int:
        nums = [int(i) for i in str(num)]
        n1 = nums.pop(nums.index(min(nums))) * 10
        n2 = nums.pop(nums.index(min(nums))) * 10
        n1 += nums.pop(nums.index(min(nums)))
        n2 += nums.pop(nums.index(min(nums)))
        return n1 + n2