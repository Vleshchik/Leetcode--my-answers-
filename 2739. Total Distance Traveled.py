class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        c = 0
        for i in range(mainTank):
            c += 1
            if c % 5 == 0:
                if additionalTank > 0:
                    c+= 1
                    additionalTank -= 1
        return c * 10