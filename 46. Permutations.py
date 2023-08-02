class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        tes = set()
        res = []

        def a(res, subset):
            if len(subset) == len(nums):
                res.append(subset)
            for i in range(len(nums)):
                if i not in tes:
                    tes.add(i)
                    a(res, subset+[nums[i]])
                    tes.remove(i)
        a(res,[])
        return res