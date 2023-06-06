class Solution:
    def compress(self, chars: List[str]) -> int:
        marks = ""
        length = -1
        cur = chars[0]
        for i, value in enumerate(chars):
            length += 1
            if value != cur:
                count = str(length) if length != 1 else ''
                marks += cur + count
                cur = value
                length = 0
            if i == len(chars) - 1:
                length += 1
                count = str(length) if length != 1 else ''
                marks += cur + count
                cur = value
                length = 0
        for i, mark in enumerate(marks):
            chars[i] = mark
        return len(marks)