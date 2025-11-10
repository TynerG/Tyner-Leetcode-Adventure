from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations_to_num_papers = dict()
        for i in citations:
            if i in citations_to_num_papers:
                citations_to_num_papers[i] += 1
            else:
                citations_to_num_papers[i] = 1

        h = len(citations)
        while h >= 0:
            sum_papers = 0
            for key in citations_to_num_papers:
                if key >= h:
                    sum_papers += citations_to_num_papers[key]

            if sum_papers >= h:
                return h

            h -= 1
