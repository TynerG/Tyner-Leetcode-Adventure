from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        def find_num_ele(query: int) -> int:
            left = 0
            right = len(prefix_sum) - 1

            while left <= right:
                mid = (left + right) // 2

                if query == prefix_sum[mid]:
                    return mid + 1

                if prefix_sum[mid] > query:
                    right = mid - 1

                else:
                    left = mid + 1

            return left

        nums = sorted(nums)

        prefix_sum = []
        curr_sum = 0
        for num in nums:
            curr_sum += num
            prefix_sum.append(curr_sum)

        answers = []
        for q in queries:
            # do a binary search in prefix sum
            answers.append(find_num_ele(q))

        return answers
