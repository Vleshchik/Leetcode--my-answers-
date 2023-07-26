class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = 'qwertyuiopasdfghjklzxcvbnm'
        for i in alphabet:
            if i not in sentence:
                return False
        return True