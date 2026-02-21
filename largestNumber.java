class Solution:
    def largestNumber(self, nums):
        # Convert numbers to strings
        arr = list(map(str, nums))

        # Custom sort using comparison of concatenations
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[j] + arr[i] > arr[i] + arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]

        # Edge case: if the largest number is "0"
        if arr[0] == "0":
            return "0"

        # Join and return result
        return "".join(arr)
