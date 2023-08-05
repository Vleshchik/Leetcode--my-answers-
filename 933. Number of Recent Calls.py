class RecentCounter:

    def __init__(self):
        self.l = []

    def ping(self, t: int) -> int:
        self.l.append(t)
        r = [t - 3000, t]
        while self.l[0] < r[0]:
            self.l.pop(0)
        return len(self.l)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)