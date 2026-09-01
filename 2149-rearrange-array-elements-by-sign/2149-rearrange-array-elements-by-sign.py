class Solution(object):
    def rearrangeArray(self, nums):
        n=len(nums)
        a=[]
        b=[]
        r=[]

        for i in range(n):
            if nums[i]<0:
                a.append(nums[i])
            else:
                b.append(nums[i])

        for i in range(n/2):
            r.append(b[i])
            r.append(a[i])
           
        
        return r

        
        