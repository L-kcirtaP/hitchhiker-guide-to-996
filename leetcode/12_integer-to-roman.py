class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = [
            {1: 'I', 4: 'IV', 5: 'V', 9: 'IX'},
            {1: 'X', 4: 'XL', 5: 'L', 9: 'XC'},
            {1: 'C', 4: 'CD', 5: 'D', 9: 'CM'}
        ]
        roman = ""
        if (num >= 1000):
            roman += 'M' * (int)(num / 1000)
            num -= (int)(num / 1000) * 1000

        for i in reversed(range(3)):
            digit = (int)(num / 10 ** i)
            if (digit == 4 or digit == 9):
                roman += mapping[i][digit]
            elif (digit >= 5):
                roman += mapping[i][5]
                roman += mapping[i][1] * (digit - 5)
            else:
                roman += mapping[i][1] * digit
            num -= (int)(num / 10 ** i) * 10 ** i
        return roman
