class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        mx = 0
        for i in accounts:
            if sum(i) > mx:
                mx = sum(i)
        return mx