
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        numbers = {}
        half = len(arr) // 2
        for number in arr:
            if number not in numbers:
                numbers[number] = 1
            else:
                numbers[number] += 1
        for index, value in enumerate(sorted(list(numbers.values()), reverse=True)):
            half -= value
            if half <= 0:
                return index + 1
