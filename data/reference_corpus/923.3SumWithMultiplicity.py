
from collections import Counter

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count = 0
        counter = Counter(arr)
        arr = list(counter.keys())
        length = len(arr)
        modulo = 1000000007

        for i in range(length):
            for j in range(i, length):
                if target - arr[i] - arr[j] in counter:
                    if arr[i] == arr[j] == target-arr[i]-arr[j]:
                        count += counter[arr[i]] * (counter[arr[i]]-1) * (counter[arr[i]]-2) // 6
                    elif arr[i] == arr[j]:
                        count += counter[target-arr[i]-arr[j]] * (counter[arr[i]]) * (counter[arr[i]]-1) // 2
                    elif arr[i] < target-arr[i]-arr[j] and arr[j] < target-arr[i]-arr[j]:
                        count += counter[arr[i]] * counter[arr[j]] * counter[target-arr[i]-arr[j]]

        return count % modulo