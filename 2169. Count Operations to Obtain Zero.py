class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        if num1 == num2 == 0:
            return 0
        elif num1 == 0 or num2 == 0:
            return 0
        c = 1
        while num1 != num2 :
            c+= 1
            if num1 > num2:
                num1 -= num2
            else:
                num2 -= num1
        return c