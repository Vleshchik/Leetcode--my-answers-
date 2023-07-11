class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        c = 1
        sentence = sentence.split()
        vowels = 'aeuioAEUIO'
        l = []
        for i in sentence:
            if i[0] in vowels:
                l.append(i + 'ma' + 'a'*c)
            else:
                l.append(i[1:] + i[0]+ 'ma' + 'a'*c)
            c += 1
        return ' '.join(l)