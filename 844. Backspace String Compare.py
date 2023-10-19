class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_res = []
        t_res = []
        for i in s:
            if i == '#':
                if len(s_res) > 0:
                    s_res.pop()
            else:
                s_res.append(i)
        for i in t:
            if i == '#':
                if len(t_res) > 0:
                    t_res.pop()
            else:
                t_res.append(i)
        return s_res == t_res