class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        num2 = int(str(num)[::-1])
        return num == int(str(num2)[::-1])