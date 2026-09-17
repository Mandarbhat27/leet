class Solution(object):
    def minSumOfLengths(self, arr, target):
        n = len(arr)

        best = [float('inf')] * n

        left = 0
        total = 0
        ans = float('inf')
        shortest = float('inf')

        for right in range(n):
            total += arr[right]

            while total > target:
                total -= arr[left]
                left += 1

            if total == target:
                length = right - left + 1

                if left > 0:
                    ans = min(ans, length + best[left - 1])

                shortest = min(shortest, length)

            best[right] = shortest

        if ans == float('inf'):
            return -1

        return ans