
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1

    def searchRecursive(self, nums: List[int], target: int) -> int:
        def helper(l, r):
            if l > r: return -1
            mid = (l + r) // 2
            if nums[mid] == target: return mid
            if nums[mid] < target: return helper(mid + 1, r)
            return helper(l, mid - 1)
        return helper(0, len(nums) - 1)
