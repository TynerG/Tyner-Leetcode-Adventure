from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_letters = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

        def build_letters(curr: List[str], idx: int) -> None:
            if len(curr) == len(digits):
                answers.append("".join(curr))
                return

            for letter in num_to_letters[int(digits[idx])]:
                curr.append(letter)
                build_letters(curr, idx + 1)
                curr.pop()

        answers = []
        build_letters([], 0)
        return answers