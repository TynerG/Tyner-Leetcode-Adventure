from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k != 0:
            nums[:k], nums[k:] = nums[-k:], nums[:-k]

if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    s = Solution()
    s.rotate(nums, 3)
    print(nums)