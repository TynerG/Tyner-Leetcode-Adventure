from typing import List

# improvements: could've used sliding window so that we don't have to store the prefix sums
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        sums = [nums[0]]
        for i in nums[1:]:
            sums.append(sums[-1] + i)

        k_rad_avg = []
        for i in range(len(nums)):
            # check if we'll get out of range
            if i - k < 0 or i + k >= len(nums):
                k_rad_avg.append(-1)
                continue

            nomi = 0
            if i - k - 1 < 0:
                nomi = sums[i + k]
            else:
                nomi = sums[i + k] - sums[i - k - 1]

            k_rad_avg.append(nomi // (2 * k + 1))

        return k_rad_avg
