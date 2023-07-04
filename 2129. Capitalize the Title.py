class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.split()
        title2 = []
        for i in title:
            if len(i) > 2:
                title2.append(i.capitalize())
            else:
                title2.append(i.lower())

        return ' '.join(title2)