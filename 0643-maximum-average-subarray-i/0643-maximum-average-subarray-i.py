class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        s=0

        for i in range(k):
            s=s+nums[i]
        
       
        ans=s/k
        for i in range(k,len(nums)):
            s=(s-nums[i-k]+nums[i])
            ans=max(ans,s/k)

        
        return ans

        