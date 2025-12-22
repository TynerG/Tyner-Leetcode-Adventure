from collections import deque
from typing import List

# improvements: use a bi-directional BFS to reduce time and space complexity
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        # BFS
        queue = deque([(beginWord, 1)])
        seen = {beginWord}
        while queue:
            node, num_trans = queue.popleft()
            for idx in range(len(beginWord)):
                for letter in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                               "s", "t", "u", "v", "w", "x", "y", "z"]:
                    list_node = list(node)
                    list_node[idx] = letter
                    str_transform = "".join(list_node)

                    if str_transform in wordSet:
                        if str_transform == endWord:
                            return num_trans + 1

                        if str_transform not in seen:
                            seen.add(str_transform)
                            queue.append((str_transform, num_trans + 1))

        return 0