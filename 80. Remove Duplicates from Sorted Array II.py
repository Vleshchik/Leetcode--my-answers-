class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == '_':
                return len([i for i in nums if i != '_'])
            elif nums.count(nums[i]) > 2:
                while nums.count(nums[i]) > 2:
                    nums.pop(i+1)
                    nums.append('_')
