import datetime
class Solution:
    def dayOfYear(self, date: str) -> int:
        date = date.split('-')
        n = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
        s = datetime.datetime(int(date[0]), 1, 1)
        delta = n - s
        return delta.days + 1