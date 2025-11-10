from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < k:
            popped = nums.pop()
            nums.insert(0, popped)
            i += 1

if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    s = Solution()
    s.rotate(nums, 3)
    print(nums)