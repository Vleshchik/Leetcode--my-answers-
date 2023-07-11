class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        mx = 0
        s = ''
        paragraph = paragraph.lower()
        for i in paragraph:
            if not i.isalpha():
                paragraph = paragraph.replace(i, ' ')
        paragraph = paragraph.split()
        for i in paragraph:
            if i not in banned:
                if paragraph.count(i) > mx:
                    s = i
                    mx = paragraph.count(i)
        return s