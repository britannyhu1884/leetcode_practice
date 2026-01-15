class Solution:
    def intToRoman(self, num: int) -> str:
        if not num:
            return ""
        dict_ = {1: 'I', 4:'IV', 5:'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L' , 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000:'M'}
        pow_ = 1
        res = ''
        while num > 0:
            left = num % 10
            num = num // 10
            val = left * pow_
            if val in dict_:
                res = dict_[left * pow_] + res
            else:
                if left < 5:
                    res = (dict_[1 * pow_] * left) + res
                else:
                    res = (dict_[5 * pow_]) + (dict_[1 * pow_] * (left - 5)) + res
            pow_ *= 10
        return res
    
class Solution:
    def intToRoman(self, num: int) -> str:
        if not num:
            return ""
        roman_numerals = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        res = []
        for value, symbol in roman_numerals:
            while num >= value:
                res.append(symbol)
                num -= value
        return "".join(res)
    
# 有意思，我自己做的时候是倒叙，答案是正序挺好玩的