class Solution:
    def digitCount(self, num: str) -> bool:
        counter = True
        for i in range(len(num)):
            if int(num[i]) != num.count(str(i)):
                counter = False
        return counter