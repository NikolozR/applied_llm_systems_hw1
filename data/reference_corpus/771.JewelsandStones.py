
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        i = len(J) - 1
        count = 0
        while i >= 0:
            if J[i] in S:
                count += S.count(J[i])
            i -= 1
        return count
