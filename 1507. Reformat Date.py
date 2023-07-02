from datetime import datetime
class Solution:
    def reformatDate(self, date: str) -> str:
        date = date.split()
        date = '-'.join([date[2], date[1], date[0][:-2]])
        return str(datetime.strptime(date, '%Y-%b-%d').date())