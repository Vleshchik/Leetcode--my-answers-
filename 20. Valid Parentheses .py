class Solution:
    def isValid(self, s: str) -> bool:
        while s.count('()') > 0 or s.count('[]') > 0 or s.count('{}') > 0:
            s = s.replace('()','')
            s = s.replace('{}','')
            s = s.replace('[]','')
        if len(s) > 0:
            return False
        else:
            return True