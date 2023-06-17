class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        s1 = 0
        s2 = 0
        for i in range(len(player1)):
            if (i > 0 and player1[i - 1] == 10) or (i > 1 and player1[i - 2] == 10):
                s1 += player1[i] * 2
            else:
                s1 += player1[i]
        for j in range(len(player2)):
            if (j > 0 and player2[j - 1] == 10) or (j > 1 and player2[j - 2] == 10):
                s2 += player2[j] * 2
            else:

                s2 += player2[j]
        if s1 == s2:
            return 0
        return 1 if s1 > s2 else 2