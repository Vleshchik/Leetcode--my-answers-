class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l1 = [0]
        l2 = []
        for i in range(len(nums)-1):
            l2.append(sum(nums[i+1:]))
            l1.append(sum(nums[:i+1]))
        l2.append(0)
        return [abs(l1[i] - l2[i]) for i in range(len(l1))]