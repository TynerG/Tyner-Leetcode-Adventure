# Issue: Correct but hard to read
class Solution:
    def romanToInt(self, s: str) -> int:
        value = 0
        i = 0
        while i < len(s):
            if i == len(s) - 1:
                if s[i] == 'I':
                    value += 1
                elif s[i] == 'V':
                    value += 5
                elif s[i] == 'X':
                    value += 10
                elif s[i] == 'L':
                    value += 50
                elif s[i] == 'C':
                    value += 100
                elif s[i] == 'D':
                    value += 500
                elif s[i] == 'M':
                    value += 1000

                i += 1

            elif s[i] == 'I':
                if s[i + 1] == 'V':
                    value += 4
                    i += 2
                elif s[i + 1] == 'X':
                    value += 9
                    i += 2
                else:
                    value += 1
                    i += 1

            elif s[i] == 'V':
                value += 5
                i += 1

            elif s[i] == 'X':
                if s[i + 1] == 'L':
                    value += 40
                    i += 2
                elif s[i + 1] == 'C':
                    value += 90
                    i += 2
                else:
                    value += 10
                    i += 1

            elif s[i] == 'L':
                value += 50
                i += 1

            elif s[i] == 'C':
                if s[i + 1] == 'D':
                    value += 400
                    i += 2
                elif s[i + 1] == 'M':
                    value += 900
                    i += 2
                else:
                    value += 100
                    i += 1

            elif s[i] == 'D':
                value += 500
                i += 1

            elif s[i] == 'M':
                value += 1000
                i += 1

        return value