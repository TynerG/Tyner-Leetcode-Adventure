from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node: int, curr: List[int]) -> None:
            if node == dest:
                answers.append(curr[:])

            for child in graph[node]:
                curr.append(child)
                dfs(child, curr)
                curr.pop()

        dest = len(graph) - 1
        answers = []
        dfs(0, [0])
        return answers