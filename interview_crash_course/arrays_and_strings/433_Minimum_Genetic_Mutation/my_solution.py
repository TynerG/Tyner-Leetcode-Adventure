from collections import defaultdict, deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0

        if endGene not in bank:
            return -1

        gene_graph = defaultdict(list)  # {gene_string : [gene_strings]}
        for gene in bank + [startGene]:
            for mutation in bank + [startGene]:
                distance = 0
                for i in range(8):
                    if gene[i] != mutation[i]:
                        distance += 1
                    if distance >= 2:
                        break

                if distance == 1:
                    gene_graph[gene].append(mutation)

        seen = {startGene}
        queue = deque([(startGene, 0)])
        while queue:
            node, num_mutations = queue.popleft()
            for nb in gene_graph[node]:
                if nb == endGene:
                    return num_mutations + 1
                if nb not in seen:
                    seen.add(nb)
                    queue.append((nb, num_mutations + 1))

        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"]))