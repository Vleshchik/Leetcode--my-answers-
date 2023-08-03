class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_keyboard = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
                          '9': 'wxyz'}

        if digits == "":
            return []

        nums = list(phone_keyboard[digits[0]])

        for digit in digits[1:]:
            nums = [i + j for i in nums for j in list(phone_keyboard[digit])]

        return nums