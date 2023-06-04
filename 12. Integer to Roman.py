class Solution:
    def intToRoman(self, n: int) -> str:
        rom_num = []
        arab_rom = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        while n > 0:
            for i, r in arab_rom:
                while n >= i:
                    rom_num.append(r)
                    n -= i
        return ''.join(map(str, rom_num))