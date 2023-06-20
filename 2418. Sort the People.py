class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heights, names = zip(*[(h, n) for h, n in sorted(zip(heights, names), reverse = True)])
        return names