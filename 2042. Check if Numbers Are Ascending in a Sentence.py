class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        n = 0
        for i in s.split():
            if i.isdigit():
                if int(i) <= n:
                    return False
                else:
                    n = int(i)
        return True