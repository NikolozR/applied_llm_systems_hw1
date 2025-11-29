
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        first = 1
        second = 2
        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third
        return second
    
    def climbStairsRecursive(self, n: int) -> int:
        memo = {}
        def helper(x):
            if x in memo: return memo[x]
            if x <= 2: return x
            memo[x] = helper(x-1) + helper(x-2)
            return memo[x]
        return helper(n)
