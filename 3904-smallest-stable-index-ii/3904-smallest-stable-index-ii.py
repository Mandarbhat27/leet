class Solution(object):
    def firstStableIndex(self, nums, k):
        n = len(nums)

        # minimum from i to end
        right = [0] * n
        right[n-1] = nums[n-1]

        for i in range(n-2, -1, -1):
            right[i] = min(nums[i], right[i+1])

        maxe = nums[0]

        for i in range(n):
            maxe = max(maxe, nums[i])
            mine = right[i]

            if maxe - mine <= k:
                return i

        return -1