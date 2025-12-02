class Solution:
    def makeGood(self, s: str) -> str:
        good_stack = []

        for c in s:
            if len(good_stack) != 0 and good_stack[-1] != c and good_stack[-1].upper() == c.upper():
                good_stack.pop()
            else:
                good_stack.append(c)

        return "".join(good_stack)