class Solution:
    def longestPalindrome(self, s: str) -> int:

        char_set = set()
        count = 0

        for char in s:
            if char in char_set:
                char_set.remove(char)
                count += 2
            else:
                char_set.add(char)

        if char_set:
            count += 1

        return count