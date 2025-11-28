
class Solution:

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        length = len(arr)
        l = 0
        r = length - 1
        while l + 1 < r:
            m = (l + r) // 2
            if arr[m-1] <= x <= arr[m]:
                l, r = self.pickNumber(arr, m, k, x, length)
                return arr[l: r+1]
            if x < arr[m]:
                r = m
            else:
                l = m
        if l == 0:
            return arr[:min(k, length)]
        if r == length - 1:
            return arr[-k:]

    def pickNumber(self, arr, m, k, x, length):
        result = []
        i = 1
        j = 0
        while k > 0:
            if m + j > length - 1:
                result.sort()
                return result[0] - k, result[-1]
            if m-i >= 0 and x - arr[m-i] <= arr[m + j] - x:
                result.append(m-i)
                i += 1
            else:
                result.append(m + j)
                j += 1
            k -= 1
        result.sort()
        return result[0], result[-1]
