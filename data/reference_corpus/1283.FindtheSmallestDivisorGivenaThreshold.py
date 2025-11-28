
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = max(nums)
        while l < r:
            m = (l+r) // 2
            result = sum([1 + n//m if n%m else n//m for n in nums])
            if result > threshold:
                l = m + 1
            else:
                r = m
        return l
