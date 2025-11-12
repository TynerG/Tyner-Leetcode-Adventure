# could've hardcoded the subtractive form into the array to avoid checking them in the loop.
class Solution:
    def intToRoman(self, num: int) -> str:
        r_to_i = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        sub_form_9 = ['I', 'X', 'C', 'M']
        sub_form_4 = ['V', 'L', 'D']

        roman = ""
        while num > 0:
            if str(num)[0] == '9':
                symbol_idx = len(str(num)) - 1
                roman += sub_form_9[symbol_idx] + sub_form_9[symbol_idx + 1]
                num -= 9 * r_to_i[sub_form_9[symbol_idx]]

            elif str(num)[0] == '4':
                symbol_idx = len(str(num)) - 1
                roman += sub_form_9[symbol_idx] + sub_form_4[symbol_idx]
                num -= 4 * r_to_i[sub_form_9[symbol_idx]]

            else:
                for r in r_to_i:
                    if num >= r_to_i[r]:
                        roman += r
                        num -= r_to_i[r]
                        break

        return roman