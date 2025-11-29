class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = set()
        for i in sentence:
            alphabet.add(i)

        return len(alphabet) == 26