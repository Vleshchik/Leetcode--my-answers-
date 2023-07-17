class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        c = 0
        for i in range(len(nums)):
            print(nums[i], c)
            if nums[i] == 0:
                c += 1
            if nums[i] == 1 and i > 1:
                if c < k:
                    return False
                c = 0
        return True