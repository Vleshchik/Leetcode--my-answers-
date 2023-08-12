class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            gifts[gifts.index(max(gifts))] = int(max(gifts) ** 0.5)

        return sum(gifts)