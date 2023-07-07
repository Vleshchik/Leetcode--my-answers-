class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        i = 1
        while i <= n:
            if citations[n-i] < i:
                return i-1
            i += 1
        return i-1
