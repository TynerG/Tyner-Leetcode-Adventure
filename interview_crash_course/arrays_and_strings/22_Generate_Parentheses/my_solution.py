from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def parenthesis(diff: int, curr: List[str]) -> None:
            if diff < 0:
                return

            if len(curr) == n * 2:
                if diff == 0:
                    answers.append("".join(curr))

                return

            diff += 1
            curr.append("(")
            parenthesis(diff, curr)
            diff -= 1
            curr.pop()

            diff -= 1
            curr.append(")")
            parenthesis(diff, curr)
            diff += 1
            curr.pop()

        answers = []
        curr = []
        parenthesis(0, curr)

        return answers