class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        mx = 0
        n = -1
        for i in nums:
            if not i % 2:
                if nums.count(i) > mx:
                    mx = nums.count(i)
                    n = i
                elif nums.count(i) == mx:
                    n = min(n,i)
        return n