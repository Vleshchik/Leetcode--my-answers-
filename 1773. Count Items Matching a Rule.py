class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        c = 0
        if ruleKey == "type":
            n = 0
        elif ruleKey == "color":
            n = 1
        else:
            n = 2
        for i in items:
            if i[n] == ruleValue:
                c += 1
        return c