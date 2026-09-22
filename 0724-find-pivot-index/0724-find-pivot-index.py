class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        s=[0]*len(nums)
        s[0]=nums[0]
        for i in range(1,len(nums)):
            s[i]=s[i-1]+nums[i]
        
        n=len(nums)
        p=[0]*len(nums)
        p[n-1]=nums[n-1]

        for i in range(n-2,-1,-1):
            p[i]=p[i+1]+nums[i]
      
        for i in range(n):
            if s[i]==p[i]:
                return i
           
        return -1

    
        
        