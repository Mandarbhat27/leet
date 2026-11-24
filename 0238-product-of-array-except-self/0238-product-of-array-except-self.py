class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        ans=[0]*n
        pre=[0]*n
        pre[0]=nums[0]
        for i in range(1,n):
            pre[i]=pre[i-1]*nums[i]
        
        suf=[0]*n
        suf[n-1]=nums[n-1]

        for i in range(n-2,-1,-1):
            suf[i]=suf[i+1]*nums[i]

        for i in range(n):
            l=1
            r=1

            if i>0:
                l=pre[i-1]
            if i<n-1:
                r=suf[i+1]

            ans[i]=l*r
        
        return ans
        
        